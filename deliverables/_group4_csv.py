# -*- coding: utf-8 -*-
import json, csv

with open("_group4_results.json") as f:
    data = json.load(f)

# Specific ward-level parents identified (name clearly derived from an already-matched
# official ward in the same district) -- per target-unit-concept.md convention, use the
# most specific ancestor with a real P-code, not just the district.
SPECIFIC_PARENT = {
    ("TZ0105", "Hombolo Bwawani"): ("Hombolo", "TZ0105101"),
    ("TZ0503", "Mang'ula B"): ("Mang'ula", "TZ0503043"),
    ("TZ0505", "Kihonda Maghorofani"): ("Kihonda", "TZ0505192"),
}

DISTRICT_DISPLAY_NAME = {
    "TZ0101": "Kondoa", "TZ0102": "Mpwapwa", "TZ0103": "Kongwa", "TZ0104": "Chamwino",
    "TZ0105": "Dodoma Municipal", "TZ0106": "Bahi", "TZ0107": "Chemba",
    "TZ0501": "Kilosa", "TZ0502": "Morogoro", "TZ0503": "Kilombero", "TZ0504": "Ulanga",
    "TZ0505": "Morogoro Municipal", "TZ0506": "Mvomero", "TZ0507": "Gairo",
    "TZ0801": "Kilwa", "TZ0802": "Lindi", "TZ0803": "Nachingwea", "TZ0804": "Liwale",
    "TZ0805": "Ruangwa", "TZ0806": "Lindi Municipal",
    "TZ1101": "Iringa", "TZ1102": "Mufindi", "TZ1103": "Iringa Municipal", "TZ1104": "Kilolo",
    "TZ1105": "Mafinga",
    "TZ2301": "Mpanda Town", "TZ2302": "Mpanda", "TZ2303": "Mlele",
}

CAPTURE_DATE = "2026-10-03"

rows_out = []
notes_report = {}

for d in data:
    distcode = d["distcode"]
    parent_name = DISTRICT_DISPLAY_NAME[distcode]
    ward_rows = d["ward_rows"]

    # assign provisional numbers: group by ancestor (specific ward parent, else district)
    pending_by_ancestor = {}
    for wr in ward_rows:
        if wr["matched"]:
            continue
        key = (distcode, wr["name"])
        if key in SPECIFIC_PARENT:
            anc_name, anc_pcode = SPECIFIC_PARENT[key]
        else:
            anc_name, anc_pcode = parent_name, distcode
        pending_by_ancestor.setdefault((anc_name, anc_pcode), []).append(wr)

    prov_id_map = {}
    for (anc_name, anc_pcode), wrs in pending_by_ancestor.items():
        wrs_sorted = sorted(wrs, key=lambda w: w["name"].lower())
        for i, wr in enumerate(wrs_sorted, start=1):
            prov_id_map[wr["name"]] = (f"{anc_pcode}-PROV{i}", anc_name, anc_pcode)

    n_official = 0
    n_prov = 0
    sum_pop = 0
    for wr in ward_rows:
        sum_pop += wr["pop"]
        source_full = f"citypopulation.de/{wr['surl'].split('citypopulation.de/',1)[-1] if 'citypopulation.de/' in wr['surl'] else wr['surl']}, tabela de wards, Census 2022-08-23"
        # surl already starts with citypopulation.de/... in our data; normalize
        source_full = f"{wr['surl']}, tabela de wards, Census 2022-08-23"

        note_parts = []
        if wr["matched"]:
            n_official += 1
            unit_id = wr["pcode"]
            is_official = "yes"
            p_name, p_pcode = parent_name, distcode
            if wr["ratio"] < 0.999:
                note_parts.append(
                    f"Grafia diverge entre fontes: HDX gazetteer 2018 usa '{wr['gaz_name']}', "
                    f"citypopulation.de usa '{wr['name']}' - mesma unidade (match por similaridade "
                    f"de string, ratio={wr['ratio']:.2f})."
                )
        else:
            n_prov += 1
            unit_id, p_name, p_pcode = prov_id_map[wr["name"]]
            is_official = "no"
            if (distcode, wr["name"]) in SPECIFIC_PARENT:
                note_parts.append(
                    f"Ward nova, nao presente no gazetteer oficial HDX 2018 sob este nome. "
                    f"Nome sugere desmembramento da ward oficial '{p_name}' ({p_pcode}) - usado "
                    f"como ancestral mais especifico com P-code real, conforme convencao de "
                    f"target-unit-concept.md."
                )
            else:
                note_parts.append(
                    f"Ward nova, nao presente no gazetteer oficial HDX 2018 (distrito {distcode}/"
                    f"{parent_name}) nem identificada sob outra grafia entre as wards oficiais "
                    f"ja casadas deste distrito. Ancestral mais proximo com P-code oficial = "
                    f"distrito ({distcode}), conforme convencao de target-unit-concept.md."
                )
        if "annexed from old" in wr["slabel"]:
            note_parts.append(
                f"Fonte de populacao: pagina citypopulation.de atual de outro distrito "
                f"({wr['slabel']}) -- P-code oficial (via gazetteer 2018) pertence a {distcode}/"
                f"{parent_name}; a fronteira municipal/urbana atual anexou esta ward. Mesma "
                f"populacao reportada no censo 2022 nao e duplicada em nenhum outro distrito "
                f"deste grupo."
            )

        rows_out.append({
            "country_id": "TZA", "country_name": "Tanzania",
            "unit_id": unit_id, "unit_name": wr["name"], "local_unit_type": "Ward",
            "is_official_id": is_official, "admin_level_used": 3,
            "parent_unit_name": p_name, "parent_pcode": p_pcode,
            "population": wr["pop"], "population_source": source_full,
            "population_date_captured": CAPTURE_DATE, "population_data_year": 2022,
            "rural_population": "", "rural_population_pct": "",
            "rural_source": "Nao disponivel na fonte (so total por ward, sem quebra rural/urbano).",
            "rural_date_captured": "", "rural_data_year": "",
            "notes": " ".join(note_parts),
            "_distcode": distcode,
        })

    notes_report[distcode] = {
        "name": parent_name, "reg_pop": d["reg_pop"], "n_gaz": d["n_gaz"],
        "n_official": n_official, "n_prov": n_prov, "sum_pop": sum_pop,
        "unmatched_gaz": d["unmatched_gaz"],
        "n_wards": len(ward_rows),
    }

# write CSV
fieldnames = ["country_id","country_name","unit_id","unit_name","local_unit_type",
              "is_official_id","admin_level_used","parent_unit_name","parent_pcode",
              "population","population_source","population_date_captured",
              "population_data_year","rural_population","rural_population_pct",
              "rural_source","rural_date_captured","rural_data_year","notes"]

out_path = "/Users/eduardo.thuler/second-brain/projects/karimu/deliverables/ward-enum-tza-group4.csv"
# sort by district order (dict insertion order preserved), then alpha by name within district
order = {d["distcode"]: i for i, d in enumerate(data)}
rows_out.sort(key=lambda r: (order[r["_distcode"]], r["unit_name"].lower()))

with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for r in rows_out:
        writer.writerow(r)

print(f"Wrote {len(rows_out)} rows to {out_path}")

with open("_group4_notes_report.json", "w") as f:
    json.dump(notes_report, f, indent=1)

total_official = sum(v["n_official"] for v in notes_report.values())
total_prov = sum(v["n_prov"] for v in notes_report.values())
print(f"TOTAL wards: {total_official+total_prov} (official={total_official}, provisional={total_prov})")

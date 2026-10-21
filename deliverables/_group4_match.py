import openpyxl, difflib, re, csv
from _group4_data import DISTRICTS

GAZ_PATH = "/Users/eduardo.thuler/.claude/jobs/8f90797d/tmp/tza_admgz.xlsx"

wb = openpyxl.load_workbook(GAZ_PATH, data_only=True)
ws = wb["tza_admbnda_adm3_20181019"]
rows = list(ws.iter_rows(values_only=True))
header = rows[0]
idx = {h: i for i, h in enumerate(header)}

gaz_by_district = {}
for r in rows[1:]:
    a2 = r[idx["ADM2_PCODE"]]
    gaz_by_district.setdefault(a2, []).append((r[idx["ADM3_EN"]], r[idx["ADM3_PCODE"]]))


def norm(s):
    s = s.lower()
    s = s.replace("'", "").replace("'", "")
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


THRESH = 0.60

results = []

for distcode, d in DISTRICTS.items():
    gaz_list = gaz_by_district.get(distcode, [])
    all_citypop = []
    for source_label, source_url, wards in d["sources"]:
        for wname, pop in wards:
            all_citypop.append((wname, pop, source_label, source_url))

    # Build all candidate pairs (citypop_idx, gaz_idx, ratio), sorted descending by ratio.
    pairs = []
    for ci, (wname, pop, slabel, surl) in enumerate(all_citypop):
        n = norm(wname)
        for gi, (gname, pcode) in enumerate(gaz_list):
            gn = norm(gname)
            ratio = difflib.SequenceMatcher(None, n, gn).ratio()
            if ratio >= THRESH:
                pairs.append((ratio, ci, gi))
    pairs.sort(key=lambda x: -x[0])

    claimed_citypop = set()
    claimed_gaz = set()
    assignment = {}  # ci -> gi
    for ratio, ci, gi in pairs:
        if ci in claimed_citypop or gi in claimed_gaz:
            continue
        claimed_citypop.add(ci)
        claimed_gaz.add(gi)
        assignment[ci] = (gi, ratio)

    ward_rows = []
    for ci, (wname, pop, slabel, surl) in enumerate(all_citypop):
        if ci in assignment:
            gi, ratio = assignment[ci]
            gname, pcode = gaz_list[gi]
            ward_rows.append({
                "name": wname, "pop": pop, "slabel": slabel, "surl": surl,
                "matched": True, "gaz_name": gname, "pcode": pcode, "ratio": ratio,
            })
        else:
            ward_rows.append({
                "name": wname, "pop": pop, "slabel": slabel, "surl": surl,
                "matched": False, "gaz_name": None, "pcode": None, "ratio": 0.0,
            })

    unmatched_gaz = [(gname, pcode) for gi, (gname, pcode) in enumerate(gaz_list) if gi not in claimed_gaz]

    results.append({
        "distcode": distcode, "name": d["name"], "reg_pop": d["reg_pop"],
        "ward_rows": ward_rows, "unmatched_gaz": unmatched_gaz, "n_gaz": len(gaz_list),
    })

for res in results:
    new_wards = [wr for wr in res["ward_rows"] if not wr["matched"]]
    official = len(res["ward_rows"]) - len(new_wards)
    print(f"=== {res['distcode']} {res['name']} (gaz={res['n_gaz']}, citypop={len(res['ward_rows'])}, official={official}, new={len(new_wards)}, lost={len(res['unmatched_gaz'])}) ===")
    if res["unmatched_gaz"]:
        print(f"  LOST (gaz ward w/ no citypop match): {res['unmatched_gaz']}")
    for wr in new_wards:
        print(f"    NEW: {wr['name']} (pop={wr['pop']})")
    print()

# Save results as a pickle-ish structure for the CSV-writing step
import json
out = []
for res in results:
    out.append({
        "distcode": res["distcode"], "name": res["name"], "reg_pop": res["reg_pop"],
        "n_gaz": res["n_gaz"],
        "ward_rows": res["ward_rows"],
        "unmatched_gaz": res["unmatched_gaz"],
    })
with open("_group4_results.json", "w") as f:
    json.dump(out, f, indent=1)

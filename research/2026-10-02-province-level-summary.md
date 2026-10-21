# Nível Província (ADM1) — resumo consolidado

Data: 2026-10-02
Entregável: `deliverables/province-level-map.csv` (258 linhas, 22 países, consolidado de `province-level-map-groupA.csv` + `province-level-map-groupB.csv`)
Notas detalhadas por país: `2026-10-02-province-level-groupA-notes.md` (11 países) e `2026-10-02-province-level-groupB-notes.md` (11 países)

## Validação de consistência (feita nesta sessão, não pelos agentes)
- 258 linhas, 22 países distintos (bate com o shortlist `country-shortlist-ldc-no-war.csv`), zero `unit_id` duplicado, headers idênticos entre os dois lotes.
- **Cadeia hierárquica ponta a ponta confirmada**: Manyara (Tanzânia) = `TZ21` neste CSV — exatamente o prefixo já validado nos wards em `2026-10-01-target-unit-concept.md` (Arri=`TZ2101111`, Dabil=`TZ2101131`, Ayalagaya=`TZ2101123-PROV1`). País → Província → Distrito → Ward bate de ponta a ponta com P-codes reais.
- Kiribati: soma dos 3 grupos de ilhas (119.940) bate com o total nacional do censo 2020 — conferido pelo agente, não só assumido.

## Cobertura por país (258 unidades no total)

| País | ISO3 | Unidades ADM1 | P-code oficial? | Fonte |
|---|---|---|---|---|
| Tanzania | TZA | 31 | sim | HDX cod-ps-tza |
| Cambodia | KHM | 25 | sim | HDX cod-ps-khm |
| Madagascar | MDG | 22 | sim | HDX cod-ps-mdg |
| Angola | AGO | 18 | sim | HDX cod-ps-ago |
| Laos | LAO | 18 | sim | HDX cod-ps-lao |
| Liberia | LBR | 15 | sim | HDX cod-ps-lbr |
| Senegal | SEN | 14 | sim | HDX cod-ps-sen |
| Timor-Leste | TLS | 13 | sim | HDX cod-ps-tls |
| Mozambique | MOZ | 11 | sim | HDX cod-ps-moz |
| Lesotho | LSO | 10 | sim | HDX cod-ps-lso |
| Solomon Islands | SLB | 10 | sim | HDX cod-ps-slb |
| Zambia | ZMB | 10 | sim | HDX cod-ps-zmb |
| Guinea-Bissau | GNB | 9 | sim (fronteira); população via Wikipedia (censo 2009) | HDX cod-ab-gnb + Wikipedia |
| Tuvalu | TUV | 9 | **não** | Wikipedia (sem COD-AB/COD-PS publicado) |
| Guinea | GIN | 8 | sim | HDX cod-ps-gin |
| Gambia | GMB | 8 | sim | HDX cod-ps-gmb |
| Sierra Leone | SLE | 5 | sim (fronteira); população parcial via Wikipedia (censo 2015) | HDX cod-ab-sle + Wikipedia |
| Nepal | NPL | 7 | sim | HDX cod-ps-npl |
| Djibouti | DJI | 6 | sim | HDX cod-ps-dji |
| Comoros | COM | 3 | sim | HDX cod-ps-com |
| Malawi | MWI | 3 | sim | HDX cod-ps-mwi |
| Kiribati | KIR | 3 | sim | HDX cod-ps-kir |

**21 de 22 países com P-code oficial** (HDX COD-AB/COD-PS). Só **Tuvalu** não tem nenhum dataset HDX publicado — usado Wikipedia, `unit_id` em branco, `is_official_id=no`. Nenhuma unidade precisou do ID provisório `-PROV<n>` — ao contrário do nível ward (onde Ayalagaya precisou), no nível província a cobertura oficial foi quase total.

## Rural/urbano neste nível: praticamente indisponível
Só **Djibouti** tinha quebra rural/urbano na fonte (coluna `R_TL`) — 5 das 6 regiões preenchidas. Nos outros 21 países, os datasets de população do HDX (COD-PS) só desagregam por idade/sexo, não por rural/urbano, neste nível administrativo. Isso é diferente do nível país, onde o World Bank tem o indicador pronto (`SP.RUR.TOTL.ZS`) — a quebra rural que o Eduardo pediu continua disponível no agregado por país (`country-shortlist-ldc-no-war.csv`), mas não granular por província na maioria dos casos. Registrado como gap para v2 (provavelmente exigiria ir ao censo nacional de cada país, não a um dataset padronizado).

## Achados que valem atenção antes de usar os dados

1. **Nomenclatura de nível não é uniforme** — nem sempre "província": Tanzânia/Malawi usam "Region", Lesoto usa "District" (sem nível intermediário), Moçambique tem "Maputo City" com estatuto provincial próprio, Camboja e Guiné têm a capital como "Zona Especial"/unidade administrativa distinta, Comores usa "Ilha Autônoma", Ilhas Salomão tem Honiara como "Território da Capital" separado das 9 províncias, Gâmbia mistura "City Council"/"Municipal Council"/"Division". Cada país tem o termo exato registrado em `local_unit_type`.
2. **Malawi**: as 3 "Regions" não têm função administrativa própria — são só agrupamento estatístico dos 28 distritos reais. Relevante para quando formos ao nível distrito/ward em Malawi.
3. **Timor-Leste**: Atauro virou município separado em 2022, mas o P-code oficial (13 unidades) ainda não reflete isso — população provavelmente ainda contabilizada em Dili. Mesmo padrão "fronteira atrasa atrás de redistritamento" já visto na Tanzânia (Ayalagaya).
4. **Sierra Leone**: tem uma 5ª província (North Western, criada em 2017) com fronteira oficial já publicada, mas sem população oficial consolidada no HDX — população daquela província veio do censo 2015 via Wikipedia enquanto as outras 4 vieram do HDX. Mistura de fontes na mesma linha de país, documentada caso a caso no CSV.
5. **Camboja**: população é projeção oficial, não censo direto — a própria fonte primária reconhece taxas de crescimento sub-nacionais artificialmente uniformes (limitação da fonte, não nossa).
6. **Kiribati**: Ilhas Fênix com população oficial 0 (quase desabitadas) — mantido como está na fonte, não estimado.

## Próximo nível pendente
Distrito/Ward (ADM2/ADM3) ainda não construído para os 22 países — só validado manualmente para a Tanzânia (Arri, Dabil, Ayalagaya) antes deste lote. É o próximo passo natural, mas 22 países × dezenas de distritos cada é a maior etapa até agora — vale decidir com o Eduardo se faz todos de uma vez ou prioriza por algum critério (ex.: maior % rural, maior população, ordem alfabética) antes de disparar.

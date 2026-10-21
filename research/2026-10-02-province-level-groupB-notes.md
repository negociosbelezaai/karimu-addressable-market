# Notas de metodologia — Nível ADM1 (província/região), Grupo B

Data: 2026-10-02

Escopo: 11 países — Sierra Leone (SLE), Zambia (ZMB), Guinea-Bissau (GNB), Senegal (SEN), Liberia (LBR), Kiribati (KIR), Gambia (GMB), Tuvalu (TUV), Nepal (NPL), Angola (AGO), Djibouti (DJI). Entregável de dados: `deliverables/province-level-map-groupB.csv` (104 linhas + cabeçalho).

Método seguido conforme `research/2026-10-01-target-unit-concept.md`: HDX CKAN via `curl` com User-Agent de navegador, tentando primeiro `cod-ps-<iso3>` (população + P-code no mesmo arquivo), depois `cod-ab-<iso3>` (gazetteer de fronteiras, sem população), com fallback para Wikipedia quando nenhum dos dois pacotes tinha dado utilizável no nível ADM1.

---

## Sierra Leone (SLE)

**P-codes/fronteiras**: pacote HDX `cod-ab-sle`, arquivo `sle_admin_boundaries.xlsx` (https://data.humdata.org/dataset/a4816317-a913-4619-b1e9-d89e21c056b4/resource/7815b9d2-a25d-470c-a032-e9d2464d942d/download/sle_admin_boundaries.xlsx), aba `sle_admin1`. **5 ADM1 encontradas**: Eastern (SL01), Northern (SL02), Southern (SL03), Western (SL04), North Western (SL05).

**População**: o pacote HDX de população oficial `cod-ps-sle` (arquivo `sle_admpop_adm1_2020_v2.csv`, https://data.humdata.org/dataset/6485db1c-096c-4949-a32f-7ec6c38d07c5/resource/c29540a5-b509-429a-8bf0-f689fc261a6f/download/sle_admpop_adm1_2020_v2.csv) **só tem 4 províncias** — não inclui North Western. Isso acontece porque a Serra Leoa criou a North West Province em 2017 por desmembramento da Northern Province, mas o dataset de população (datado 2020) aparentemente não foi recalculado para a nova fronteira de 5 províncias, só o dataset de fronteiras (`cod-ab-sle`) foi atualizado. Para manter consistência entre as 5 unidades, usei como fonte de população o censo 2015 via Wikipedia "Districts of Sierra Leone" (https://en.wikipedia.org/wiki/Districts_of_Sierra_Leone), somando os distritos de cada província (ex.: Eastern = Kailahun+Kenema+Kono). Rural population não encontrada em nenhuma das fontes neste nível.

**Nome do nível local**: "Province" para 4 das 5 unidades; a 5ª ("Western") é oficialmente "Western Area" (contém a capital Freetown), não uma província.

## Zambia (ZMB)

**P-codes + população**: pacote HDX `cod-ps-zmb`, arquivo `zmb_admpop_adm1_2020_v2.csv` (https://data.humdata.org/dataset/eade6bae-9be6-43f4-bbf0-75c49ccecb2e/resource/ed9e753b-5dc6-4d96-9e9d-a44764d60280/download/zmb_admpop_adm1_2020_v2.csv) — melhor caso possível: P-code oficial + população (projeção 2020) no mesmo arquivo. **10 províncias encontradas**: Central, Copperbelt, Eastern, Luapula, Lusaka, Muchinga, Northern, North-Western, Southern, Western. Nome do nível local: "Province" para todas. Rural population não disponível neste dataset (só breakdown por idade/sexo).

## Guinea-Bissau (GNB)

Testados os slugs `gnb` e `gw` no HDX; confirmado que o slug correto é **`gnb`** (`gw` não existe como dataset). Não existe pacote `cod-ps-gnb` (população) no HDX. Usado `cod-ab-gnb`, arquivo `gnb_admin_boundaries.xlsx` (https://data.humdata.org/dataset/3db6297f-55d7-4e79-8969-281b1838ef79/resource/8aeca94e-2338-45af-8f9e-58902df2a237/download/gnb_admin_boundaries.xlsx), aba `gnb_admin1` — **9 unidades ADM1 encontradas** (P-codes oficiais): Bafata (GW01), Biombo (GW02), Bolama/Bijagos (GW03), Cacheu (GW04), Gabu (GW05), Oio (GW06), Quinara (GW07), Bissau (GW08), Tombali (GW09).

**População**: sem dataset oficial de população no HDX para este nível, fallback para Wikipedia "Regions of Guinea-Bissau" (https://en.wikipedia.org/wiki/Regions_of_Guinea-Bissau), censo 2009. Rural population não encontrada em nenhuma fonte consultada.

**Nome do nível local**: 8 das 9 unidades são "Region"; **Bissau (GW08) é "Autonomous Sector"**, não uma região convencional — contém a capital.

## Senegal (SEN)

Fonte: HDX, pacote `cod-ps-sen`, resource `sen_admpop_adm1_2022.csv` (https://data.humdata.org/dataset/c686be28-1858-44e9-a44b-598ce32ca20b/resource/7ee68aac-145f-4e50-b152-39da723d83e6/download/sen_admpop_adm1_2022.csv). P-code oficial (ANSD/OCHA), nível ADM1 = **Région** (francês, idioma oficial das fontes ANSD). **14 régions** encontradas (Dakar, Diourbel, Fatick, Kaffrine, Kaolack, Kédougou, Kolda, Louga, Matam, Saint-Louis, Sédhiou, Tambacounda, Thiès, Ziguinchor), todas com P-code oficial (SN01–SN14), população total censo/projeção 2022. Rural/urbano não disponível neste arquivo nesse nível.

## Liberia (LBR)

Fonte: HDX, pacote `cod-ps-lbr`, resource `lbr_admpop_adm1_2020_v2.csv` (https://data.humdata.org/dataset/31e5e358-284a-4f21-9af7-03c755eee555/resource/0bbdeb7a-34e3-42ac-b621-a8824d8d1e28/download/lbr_admpop_adm1_2020_v2.csv). P-code oficial, nível ADM1 = **County**. **15 counties** encontradas (Bomi, Bong, Gbarpolu, Grand Bassa, Grand Cape Mount, Grand Gedeh, Grand Kru, Lofa, Margibi, Maryland, Montserrado, Nimba, River Gee, Rivercess, Sinoe), censo nacional 2020. Rural/urbano não disponível nesse nível.

## Gambia (GMB)

Fonte: HDX, pacote `cod-ps-gmb`, resource `gmb_popadm_2021_admin1.csv` (https://data.humdata.org/dataset/b59b17f3-a3c7-45c0-a61d-539a01180494/resource/57a8f480-4893-4d3f-8905-6e5cde149930/download/gmb_popadm_2021_admin1.csv). P-code oficial, nível ADM1 = **Local Government Area (LGA)** — nomenclatura mista: Banjul é City Council, Kanifing é Municipal Council, as demais 6 (Basse, Brikama, Janjanbureh, Kerewan, Kuntaur, Mansakonko) são Divisions/Regions rurais; documentado como "Local Government Area (Division/City/Municipality)" por unidade, sem assumir termo único. **8 LGAs** encontradas, todas com P-code oficial (GM01–GM08), censo 2021. Rural/urbano não disponível nesse nível.

Nota técnica comum a SEN/LBR/GMB: a API `package_show` retorna o link de download, mas o download direto via `curl -A <UA>` sem `-L` retornava um HTML de redirect (302 → S3 assinado) — foi necessário `curl -sL` para seguir o redirect e obter o CSV real. Nenhum fetch falhou para esses 3 países.

## Djibouti (DJI)

Fonte: HDX, pacote `cod-ps-dji`. Arquivo: `dji_admpop_adm1_2009.csv` (https://data.humdata.org/dataset/ac1e22fd-a89d-45d8-ad05-d6282ac4ffce/resource/8abff79f-2a36-4600-bcb6-73a12885ca1c/download/dji_admpop_adm1_2009.csv). Nomes de ADM1 confirmados contra o gazetteer oficial `cod-ab-dji`, arquivo `dji_admgz_gadm_2022.xlsx` (aba `dji_admgz_gadm_adm1_2022`) — há pequenas variações de grafia entre os dois arquivos (ex.: "Tadjourah" vs. "Tadjoura"; "Dilkhil" vs. "Dikhil"; "Ali Sabeh" vs. "Ali Sabieh"); mantida a grafia do CSV de população (fonte primária dos números) na coluna `unit_name`.

**6 regiões encontradas** (todas com P-code oficial COD-AB, prefixo `DJ`): Obock (DJ01), Tadjourah (DJ02), Dilkhil (DJ03), Djibouti/capital (DJ04), Ali Sabeh (DJ05), Arta (DJ06). Nome local do nível: **"Region"**. Dado de população é do **censo de 2009** — nenhum dataset mais recente com quebra ADM1 encontrado no HDX para o Djibouti. Para a região da capital (DJ04), a fonte não reporta população rural (coerente — é inteiramente urbana). O arquivo-fonte também tem duas colunas extras (`N_TL`, `P_TL`) sem definição documentada nos metadados do pacote HDX — não usadas, para não arriscar interpretação errada.

## Kiribati (KIR)

Fonte: HDX, pacote `cod-ps-kir`. Arquivo: `kir_admpop_adm1_2020.csv` (https://data.humdata.org/dataset/e656842e-9643-4ef7-97f9-18c33654022d/resource/8ad2d41b-4b40-495d-a1d3-c1ad6b36a64c/download/kir_admpop_adm1_2020.csv). Nomes e P-codes confirmados contra o gazetteer oficial `cod-ab-kir`, arquivo `kir_admgz_2020.xlsx` (aba `kir_admgz_adm1`) — sem variação de grafia entre as fontes.

**3 grupos de ilhas encontrados**, todos com P-code oficial COD-AB (prefixo `KI`): Gilbert Islands (KI1, 108.661 hab.), Phoenix Islands (KI2, 0 hab.), Line Islands (KI3, 11.279 hab.). Nome local do nível: **"Island Group"**. Soma dos 3 grupos = 119.940, batendo com o total nacional conhecido do censo 2020 de Kiribati — validação cruzada positiva.

**Achado notável**: Phoenix Islands consta com população **0** na fonte oficial (grupo de atóis quase desabitado — só Kanton tem residentes, não contados como população permanente no censo 2020). Mantido o 0 exatamente como na fonte, sem estimar. Rural/urbano não disponível nesse nível.

## Tuvalu (TUV)

**Sem pacote COD-AB/COD-PS no HDX**: `package_show?id=cod-ps-tuv` e `package_show?id=cod-ab-tuv` retornaram `"success": false` para ambos — Tuvalu não tem Common Operational Dataset de fronteiras administrativas publicado no HDX (resultado esperado para país muito pequeno). Fallback adicional tentado antes da Wikipedia: API pública do **geoBoundaries** (`https://www.geoboundaries.org/api/current/gbOpen/TUV/ADM1/`) retorna metadados de um dataset ADM1 (fonte OpenStreetMap/Wambacher, 8 unidades, ref. 2017) — mas é dataset acadêmico/comunitário (não GADM, não oficial) e não expõe um código individual por unidade sem processar o GeoJSON/TopoJSON (fora de escopo). Por isso **nenhum ID foi usado** — `unit_id` em branco, `is_official_id = "no"`.

Fallback final: **Wikipedia — "Islands of Tuvalu"** (https://en.wikipedia.org/wiki/Islands_of_Tuvalu), tabela com dados do censo de 2022.

**9 ilhas/atóis encontrados** (lista completa do país): Funafuti (6.602 hab., capital, "Town Council"), Nanumea (610), Nui (514), Nukufetau (581), Nukulaelae (341), Vaitupu (1.007) — atóis com "Island Council"; e as reef islands Nanumanga (391), Niutao (550) e Niulakita (36).

**Achado notável sobre nível administrativo**: Tuvalu **não tem hierarquia ADM1/ADM2 distinta** — a ilha/atol é a única subdivisão administrativa formal do país. Registrado `admin_level_used = "1"` por ser o nível mais próximo disponível, mas não é um "ADM1" no sentido de província/região dos demais 10 países — é a única camada subnacional existente. Nome local do nível: **"Island"**, governo local **"Island Council"** ("Town Council" só para Funafuti).

## Nepal (NPL)

Pacote HDX: `cod-ps-npl`. Arquivo: `npl_admpop_adm1_2023.csv` (https://data.humdata.org/dataset/e71f53d9-2339-4df5-b76e-397957ec65dc/resource/f188f906-1647-4655-908f-a6e75bd655f5/download/npl_admpop_adm1_2023.csv) — P-code ADM1 + população total/sexo/faixa etária, ref. 2023. **7 províncias** encontradas: Bagmati (NP03), Gandaki (NP04), Karnali (NP06), Koshi (NP01), Lumbini (NP05), Madhesh (NP02), Sudurpaschim (NP07). Nome exato do nível local: **Province** (Pradesh). Todos os nomes já na convenção pós-reforma de 2015/2017 (nenhum "Province No. X"). Nenhum fetch falhou. Rural não disponível neste nível no arquivo COD-PS.

## Angola (AGO)

Pacote HDX: `cod-ps-ago`. Arquivo: `ago_admpop_adm1_2024.csv` (https://data.humdata.org/dataset/01679d5e-9cf1-45a4-a212-662a2309780c/resource/6a92e532-7c99-4d0d-864b-05ee4599492e/download/ago_admpop_adm1_2024.csv) — P-code ADM1 + população total/sexo/faixa etária, ref. 2024. **18 províncias** encontradas: Bengo, Benguela, Bié, Cabinda, Cuando Cubango, Cuanza Norte, Cuanza Sul, Cunene, Huambo, Huíla, Luanda, Lunda Norte, Lunda Sul, Malanje, Moxico, Namibe, Uíge, Zaire (P-codes AO01–AO18). Nome exato do nível local: **Province** (Província). Dataset COD-PS 2024 (mais recente disponível) lista a contagem tradicional de 18 províncias — sem evidência, nesta fonte, de reorganização territorial adicional. Nenhum fetch falhou. Rural não disponível neste nível.

---

## Resumo consolidado

| País | ISO3 | Unidades ADM1 | Fonte de população | P-code oficial? |
|---|---|---|---|---|
| Sierra Leone | SLE | 5 | HDX cod-ab (fronteira) + Wikipedia/censo 2015 (população) | Sim |
| Zambia | ZMB | 10 | HDX cod-ps (2020) | Sim |
| Guinea-Bissau | GNB | 9 | HDX cod-ab (fronteira) + Wikipedia/censo 2009 (população) | Sim |
| Senegal | SEN | 14 | HDX cod-ps (2022) | Sim |
| Liberia | LBR | 15 | HDX cod-ps (2020) | Sim |
| Gambia | GMB | 8 | HDX cod-ps (2021) | Sim |
| Djibouti | DJI | 6 | HDX cod-ps (2009) | Sim |
| Kiribati | KIR | 3 | HDX cod-ps (2020) | Sim |
| Tuvalu | TUV | 9 | Wikipedia (censo 2022) | Não |
| Nepal | NPL | 7 | HDX cod-ps (2023) | Sim |
| Angola | AGO | 18 | HDX cod-ps (2024) | Sim |

**Total: 104 unidades ADM1** em 11 países.

Rural population: não disponível em nenhum dos 11 países no nível ADM1, com exceção de **Djibouti** (único caso com coluna rural/urbano no dataset COD-PS, `R_TL`). Em todos os demais, a tentativa e o motivo da ausência estão documentados por linha no campo `notes` do CSV.

Nenhum fetch falhou de forma completa (sem nenhum dado) para nenhum dos 11 países — o pior caso foi Tuvalu, que não teve P-code oficial mas teve população via Wikipedia.

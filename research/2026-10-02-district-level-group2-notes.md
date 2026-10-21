# Nível Distrito (ADM2) — Grupo 2: Moçambique, Guiné, Laos, Camboja, Lesoto

Data: 2026-10-02
Entregável: `deliverables/district-level-map-group2.csv` (622 linhas, 5 países)

## Resumo por país

| País | ISO3 | Unidades ADM2 | P-code oficial | Fonte população |
|---|---|---|---|---|
| Moçambique | MOZ | 159 | 159/159 sim | HDX COD-PS (cod-ps-moz) |
| Guiné | GIN | 34 | 34/34 sim | HDX COD-PS (cod-ps-gin) |
| Laos | LAO | 148 | 148/148 sim | HDX COD-PS (cod-ps-lao) |
| Camboja | KHM | 203 (197 oficiais + 6 provisórios) | 197/203 sim | HDX COD-AB (fronteira) + NIS Cambodia (população) |
| Lesoto | LSO | 78 | 78/78 sim | HDX COD-AB (fronteira) + Statoids.com/censo 2006 (população, parcial) |
| **Total** | | **622** | | |

## Moçambique (MOZ) — 159 distritos

- Fonte: HDX `cod-ps-moz`, recurso `moz_admpop_adm2_2025.csv` (projeção 2025, mesma vintage já usada no nível província).
  URL: https://data.humdata.org/dataset/46b79d47-0667-4baa-8d69-468b208855ed/resource/8bbafaba-2ad5-41e6-9df1-34b25fa915f0/download/moz_admpop_adm2_2025.csv
- `parent_pcode` = `ADM1_PCODE` da própria fonte, conferido contra `province-level-map.csv` — bate 100%.
- `local_unit_type` = "Distrito" (nome oficial moçambicano do nível, incluindo "Cidade de Pemba" etc. que mantêm status de distrito nesta fonte).
- **4 distritos com população "NA" na própria fonte** (não é omissão nossa, é o valor literal do arquivo COD-PS): Ilha Licom (MZ0804), Ilha Risunodo (MZ0805) e Lago Niassa (MZ0807), todos em Niassa (provavelmente ilhas/corpo d'água do Lago Niassa com população resident muito baixa ou não leventada nesta rodada), e Maquival (MZ1112) em Zambézia. Campo `population` deixado em branco, `notes` registra o "NA" da fonte.
- Sem quebra rural/urbano neste nível (mesmo padrão já visto no nível província — a fonte só desagrega por idade/sexo).

## Guiné (GIN) — 34 prefeituras

- Fonte: HDX `cod-ps-gin`, recurso `gin_admpop_adm2_2024.csv` (projeção 2024).
  URL: https://data.humdata.org/dataset/944d6072-f333-4da5-87a7-7516f197a7c2/resource/c71ff241-76c6-4b36-a012-c808ddb0dd95/download/gin_admpop_adm2_2024.csv
- `local_unit_type` = "Préfecture" (nome oficial guineense do ADM2), exceto Conakry que é tratada como unidade única na fonte (capital, pop. 2.211.435) — nota registrada explicando que administrativamente Conakry tem 5 comunas urbanas (ADM3), fora do escopo desta tarefa.
- `parent_pcode` confere 100% com as 8 regiões já no `province-level-map.csv`.
- Sem rural/urbano disponível na fonte.

## Laos (LAO) — 148 distritos

- Fonte: HDX `cod-ps-lao`, recurso `lao_admpop_adm2_2024.csv` (projeção 2024).
  URL: https://data.humdata.org/dataset/f9ec8c86-e300-443b-bd04-a6c9923c29ef/resource/87e60232-7af8-43c3-bc47-685f2a770ab1/download/lao_admpop_adm2_2024.csv
- `local_unit_type` = "District" (Muang).
- `parent_pcode` confere 100% com as 18 províncias já no `province-level-map.csv`.
- Sem rural/urbano disponível na fonte.

## Camboja (KHM) — 203 unidades (197 oficiais + 6 provisórios)

Caso mais trabalhoso do lote: `cod-ps-khm` só publica população em bulk até **ADM1** (não tem arquivo `..._admpop_adm2_...`). Método usado:

1. **Fronteira/P-code**: `cod-ps-khm` → recurso `KHM_AdminBoundaries_TabularData.xlsx` (aba `ADM2`) — 197 distritos oficiais com P-code (ex. `KH0205`) e `ADM1_PCODE` pai.
   URL: https://data.humdata.org/dataset/770386b0-d7c6-4ea7-abbc-beccac38c192/resource/2b98698e-2d94-41d4-9adc-99dd0024a8ce/download/khm_adminboundaries_tabulardata.xlsx
2. **População**: como não há COD-PS em ADM2, foi usada a fonte primária nacional — National Institute of Statistics (NIS) Cambodia, relatório **"District Population Projection 2020-2033 Based on Age Restructure of National Population Projection 2019-2050 and CDHS 2021-22"** (julho 2023), tabela 4.1 a 4.25 (uma por província), coluna total do ano **2025** extraída.
   URL: https://www.nis.gov.kh/nis/Population%20Projection/Cambodia_District_Population_Projection_2020-2023.pdf
3. **Casamento por nome**: a grafia do PDF da NIS difere da grafia oficial do COD-AB em dezenas de casos (ex. "Krong Bat Dambang" = "Battambang"; "Krong X" = capital do distrito X; variações como "Phnum"/"Phnom", "Rukh Kiri"/"Rukhak Kiri", apóstrofos removidos). Reconciliado manualmente nome a nome — **196 dos 197 distritos oficiais casados com população**.
4. **1 distrito oficial sem população encontrada**: **Saen Monourom** (`KH1105`, capital de Mondul Kiri) — a tabela 4.11 da NIS lista só 4 dos 5 distritos oficiais da província, Saen Monourom simplesmente não aparece em nenhuma das 93 páginas do PDF. Não foi feita estimativa por diferença contra o total provincial (regra de não inventar número) — campo em branco.
5. **6 unidades extras sem P-code oficial** (presentes na tabela da NIS, ausentes do COD-AB de 2018, mesmo padrão "fronteira atrasada atrás de redistritamento" já visto em Ayalagaya/TZA e Atauro/TLS): `Taing Kouk` (Kampong Thom), `Boeng Keng Kang` e `Kambol` (Phnom Penh — reorganização de khans pós-2018), `Ta Lou Sen Chey` (Pursat), `Koh Rung` (Preah Sihanouk), `Borei OSvay Sen Chey` (Stung Treng). Recebem ID provisório `<p-code-provincia>-PROV<n>` — usando a província como pai, não o distrito-irmão exato de origem do desmembramento (não verificado contra fonte cartográfica nesta rodada, fica como gap conhecido).
6. `local_unit_type` = "Khan" para Phnom Penh, "Srok (Distrito)" para as demais.
7. Sem rural/urbano disponível.

## Lesoto (LSO) — 78 community/urban councils

Caso mais incerto do lote — sinalizado para possível aprofundamento futuro:

1. **Fronteira/P-code**: `cod-ab-lso`, arquivo `lso_adm_FAO_MLGCA_2019_FIS.xls`, aba `lso_admbnda_adm2_FAO_MLGCA_2019` — **78 unidades** (community councils + urban councils pós-reforma de governo local de 2017), com P-code tipo `LSG01` e distrito-pai (já confirmado = nível província/distrito do `province-level-map.csv`).
   URL: https://data.humdata.org/dataset/55b1367e-667a-447b-952d-5bb139835628/resource/f94ad63f-b7ff-4a85-a1de-e828384a545d/download/lso_adm_fao_mlgca_2019_fis.xls
2. **População**: `cod-ps-lso` só tem ADM0/ADM1 (confirmado, sem arquivo ADM2). Única fonte estruturada encontrada com população por community council é **Statoids.com, "Councils of Lesotho"** (http://www.statoids.com/yls.html) — compilação de terceiros a partir do **censo 2006**, listando **129 community councils** (antes da reforma de 2017, que reduziu/reorganizou os councils para o número atual de 78 — incluindo a criação de "Urban Councils" separados para as vilas-sede de distrito).
3. **Casamento por nome, pré-reforma → pós-reforma**: só **36 dos 78 councils atuais** têm correspondência de nome exata com a lista de 2006 — **42 ficam em branco**, majoritariamente os novos Urban Councils (ex. "Maseru (Maseru District)", "Mafeteng", "Butha-Buthe (Butha-Buthe District)") que não existiam como unidade separada em 2006, ou councils renomeados/fundidos sem equivalente 1:1 óbvio.
4. Onde casado, a população é de **2006** (20 anos desatualizada, pré-reforma) — marcado explicitamente em `population_data_year=2006` e nota de limitação. Não foi feita atualização/projeção pro-rata (evitar número inventado).
5. Nenhuma tabela oficial pós-2017 com população por council foi localizada nesta pesquisa — nem no Bureau of Statistics Lesotho (`bos.gov.ls`), nem em fontes agregadoras. **Recomendação**: se este país virar alvo prioritário, vale um request direto ao BOS Lesotho ou tentar o microdado do censo 2016 (que tem variável "Community Council" por registro individual, segundo o catálogo IHSN) para recalcular população por council atual — fora do escopo de bulk-fetch desta tarefa.
6. `local_unit_type`: "Urban Council" para as 12 unidades identificadas como vila-sede de distrito (nome igual ou "(Nome District)"), "Community Council" para as demais 66.

## Falhas e gaps conhecidos (resumo)

- MOZ: 4 distritos com população "NA" na própria fonte (Niassa x3, Zambézia x1).
- KHM: 1 distrito oficial sem população (Saen Monourom); 6 unidades com população mas sem P-code oficial confirmado (ID provisório, pai = província, não o distrito-irmão exato).
- LSO: 42 de 78 councils sem população (reforma de 2017 sem fonte estruturada pós-reforma encontrada).
- Nenhum dos 5 países tem rural/urbano disponível neste nível (mesmo gap já documentado no nível província).

## Validação de consistência feita

- Zero `unit_id` duplicado nas 622 linhas.
- Todos os `parent_pcode` conferidos contra `deliverables/province-level-map.csv` (MOZ, GIN, LAO, KHM, LSO) — 100% de match para as unidades com P-code oficial.

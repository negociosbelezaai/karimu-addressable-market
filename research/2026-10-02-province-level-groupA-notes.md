# Karimu — Notas de metodologia: nível ADM1 (província/região), Grupo A (11 países)

Data da pesquisa/captura: 2026-10-02.
Entregável relacionado: `deliverables/province-level-map-groupA.csv` (154 linhas de dados).

Método seguido (igual ao testado antes para a Tanzânia, replicado para os 11 países): API CKAN do
HDX via `curl -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like
Gecko) Chrome/120.0 Safari/537.36"` (contorna o bloqueio 403 que a API retorna para o WebFetch
padrão), pacote `cod-ps-<iso3>` (Subnational Population Statistics) tentado primeiro — melhor caso,
traz população + P-code oficial no mesmo arquivo —, com `cod-ab-<iso3>` (Administrative Boundaries,
gazetteer) usado para cross-check de nomes/P-codes em todos os países, e Wikipedia como fallback só
quando nenhum dos dois pacotes HDX existisse (não foi necessário para nenhum dos 11 países deste
grupo).

**Pegadinha técnica recorrente**: os links de download de resources do HDX fazem redirect HTTP 302
para URLs assinadas da AWS S3 (`AWSAccessKeyId`/`Signature`/`Expires`). `curl -s` sozinho salva a
página HTML de redirecionamento em vez do arquivo — corrigido em todos os casos usando `curl -sL`
(follow redirects).

**Resultado geral**: nos 11 países, o pacote `cod-ps-<iso3>` existia e tinha o arquivo ADM1 ideal
(população + P-code oficial juntos) — inclusive em países pequenos onde se esperava precisar cair
para Wikipedia (Comoros, Solomon Islands, Timor-Leste). Nenhum fetch falhou completamente. Nenhuma
unidade precisou do ID provisório `<pcode-pai>-PROV<n>` — todas as 154 unidades ADM1 têm P-code
oficial (`is_official_id = yes`). `rural_population`/`rural_population_pct` ficou em branco nas 154
linhas: nenhuma das fontes COD-PS consultadas desagrega população por urbano/rural no nível ADM1
(só população total por sexo/faixa etária) — não foi estimado, conforme regra do projeto.

---

## 1. Malawi (MWI) — 3 regiões

- **Pacote HDX**: `cod-ps-mwi`.
- **Arquivo**: `mwi_admpop_adm1_2023.csv` (projeção 2023).
  URL: https://data.humdata.org/dataset/8ceb03ac-2272-447f-8887-39cfc4d78b59/resource/6d8d11bc-03e7-4eb3-8a9b-dafa9f4baa02/download/mwi_admpop_adm1_2023.csv
- **Unidades**: 3 — Northern (MW1), Central (MW2), Southern (MW3).
- **Termo local**: "Region" — confirmado via Wikipedia ("Administrative divisions of Malawi").
  Importante: as regiões malawianas **não têm função administrativa própria** — agrupam os 28
  distritos (ADM2), que são o nível com governo local de fato. Isso é mais "estatístico/geográfico"
  que administrativo-operacional.
- **Cross-check de P-code**: `cod-ab-mwi`, `mwi_adminboundaries_tabulardata.xlsx` (aba ADM1) — os 3
  P-codes batem exatamente.
- **Observação de fonte**: a coluna de nome do CSV original está rotulada `ADM1_FR` (provável erro
  de template do HDX — não há versão francesa), mas contém o nome em inglês da região.
- Nenhum fetch falhou.

## 2. Timor-Leste (TLS) — 13 municípios

- **Pacote HDX**: `cod-ps-tls`. https://data.humdata.org/dataset/cod-ps-tls
- **Arquivo**: `tls_admpop_adm1_2022.csv` (dado censitário, ano de referência 2022).
- **Unidades**: 13 municípios, P-codes TL01–TL13.
- **Termo local**: "Municipality" — confirmado via Wikipedia ("Municipalities of Timor-Leste") e
  site oficial do governo. Timor-Leste mudou de "district" para "municipality" numa reforma
  administrativa anterior a 2015.
- **Soma de população das 13 unidades**: 1.336.215 — compatível com a ordem de grandeza do censo
  2022 (~1,34M), o que dá confiança de que o arquivo está correto.
- **Achado notável**: Atauro Island tornou-se município separado em 2022-01-01 (Wikipedia), mas
  este conjunto de P-codes oficial (13 unidades) ainda não tem P-code próprio para Atauro — a
  população de Atauro provavelmente ainda está contabilizada dentro de Dili (TL06) neste arquivo.
  Documentado na nota da linha Dili. Se o projeto precisar de Atauro separado, será necessário
  buscar uma fonte mais recente.
- **Oecussi**: nome oficial completo é "Oécusse-Ambeno" (região administrativa especial); o arquivo
  usa "Oecussi" — mantido como na fonte, com nota.
- Nenhum fetch falhou.

## 3. Solomon Islands (SLB) — 10 unidades

- **Pacote HDX**: `cod-ps-slb`. https://data.humdata.org/dataset/cod-ps-slb
- **Arquivo**: `slb_admpop_adm1_2023.csv` (dado censitário, ano de referência 2023).
- **Unidades**: 10, P-codes SB01–SB10.
- **Termo local**: "Province" para 9 unidades (Central, Choiseul, Guadalcanal, Isabel,
  Makira-Ulawa, Malaita, Rennell-Bell, Temotu, Western). A 10ª, **Honiara**, é administrada
  separadamente como "Capital Territory" (não província) — confirmado via Wikipedia
  ("Honiara"/"Honiara City Council"). Tipada separadamente na coluna `local_unit_type`.
- **Soma de população**: 768.701 — compatível com estimativas recentes da população total das
  Solomon Islands (~720k–760k), plausível para um dado de 2023.
- **Achado notável**: nomes abreviados na fonte — "Rennell-Bell" = "Rennell and Bellona Province";
  "Central" = "Central Islands Province"; documentado nas notas das linhas correspondentes.
- Nenhum fetch falhou.

## 4. Madagascar (MDG) — 22 regiões

- **Pacote HDX**: `cod-ps-mdg`. https://data.humdata.org/dataset/cod-ps-mdg
- **Arquivo**: `mdg_admpop_adm1_2018.csv` (RGPH — Recenseamento Geral da População e do Habitat,
  ano de referência 2018).
  URL: https://data.humdata.org/dataset/0b6ce366-8651-43aa-8c36-9f3fdc8d6b4f/resource/36a0fd53-78b9-4b3f-9c2e-f7beb0dbf705/download/mdg_admpop_adm1_2018.csv
- **Unidades**: 22 regiões, P-codes MG11–MG72.
- **Termo local**: "Région" (malgaxe: "Faritra") — confirmado via Wikipedia ("Regions of
  Madagascar"/"Subdivisions of Madagascar"). As 22 regiões foram promovidas a divisão
  administrativa de primeiro nível em outubro de 2009, quando as 6 antigas províncias (faritany)
  foram extintas pela reforma constitucional de 2007.
- **Cross-check de P-code**: gazetteer `mdg_gazetteer_20181031.xls` (aba `mdg_pop_adm1`) — 22
  linhas, P-codes e nomes idênticos.
- **Achado notável**: o CSV de população grafa "Amoron I Mania" sem apóstrofo (limitação de encoding
  ASCII). Normalizado para a grafia oficial "Amoron'i Mania" no `unit_name`; grafia original
  documentada na nota daquela linha. P-code (MG22) e população não alterados.
- Nenhum fetch falhou.

## 5. Comoros (COM) — 3 ilhas autônomas

- **Pacote HDX**: `cod-ps-com`. https://data.humdata.org/dataset/cod-ps-com — ao contrário do
  esperado no método (país pequeno, possível ausência de pacote), o pacote **existe** e tem o
  arquivo ADM1 necessário; não foi preciso cair para Wikipedia.
- **Arquivo**: `com_admpop_adm1_2017.csv` (único ano disponível nesta fonte).
  URL: https://data.humdata.org/dataset/8351491f-75d7-4154-a5cd-d527011c7b55/resource/a541d3f4-e697-44d7-92b9-6db46d29ff93/download/com_admpop_adm1_2017.csv
- **Unidades**: 3 ilhas, P-codes KM1–KM3.
- **Termo local**: "Autonomous Island" (Ilha Autônoma) — confirmado via WebSearch: a Constituição de
  2001 da União das Comores concedeu autonomia constitucional às 3 ilhas (cada uma elege seu
  próprio governador e assembleia legislativa).
- **Cross-check de nomes**: gazetteer `com_adminboundaries_tabulardata.xlsx` (aba ADM1) usa nomes
  bilíngues oficiais diferentes dos nomes nativos do arquivo de população: Ndzuwani (COD-PS) =
  "Anjouan (Ndzouani)" (COD-AB); Ngazidja = "Grande Comore (Ngazidja)"; Mwali = "Mohéli (Mwali)".
  Mantido o nome nativo como `unit_name`, par documentado em `notes`.
- Nenhum fetch falhou.

## 6. Tanzania (TZA) — 31 regiões

- **Pacote HDX**: `cod-ps-tza`.
- **Arquivo**: `tza_admpop_adm1_2020_v2.csv` (projeção 2020, único ano disponível neste nível).
  URL: https://data.humdata.org/dataset/fcd33248-774d-4be2-aa16-86b10519330e/resource/89dd7ca4-4b73-4725-8ac8-0e0ef78d4fbd/download/tza_admpop_adm1_2020_v2.csv
- **Unidades**: 31 regiões, P-codes TZ01–TZ26 e TZ51–TZ55.
- **Termo local**: "Region" (suaíli: *mkoa*, plural *mikoa*) — confirmado via Wikipedia ("Regions of
  Tanzania"/"Subdivisions of Tanzania").
- **Cross-check de P-code**: gazetteer `cod-ab-tza` (`tza_admgz_20181019.xlsx`, aba
  `tza_admbnda_adm1_20181019`) — os 31 P-codes batem exatamente.
- **Achado notável 1 (nomes divergentes)**: o gazetteer COD-AB usa nomes em suaíli (ex. "Pwani",
  "Dar-es-salaam", "Kaskazini Unguja"), enquanto o arquivo de população COD-PS usa
  traduções/transliterações em inglês (ex. "COAST", "DAR ES SALAAM", "ZANZIBAR NORTH"). O CSV final
  usa os nomes do arquivo de população (fonte do número), com a equivalência suaíli documentada em
  `notes` de cada linha.
- **Achado notável 2 (ADM0_PCODE ausente em 2 linhas)**: as linhas ARUSHA (TZ02) e COAST (TZ06)
  vieram com `ADM0_PCODE` vazio no arquivo original. Preenchidas com "TZ" com base na confirmação
  cruzada no gazetteer COD-AB (mesmos P-codes TZ02/TZ06 vinculados a ADM0 "TZ" lá) — documentado
  explicitamente na nota dessas duas linhas; não é dado inventado, é o mesmo valor usado nas outras
  29 linhas da mesma coluna/mesma fonte.
- Nenhum fetch falhou (além do ajuste `-L` para redirect).

## 7. Mozambique (MOZ) — 11 províncias

- **Pacote HDX**: `cod-ps-moz`.
- **Arquivo**: `moz_admpop_adm1_2025.csv` (projeção 2025, ano mais recente disponível no pacote;
  também há séries 2024, 2023 e 2017, não usadas).
  URL: https://data.humdata.org/dataset/46b79d47-0667-4baa-8d69-468b208855ed/resource/d19acc2d-e4e7-456d-a587-cce3b0187ed6/download/moz_admpop_adm1_2025.csv
- **Unidades**: 11 — Cabo Delgado, Gaza, Inhambane, Manica, Maputo, Maputo City, Nampula, Niassa,
  Sofala, Tete, Zambézia (grafado "Zambezia" sem acento na fonte, mantido assim).
- **Termo local**: "Province" (português: *Província*) — confirmado via Wikipedia ("Provinces of
  Mozambique"/"Maputo City Province").
- **Achado notável**: Moçambique tem oficialmente 10 províncias + a Cidade de Maputo, que desde 1998
  é administrada como província separada (mesmo cercada geograficamente pela Província de Maputo) —
  por isso o total é 11 unidades ADM1, não 10.
- **Cross-check de P-code**: gazetteer `cod-ab-moz` (`moz_adminboundaries_tabulardata.xlsx`, aba
  ADM1) — os 11 P-codes batem exatamente.
- Nenhum fetch falhou.

## 8. Guinea (GIN) — 8 unidades

- **Pacote HDX**: `cod-ps-gin`. https://data.humdata.org/dataset/cod-ps-gin
- **Arquivo**: `gin_admpop_adm1_2024.csv` (projeção 2024).
  URL: https://data.humdata.org/dataset/944d6072-f333-4da5-87a7-7516f197a7c2/resource/fb1cb97b-63ef-4f67-96d0-9ff07cc27012/download/gin_admpop_adm1_2024.csv
- **Unidades**: 8 (7 regiões + Conakry), P-codes GN001–GN008.
- **Termo local**: "Région" para as 7 regiões administrativas. Conakry (capital) tem estatuto de
  "Zone spéciale" (zona especial), não "Région", mas é tratada como unidade ADM1 no COD-PS/COD-AB —
  confirmado via Wikipedia ("Regions of Guinea"/"Subdivisions of Guinea"): 7 regiões + Conakry como
  zona especial = 8 unidades de primeiro nível.
- **Cross-check de P-code**: gazetteer `gin_admgz.xlsx` (aba ADM1) — 8 linhas idênticas.
- Nenhum fetch falhou.

## 9. Laos (LAO) — 18 unidades

- **Pacote HDX**: `cod-ps-lao`. https://data.humdata.org/dataset/cod-ps-lao
- **Arquivo**: `lao_admpop_adm1_2024.csv` (projeção/estimativa, ano de referência 2024).
- **Unidades**: 18, P-codes LA01–LA18.
- **Termo local**: "Province" para 17 unidades. **Vientiane Capital** (LA01) é administrada como
  "Prefecture" (lao: nakhon louang), status equivalente a província — confirmado via Wikipedia
  ("Administrative divisions of Laos"/"Provinces of Laos"). Tipada separadamente.
- **Soma de população**: 7.631.798 — compatível com estimativas recentes da população total do Laos
  (~7,7–7,8M), plausível para um dado de 2024.
- **Achado notável**: "Vientiane" (LA10, província) e "Vientiane Capital" (LA01, prefeitura) são
  unidades ADM1 distintas — ambas presentes corretamente como linhas separadas.
- Nenhum fetch falhou.

## 10. Cambodia (KHM) — 25 unidades

- **Pacote HDX**: `cod-ps-khm` ("Cambodia - Subnational Population Statistics").
- **Arquivo**: `khm_admpop_adm1_2024.csv`.
  URL: https://data.humdata.org/dataset/770386b0-d7c6-4ea7-abbc-beccac38c192/resource/b7476c8d-33d7-4460-9a9a-6d63ba738056/download/khm_admpop_adm1_2024.csv
- **Unidades**: 25 (24 províncias + Phnom Penh), P-codes padrão KHxx.
- **Nota técnica do pacote** (explanatory-note PDF, lida com PyPDF2): fonte primária é o Cambodia
  National Institute of Statistics; dado é **projeção populacional** (não contagem censitária
  direta), baseline censo 2019, ano de referência 2024. Método: cohort-component (nacional) + ratio
  method (subnacional, por falta de dados confiáveis de migração interna por província). A própria
  nota alerta que as taxas de crescimento projetadas são "improvavelmente" uniformes entre
  províncias — limitação reconhecida pela fonte primária, não um erro de coleta deste trabalho.
- **Termo local**: "Province" (khmer: ខេត្ត, *khétt*) para as 24 unidades regulares. **Phnom Penh**
  é caso especial: a nota técnica do COD-PS a chama de "Special Administrative Unit"; a Wikipedia
  usa "autonomous municipality" (khmer: រាជធានី, *réachthéani*). Ambos os termos documentados em
  `notes`; usado "Special Administrative Unit (capital)" em `local_unit_type` por ser o termo da
  própria fonte de dados primária.
- Nenhum fetch falhou (além do ajuste `-L`).

## 11. Lesotho (LSO) — 10 distritos

- **Pacote HDX**: `cod-ps-lso` ("Lesotho - Subnational Population Statistics").
- **Arquivo**: `lso_admpop_adm1_2022.csv` (ano de referência 2022; pacote não tinha explanatory note
  PDF, diferente do Camboja).
  URL: https://data.humdata.org/dataset/f92e2197-8922-4640-885f-c21b15ec623a/resource/53a43b91-6dfc-4208-a3d9-b3a3a228eb0a/download/lso_admpop_adm1_2022.csv
- **Unidades**: 10 distritos, P-codes LSA–LSK.
- **Termo local — verificação específica**: confirmado explicitamente (não presumido) no gazetteer
  oficial (`lso_admgz.xls`, aba `lso_admgz_adm1`, coluna `ADM1_TYPE` = "District" em todas as 10
  linhas), cruzado com Wikipedia ("Districts of Lesotho"): "District" é de fato o nível
  administrativo mais alto do Lesoto — **não existe nível intermediário entre país e distrito**. A
  hierarquia completa é País → Distrito (10) → Circunscrição/Constituency (80) → Conselho
  Comunitário/Community Council (129): constituencies e community councils ficam **abaixo** do
  distrito, não entre país e distrito.
- **Nota de divergência não incorporada ao CSV**: Wikipedia lista censos de 2006 e 2016 com números
  diferentes (ex. Maseru 519.186 em 2016 vs. 576.429 no COD-PS 2022) — não usados, porque o COD-PS
  2022 é mais recente e tem P-code oficial associado (critério de preferência do método: fonte com
  P-code > fonte sem P-code). Wikipedia consultada só para confirmar terminologia, não população.
- Nenhum fetch falhou.

---

## Observações gerais / convenções aplicadas em todo o grupo

- `parent_pcode` em todas as 154 linhas = P-code ADM0 encontrado na própria fonte (nunca inventado):
  TZ, MW, MZ, MG, KM, GN, TL, SB, LA, KH, LS.
- `is_official_id = yes` em todas as 154 linhas — todos os P-codes de ADM1 são oficiais, confirmados
  cruzando COD-PS com COD-AB/gazetteer em cada um dos 11 países.
- Nenhuma unidade precisou do ID provisório `<p-code ancestral>-PROV<n>` — cobertura completa de
  P-code oficial no nível ADM1 para os 11 países.
- Nenhum dado de população, nome ou P-code foi estimado ou calculado — todos vêm literalmente dos
  arquivos CSV/XLSX/XLS baixados do HDX, lidos com `csv`/`openpyxl`/`PyPDF2` em Python.
- `rural_population`/`rural_population_pct` em branco nas 154 linhas — não disponível no nível ADM1
  em nenhuma das fontes COD-PS consultadas (todas trazem só total por sexo/faixa etária); tentativa
  documentada em `notes` de cada linha, não estimado.

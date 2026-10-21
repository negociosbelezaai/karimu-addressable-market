# Enumeração de wards — Tanzânia, Grupo 3 (Kagera, Mwanza, Manyara, Rukwa, Dar es Salaam)

Data: 2026-10-03
Entregável: `deliverables/ward-enum-tza-group3.csv`
Método: mesmo de `research/2026-10-02-ward-level-pilot-summary.md` (Babati) — fonte de população: citypopulation.de, tabela "com wards" por distrito, Census 2022-08-23. Gazetteer oficial: HDX `cod-ab-tza` (`tza_admbnda_adm3_20181019`), extraído para `/tmp/karimu_g3/gazetteer.json` nesta sessão.

Babati (TZ2101) NÃO está neste arquivo — já consta em `deliverables/ward-level-pilot.csv`, conforme instrução.

## Achado estrutural novo neste grupo (não visto em Babati): distritos reorganizados pós-2018

Em 3 distritos, o "distrito" que o nosso gazetteer oficial (fronteira 2018) e a população já registrada descrevem **não existe mais como unidade única** na estrutura atual do censo 2022 — foi desmembrado em 2+ unidades administrativas novas. Isso é uma escala acima do fenômeno já visto em Babati (lá, só wards individuais eram novas; aqui, o próprio distrito mudou de fronteira).

- **Dar es Salaam** (esperado pelo método, documentado nas instruções da task): Kinondoni (TZ0701) e Temeke (TZ0703) viraram 2 municípios atuais cada (Kinondoni Municipal+Ubungo Municipal; Temeke Municipal+Kigamboni Municipal). Ilala (TZ0702) permanece 1:1 com "Dar es Salaam City" no site atual. **Reconstituí cada distrito antigo somando as wards das páginas atuais** — ver seção Dar es Salaam abaixo.
- **Mbulu** (Manyara, TZ2103) — **achado novo, não documentado antes de rodar**: a página atual `2103__mbulu_rural` só lista 18 wards, mas o gazetteer tem 32. Confirmado por fetch adicional que NÃO é truncamento de tabela (pedi explicitamente por nomes específicos do gazetteer ausente — nenhum apareceu). Indício forte de que existe um "Mbulu Town/Mjini" (town council) criado depois de 2018 que ficou com as ~16 wards ausentes, só que essa unidade não está no escopo desta task (não foi listada nos distritos do grupo) — não foi buscada.
- **Sengerema** (Mwanza, TZ1905) — mesmo padrão: só 26 de 34 wards do gazetteer aparecem na página atual; a soma de wards (425.415) é ~51% da população já registrada (867.932). Tanzânia criou o distrito de **Buchosa** a partir de Sengerema (visível no índice da região Mwanza, código 1908, fora do escopo desta task) — explica a diferença.

Nos dois casos (Mbulu, Sengerema) **não tentei buscar o distrito novo** (Mbulu Town / Buchosa) por estar fora do escopo definido pela task — fica registrado aqui como gap conhecido para uma eventual Fase 2 "Tanzânia distritos novos pós-2018", que provavelmente afeta outros grupos também.

## Por distrito

### Região KAGERA
| Distrito | Wards achadas | Oficiais | Provisórias | Soma pop. wards | Pop. já registrada | Diferença |
|---|---|---|---|---|---|---|
| Karagwe (TZ1801) | 23 | 22 | 1 (Kamagambo) | 385.744 | 514.498 | -25,0% |
| Bukoba (TZ1802) | 29 | 28 | 1 (Kyaitoke) | 322.448 | 352.127 | -8,4% |
| Muleba (TZ1803) | 42 | 42 | 0 | 631.309 | 731.109 | -13,7% |
| Biharamulo (TZ1804) | 17 | 15 | 2 (Katahoka, Nyanza) | 457.114 | 587.544 | -22,2% |
| Ngara (TZ1805) | 22 | 20 | 2 (Kibogora, Nyamagoma) | 383.092 | 324.191 | +18,2% |
| Bukoba Municipal (TZ1806) | 14 | 14 | 0 | 144.938 | 192.389 | -24,7% |
| Missenyi (TZ1807) | 20 | 20 | 0 | 245.394 | 267.161 | -8,1% |
| Kyerwa (TZ1808) | 24 | 18 | 6 (Bugara, Iteera, Kakanja, Kitwe, Kitwechenkura, Nyaruzumbura) | 412.910 | 451.170 | -8,5% |

Notas específicas:
- **Karagwe**: maior divergência do grupo (-25%). Soma de wards bate exatamente com o "total do distrito" mostrado na própria página de wards (385.744) — ou seja, não é erro de soma, é a população já registrada (514.498, de outra fonte/vintage) que diverge da fonte censitária usada aqui. Mesmo padrão de divergência projeção-vs-censo já visto em Babati.
- **Muleba**: ward "Buhangaza" do gazetteer oficial não aparece na fonte censitária atual — não identificada sob outra grafia nem como fusão óbvia.
- **Bukoba (rural)**: ward "Butulage" do gazetteer não aparece na fonte atual; ward nova "Kyaitoke" aparece sem ward-mãe identificável — usado o distrito como ancestral.
- **Kyerwa**: maior crescimento proporcional do grupo (18→24 wards, +33%).

### Região MWANZA
| Distrito | Wards achadas | Oficiais | Provisórias | Soma pop. wards | Pop. já registrada | Diferença |
|---|---|---|---|---|---|---|
| Ukerewe (TZ1901) | 25 | 24 | 1 (Kakukuru) | 387.815 | 443.073 | -12,5% |
| Magu (TZ1902) | 25 | 18 | 7 (Buhumbi, Bujora, Chabula, Isandula, Itumbili, Kabila, Kandawe) | 421.119 | 370.502 | +13,7% |
| Nyamagana (TZ1903) | 18 | 12 | 6 (Kishili, Luchelele, Lwanhima, Mabatini, Mhandu, Nyegezi) | 594.834 | 566.150 | +5,1% |
| Kwimba (TZ1904) | 30 | 30 | 0 | 480.025 | 522.169 | -8,1% |
| Sengerema (TZ1905) | 26 | 20 | 6 (Bitoto, Ibondo, Kahumulo, Mission, Ngoma, Nyamizeze) | 425.415 | 867.932 | **-51,0%** |
| Ilemela (TZ1906) | 19 | 9 | 10 (Buzuruga, Ibungilo, Kahama, Kawekamo, Kayenze, Kiseke, Mecco, Nyamhongolo, Nyasaka, Shibula) | 509.687 | 428.485 | +19,0% |
| Misungwi (TZ1907) | 27 | 25 | 2 (Buhunda, Isenengeja) | 467.867 | 467.964 | -0,02% |

Notas específicas:
- **Sengerema**: ver "achado estrutural" acima — distrito Buchosa foi desmembrado, explica -51%.
- **Magu, Ilemela**: crescimento grande de wards (Magu 18→25, +39%; Ilemela 9→19, +111%) sem indício de fusão/perda — parece crescimento orgânico de wards, não redistritamento.
- **Nyamagana**: soma bate exatamente com o total mostrado na página atual ("Mwanza City" 594.834) — mas diverge da população já registrada (566.150, vintage diferente).
- **Misungwi**: wards "Ilalambogo" e "Isesa" do gazetteer não aparecem na fonte atual; melhor consistência do grupo (-0,02%).

### Região MANYARA (exceto Babati, já feito)
| Distrito | Wards achadas | Oficiais | Provisórias | Soma pop. wards | Pop. já registrada | Diferença |
|---|---|---|---|---|---|---|
| Hanang (TZ2102) | 33 | 25 | 8 (Dawar, Dumbeta, Endagaw, Garawja, Ishponga, Jorodom, Mulbadaw, Wareta) | 367.391 | 365.468 | +0,5% |
| Mbulu (TZ2103) | 18 | 16 | 2 (Endahagichan, Labay) | 238.272 | 424.795 | **-43,9%** |
| Simanjiro (TZ2104) | 18 | 17 | 1 (Langai) | 291.169 | 224.085 | +29,9% |
| Kiteto (TZ2105) | 23 | 19 | 4 (Bwawani, Kaloleni, Laiseri, Ndirgishi) | 352.305 | 375.056 | -6,1% |
| Babati Town (TZ2106) | 8 | 8 | 0 | 129.572 | 103.789 | +24,8% |

Notas específicas:
- **Mbulu**: ver "achado estrutural" acima — 16 wards do gazetteer oficial (quase metade do distrito) não aparecem na fonte atual, consistente com a criação de um "Mbulu Town Council" separado pós-2018, fora do escopo desta task.
- **Hanang**: maior contagem de wards novas em termos absolutos do grupo (25→33, +32%), mas soma de população quase idêntica à já registrada (+0,5%) — sugere que a população já registrada para este distrito já usava o censo 2022 como fonte.
- **Babati Town**: 8/8 wards batem perfeitamente com o gazetteer, sem nenhuma nova — único distrito do grupo (fora Babati Rural, já feito) com correspondência 1:1 total.

### Região RUKWA
_Processado por agente paralelo (fork) — ver seção ao final deste documento quando concluído, ou `deliverables/ward-enum-tza-group3.csv` filtrando `parent_pcode` TZ1501/TZ1502/TZ1503/TZ1504._

### Região DAR ES SALAAM (reconstituída sob fronteiras antigas 2018)
| Distrito (fronteira 2018) | Páginas atuais usadas | Wards achadas | Oficiais | Provisórias | Soma pop. wards | Pop. já registrada | Diferença |
|---|---|---|---|---|---|---|---|
| Kinondoni (TZ0701) | Kinondoni Municipal + Ubungo Municipal | 34 | 34 | 0 | 2.069.240 | 2.698.552 | -23,3% |
| Ilala (TZ0702) | "Dar es Salaam City" (= Ilala atual) | 36 | 26 | 10 (Bonyokwa, Buyuni, Kipunguni, Kisukuru, Liwiti, Minazi Mirefu, Mnyamani, Mzinga, Pugu Station, Zingiziwa) | 1.649.912 | 2.103.669 | -21,6% |
| Temeke (TZ0703) | Temeke Municipal + Kigamboni Municipal | 32 | 30 | 2 (Kibondemaji, Kilungule) | 1.664.576 | 2.235.356 | -25,5% |

Notas específicas:
- **Reconstituição**: Dar es Salaam reorganizou seus distritos pós-2018 criando Ubungo Municipal (a partir de Kinondoni) e Kigamboni Municipal (a partir de Temeke) — ambos fora do escopo original da task, mas incluídos aqui *dentro* de Kinondoni/Temeke (somando as wards das páginas atuais) para bater com a fronteira 2018 do gazetteer e com a população já registrada. Ilala não foi dividido — a página atual "Dar es Salaam City" é o próprio Ilala.
- **Match perfeito de fronteira**: Kinondoni reconstituído bateu 34/34 com o gazetteer (nenhuma ward nova, nenhuma perdida) — a soma das duas páginas atuais reproduz exatamente a fronteira 2018, só a contagem populacional mudou (divergência explicada por vintage/metodologia, não por fronteira).
- **Divergência de população uniforme** (~-21% a -26% nos 3 distritos) é bem maior e mais consistente que nos outros grupos — population já registrada parece ser de uma fonte/ano diferente do censo 2022 usado aqui (possivelmente projeção anterior ou número de outra tabela de origem).

## Falhas de fonte
Nenhuma falha completa de distrito neste grupo (diferente de uma possível falha esperada). Todas as 23 páginas de wards consultadas (8 Kagera + 7 Mwanza + 5 Manyara + 5 páginas Dar es Salaam, excluindo Rukwa) carregaram e retornaram dados utilizáveis. Dois fetches extras foram necessários por path incorreto (URLs no formato `/en/tanzania/lake|northern|coastal/admin/...` em vez de `/en/tanzania/admin/<região>/...`, que só mostra total distrital sem wards) — resolvido re-fetchando com o path correto "com wards".

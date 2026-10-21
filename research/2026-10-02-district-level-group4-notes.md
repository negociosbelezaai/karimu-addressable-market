# Nível Distrito (ADM2) — Grupo 4: Kiribati, Gambia, Tuvalu, Nepal, Angola, Djibouti

Data: 2026-10-02
Entregável: `deliverables/district-level-map-group4.csv` (344 linhas: 343 unidades ADM2 reais + 1 linha de nota para Tuvalu)

## Método
API CKAN do HDX via `curl -L` com User-Agent de navegador (WebFetch puro bloqueado com 403), seguindo o mesmo método já validado no nível província. Para cada país: `package_show` em `cod-ps-<iso3>` primeiro (população pronta por ADM2), fallback para `cod-ab-<iso3>` (gazetteer de fronteiras, sem população) + Wikipedia/citypopulation.de quando a população ADM2 não estava disponível no HDX.

---

## Kiribati (KIR) — 36 unidades, P-code oficial, população oficial

- **Fonte**: HDX `cod-ps-kir`, recurso `kir_admpop_adm2_2020.csv` — https://data.humdata.org/dataset/e656842e-9643-4ef7-97f9-18c33654022d/resource/39f3de96-0176-4397-aa9f-b3c44d3e0515/download/kir_admpop_adm2_2020.csv
- **P-codes**: padrão `KIxyy` (ex.: `KI101` = Banaba), confirmados contra `ADM1_PCODE` (`KI1`/`KI2`/`KI3`) já presentes em `province-level-map.csv`.
- **Local_unit_type**: "Island" — o ADM2 aqui é a ilha individual dentro de cada grupo de ilhas (ADM1).

### Achado notável 1 — Kiribati TEM nível ADM2 distinto
O `2026-10-02-province-level-summary.md` (etapa anterior) tratou Kiribati como tendo só 3 unidades ADM1 (grupos de ilhas) e não afirmou explicitamente ausência de ADM2, mas a instrução desta tarefa pedia para pesquisar antes de concluir ausência. Pesquisa confirmou: **existe sim um nível ADM2** — 36 ilhas individuais dentro dos 3 grupos (19 nas Gilbert Islands, 3 nas Line Islands "habitadas" + 5 "despovoadas" adicionais, 8 nas Phoenix Islands, e 1 unidade extra "Betio" dentro das Gilbert Islands — ver achado 2). Várias ilhas das Phoenix Islands (Kanton, Rawaki, Birnie, Mackean, Enderbury, Nikumaroro, Manra, Orona) e algumas das Line Islands (Malden, Starburk, Millenium, Vostok, Flint) têm população 0 — mesmo padrão de "quase desabitado" já visto no nível província para as Phoenix Islands.

### Achado notável 2 — Betio (KI124) com população 0 na fonte oficial
Betio é, na realidade, um bairro populoso do atol de Tarawa (~17 mil hab. em 2015 segundo fontes externas pesquisadas via web search), mas o dataset oficial COD-PS mostra **Betio = 0 habitantes**, enquanto South Tarawa (KI107) aparece com 63.439. Interpretação mais provável: a população de Betio está contabilizada dentro do total de South Tarawa no censo 2020, apesar de ter P-code próprio reservado (KI124). Mantido como está na fonte (0), **não corrigido nem estimado** — risco de dupla contagem se simplesmente somado ao de South Tarawa sem confirmação metodológica do instituto de estatística de Kiribati.

---

## Gambia (GMB) — 49 unidades, P-code/fronteira oficial; população parcial (41/49) via Wikipedia

- **Fronteira/P-code**: HDX `cod-ab-gmb`, recurso `gmb_admin_boundaries.xlsx`, aba `gmb_admin2` — https://data.humdata.org/dataset/9f2ce756-2e50-4042-a952-32160977d223/resource/e508fc11-270c-45b5-a77b-32c510bc51a0/download/gmb_admin_boundaries.xlsx (cod-ps-gmb não tem arquivo de população ADM2, só `gmb_popadm_2021_admin1.csv`).
- **População**: Wikipedia "Districts of the Gambia" (censo 2013-04-15) — https://en.wikipedia.org/wiki/Districts_of_the_Gambia
- **Local_unit_type**: "District".

### Achado notável — granularidade da fonte de fronteira é maior que a da fonte de população
O gazetteer oficial HDX tem 49 distritos (ADM2); a Wikipedia só lista população para 43 "distritos", porque agrega:
- As 6 subdivisões de Kanifing Municipal Council (Bakau, Jeshwang, Mangrove, Sere Kunda Central/East/West) em 1 único valor "Kanifing" (382.096 hab.).
- As 2 subdivisões "Lower Fuladu West" / "Upper Fuladu West" em 1 único valor "Fulladu West" (84.961 hab.).

Essas **8 unidades ADM2** (das 49) ficaram com `population` em branco — distribuir o total agregado entre as sub-unidades seria inventar dado, então não foi feito. As outras 41 unidades têm correspondência de nome 1:1 (com pequenos ajustes de grafia documentados linha a linha: "Basse"↔"Basse Fulladu East", "Foni Bintang Karenai"↔"Foni Bintang-Karenai", "Kombo North/St Marie"↔"Kombo North", "Illiassa"↔"Illiasa", "Sabach - Sanjal"↔"Sabach Sanjal").

---

## Tuvalu (TUV) — não aplicável

- Confirmado rapidamente: `package_show` em `cod-ps-tuv` e `cod-ab-tuv` retornam `success:false` (dataset não existe no HDX) — mesmo resultado já obtido na etapa de província.
- **Não foi criada tabela ADM2 forçada**, conforme instrução. Uma única linha de nota no CSV documenta a não-aplicabilidade: Tuvalu tem hierarquia país→ilha sem nível intermediário, e as 9 ilhas já foram cobertas como ADM1 em `province-level-map.csv`.

---

## Nepal (NPL) — 77 unidades, P-code oficial, população oficial

- **Fonte**: HDX `cod-ps-npl`, recurso `npl_admpop_adm2_2023.csv` — https://data.humdata.org/dataset/e71f53d9-2339-4df5-b76e-397957ec65dc/resource/57161f46-c404-4784-a952-a6e5ba2ed625/download/npl_admpop_adm2_2023.csv
- **P-codes**: padrão `NPxxyy` (ex.: `NP0320` = Sindhuli, dentro de Bagmati `NP03`).
- **Local_unit_type**: "District". 77 distritos confirmados — número conhecido e estável da divisão administrativa do Nepal, todas as 7 províncias (ADM1) representadas.
- Sem achados anômalos; projeção populacional 2023, cobertura completa.

---

## Angola (AGO) — 161 unidades, P-code oficial, população oficial

- **Fonte**: HDX `cod-ps-ago`, recurso `ago_admpop_adm2_2024.csv` — https://data.humdata.org/dataset/01679d5e-9cf1-45a4-a212-662a2309780c/resource/8eaff3c4-277c-4404-b135-2bf512a280ff/download/ago_admpop_adm2_2024.csv
- **P-codes**: padrão `AOxxyyy` (ex.: `AO01001` = Ambriz, dentro de Bengo `AO01`).
- **Local_unit_type**: "Município" (termo oficial angolano para ADM2).
- **Nota técnica**: arquivo fonte em encoding Latin-1 (não UTF-8) — acentos portugueses ("Bié", "Huíla", "Cuíto") exigiram leitura com `encoding=latin-1` para não corromper. Convertido para UTF-8 no CSV final.
- Sem achados anômalos; projeção populacional 2024, cobertura completa (todas as 18 províncias ADM1 representadas, 161 municípios).

---

## Djibouti (DJI) — 20 unidades, P-code/fronteira via GADM (fallback); população NÃO encontrada de forma confiável neste nível

- **Fronteira/P-code**: HDX `cod-ab-dji`, recurso `dji_admgz_gadm_2022.xlsx`, aba `dji_admgz_gadm_adm2_2022` — https://data.humdata.org/dataset/ceee47a3-cd1d-4eae-ab93-87d6f2ca00b9/resource/f7873681-7ab1-4d45-b66d-ecb3d02d7a3b/download/dji_admgz_gadm_2022.xlsx. Fonte primária é **GADM 2022**, não um COD-AB nacional oficial direto — Djibouti não tem COD-AB nacional próprio publicado no HDX (mesmo padrão de exceção já usado no nível província para Tuvalu e parcialmente Guiné-Bissau/Serra Leoa). `is_official_id` mantido "yes" porque o P-code segue o padrão oficial (sem hífen/`-PROV`), mas a origem fallback está registrada em cada linha.
- **Local_unit_type**: "Sub-prefecture" (termo em inglês usado na literatura/Wikipedia; 20 sub-prefeituras confirmadas, batendo com a Wikipedia "Sub-prefectures of Djibouti").
- **População**: `cod-ps-dji` só publica população até ADM1 (censo 2009, já usado no nível província). **Nenhuma fonte oficial com quebra ADM2 foi encontrada.**

### Achado notável — fonte secundária encontrada, mas descartada por risco de dupla contagem
`citypopulation.de/en/djibouti/admin/` lista uma tabela atribuída a um censo 2024 com quebra por sub-prefeitura, mas a estrutura separa a **cidade-sede** de cada região (tabela "cities", ex.: Ali-Sabieh = 45.092 hab.) da sua **sub-prefeitura periférica rural** (tabela "admin", ex.: "Ali-Sabieh-Périphérique" = 3.564 hab.) — são dois recortes administrativos sobrepostos, não um único total por sub-prefeitura. Somar as duas tabelas produziria um número não oficialmente confirmado, com risco de dupla contagem ou contagem incompleta (a tabela "admin" nem cobre todas as 20 sub-prefeituras do GADM — faltam Balho, Mousa Ali, Moulhoule, Galafi, provavelmente postos fronteiriços quase desabitados). **Por regra de não inventar dado, população deixada em branco nas 20 linhas de Djibouti.**

---

## Resumo de falhas/gaps desta etapa
1. **Gambia**: 8 de 49 distritos sem população (agregação da fonte, ver acima).
2. **Djibouti**: 20 de 20 sub-prefeituras sem população (nenhuma fonte ADM2 confiável encontrada).
3. **Tuvalu**: não aplicável, documentado.
4. **Rural/urbano**: não disponível em nenhuma das fontes usadas neste nível, para nenhum dos 6 países — mesmo gap já registrado no nível província (datasets COD-PS só desagregam por idade/sexo neste nível administrativo).

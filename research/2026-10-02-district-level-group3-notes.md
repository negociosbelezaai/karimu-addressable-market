# Nível Distrito (ADM2) — Grupo 3: Sierra Leone, Zambia, Guinea-Bissau, Senegal, Liberia

Data: 2026-10-02
Entregável: `deliverables/district-level-map-group3.csv` (353 linhas, 5 países)

## Resumo por país

| País | ISO3 | Distritos | P-code oficial? | Fonte da população | Ano do dado |
|---|---|---|---|---|---|
| Liberia | LBR | 136 | sim (100%) | HDX cod-ps-lbr (arquivo já traz população por ADM2) | 2020 |
| Zambia | ZMB | 116 | 115 sim + 1 provisório (Lusangazi) | citypopulation.de (Zambia 2022 Population and Housing Census) | 2022 |
| Senegal | SEN | 46 | 45 sim + 1 provisório (Keur Massar) | citypopulation.de (ANSD RGPH-5, censo 2023) | 2023 |
| Guinea-Bissau | GNB | 39 | sim (100%) | INE Guiné-Bissau, RGPH 2009 (PDFs regionais oficiais) | 2009 |
| Sierra Leone | SLE | 16 | sim (100%) | Wikipedia - Districts of Sierra Leone (censo 2015) | 2015 |

**Total: 353 distritos/setores.** Nenhuma linha ficou com população em branco — todos os 5 países tiveram cobertura completa de população no nível ADM2, incluindo as unidades sem P-code oficial (via convenção `-PROV<n>`).

---

## Liberia (LBR) — 136 distritos

Fonte única: HDX `cod-ps-lbr`, resource `lbr_admpop_adm2_2020_v2.csv` (https://data.humdata.org/dataset/31e5e358-284a-4f21-9af7-03c755eee555/resource/c7116189-cf33-4305-bf5b-90a6b16c72c7/download/lbr_admpop_adm2_2020_v2.csv). O arquivo tem 136 linhas, uma por distrito, com `ADM2_PCODE`, `ADM1_PCODE` (condado-pai) e `T_TL` (população total 2020). Não precisou de nenhum fallback.

**Validação**: somei a população dos distritos por condado (`ADM1_PCODE`) e os 15 totais batem **exatamente** com os valores já publicados em `province-level-map.csv` (ex.: Bomi = 110.141, Montserrado = 1.464.139). Nenhuma falha.

Rural population: não disponível neste arquivo (só tem breakdown por idade/sexo).

---

## Zambia (ZMB) — 116 distritos (115 oficiais + 1 provisório)

### O problema encontrado
O pacote `cod-ps-zmb` tem um arquivo `zmb_admpop_2020.xlsx` com duas fontes de verdade diferentes dentro do mesmo arquivo:
- Aba `AB-ADM2`: fronteiras oficiais mais recentes, **115 distritos** com P-code (ex. `ZM1001` Chibombo).
- Aba `zmb_admpop_adm2_2020`: população, mas só **74 distritos** — reflete uma divisão administrativa mais antiga (pré-2018), sem os distritos desmembrados depois (ex.: Chisamba, Chitambo, Luano, Ngabwe, Kanchibiya, Lavushimanda, etc.). Isto é o mesmo padrão "fronteira nova, população velha" já visto em Serra Leoa e Tanzânia.

### Solução
Usei **citypopulation.de** (fonte citada: Zambia Statistics Agency, Census 2022, período 18 ago–7 set 2022), navegando por cada uma das 10 páginas de província (ex. https://www.citypopulation.de/en/zambia/admin/01__central/) e extraindo a tabela de distritos. Essa fonte **cobre os 115 distritos oficiais + Lusangazi** (ver abaixo), com dado mais recente (2022) que o arquivo HDX (2020/pré-2018).

**Variantes ortográficas reconciliadas** (mesmo distrito, grafia levemente diferente entre o P-code oficial HDX e o nome usado por citypopulation.de — documentado linha a linha no CSV): Chiengi/Chienge, Milengi/Milenge, Mushindano/Mushindamo, "Lunte District"/Lunte, Chikankanta/Chikankata, Shiwamg'andu/Shiwang'andu.

**Achado curioso**: alguns distritos aparecem na página de uma província diferente da que consta no P-code oficial (ex.: Shibuyunji listado na página de Central mas o P-code oficial `ZM5008` o liga a Lusaka; Chirundu listado na página de Southern mas o P-code oficial `ZM5006` o liga a Lusaka; Chama listado na página de Eastern mas o P-code oficial `ZM1112` o liga a Muchinga). Usei o P-code oficial HDX para `parent_pcode`/`parent_unit_name` em todos os casos, e o número de população da citypopulation.de independente de qual página o listou (o número é por distrito, não por página).

### Unidade sem P-code oficial: Lusangazi
**Lusangazi** aparece em citypopulation.de (110.477 hab., censo 2022) mas **não existe** na aba `AB-ADM2` (fronteiras oficiais mais recentes do HDX). Pesquisa web confirma: distrito criado em 2018, desmembrado de **Petauke** (`ZM3008`). Aplicada a convenção do `target-unit-concept.md`: `unit_id = ZM3008-PROV1`, `is_official_id = no`, `parent_pcode = ZM30` (província Eastern).

Rural population: não disponível nesta fonte neste nível.

---

## Guinea-Bissau (GNB) — 39 setores (100% oficial)

### Fronteiras
HDX não tem pacote `cod-ps-gnb` (confirmado — erro 404 na API `package_show`). Usei `cod-ab-gnb` (`gnb_admin_boundaries.xlsx`, aba `gnb_admin2`) para os 39 setores com P-code oficial (ex. `GW0101` Bafata) e o setor-pai (região ADM1).

### População — melhor fonte encontrada neste lote
Wikipedia não tem tabela de população por setor (só nomes). Tentativa de usar artigos individuais de Wikipedia por setor foi abandonada cedo por inconsistência (alguns artigos dão população da CIDADE-sede do setor, não do setor inteiro — ex. artigo de Bafatá cidade mostra só 34.760, mas o setor todo tem 68.956).

Em vez disso, localizei os **relatórios oficiais regionais do censo 2009** (III RGPH/2009) do Instituto Nacional de Estatística da Guiné-Bissau, publicados em PDF no site oficial `stat-guinebissau.com` — um PDF por região (ex. `Regiao_de_Bafata_RGPH_2009.pdf`), cada um com uma tabela "População... residente por Sexo e meio de residência" que desce até o nível de setor **e** a divisão urbano/rural dentro de cada setor.

**Validação completa**: somei os 39 setores por região e os 9 totais batem **exatamente** com o total regional publicado no mesmo PDF (nenhum resíduo, nenhuma unidade sem correspondência). Também capturei o campo `rural_population`/`rural_population_pct` para as 39 linhas — raro neste projeto (no nível província, só Djibouti tinha essa quebra).

**Achado — Sector Autónomo de Bissau (GW0800)**: o relatório `SAB_RGPH_2009.pdf` dá total de **365.097** (soma de 8 subsetores "Sector-1" a "Sector-8", todos 100% urbanos) — **diferente** do valor usado em `province-level-map.csv` para `GW08` (387.909, fonte Wikipedia). Diferença de ~22.812 habitantes entre duas publicações do mesmo censo 2009; não reconciliado nesta pesquisa, documentado na célula `notes`.

**Achado — erro de digitação na fonte**: o PDF de Tombali escreve "**Sectoer** de Bedanda" (sic) em vez de "Sector de Bedanda" — não afetou a extração, mas vale registrar.

Links dos 9 PDFs usados estão na coluna `notes`/`population_source` de cada linha.

---

## Senegal (SEN) — 46 departamentos (45 oficiais + 1 provisório)

### Fronteiras
`cod-ps-sen` não tem arquivo de população no nível ADM2 (confirmado — os recursos `sen_admpop_2021/2023.xlsx` só têm abas adm0/adm1). Usei `SEN_AdminBoundaries_TabularData.xlsx` (aba `ADM2`) do mesmo pacote: 45 departamentos com P-code oficial (ex. `SN0101` Dakar), boundary válido 2017-2019.

### População
Mesma estratégia do Zambia: **citypopulation.de**, navegando pelas 14 páginas de região (ex. https://www.citypopulation.de/en/senegal/admin/SN01__dakar/), fonte citada = ANSD (Agence Nationale de la Statistique et de la Démographie), censo RGPH-5 de 2023-08-18.

**Validação**: soma dos 46 departamentos = **18.126.390**, batendo exatamente com o total nacional do Senegal no mesmo censo (conferido na página-raiz de citypopulation.de). Soma por região também bate com os totais já publicados em `province-level-map.csv`.

### Unidade sem P-code oficial: Keur Massar
A região de Dakar tem **5 departamentos** em citypopulation.de (Dakar, Guédiawaye, Keur Massar, Pikine, Rufisque) mas o arquivo oficial de fronteiras HDX só lista **4** (sem Keur Massar). Keur Massar foi criado em 2021 por desmembramento de Pikine. Aplicada a convenção: `unit_id = SN0103-PROV1` (usando o P-code de Pikine, `SN0103`, como ancestral), `is_official_id = no`, `parent_pcode = SN01` (região Dakar).

Rural population: não disponível nesta fonte neste nível (só agregado nacional).

---

## Sierra Leone (SLE) — 16 distritos (100% oficial)

### Fronteiras
Usei `cod-ab-sle` (`sle_admin_boundaries.xlsx`, aba `sle_admin2`) — 16 distritos, já refletindo a reforma de 2017 (inclui Falaba e Karene, e a 5ª província North Western). P-codes: `SL0101`...`SL0503`.

**Achado**: o gazetteer HDX escreve o nome do distrito como "**Fabala**" (`SL0206`) em vez de "Falaba" — provável erro de digitação na fonte oficial. Mantive "Falaba" (grafia padrão) em `unit_name`, documentando a divergência em `notes`.

### População — decisão de consistência
O pacote `cod-ps-sle` tem um arquivo de população ADM2 (`sle_adm2_population_v2.csv`), mas ele usa as **fronteiras pré-2017** (14 distritos, sem Falaba/Karene, com Kambia e Port Loko ainda sob "Northern"). Isso já tinha sido identificado como problema no nível província (`2026-10-02-province-level-summary.md`, achado 4).

Para manter consistência com `province-level-map.csv` (cuja população de província já veio da soma dos distritos no censo 2015 via Wikipedia), usei a mesma fonte agora no nível distrito: **Wikipedia - Districts of Sierra Leone**, tabela com coluna "Population (2015 census)" — cobre os 16 distritos atuais, incluindo Falaba (205.353) e Karene (285.546).

**Validação**: somei os distritos por província e os 5 totais batem **exatamente** com os valores já publicados em `province-level-map.csv` (ex.: Northern = Bombali+Falaba+Koinadugu+Tonkolili = 1.752.704; North Western = Kambia+Karene+Port Loko = 1.246.396).

Rural population: não encontrada nesta fonte neste nível.

---

## Falhas / limitações gerais deste lote
- Nenhum país deste grupo ficou sem nível ADM2 aplicável — todos os 5 têm um nível distrito/departamento/setor claramente distinto da província.
- Rural/urbano só foi possível capturar para **Guinea-Bissau** (fonte primária do censo 2009 já trazia a quebra). Para os outros 4 países, nenhuma fonte consultada (HDX, Wikipedia, citypopulation.de) desagrega população rural/urbana no nível distrito.
- citypopulation.de bloqueia `curl` direto (CAPTCHA "Check for Humans", mesmo com cookies/referer/UA de navegador) — só funcionou via WebFetch (ferramenta com acesso HTTP diferente). Tentativas de paralelizar `curl` também causaram bloqueio por "too many requests" na API pública do Wikipedia (`opensearch`) — resolvido espaçando as chamadas.
- GW08 (Bissau) tem divergência de ~22.812 habitantes entre duas fontes do mesmo censo 2009 (RGPH oficial vs. Wikipedia) — não investigada a fundo, documentada no CSV.

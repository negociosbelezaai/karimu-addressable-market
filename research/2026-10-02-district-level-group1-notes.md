# Nível Distrito (ADM2) — Grupo 1 — notas por país

Data: 2026-10-02
Entregável: `deliverables/district-level-map-group1.csv` (454 linhas de dados, 6 países)
Países: Malawi (MWI), Timor-Leste (TLS), Solomon Islands (SLB), Madagascar (MDG), Comoros (COM), Tanzania (TZA)

Método: mesmo da etapa província — HDX CKAN API via `curl -sL` com User-Agent de navegador (bloqueio 403 em WebFetch puro), buscando primeiro o arquivo `..._admpop_adm2_...` dentro do pacote `cod-ps-<iso3>`; fallback para `cod-ab-<iso3>` (gazetteer/fronteira) + Wikipedia quando o COD-PS não cobre ADM2. `parent_pcode` de cada distrito conferido linha a linha contra `deliverables/province-level-map.csv`.

---

## Malawi (MWI)
Fonte: HDX COD-PS Malawi (cod-ps-mwi), arquivo `mwi_admpop_adm2_2023.csv`, projeção populacional 2023. URL: https://data.humdata.org/dataset/8ceb03ac-2272-447f-8887-39cfc4d78b59/resource/28082779-76b1-49cb-bc4a-61efb19a7e1b/download/mwi_admpop_adm2_2023.csv

Distritos encontrados: 32 (todos com P-code oficial e população).

Falhas/observações: Nenhuma falha de dado. Achado notável: o arquivo tem 32 unidades ADM2, não 28 — porque 4 cidades com status administrativo próprio (Lilongwe City, Blantyre City, Zomba City, Mzuzu City) são contadas separadamente da área rural do distrito homônimo (ex.: "Lilongwe City" + "Lilongwe Rural District" são duas linhas distintas, cada uma com seu próprio P-code). Os 28 distritos "clássicos" citados no resumo do nível província viram 32 quando essas 4 cidades são desagregadas. `local_unit_type` registrado como "City" ou "District" conforme o nome original no arquivo. P-code pai (ADM1) confere com `province-level-map.csv` (MW1/MW2/MW3). `rural_population` não disponível nesta fonte neste nível.

---

## Timor-Leste (TLS)

Fonte principal (população): Timor-Leste Population and Housing Census 2022 (General Directorate of Statistics / UNFPA), "Population and Housing Census 2022 Timor-Leste - Preliminary Results", Annex I (total/por sexo) e Annex III (componente urbano). URL: https://timor-leste.unfpa.org/sites/default/files/pub-pdf/censuspreliminaryresults2022_4.pdf

Fonte de fronteiras/P-code (cross-check): HDX cod-ps-tls, arquivo `TLS_AdminBoundaries_TabularData.xlsx`, aba `ADM2` (VALIDTO 2020-09-11). URL do pacote: https://data.humdata.org/api/3/action/package_show?id=cod-ps-tls (recurso `TLS_AdminBoundaries_TabularData.xlsx`).

Unidades encontradas: 67 postos administrativos ("Administrative Post" — termo oficial confirmado via Wikipedia/Wikidata; estrutura invertida frente ao padrão: ADM1 = Municipality, ADM2 = Administrative Post).

Soma de população dos 67 postos = 1.340.434, idêntica ao total nacional do censo 2022. Soma do componente urbano (19 postos com dado explícito no Anexo III) = 492.752, também idêntica ao total urbano nacional reportado.

Falhas/observações:
1. **O pacote HDX cod-ps-tls NÃO tem um recurso `admpop_adm2`** — ao contrário do esperado, o pacote só vai até ADM1 (`tls_admpop_adm1_2022.csv`). Por isso a população ADM2 foi buscada em fonte alternativa oficial (censo 2022, GDS/UNFPA), não no COD-PS.
2. **Metodologias diferentes entre ADM1 (já existente) e ADM2 (este arquivo)**: o nível província usa projeções pós-censitárias da HDX COD-PS (NSO); este nível distrito usa a contagem real do Censo 2022. Ambos têm base 2022, mas não são a mesma fonte — a soma dos postos de um município pode não bater exatamente com o total ADM1 já registrado. Anotado em cada linha do CSV.
3. **Atauro**: confirmado que virou município (ADM1) separado em 1º de janeiro de 2022. O P-code oficial ADM2 (COD-AB) ainda lista "Atauro" (TL0604) como posto dentro do município de Dili (TL06) — mesma ressalva já registrada no nível ADM1. O CSV manteve parent_pcode=TL06 por fidelidade ao P-code oficial vigente, com a inconsistência documentada na nota da linha.
4. **Dois postos administrativos foram divididos em 1º de janeiro de 2022 (antes do censo), mas o P-code oficial (COD-AB) ainda não foi atualizado**:
   - "Hatolia" (TL0705, Ermera) → dividido em "Hatulia A" e "Hatulia B". Nenhum reteve o P-code original. IDs provisórios atribuídos seguindo a convenção `<pcode-pai>-PROV<n>` (ordem alfabética entre os pendentes do mesmo pai): **`TL07-PROV1`** (Hatulia A) e **`TL07-PROV2`** (Hatulia B), `is_official_id=no`. *(Nota de correção: o agente que coletou os dados originalmente usou os rótulos `TL07-PROVHATA`/`TL07-PROVHATB`; corrigidos nesta consolidação para o formato numérico sequencial documentado em `target-unit-concept.md`.)*
   - "Lospalos" (TL0901, Lautém) → "Loré" foi separado de Lospalos. Lospalos (remanescente) manteve o P-code oficial TL0901. Loré recebeu ID provisório **`TL09-PROV1`**, `is_official_id=no` *(corrigido de `TL09-PROVLORE` pela mesma razão acima)*.
   - Confirmado via Wikipedia/Wikidata ("Hatulia B Administrative Post", "Loré Administrative Post").
5. **Rural/urbano**: dado explícito de urbano por posto vem do Anexo III do censo (19 dos 67 postos). Para os 48 postos sem entrada no Anexo III, o relatório afirma textualmente que os municípios fora de Dili são "predominantemente rurais" e que Atauro é "completamente rural" — por isso tratados como 100% rurais (urbano=0, rural_population=population total). Nenhum valor inventado: classificação vem da ausência confirmada de linha no Anexo III combinada com a afirmação textual do relatório.
6. Nenhuma unidade ficou sem dado de população — todas as 67 têm população do censo 2022.
7. Pequenas diferenças de grafia entre o censo e o COD-AB foram reconciliadas por correspondência direta (ex.: "Lequidoe"→"Liquidoe", "Hato-Udo"→"Hatu-Udo", "Fohorem"→"Forohem", "Liquica"→"Liquiçá", "Lautem"→"Lautém").

---

## Solomon Islands (SLB)
Fonte: HDX COD-PS Solomon Islands (cod-ps-slb), recurso `slb_admpop_adm2_2023.csv` (população por idade/sexo, nível ADM2, ano de referência 2023). `local_unit_type` confirmado como "Constituency" pelo metadado oficial do pacote irmão COD-AB (cod-ab-slb): "Administrative level 2 contains 50 feature(s). The normal administrative level 2 feature type is Constituency." URL: https://data.humdata.org/dataset/53e6df8b-ca6e-42b8-a13a-d16e033865eb/resource/b84d42cf-a0b2-48e8-bac2-14458754ab07/download/slb_admpop_adm2_2023.csv

Unidades encontradas: 50 (todas as constituencies oficiais do COD-AB, contagem bate exatamente com o metadado, incluindo as 3 constituencies urbanas de Honiara).

Falhas/observações: Nenhuma unidade sem população — todas as 50 linhas têm população total preenchida. Todos os `ADM1_PCODE` pai batem com a tabela de referência (SB01–SB10). Não foi necessário recorrer a Wikipedia — o COD-PS já trouxe o recurso ADM2 direto com população. Dado rural/urbano não disponível neste nível na fonte; campos `rural_*` deixados em branco para todas as 50 unidades.

---

## Madagascar (MDG)
Fonte: HDX COD-PS Madagascar (cod-ps-mdg), arquivo `mdg_admpop_adm2_2018.csv` (coluna final `T_TL` = população, ano de referência 2018, RGPH). URL: https://data.humdata.org/dataset/0b6ce366-8651-43aa-8c36-9f3fdc8d6b4f/resource/5ecd33f3-87f2-4606-9174-92caaab408ea/download/mdg_admpop_adm2_2018.csv

Distritos encontrados: 119 (todas as 22 regiões ADM1 cobertas, P-code pai conferido linha a linha contra `province-level-map.csv` — zero divergência).

Falhas/observações: nenhum distrito ficou sem população. Achado notável: o distrito-capital Antananarivo Renivohitra não aparece como uma única linha — a fonte o reporta como 6 "arrondissements" separados (1er a 6e Arrondissement, P-codes tipo `MG11101001A`), diferente do padrão dos demais 113 distritos (P-code de 7 caracteres). Mantido como veio da fonte (não forçado a agregar numa linha só), com nota em cada uma das 6 linhas explicando a particularidade.

*(Nota de processo: a primeira tentativa de coleta para este país falhou — o agente terminou sem escrever os arquivos de saída e com um relatório final confuso. Foi refeita do zero com sucesso; os dados acima vêm exclusivamente da segunda tentativa.)*

---

## Comoros (COM)

Fonte estrutura/fronteira (ADM2): HDX COD-AB Comoros (cod-ab-com), arquivo `com_adminboundaries_tabulardata.xlsx` (aba `ADM2`), válido desde 2018-12-28. URL do pacote: `https://data.humdata.org/api/3/action/package_show?id=cod-ab-com`.

Fonte população (ADM2): HDX COD-PS Comoros (cod-ps-com) **não tem** nível ADM2 — o arquivo `com_admpop_2017.xlsx` só contém as abas ADM0 e ADM1 (confirmado abrindo o workbook). Por isso a população veio de fonte secundária: **citypopulation.de** (`https://www.citypopulation.de/en/comoros/admin/`, citando censo 2017-12-15/INSEED), acessada via snapshot arquivado do Wayback Machine (`https://web.archive.org/web/20250209142956/https://www.citypopulation.de/en/comoros/admin/`) por o site original bloquear acesso automatizado.

Unidades encontradas: **17 prefeituras oficiais** (P-code HDX) — nível ADM2 confirmado como existente e oficialmente reconhecido (pesquisado, não assumido): Anjouan/Ndzuwani com 5 prefeituras (KM11–KM15), Grande Comore/Ngazidja com 9 (KM21–KM29), Mohéli/Mwali com 3 (KM31–KM33).

Falhas/observações:
- População disponível para 15 prefeituras diretamente + 1 derivada por soma de duas unidades do censo 2017 (`Mitsamiouli-Mboudé` = soma de `Mitsamiouli` + `Mboudé`, cuja soma de área bate quase exatamente com a área oficial do P-code atual) = 16 preenchidas.
- **1 prefeitura sem população**: `Kartala` (KM29, Grande Comore, área 5,46 km² — provável cratera/zona do vulcão Karthala) não tem equivalente na lista de 2017 do citypopulation.de. Há indício aritmético indireto (soma das 16 prefeituras conhecidas = 734.176; total nacional censo 2017 = 758.316; resíduo = 24.140, valor idêntico ao de uma prefeitura "Moya" que aparece no citypopulation.de mas não tem P-code oficial correspondente hoje) de que a população de Kartala é próxima de zero — mas por não ser uma fonte direta, o campo foi deixado em branco, conforme a regra de não inventar número. Nenhuma linha extra "Moya"/provisória foi criada no CSV: a evidência é indireta demais para justificar uma nova unidade — registrado aqui apenas como achado de pesquisa.
- Todas as 17 linhas usam P-code oficial do HDX (`is_official_id=yes`).
- `rural_population` e campos relacionados: não encontrados em nenhuma fonte neste nível — deixados em branco em todas as linhas.

---

## Tanzania (TZA)
Fonte: HDX COD-PS Tanzania (cod-ps-tza), arquivo `tza_admpop_adm2_2020_v2.csv`, projeção populacional 2020. URL: https://data.humdata.org/dataset/fcd33248-774d-4be2-aa16-86b10519330e/resource/8af542c3-9f80-4f5c-9362-d5954d7824ec/download/tza_admpop_adm2_2020_v2.csv

Distritos encontrados: 169.

Falhas/observações: Nenhuma. Todos os 169 distritos têm P-code ADM2 oficial (formato TZXXYY) e população preenchida. `parent_pcode` (ADM1) de cada distrito conferido contra as 31 regiões já validadas em `province-level-map.csv` — 100% de correspondência, nenhum P-code pai órfão. `local_unit_type` = "District" (hierarquia Region > District > Division > Ward). `rural_population` deixado em branco para todos — mesma limitação já documentada no nível província.

---

## Nota de QA — verificação independente dos dados de Timor-Leste (2026-10-02)
O agente que coletou os dados de Timor-Leste continuou rodando em segundo plano depois de já ter escrito o arquivo com os 67 postos (fonte: Censo 2022 UNFPA/GDS, Annex I/III). Numa etapa posterior da mesma sessão, ele tentou complementar com `citypopulation.de`, descobriu que esse site bloqueia fetch automatizado com captcha, e que uma ferramenta de fetch anterior havia **alucinado** uma tabela de população plausível a partir da página de bloqueio (números que pareciam reais mas não vinham de lugar nenhum). Ele descartou corretamente esse dado alucinado — mas, ao reiniciar do zero, abandonou também o arquivo original (verdadeiro) de 67 postos e entregou um segundo relatório final com uma tabela diferente (65 postos, população do censo 2015 via Wikipedia), sem mencionar que já existia uma primeira versão.

**Verificação feita nesta consolidação**: baixei o PDF original (`censuspreliminaryresults2022_4.pdf`) diretamente via `curl` e extraí o texto de todas as 25 páginas com `pypdf` (sem depender de sumarização por modelo, para evitar o mesmo modo de falha). Confirmado:
- O documento realmente tem Annex I (população por posto administrativo), Annex II (urbano/rural por município) e Annex III (população urbana por posto administrativo) — não é uma alucinação.
- Contagem de postos no Annex I bate exatamente com 67 (as mesmas 33 no primeiro bloco + 34 no segundo).
- Todos os 67 valores de população no CSV final conferidos um a um contra o texto extraído do PDF — 100% de correspondência exata, incluindo os casos provisórios (Hatulia A=20.305, Hatulia B=21.537, Lore=3.631).

**Conclusão**: os dados de Timor-Leste já incorporados em `district-level-map-group1.csv` (67 postos, fonte censo 2022) são genuínos e foram mantidos sem alteração. O segundo arquivo (65 postos, Wikipedia 2015) foi descartado por ser uma duplicata inferior do mesmo trabalho, não por erro nos dados já usados. Risco de processo registrado para lotes futuros: um agente que continua rodando em background pode reiniciar do zero e sobrescrever um resultado já correto sem avisar — vale conferir o arquivo final contra a fonte primária antes de aceitar um "relatório de conclusão" como verdade, especialmente quando o agente menciona ter descartado dados alucinados em qualquer ponto do processo.

## Validação de consistência (feita nesta sessão, no CSV consolidado)
- 454 linhas de dados, 6 países, header idêntico ao do nível província com semântica de distrito.
- Zero `unit_id` duplicado; zero `unit_id` em branco (toda unidade recebeu P-code oficial ou ID provisório).
- Apenas **1 linha com `population` em branco** em todo o grupo (Kartala, Comores — ver acima).
- `parent_pcode` de todas as 454 linhas conferido programaticamente contra `deliverables/province-level-map.csv`: **zero divergências**.
- 3 linhas com `is_official_id=no` (as 3 unidades provisórias de Timor-Leste); as demais 451 são oficiais.
- Rural/urbano disponível apenas para Timor-Leste (67 de 67 linhas, via censo 2022) — nos outros 5 países, mesma limitação já documentada no nível província (COD-PS só desagrega por idade/sexo).

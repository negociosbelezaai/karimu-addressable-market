# Metodologia e Fontes — Mapeamento de Mercado Endereçável Karimu (v1 / first pass)

Data da pesquisa: **2026-10-01**
Arquivo de dados: `deliverables/country-market-map.csv`

Este documento registra, para cada fonte usada, a URL exata, o que ela fornece, limitações conhecidas, e os desvios feitos em relação ao plano original de pesquisa (porque uma das 4 fontes planejadas mudou de formato/ficou indisponível durante a execução).

---

## 1. Lista de países, ISO3, continente, membresia ONU

### Desvio em relação ao plano original
O plano original pedia `https://restcountries.com/v3.1/all?fields=...`. Esse endpoint **está desativado**: toda chamada (testada com `curl -sL`) retorna hoje:

```json
{"success": false, "data": null, "errors": [{"message": "This API version has been deprecated. Please visit https://restcountries.com/docs/countries/legacy-api-deprecation to migrate to our new version."}]}
```

A página de migração (`https://restcountries.com/docs/countries/legacy-api-deprecation`) confirma que as versões v1–v4 foram descontinuadas sem aviso prévio e que a v5 exige **criação de conta + API key** (`Authorization: Bearer YOUR_KEY`). Por política (nunca usar API keys para tarefas pontuais quando há alternativa sem autenticação, e não criar contas/credenciais em nome do usuário sem necessidade), **não foi criada conta/API key**. Em vez disso, usei o mirror estático mantido no GitHub pelo mesmo projeto fonte original dos dados do restcountries:

- **URL usada**: `https://raw.githubusercontent.com/mledoze/countries/master/countries.json`
- **O que fornece**: lista de 250 países/territórios com `name.common`, `cca3` (ISO 3166-1 alpha-3), `region`, `subregion`, `unMember` (bool), `independent` (bool), `status`.
- **Limitação conhecida**: é um **mirror comunitário não-oficial**, mantido por um desenvolvedor individual (mledoze) — mesma limitação de fundo do restcountries original: não é fonte oficial de dados demográficos/políticos, é um agregador de dados de ISO, CIA World Factbook, Wikipedia, etc. Para v2, vale considerar a lista oficial da ONU (UNSD M49) ou ISO 3166 diretamente.
- **Bug de dado identificado**: a fonte marca `unMember=true` para a **Santa Sé (VAT)**, o que é factualmente incorreto — a Santa Sé é **observadora permanente** da ONU, não membro pleno. Mantive a Santa Sé na lista final (como observadora, não membro), e documentei a divergência na coluna `notes` da linha VAT no CSV.
- Este arquivo **não contém população** (campo removido da versão atual do mirror) — ver seção 2 para a fonte de população usada.

### Critério de inclusão (195 "países")
`193 estados-membros plenos da ONU` (via `unMember == true`, com a correção acima para VAT) `+ 2 observadores permanentes` (Santa Sé/VAT e Palestina/PSE) = **195 linhas** na tabela. Isso segue a convenção comum de "193 + 2 observadores = 195 países do mundo".

Territórios não-soberanos (ex.: Hong Kong, Porto Rico, Groenlândia, Taiwan, Kosovo) **ficaram de fora** desta v1 por não serem estados-membros nem observadores permanentes da ONU — ver gaps conhecidos (seção 5). Isso é relevante porque Taiwan, por exemplo, tem ~23M habitantes e renda alta; Kosovo tem reconhecimento parcial. Nenhum dos dois tem dado de pobreza nas fontes do World Bank nesta pesquisa de qualquer forma.

### Mapeamento de continente
A tabela usa os 6 continentes padrão. Mapeamento aplicado a partir de `region`/`subregion` do mirror:
- `region=Africa` → Africa
- `region=Asia` → Asia
- `region=Europe` → Europe
- `region=Oceania` → Oceania
- `region=Americas` + `subregion=South America` → South America
- `region=Americas` + `subregion` em (North America, Central America, Caribbean) → North America

**Limitação conhecida**: países transcontinentais seguem a classificação do próprio `region` da fonte, que é debatível em alguns casos (ex.: Rússia e Turquia/Türkiye entram como fontes classificam — Rússia aparece como `Europe` e Turquia como `Asia` no mirror usado; Chipre aparece como `Europe`). Isso é uma simplificação consciente — não há um padrão único e isento de debate para esses casos.

---

## 2. População

### Desvio em relação ao plano original
Como o restcountries não está mais disponível (seção 1), a população também precisou de fonte alternativa. Em vez de reintroduzir outro agregador, usei o próprio **World Bank**, já que outra fonte do plano (indicador de pobreza) já vem de lá — isso na prática *melhora* a qualidade da fonte em relação ao plano original, porque o World Bank é uma fonte primária oficial de estatística, enquanto o restcountries sempre foi (nas palavras do próprio briefing) "um agregador, não uma fonte oficial de população".

- **URL usada**: `https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&per_page=5000&mrnev=1`
- **O que fornece**: população total por país/ano, retornando o valor mais recente não-vazio por país (`mrnev=1` = "most recent non-empty value").
- **Limitações conhecidas**:
  - A resposta inclui agregados regionais/de renda (ex.: "East Asia & Pacific", "World") misturados com países reais — filtrados usando a lista de ISO3 reais da seção 1 (agregados não têm `cca3` correspondente a um país real).
  - Estimativas do Banco Mundial podem divergir de censos nacionais mais recentes ou de outras fontes (ONU/DESA, por exemplo), especialmente em países com dados defasados.
  - **Vaticano (VAT) não tem dado de população no World Bank** — campo ficou em branco no CSV, conforme a regra de não estimar.

---

## 3. % da população abaixo da linha de pobreza internacional

- **URL usada**: `https://api.worldbank.org/v2/country/all/indicator/SI.POV.DDAY?format=json&per_page=5000&mrnev=1`
- **O que fornece**: % da população abaixo da linha de pobreza internacional extrema, valor mais recente não-vazio por país, com o ano do dado (`date`).

### ⚠️ Mudança de critério em relação ao plano original
O briefing original especificava a linha de **US$2,15/dia (PPP 2017)**. Ao buscar os dados, o indicador `SI.POV.DDAY` do World Bank **já não usa esse critério** — a resposta da API identifica o indicador como:

> `"Poverty headcount ratio at $3.00 a day (2021 PPP) (% of population)"`

Isso reflete uma atualização real e documentada do Banco Mundial: em 2025 o Banco Mundial revisou as Paridades de Poder de Compra (PPP) de referência de 2017 para 2021 e, com isso, recalculou a linha internacional de pobreza extrema de US$2,15 para **US$3,00/dia (PPP 2021)**. Não inventei esse número — é o que a própria API retornou e documentou no campo `indicator.value` da resposta. A coluna `poverty_rate_criterion` do CSV registra o texto exato retornado pela API, não o critério original de US$2,15 do briefing (que está desatualizado).

- **Critério final registrado no CSV**: *"Poverty headcount ratio at $3.00/day (2021 PPP), % da população — World Bank SI.POV.DDAY"*.
- **Ano do dado**: registrado por país na coluna `poverty_data_year` (varia de país para país — a resposta tem `mrnev=1`, ou seja, o ano mais recente disponível para *aquele* país, não um ano fixo).

### Por que não usar linhas de pobreza nacionais
Linhas de pobreza nacionais (ex.: a linha de pobreza oficial do Brasil, do Quênia, etc.) são definidas por cada governo com metodologia própria (cesta básica local, custo de vida local). Usar ~190 critérios diferentes tornaria a coluna **não comparável entre países** — o objetivo aqui é uma métrica única e comparável globalmente, por isso a escolha da linha internacional do World Bank. **Gap conhecido**: isso sacrifica precisão de contexto local (uma linha nacional pode capturar melhor a realidade de pobreza relativa em países de renda média/alta) em troca de comparabilidade — fica registrado como limitação para v2 (ex.: adicionar uma segunda coluna com linha de pobreza nacional onde disponível, sem remover a internacional).

### Limitação conhecida da fonte
O World Bank Poverty and Inequality Platform (PIP) depende de pesquisas domiciliares nacionais (household surveys), que não são realizadas com a mesma frequência em todos os países. Por isso:
- **25 dos 195 países/territórios ficaram sem dado** (coluna em branco) — majoritariamente países de alta renda (que não fazem esse tipo de pesquisa porque a linha de pobreza extrema não é relevante para eles) e alguns países em conflito/com baixa capacidade estatística (ex.: Afeganistão, Eritreia, Líbia, Coreia do Norte, Somália, Camboja). Lista completa na seção 5.
- Isso **não significa pobreza zero** nesses países — o campo foi deixado em branco, conforme instrução explícita de não assumir 0%.

---

## 4. Situação de guerra / conflito armado

- **URL usada**: `https://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts`
- **Data de captura**: 2026-10-01 (página consultada e seu HTML salvo/parseado nesta data; é uamente uma lista viva e pode já ter mudado quando este documento for lido).
- **O que fornece**: tabela de conflitos armados em curso, segmentada por faixas de intensidade (mortes relacionadas a combate por ano). Usei as duas faixas de maior intensidade, exatamente como pedido:
  - **"Major wars"** (10.000+ mortes/ano): 8 conflitos listados.
  - **"Minor wars"** (1.000–9.999 mortes/ano): 13 conflitos listados (a página chama essa faixa de "Minor wars", não "Wars" — mantive a classificação literal da página).
- **Método**: o HTML da página foi baixado e as duas tabelas foram parseadas diretamente (não só via resumo de IA), extraindo a coluna "Location" de cada linha de conflito para montar a lista de países.

### Países marcados `at_war: yes` (63 no total — lista completa no relatório final)
Inclui todo país listado na coluna "Location" de qualquer conflito nas duas faixas — isso inclui tanto o(s) país(es) onde o conflito principal ocorre quanto países listados por "spillover" (transbordamento) do conflito. **Limitação importante**: isso pode **superestimar** o envolvimento de alguns países — por exemplo, Bielorrússia aparece como local da Guerra Russo-Ucraniana por risco geopolítico/transbordamento, não porque há combate em larga escala em território bielorrusso; o mesmo vale para vários países do Oriente Médio listados na linha "Arab–Israeli/Iran–Israel proxy wars" (ex.: Kuwait, Catar, Bahrein, Omã, Jordânia, Egito) — aparecem como locais por causa de ataques/mísseis pontuais relatados em 2026, não guerra terrestre doméstica extensa. Para v2, vale diferenciar "território do conflito principal" de "país afetado por transbordamento" em duas colunas separadas.

Somaliland (região separatista não reconhecida pela ONU, listada como local do conflito somali) não tem código ISO3 próprio e foi tratado como parte da Somália (SOM), que já está marcada `at_war: yes`.

### Limitação da fonte
A Wikipedia é uma **lista viva e editável por qualquer pessoa**, não uma fonte primária acadêmica. Serve bem para uma primeira varredura rápida, mas para uma v2 mais rigorosa, as fontes recomendadas são:
- **UCDP (Uppsala Conflict Data Program)** — base de dados acadêmica com contagem de mortes por conflito, ano a ano, com metodologia documentada.
- **Geneva Academy RULAC** (Rule of Law in Armed Conflict) — classificação jurídica de conflitos armados internacionais/não-internacionais, mantida por instituição acadêmica.

---

## 5. Grameen PPI (Progress out of Poverty Index) — seção separada, não incorporada à tabela principal

### O que é
O **Progress out of Poverty Index® (PPI®)**, hoje renomeado **Poverty Probability Index (PPI)**, é uma ferramenta de **medição de probabilidade de pobreza no nível domiciliar** (não no nível país) — um questionário curto (10 perguntas, específicas por país) que uma organização (ONG, instituição de microfinanças, governo local) aplica a um domicílio para estimar a probabilidade de aquele domicílio estar abaixo de uma ou mais linhas de pobreza.

### Origem e governança
Foi criado e mantido originalmente pela **Grameen Foundation**. Em **15 de julho de 2016**, a ferramenta passou a ser governada pela **"PPI Alliance"** e operacionalmente mantida pela **Innovations for Poverty Action (IPA)** (Washington, DC) — a página atual é `https://www.povertyindex.org/` (antigo domínio: progressoutofpoverty.org). A mudança buscou "ownership" mais amplo da indústria e um modelo de governança/financiamento mais robusto (membros incluem Bill & Melinda Gates Foundation, Cisco Foundation, Catholic Relief Services, entre outros).

### Para que serve
Organizações de combate à pobreza usam o PPI para: (a) segmentar/priorizar quais domicílios atender, (b) monitorar se os beneficiários estão saindo da pobreza ao longo do tempo, (c) reportar impacto a doadores/investidores com um proxy padronizado e de baixo custo (não precisa de levantamento de renda/consumo completo, que é caro e demorado).

### Lista pública de países com scorecard — encontrada
Sim, há lista pública em `https://www.povertyindex.org/ppi-country`. Na consulta de 2026-10-01, o site lista scorecards organizados em duas faixas de atualidade:

- **PPIs atuais (dado coletado nos últimos 10 anos)**: Bangladesh, Benin, Bolívia, Burkina Faso, Camboja, Colômbia, Costa Rica, Costa do Marfim, República Dominicana, Equador, El Salvador, Etiópia, Gana, Guatemala, Honduras, Índia, Indonésia, Quênia, Madagascar, Malaui, México, Mongólia, Moçambique, Myanmar, Nicarágua, Nigéria, Papua-Nova Guiné, Peru, Filipinas, Ruanda, Serra Leoa, África do Sul, Tanzânia, Togo, Uganda, Vietnã, Zâmbia.
- **PPIs mais antigos (dado com mais de 10 anos)**: Afeganistão, Brasil, Egito, Haiti, Quirguistão, Mongólia, Marrocos, Moçambique, Nepal, Nicarágua, Paraguai, Romênia, Rússia, Senegal, Sri Lanka, Tajiquistão.

Total aproximado: ~50 países únicos com scorecard (atual ou histórico) nesta checagem — não foi feita contagem exaustiva de duplicatas entre as duas listas, e a lista do site muda com o tempo (novos scorecards são desenvolvidos continuamente, conforme pipeline publicado em `povertyindex.org/ppis-development`).

### Por que não foi incorporado à tabela principal
O PPI é uma **ferramenta operacional de nível domicílio** — não produz uma estatística agregada e comparável por país do tipo "X% da população está em pobreza segundo o PPI" pronta para consumo direto (isso dependeria de uma pesquisa amostral aplicada país a país, que a Karimu não tem). Incluir "tem scorecard PPI: sim/não" na tabela principal misturaria uma coluna de *disponibilidade de ferramenta operacional* com colunas de *estatística agregada* (população, % pobreza, guerra) — categorias de dado diferentes.

### Recomendação para v2
Numa versão futura, o PPI pode **complementar** (não substituir) a tabela principal assim:
1. Adicionar uma coluna binária "tem scorecard PPI disponível (sim/não)" por país, puxada da lista pública acima — isso sinaliza onde a Karimu já poderia aplicar uma ferramenta pronta de triagem domiciliar se decidir expandir operação para aquele país.
2. Para países-alvo já priorizados (depois de um primeiro corte pela tabela principal: população + % pobreza + não estar em guerra), usar o PPI como ferramenta de **segunda camada**, aplicada em campo pela própria Karimu ou parceiros locais, para priorizar comunidades/domicílios dentro do país escolhido — não para re-ranquear países entre si.

---

## 6. Filtro de shortlist — "países pobres e sem guerra" (2026-10-01)

### Critério de pobreza usado: UN LDC (Least Developed Countries), não um corte % próprio
Eduardo pediu inicialmente um padrão internacional reconhecido em vez de um corte percentual inventado, e levantou o PPI do Grameen como candidato. **Checado e descartado**: o PPI é uma ferramenta de nível domicílio (ver seção 5) — não classifica países inteiros, não tem "corte" aplicável aqui.

Usado em vez disso: **lista UN LDC (Least Developed Countries)**, mantida pelo UN Committee for Development Policy, critério multidimensional (RNB per capita + Índice de Ativos Humanos: mortalidade infantil, mortalidade materna, desnutrição, educação + Índice de Vulnerabilidade Econômica e Ambiental). Revisão trienal mais recente: **dezembro de 2024**, 44 países. Fonte consultada: [en.wikipedia.org/wiki/Least_developed_countries](https://en.wikipedia.org/wiki/Least_developed_countries) (tentativa de acesso direto a `unctad.org/topic/least-developed-countries/list`, a fonte primária, retornou HTTP 403 — bloqueio de bot, não ausência de dado; Wikipedia foi usada como espelho e os 44 nomes batem com a contagem oficial).

**Por que UN LDC em vez de World Bank Low-Income Country (RNB per capita ≤ US$1.175/ano, FY27)**: LDC é multidimensional (também mede saúde/educação/vulnerabilidade, não só renda) — mais alinhado ao enfoque da Karimu nos "cinco desafios da pobreza" (água, saneamento, educação, saúde, serviços financeiros) do que um corte de renda puro. Registrado aqui como decisão, não como único critério correto — trocável em v2 se fizer mais sentido usar o World Bank LIC.

**Alerta de validade temporal**: Bangladesh, Laos e Nepal têm graduação da lista LDC **agendada para 24/nov/2026** — menos de 2 meses à frente da data desta pesquisa (2026-10-01). Laos e Nepal estão na shortlist final (não em guerra); quando a graduação for efetivada, tecnicamente deixam de ser LDC pelo critério usado aqui. Mantidos nesta v1 porque ainda são LDC na data da pesquisa — revisar na próxima atualização.

### Filtro aplicado
`UN LDC (44 países) AND at_war == "no"` → **22 países restantes**. Os outros 22 LDC foram excluídos por `at_war == "yes"` (lista completa no CSV de saída e no relatório da sessão).

### Nova quebra: população total vs. rural
Pedido: para cada país restante, quebrar população total e população rural (justificativa: o modelo de atuação da Karimu é de ward/vila rural — ver `2026-10-01-target-unit-concept.md` — então % rural é um proxy direto de adequação do modelo, não só tamanho de mercado).

- **URL usada**: `https://api.worldbank.org/v2/country/all/indicator/SP.RUR.TOTL.ZS?format=json&per_page=5000&mrnev=1` (% rural da população) e o indicador irmão `SP.RUR.TOTL` (população rural absoluta), mesmo padrão `mrnev=1` (valor mais recente não-vazio por país) usado para população e pobreza.
- **Limitação conhecida**: "rural" aqui segue a definição administrativa de cada país (o Banco Mundial usa a definição nacional de cada governo para rural/urbano, não um critério global único) — mesma limitação de fundo já registrada para linhas de pobreza nacionais (seção 3).

### Entregável
`deliverables/country-shortlist-ldc-no-war.csv` — 22 países, ordenado por % rural decrescente (Malawi no topo, 82,4% rural; Djibouti no fim, 27,0%).

### Nota sobre "província"
Eduardo mencionou "província" ao pedir a quebra rural — mapeada aqui como a necessidade de instrumento ao nível país por ora, dado que o próximo nível (ADM1 — região/província/estado, dependendo do país) ainda não foi construído: isso exigiria dados de censo país a país (muito mais trabalhoso que os indicadores agregados do World Bank usados até aqui) e só faz sentido descontinuar/escopar depois que o shortlist de país estiver fechado. Ver gap conhecido abaixo.

---

## Gaps conhecidos (resumo)

| Tipo | Detalhe |
|---|---|
| Fetch que mudou de formato | `restcountries.com/v3.1` descontinuado — substituído por mirror GitHub `mledoze/countries` (ver seção 1) |
| Critério de pobreza mudou | Linha internacional é hoje US$3,00/dia (PPP 2021), não US$2,15/dia (PPP 2017) como no briefing original (ver seção 3) |
| Dado de pobreza ausente | 25 de 195 países sem valor (principalmente alta renda + alguns países de baixa capacidade estatística/conflito) — lista completa no relatório de entrega |
| Dado de população ausente | 1 país (Vaticano) sem dado de população no World Bank |
| Território não-soberano excluído | Taiwan, Hong Kong, Macau, Kosovo, Porto Rico, Groenlândia e demais territórios não são estados-membros/observadores da ONU — fora da v1 |
| Bug de dado na fonte | Santa Sé (VAT) marcada incorretamente como `unMember=true` na fonte `mledoze/countries`; corrigido via nota, mantida como observadora |
| Superestimação de conflito | Lista de guerra inclui países de "spillover"/transbordamento junto com o país do conflito principal — pode superestimar envolvimento bélico direto de alguns países (ver seção 4) |
| Continente de países transcontinentais | Segue classificação da fonte (`region` do mirror), sem ajuste manual próprio |
| PPI não quantificado por país | Ver seção 5 — é ferramenta operacional, não estatística agregada; não entrou na tabela principal por desenho |
| Fonte primária da LDC bloqueada | `unctad.org/topic/least-developed-countries/list` retornou HTTP 403 (bloqueio de bot); usado espelho Wikipedia, contagem conferida (44) — ver seção 6 |
| LDC em transição | Bangladesh, Laos, Nepal graduam da lista LDC em 24/nov/2026 — shortlist atual (seção 6) ainda os trata como LDC por serem os dados vigentes em 2026-10-01 |
| Rural = definição nacional, não global | % rural do World Bank segue a definição de cada governo, não um critério único comparável — mesma limitação já registrada para linhas de pobreza nacionais (seção 3) |
| Nível província/ADM1 não construído | Quebra rural feita só no nível país nesta v1; detalhar por província (ADM1) exige censo país a país e foi adiada até o shortlist de país estar fechado (ver seção 6) |

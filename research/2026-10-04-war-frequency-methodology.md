# Metodologia — Frequência histórica de guerra/conflito armado nos 44 países LDC (2016-2025)

Data da pesquisa: **2026-10-04**
Arquivo de dados: `deliverables/war-frequency-ldc-10y.csv`

## 0. Por que esta pesquisa

A primeira pesquisa (`2026-10-01-data-sources-methodology.md`, seção 4) mediu "estar em guerra" como uma **foto de um único momento**: a lista viva da Wikipedia "List of ongoing armed conflicts", consultada em 2026-10-01, usando só as faixas de maior intensidade ("Major wars" e "Minor wars", ou seja, 1.000+ mortes/ano). Essa pesquisa aprofunda a pergunta: a lista de países em guerra varia muito ao longo do tempo? O mercado endereçável aumenta quando uma guerra acaba, ou alguns países tendem a estar sempre em guerra (conflito crônico/estrutural)? Para responder, foi necessário: (a) uma janela de 10 anos (2016-2025), não um instante; (b) um critério mais abrangente de "conflito armado" (limiar UCDP de 25 mortes em combate/ano, não só guerras de grande escala de 1.000+/ano); (c) uma fonte acadêmica com metodologia documentada e reprodutível, não uma lista editável.

## 1. Fonte usada e método exato

A fonte primária escolhida foi a **UCDP (Uppsala Conflict Data Program)**, `ucdp.uu.se` — mesma recomendação já registrada como gap conhecido na pesquisa de 2026-10-01. Dentro da UCDP, dois datasets brutos (download direto em CSV, sem necessidade de conta/token de API) cobriram a maior parte dos 44 países:

- **UCDP/PRIO Armed Conflict Dataset, v26.1** (conflito **estatal** — governo vs. outro governo ou grupo armado): `https://ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-261-csv.zip`
- **UCDP Non-State Conflict Dataset, v26.1** (conflito **não-estatal** — entre grupos armados, sem o governo necessariamente envolvido): `https://ucdp.uu.se/downloads/nsos/ucdp-nonstate-261-csv.zip`

**Ponto-chave de método**: cada linha desses dois datasets já é um "conflito-ano" que **atende o limiar de 25 mortes relacionadas a combate/ano da própria UCDP** como critério de inclusão no dataset. Ou seja, a presença de qualquer linha para um país em um ano específico (campo `location`, que pode listar múltiplos países por conflito — casado por nome de país em qualquer posição do campo) já significa "yes" diretamente, sem necessidade de somar mortes manualmente. Isso tornou possível cobrir os 44 países com cobertura completa 2016-2025, sem nenhuma célula "sem_dado" nesses casos.

Para **9 países** (Nepal, Níger, República Centro-Africana, RD Congo, Ruanda, Senegal, Serra Leoa, Somália, Sudão), um subgrupo de pesquisa usou em vez disso o mirror da **Our World in Data** dos mesmos dados UCDP (`ourworldindata.org/grapher/deaths-in-armed-conflicts-by-country.csv` e `deaths-from-one-sided-violence.csv`), calculando mortes líquidas (total menos violência unilateral contra civis) por país-ano e aplicando o mesmo limiar de 25. É uma via alternativa igualmente fundamentada na UCDP, mas **metodologicamente um pouco diferente**: em vez de contar linhas de conflito já pré-classificadas pela UCDP, soma contagens de mortes agregadas e aplica o limiar por fora. Na prática, para esses 9 países os resultados foram inequivocamente ou muito acima do limiar (os 6 países "crônicos" desse grupo: Níger, CAR, RD Congo, Somália, Sudão — todos com centenas a milhares de mortes/ano) ou muito abaixo/zero (Nepal, Senegal, Serra Leoa, Ruanda) — não há casos-limite nesse subconjunto que tornassem a diferença metodológica sensível ao resultado final.

A coluna `source` do CSV registra, linha a linha, qual dos dois métodos foi usado para aquele país.

### Data de captura e versão
Ambos os datasets UCDP foram baixados em **2026-10-04** (v26.1, a versão mais recente disponível nessa data). A OWID foi consultada na mesma data.

## 2. Critério aplicado

Conflito armado ativo num ano = pelo menos uma linha em qualquer um dos dois datasets UCDP para aquele país naquele ano, cobrindo tanto:
- **Estatal** (state-based): governo vs. outro governo ou grupo armado, OU
- **Não-estatal** (non-state): entre grupos armados, sem o governo necessariamente envolvido,

ambos com o limiar padrão da UCDP de **≥25 mortes relacionadas a combate no ano**. Violência unilateral (governo ou grupo armado contra civis desarmados) foi **deliberadamente excluída** do critério, conforme instrução original — isso é relevante para pelo menos um caso (Ruanda 2016: 27 mortes totais, mas 100% unilaterais, logo "no" pelo critério usado aqui).

## 3. Resultado por país — tabela completa

Ver `deliverables/war-frequency-ldc-10y.csv` para a tabela ano a ano completa. Resumo por classificação:

| Classificação | Critério | Nº de países | Países |
|---|---|---|---|
| **Crônico** | ≥8 de 10 anos em guerra | **14** | Afeganistão (10), Burkina Faso (8), Chade (9), Etiópia (10), Mali (10), Moçambique (9), Mianmar (10), Níger (10), Rep. Centro-Africana (10), RD Congo (10), Somália (10), Sudão (10), Sudão do Sul (10), Iêmen (10) |
| **Frequente** | 5-7 de 10 | **3** | Angola (7), Burundi (6), Haiti (5) |
| **Intermitente** | 2-4 de 10 | **4** | Bangladesh (3), Benin (4), Togo (4), Uganda (3) |
| **Raro/nenhum** | 0-1 de 10 | **23** | Camboja (1), Comores (0), Djibouti (1), Eritreia (1), Gâmbia (0), Guiné (1), Guiné-Bissau (0), Ilhas Salomão (0), Kiribati (0), Laos (0), Lesoto (0), Libéria (0), Madagascar (0)*, Malawi (0), Mauritânia (0), Nepal (0), Ruanda (0), Senegal (0), Serra Leoa (0), Tanzânia (1), Timor-Leste (0), Tuvalu (0), Zâmbia (0) |

*Madagascar tem uma ressalva importante — ver seção 5.

**Total: 14 + 3 + 4 + 23 = 44 países.**

## 4. Resposta direta à pergunta do Eduardo

> "O mercado endereçável aumenta quando uma guerra acaba, ou alguns países tendem a estar sempre em guerra?"

**As duas coisas são verdadeiras ao mesmo tempo, mas a distribuição é bimodal, não um meio-termo contínuo** — e isso é a descoberta central desta pesquisa:

- **Um terço dos 44 países LDC (14 de 44, 32%) é estruturalmente/cronicamente em guerra** — 8 ou mais dos últimos 10 anos completos com conflito armado ativo. Nesse grupo, "a guerra acabar" não é o padrão esperado: são conflitos com décadas de persistência (Afeganistão desde 1978 segundo a codificação da UCDP; Somália desde 2006; Iêmen, RD Congo, Sudão do Sul, Mianmar, Mali, Níger, RCA — todos superando 2010). Para esses países, tratar "fim da guerra" como evento provável de curto prazo no horizonte de planejamento da Karimu seria otimismo não sustentado pelos dados — o padrão histórico é de conflito recorrente ou contínuo, não de encerramento permanente.
- **Mais da metade (23 de 44, 52%) teve 0 ou apenas 1 ano de conflito qualificante em toda a década** — ou seja, para a maioria dos países LDC, "estar em guerra" não é o estado natural; é a exceção. Isso inclui praticamente todo o shortlist atual da Karimu (ver seção 6).
- **O meio-termo (frequente + intermitente = 7 de 44, 16%) é onde a pergunta do Eduardo faz mais sentido em sua forma literal**: países como Angola (conflito de Cabinda recorrente em surtos, não contínuo), Haiti (escalada recente e real, de violência de gangues a guerra civil codificada pela UCDP), Benin e Togo (transbordamento jihadista do Sahel iniciado em 2022, ainda em curso, trajetória ainda incerta — pode se tornar crônico ou arrefecer), e Uganda/Bangladesh/Burundi (picos isolados que de fato começaram e terminaram dentro da década). Para esses, o mercado endereçável de fato muda de tamanho dependendo de quando se mede — mas são a minoria dos países, não a regra.

**Conclusão prática para a Karimu**: o filtro binário "está em guerra hoje: sim/não" aplicado em 2026-10-01 provavelmente captura corretamente a maioria dos casos (a maior parte dos países raro/nenhum tende a permanecer assim, e a maior parte dos crônicos tende a permanecer em guerra) — mas tem dois pontos cegos relevantes, detalhados na seção 6: (1) países no shortlist atual que são historicamente mais instáveis do que sua foto de "sem guerra hoje" sugere (Moçambique, Angola); e (2) países excluídos do shortlist hoje que, por critério territorial estrito, têm histórico de conflito muito mais raro do que sua inclusão na lista de "em guerra" da Wikipedia sugeria (Mauritânia, Ruanda — provavelmente excluídos por associação com conflito transfronteiriço/vizinho, não por conflito em seu próprio território).

## 5. Limitações e ressalvas conhecidas

- **Madagascar — discrepância genuína entre fontes**: a UCDP registra **zero conflito** em Madagascar desde 2002 (nem estatal, nem não-estatal, confirmado nos dois datasets brutos). Mas fontes jornalísticas e de ONGs (ISS Africa, IOM, Oxford Journal of Peace Research) descrevem violência letal contínua de "dahalo" (ladrões de gado armados) contra o exército e a gendarmaria malgaxe — por exemplo, 161 mortos em 2016 incluindo 12 soldados, e ~25 oficiais do exército mortos entre 2015-2017. A UCDP aparentemente não codifica essa violência como "conflito armado" porque seu critério exige um ator com **incompatibilidade política** explícita (separatismo, disputa de governo) — dahalo é tratado como criminalidade/banditismo organizado, não conflito político armado. **Esta pesquisa manteve Madagascar como "no" em todos os 10 anos por seguir estritamente a fonte escolhida (UCDP)**, mas a discrepância é real e relevante: se a Karimu quiser um critério mais amplo de "violência armada estrutural" (não só "conflito político-armado" no sentido UCDP), Madagascar mudaria de classificação.
- **Haiti — conflito de gangues codificado como guerra civil**: a UCDP passou a codificar a violência de gangues no Haiti (G9 vs G-Pep, depois Governo do Haiti vs. Viv Ansanm) como conflito armado organizado a partir de 2021, culminando em intensidade "guerra" (1.000+ mortes) em 2025. Essa é uma decisão metodológica da própria UCDP, não um fato incontestável — é qualitativamente diferente dos conflitos separatistas/ideológicos do resto da lista, mas foi mantida como "yes" por seguir a classificação da fonte escolhida.
- **Angola e Chade — conflitos de baixa intensidade, recorrentes "no limiar"**: o conflito de Cabinda em Angola e algumas fases do conflito do Chade aparecem e desaparecem de ano a ano porque a contagem de mortes muitas vezes fica **exatamente no limiar de 25** — pequenas variações na contagem podem mudar a classificação de um ano específico. Tratar esses "sim/não" ano a ano como uma medição precisa de intensidade real seria um excesso de confiança; são corretos quanto à classificação binária da UCDP, mas a diferença entre um ano "sim" e um ano "não" nesses casos é frequentemente pequena.
- **9 países usaram metodologia ligeiramente diferente** (Our World in Data, cálculo líquido de mortes, não contagem direta de linhas de conflito pré-classificadas) — ver seção 1. Não houve casos-limite sensíveis a essa diferença nesse subconjunto, mas é uma diferença de método registrada por transparência.
- **Nenhuma célula "sem_dado" foi necessária** — ao contrário da expectativa inicial do briefing, os datasets brutos da UCDP cobriram todos os 44 países em todos os 10 anos sem lacunas, inclusive os países pequenos esperados sem registro (Kiribati, Tuvalu, Ilhas Salomão, Gâmbia, Guiné-Bissau, Lesoto, Malawi, Mauritânia, Nepal, Ruanda, Senegal, Serra Leoa, Timor-Leste, Zâmbia, Comores — todos confirmados "no" em todos os 10 anos, não assumidos).
- **2025 é o ano mais recente coberto pela versão v26.1 do UCDP/PRIO ACD** (dataset "final" para 2025, não um "ano corrente parcial") — não houve necessidade de excluir 2025 por incompletude.
- **"Spillover"/transbordamento como limitação de leitura, não desta pesquisa**: ao contrário da pesquisa de 2026-10-01 (que usava a localização listada na Wikipedia, incluindo países afetados por transbordamento), esta pesquisa usa o campo `location` da UCDP, que atribui o conflito ao(s) país(es) onde o **combate ocorre**, não a todo país geopoliticamente "envolvido". Isso explica, por exemplo, por que a Eritreia aparece com apenas 1 de 10 anos em guerra mesmo com tropas eritreias combatendo na guerra do Tigré (2020-22) — a UCDP codifica esse conflito como ocorrendo na Etiópia, não na Eritreia.

## 6. O que isso muda (ou não) no shortlist atual de 22 países

O shortlist atual (`deliverables/country-shortlist-ldc-no-war.csv`, filtro LDC + "não em guerra" pela foto de 2026-10-01) tem **22 países**. Cruzando com a classificação desta pesquisa:

**20 de 22 são estáveis** — raro/nenhum conflito ao longo da década (Malawi, Timor-Leste, Ilhas Salomão, Madagascar*, Comores, Tanzânia, Guiné, Laos, Camboja, Lesoto, Serra Leoa, Zâmbia, Guiné-Bissau, Senegal, Libéria, Kiribati, Gâmbia, Tuvalu, Nepal, Djibouti) — o filtro de "não em guerra hoje" bate com o histórico de 10 anos para esses países. Risco de o shortlist mudar para eles em uma reavaliação futura é baixo.

**2 de 22 são uma bandeira amarela real**:
- **Moçambique — classificado "crônico" (9 de 10 anos em guerra)**. Está no shortlist como "não em guerra" porque, na foto de 2026-10-01, a insurgência de Cabo Delgado não atingiu o patamar de "Major war" ou "Minor war" da Wikipedia (1.000+ mortes/ano) — mas pela UCDP, com limiar de 25 mortes/ano, Moçambique teve conflito ativo em 9 dos últimos 10 anos (Renamo até 2016, Cabo Delgado contínuo desde 2018). **Isso é o oposto do que "guerra que já acabou libera mercado" sugeriria** — é o caso mais claro desta pesquisa de um país que parece "não em guerra" só porque o critério de medição (limiar alto de mortes) escondeu um conflito de menor intensidade mas praticamente ininterrupto.
- **Angola — classificado "frequente" (7 de 10 anos em guerra)**. O conflito de Cabinda é recorrente em surtos (2016-17, 2019-20, 2022, 2024-25), nunca formalmente "encerrado" por mais de 1-2 anos seguidos desde 2019. Não é tão grave quanto Moçambique, mas também não é um caso de paz estável — é plausível que reapareça na lista de "em guerra" de uma futura foto da Wikipedia.

Isso **não significa remover esses 2 países do shortlist agora** (a decisão de critério é do Eduardo), mas significa que **o shortlist de 22 países não é tão estável quanto parece** — pelo menos 2 dos 22 (9%) têm um padrão histórico de conflito recorrente/quase-contínuo que pode reaparecer em qualquer atualização futura do filtro "em guerra hoje".

**Achado adicional, fora do shortlist**: dos 22 países LDC hoje classificados "em guerra" (excluídos do shortlist), pelo menos **2 têm zero conflito registrado no próprio território pela UCDP na década inteira** — Mauritânia e Ruanda. Ambos provavelmente entraram na lista de "em guerra" de 2026-10-01 por associação com conflito vizinho/transbordamento (Mauritânia: participação em operações antiterror do G5 Sahel fora de seu território; Ruanda: papel de apoio ao M23 na RD Congo) — não por combate em solo próprio. Isso é consistente com a limitação já registrada na pesquisa de 2026-10-01 (seção 4: "pode superestimar o envolvimento de alguns países"). Esses 2 países são candidatos a **reconsideração** (não garantia de inclusão — depende de critério que a Karimu queira aplicar) se o filtro de guerra for refeito com um critério territorial estrito como o desta pesquisa. Eritreia (1 de 10 anos) é um terceiro candidato mais fraco na mesma direção.

## 7. Lista de fontes exatas por país

Ver coluna `source` no CSV (`deliverables/war-frequency-ldc-10y.csv`) — registrada linha a linha. Resumo:

- **35 países**: UCDP/PRIO Armed Conflict Dataset v26.1 + UCDP Non-State Conflict Dataset v26.1 (download direto, `ucdp.uu.se/downloads/ucdpprio/ucdp-prio-acd-261-csv.zip` e `ucdp.uu.se/downloads/nsos/ucdp-nonstate-261-csv.zip`).
- **9 países** (Nepal, Níger, RCA, RD Congo, Ruanda, Senegal, Serra Leoa, Somália, Sudão): Our World in Data, mirror de dados UCDP (`ourworldindata.org/grapher/deaths-in-armed-conflicts-by-country.csv` e `deaths-from-one-sided-violence.csv`).

Todas as fontes foram consultadas/baixadas em **2026-10-04**.

# Reconciliação: população dos 3 wards (nosso censo 2022) vs. números públicos do site da Karimu

Data: 2026-10-04
Motivação: Eduardo pediu reconciliação porque, para a audiência da Karimu (time exec + investidores), a diferença entre nossos números e os que a própria Karimu já divulga publicamente é importante — uma inconsistência visível prejudica credibilidade.

## Fontes
- Nossa base: citypopulation.de, censo 2022-08-23 (já documentado em `2026-10-01-target-unit-concept.md` e `ward-level-pilot.csv`).
- Site da Karimu: `karimufoundation.org/where-we-work` e `karimufoundation.org/where-we-work/facts` — fetch direto bloqueado (HTTP 403), conteúdo obtido via snippets de busca (Google), não via leitura completa da página. **Limitação**: não li a página inteira, só os trechos que a busca indexou — pode haver mais contexto na página original que explique a diferença.

## Números lado a lado

| Ward | Nosso censo 2022 | Domicílios (Karimu) | Domicílios × 5 (estimado) | "Impacto" divulgado pela Karimu |
|---|---|---|---|---|
| Ayalagaya | 11.935 | 2.400 | ~12.000 | "tirou 15.000 pessoas da pobreza extrema" |
| Arri | 16.114 | 3.300 | ~16.500 | "20.000 pessoas com acesso a água limpa" |
| Dabil | 19.311 | não informado separadamente | — | incluído no combinado abaixo |
| **Arri + Dabil** | **35.425** | — | — | **"impactar 45.000 pessoas vivendo em pobreza extrema"** |

## Achado 1 — o dado de base bate
Domicílios × ~5 pessoas (estimativa padrão de tamanho de família rural na Tanzânia) reproduz quase exatamente nosso número de censo em Ayalagaya (12.000 vs. 11.935) e Arri (16.500 vs. 16.114). **Isso é uma boa notícia**: confirma que nosso dado de população (censo 2022, citypopulation.de) está alinhado com a contagem de domicílios que a própria Karimu usa em campo.

## Achado 2 — os números de "impacto" divulgados publicamente são maiores que a população real, e um deles é logicamente impossível
- Ayalagaya: "15.000 pessoas tiradas da pobreza" é 25% maior que a população total do ward (11.935) — ou seja, estaria afirmando ter impactado mais gente do que mora lá.
- Arri: "20.000 pessoas com acesso a água" é 24% maior que a população total (16.114).
- **Arri + Dabil combinado: "45.000 pessoas em pobreza extrema" excede a população TOTAL dos dois wards juntos (35.425)** — isso não é só arredondamento, é uma contradição lógica: não existe um subconjunto ("pessoas em pobreza extrema") maior que o conjunto todo ("todas as pessoas que moram lá").

## Explicações possíveis (nenhuma confirmada)
1. **Números cumulativos**: "15.000 tiradas da pobreza" pode somar impacto ao longo de vários anos/cohorts, não uma fotografia da população atual num único ano.
2. **Área de cobertura maior que a fronteira administrativa**: sistemas de água/infraestrutura podem alcançar sub-aldeias vizinhas fora do limite oficial do ward.
3. **Projeção futura**: o "45.000" pode ser a meta de um plano estratégico de vários anos (crescimento populacional projetado), não o presente.
4. **Arredondamento/estimativa de marketing de impacto**: comum em material de captação de recursos de ONGs usar números redondos e otimistas sem recálculo censitário.

## Recomendação
Esta divergência **não é resolvível só com pesquisa externa** — a página completa do site (que não consegui ler por bloqueio HTTP 403) pode ter a explicação, mas o caminho mais confiável é perguntar diretamente ao time da Karimu qual é a metodologia/período por trás do número "45.000". Isso é importante antes de qualquer material for investidor citar os dois conjuntos de número lado a lado sem explicação — caso contrário, um investidor atento vai notar a mesma inconsistência que notamos aqui.

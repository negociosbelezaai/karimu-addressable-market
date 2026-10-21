# Índice de corrupção (CPI 2025) — os 44 países LDC

Data: 2026-10-04

## Índice escolhido
**Corruption Perceptions Index (CPI)**, Transparency International — o índice mais usado globalmente pra isso, citado por investidores, agências de rating e organismos multilaterais. Escala **0 (altamente corrupto) a 100 (muito íntegro)** — maior é melhor, o oposto do que "índice de corrupção" sugere à primeira vista; por isso toda comparação abaixo usa explicitamente "mais/menos corrupto", não só o número cru.

## Fonte
`https://images.transparencycdn.org/images/CPI2025_Results.xlsx` — planilha oficial da Transparency International, aba "CPI2025". Dado de **2026-10-04**, CPI 2025 (embargo até 02/10/2026, já público). Arquivo em formato OOXML "strict" (não o padrão usual) — teve que ser parseado manualmente via XML bruto porque `openpyxl`/`pandas` não leem esse formato; método documentado em caso de necessidade de reprodução.

## Cobertura
42 dos 44 países LDC têm CPI 2025. **Kiribati e Tuvalu não têm dado** — a metodologia do CPI exige no mínimo 3 fontes independentes de dado por país, e esses dois micro-estados do Pacífico não têm essa cobertura. Não é erro nosso, é limitação da própria fonte.

## Referência: Tanzânia
CPI 2025 = **40** (rank 84 de 182 países) — classificação "média" globalmente, mas (achado principal, ver abaixo) relativamente boa dentro do nosso próprio shortlist de países pobres/frágeis.

## Achado principal: a maioria do shortlist já é mais corrupta que a Tanzânia
Dos 22 países do shortlist atual (LDC + sem guerra), **18 de 20 com dado disponível são mais corruptos que a Tanzânia** (CPI menor) — só Timor-Leste, Ilhas Salomão e Senegal são menos corruptos; Kiribati e Tuvalu não têm dado. Isso significa que **"mais corrupto que a Tanzânia" sozinho não é um critério de corte útil** (descartaria quase tudo) — o que importa é o TAMANHO do gap.

## Maiores gaps dentro do shortlist atual (22 países)

| País | CPI 2025 | Rank/182 | Delta vs. Tanzânia (40) |
|---|---|---|---|
| Comores | 20 | 163 | -20 |
| Camboja | 20 | 163 | -20 |
| Guiné-Bissau | 21 | 161 | -19 |
| **Moçambique** | 21 | 161 | -19 |
| Madagascar | 25 | 148 | -15 |
| Guiné | 26 | 142 | -14 |
| Libéria | 28 | 136 | -12 |
| Mauritânia* | 30 | 130 | -10 |
| Djibouti* | 31 | 124 | -9 |
| Angola | 32 | 120 | -8 |
| Laos | 34 | 109 | -6 |
| Malawi | 34 | 109 | -6 |
| Nepal | 34 | 109 | -6 |
| Serra Leoa | 34 | 109 | -6 |
| Gâmbia | 37 | 99 | -3 |
| Lesoto | 37 | 99 | -3 |
| Zâmbia | 37 | 99 | -3 |

\* Mauritânia está nos 44 LDC mas foi excluída do shortlist de 22 por "estar em guerra" (ver achado da pesquisa de 2026-10-04 sobre frequência de guerra: Mauritânia teve zero conflito no próprio território no UCDP — provável exclusão por associação a conflito vizinho, candidata a reconsideração).

## Cruzamento com o achado de guerra crônica (2026-10-04)
**Moçambique (nosso #2 maior mercado) acumula dois sinais de risco**: conflito crônico (9 de 10 anos, Cabo Delgado) **e** corrupção bem acima da média do shortlist (-19 vs. Tanzânia). **Madagascar (nosso #3 maior mercado)** também tem gap grande de corrupção (-15), embora sem o sinal de conflito. Isso não significa necessariamente excluir esses países — mas são os dois candidatos mais fortes a uma análise de risco mais profunda antes de qualquer decisão de priorização, já que concentram boa parte do volume populacional do shortlist inteiro.

## Decisão de corte — não tomada aqui
Eduardo pediu pra sinalizar países "muito mais corruptos" que a Tanzânia como candidatos a exclusão, mas não definiu o limiar numérico. Este documento traz os dados ordenados; a decisão de onde cortar (-10? -15? -20?) fica para definição explícita antes de qualquer exclusão ser aplicada ao shortlist.

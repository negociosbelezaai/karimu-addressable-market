# Filtro de corrupção aplicado — shortlist 22 → 17 países

Data: 2026-10-04
Decisão do Eduardo: excluir países do shortlist com gap de CPI ≥ 15 pontos abaixo da Tanzânia (ver `2026-10-04-corruption-cpi-methodology.md` para a tabela completa de gaps).

## Países removidos (5)

| País | CPI 2025 | Gap vs. Tanzânia |
|---|---|---|
| Comores | 20 | -20 |
| Camboja | 20 | -20 |
| Guiné-Bissau | 21 | -19 |
| Moçambique | 21 | -19 |
| Madagascar | 25 | -15 |

## Impacto numérico (antes → depois)

| Métrica | 22 países (antes) | 17 países (depois) | Removido |
|---|---|---|---|
| População total | 337.915.066 | 248.562.391 | 89.352.675 (-26,4%) |
| Pobres estimados (US$3/dia) | 151.486.524 | 98.883.228 | 52.603.296 (-34,7%) |
| **Pobres rurais (ajustado)** | **110.602.137** | **72.153.737** | **38.448.400 (-34,8%)** |
| Comunidades-alvo estimadas | 20.141 | 14.756 | 5.385 (-26,7%) |

**Isso é uma redução grande, não marginal** — Moçambique e Madagascar eram o #2 e #3 maiores mercados do shortlist. O TAM de pobres rurais cai mais de um terço.

## Onde isso fica registrado
- `deliverables/country-shortlist-ldc-no-war-no-corruption.csv` — os 22 países originais, com coluna `excluded_by_corruption_filter` (yes/no), nada apagado.
- `deliverables/target-unit-map.csv` — mesma coluna adicionada, nenhuma linha removida (dado de distrito/comunidade continua disponível pra consulta futura, só marcado como fora do cálculo "ativo").
- Os dados brutos desses 5 países (província, distrito, piloto de ward onde aplicável) **continuam no projeto, intactos** — a decisão de excluir é sobre o shortlist ativo de priorização, não um apagamento de pesquisa já feita. Se o critério mudar depois, basta refiltrar.

## Interação com achados anteriores
Moçambique já tinha sido sinalizado com conflito crônico (9/10 anos) — agora sai do shortlist por dois motivos independentes e convergentes (guerra + corrupção), reforçando que a exclusão é bem fundamentada, não um artefato de um único critério isolado.

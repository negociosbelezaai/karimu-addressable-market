# Disparidade real de pobreza rural vs. urbana — Tanzânia, Moçambique, Madagascar

Data: 2026-10-03

## Motivação
A estimativa anterior de pobres rurais no shortlist (90,9M de 151,5M, 60%) assumia taxa de pobreza uniforme entre campo e cidade — sabidamente uma subestimativa, já sinalizado quando foi calculada. Esta pesquisa busca a disparidade real nos 3 países que concentram o maior volume de pobreza (Tanzânia, Moçambique, Madagascar).

## Dados encontrados (linha de pobreza NACIONAL, não a internacional de US$3/dia)

| País | Pobreza rural | Pobreza urbana | Pobreza nacional | Fonte |
|---|---|---|---|---|
| Tanzânia | 31,3% | 15,8% | 26,4% | HBS 2017/18 (Household Budget Survey), NBS Tanzania — [2017_18_HBS_Key_Indicators_Report](https://www.nbs.go.tz/nbs/takwimu/hbs/2017_18_HBS_Key_Indicators_Report_Englll.pdf). Também traz contagem absoluta: ~11,3M pobres rurais + ~2,6M pobres urbanos = ~13,9M pobres no total (linha nacional, 2018) — número bem menor que os 36,2M que calculamos pela linha de US$3/dia, porque são critérios de pobreza diferentes (ver limitação abaixo).
| Moçambique | 70,9% | 47,6% | — | IOF 2019/20 (Inquérito ao Orçamento Familiar), INE Moçambique, citado em World Bank Poverty & Equity Brief. Confirmado o ano exato via busca cruzada (a mesma cifra aparece associada a IOF 2019/20 em múltiplas fontes).
| Madagascar | 79,9% | 55,5% | 75,2% | EPM 2022 (Enquête Périodique auprès des Ménages), INSTAT Madagascar, citado no Madagascar Poverty Assessment (World Bank, fev/2024).

## Método de ajuste
Não dá pra só somar os números absolutos acima aos 151,5M calculados antes — são métricas de pobreza diferentes (linha nacional vs. linha internacional de US$3/dia 2021 PPP). Em vez disso, usei a **razão de disparidade** (pobreza rural ÷ pobreza urbana) de cada país, aplicada sobre o total de pobres já calculado pela linha de US$3/dia, via:

```
share_rural_ajustado = (pop_rural% × taxa_pobreza_rural) / (pop_rural% × taxa_pobreza_rural + pop_urbana% × taxa_pobreza_urbana)
```

Isso assume que a *proporção* de disparidade rural/urbana é parecida entre as duas linhas de pobreza — razoável (a relação estrutural costuma ser similar), mas **não verificado** — seria preciso achar a razão calculada diretamente na linha de US$3/dia pra confirmar.

## Resultado

| País | Pobres (US$3/dia) | Rural — ingênuo (=%pop rural) | Rural — ajustado pela disparidade real |
|---|---|---|---|
| Tanzânia | 36.190.029 | 22.835.908 (63,1%) | **27.941.750 (77,2%)** |
| Moçambique | 29.004.166 | 18.214.616 (62,8%) | **20.751.510 (71,5%)** |
| Madagascar | 22.656.549 | 15.202.544 (67,1%) | **16.900.553 (74,6%)** |
| **Total (3 países)** | 87.850.744 | 56.253.069 (64,0%) | **65.593.813 (74,7%)** |

A correção aumenta o total rural desses 3 países em **~9,3 milhões de pessoas** (de 64,0% pra 74,7% do total de pobres). Extrapolando esse mesmo padrão proporcionalmente para o total de 18 países do cálculo original (90,9M estimados de forma ingênua), o número real de pobres rurais no shortlist inteiro provavelmente passa de **100 milhões** — não foi recalculado país a país pros outros 15, só extrapolado pela mesma ordem de grandeza de correção.

## Limitações explícitas
1. **Duas linhas de pobreza diferentes** (nacional vs. US$3/dia) — a razão de disparidade foi transferida de uma pra outra por premissa, não por dado direto.
2. **Só 3 dos 21 países** com ajuste real — os outros 18 continuam na estimativa ingênua (uniforme).
3. Moçambique: ano exato (2019/20) inferido por citação cruzada entre fontes, não confirmado num único PDF com texto extraível (os PDFs oficiais do World Bank "Poverty & Equity Brief" são gráficos rasterizados, sem texto selecionável).

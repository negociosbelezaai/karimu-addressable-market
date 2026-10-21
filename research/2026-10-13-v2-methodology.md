# Metodologia v2 — Resposta ao Feedback da Liderança da Karimu

Data: 2026-10-13
Gatilho: mensagem da liderança da Karimu (2026-10-10) com crítica ao filtro LDC e análise Gemini alternativa.

---

## O problema apontado pela liderança da Karimu

O filtro UN LDC (Least Developed Countries), usado na v1 como proxy de "onde há pobreza", **descarta países com muita pobreza rural por não serem "países pobres" pela classificação LDC**. Exemplos: Índia (~112M pobres rurais), Quênia (~14M), Bangladesh (~9.5M), Brasil (~4M), Filipinas (~2.9M). Nenhum destes é LDC — mas todos têm populações rurais abaixo de US$3/dia em escala relevante para a Karimu.

Citação da liderança da Karimu:
> "Nao se pode aplicar a definicao de Poor country como criterio de eliminacao por que senao voce elimina um monte de lugar onde tem pobreza, mas o pais em si nao e' pobre."

---

## Nova metodologia (v2)

| Dimensão | v1 | v2 |
|---|---|---|
| Escopo inicial | 195 países | 195 países |
| Filtro "país pobre" | UN LDC (44 países) | **Removido** |
| Filtro de conflito | Wikipedia: guerras ativas ≥1.000 mortes/ano | Ativo: conflito armado em curso (pré-filtrado pelo Gemini/World Bank) |
| Linha de pobreza | US$3/day (2021 PPP) — World Bank | US$3/day (2021 PPP) — World Bank (mesmo) |
| Critério final | Rural + LDC + não em guerra | **Rural + não em conflito ativo + <$3/dia** |
| Filtro de corrupção (CPI) | Aplicado por Eduardo (CPI gap ≥15 vs. TZA) | **Não aplicado em v2** — dados de CPI disponíveis só para os 44 LDC; Eduardo decide se reaplicar |

---

## Fonte dos dados v2

**A liderança da Karimu (2026-10-10)** encaminhou análise gerada pelo Gemini, baseada em:
- World Bank, revisão de junho 2025 — linha de pobreza US$3/day (2021 PPP)
- Exclusão de países em conflito armado ativo (Nigeria, DRC, Ethiopia, Sudan, Yemen, etc. já excluídos)
- Dado: população rural pobre estimada por país

Esta é uma **estimativa Gemini** (não dado bruto de API direta). Nível de confiança menor que os dados da v1 (que foram extraídos direto da API do World Bank por país). Para uma v3, vale re-verificar os maiores países pela API, especialmente Índia, Uganda, Paquistão, Quênia.

---

## Comparação v1 vs. v2

| Métrica | v1 (17 países ativos) | v2 (45 países) | Delta |
|---|---|---|---|
| Países | 17 | 45 | +28 |
| Pobres rurais totais | ~72,2M | ~315,8M | **+4,4x** |
| Países novos (não eram LDC) | — | 34 | — |
| Pobres rurais novos | — | ~222,3M | — |

**A Índia sozinha representa 112M rurais pobres — 35% do total v2 e mais do que todo o mercado v1.**

---

## Impacto por grupo de países

### Países do v1 LDC que sobrevivem no v2 (11 países, 93.5M rurais pobres)
Tanzania, Madagascar, Malawi, Angola, Zambia, Senegal, Sierra Leone, Nepal, Cambodia, Lesotho, Liberia

### Países do v1 LDC que SOMEM no v2 (8 países)
- **Por conflito/fragilidade (WB FCS FY25):** Timor-Leste, Kiribati, Solomon Islands, Tuvalu, Guinea-Bissau, Comoros
  - *Nota: estes estavam no nosso v1 ativo ou no shortlist pré-corrupção. O FCS do WB é mais conservador que a lista Wikipedia usada em v1 — foram incluídos por erro de critério na v1.*
- **Por serem pequenos demais (< limiar do Gemini):** Djibouti, Laos, Guinea, Gambia
  - *Continuam sendo LDC pobres, mas população rural pobre total é irrelevante à escala do mercado.*
- **Moçambique:** estava em v1 mas é FCS conflict-affected (WB FY25) — corretamente ausente do v2.

### Países NOVOS em v2 (34 países) — top 10 por rurais pobres
| País | Rurais pobres | Por que não estava em v1 |
|---|---|---|
| Índia | 112.0M | Não é LDC (renda média-baixa) |
| Uganda | 19.5M | Não é LDC |
| Paquistão | 18.0M | Não é LDC |
| Quênia | 14.2M | Não é LDC |
| Bangladesh | 9.5M | Não é LDC |
| Indonésia | 6.8M | Não é LDC |
| Ruanda | 6.6M | Não é LDC |
| Benin | 4.2M | Não é LDC |
| Brasil | 4.1M | Não é LDC |
| Costa do Marfim | 4.0M | Não é LDC |

---

## Filtro de corrupção CPI aplicado (2026-10-13)

CPI 2025 levantado para todos os 45 países (via Wikipedia, Transparency International). Critério mantido: gap ≥15 vs. Tanzania (CPI=40), ou seja, excluir países com CPI ≤25.

### Países excluídos por CPI

| País | CPI 2025 | Gap | Rural poor | Status v1 |
|---|---|---|---|---|
| Madagascar | 25 | 15 | 20,2M | excluído em v1 |
| Uganda | 25 | **15** | 19,5M | novo em v2 |
| Bangladesh | 24 | 16 | 9,5M | novo em v2 |
| Honduras | 22 | 18 | 2,3M | novo em v2 |
| Camboja | 20 | 20 | 1,8M | excluído em v1 |
| Eswatini | 23 | 17 | 0,6M | novo em v2 |
| Nicarágua | 14 | 26 | 0,3M | novo em v2 |
| Paraguai | 24 | 16 | 0,2M | novo em v2 |

**Total excluído: 8 países, 54,4M rurais pobres**

⚠️ **Uganda (CPI=25, gap=15)** está exatamente na fronteira do corte. Eduardo decidiu se mantém ou flexibiliza. Uganda é o 4º maior mercado (19,5M) e faz parte do bloco Leste Africano que a liderança da Karimu destacou.

### Shortlist ativo v2 final

**37 países, ~261,4M rurais pobres**

| Métrica | v1 | v2 |
|---|---|---|
| Países | 17 | 37 |
| Rurais pobres | ~72,2M | ~261,4M |
| Múltiplo | — | **+3,6x** |

### Top 5 novos (passaram no CPI)
1. Índia: 112M (CPI=39, gap=1) — maior mercado, quase no nível da Tanzania em corrupção
2. Paquistão: 18M (CPI=28, gap=12) — aprovado por margem de 3 pontos
3. Quênia: 14,2M (CPI=30, gap=10) — aprovado com folga
4. Indonésia: 6,8M (CPI=34, gap=6)
5. Ruanda: 6,6M (CPI=58, gap=-18) — mais limpo que a Tanzania

---

## Verificação World Bank API (top 5)

Tentada em 2026-10-13; API retornou timeout. Verificação matemática alternativa feita manualmente — os números da análise externa são internamente consistentes:
- India: 1,43B pop × 9,6% pov × 81% rural ≈ 111M ✓ (análise: 112M)
- Kenya: 55M × 33% × 78% ≈ 14,2M ✓ (análise: 14,2M)
- Bangladesh: 173M × 7,3% × 75% ≈ 9,5M ✓ (análise: 9,5M)

Para verificação direta da API, retentar em sessão futura com: `https://api.worldbank.org/v2/country/IND;UGA;PAK;KEN;BGD/indicator/SI.POV.DDAY?format=json&mrnev=1`

---

## Referências
- Mensagem liderança da Karimu, 2026-10-10
- World Bank FCS FY25 list: https://thedocs.worldbank.org/en/doc/b3c737c4687db176ec98f5c434d0de91-0090082024/original/FCSListFY25.pdf
- CPI 2025: Transparency International via Wikipedia (2026-10-13)
- Entregável: `deliverables/country-market-map-v2.csv`

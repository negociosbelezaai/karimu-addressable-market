# Metodologia — Mapeamento de Distritos v2 (2026-10-13)

## Objetivo

Construir um mapa de distritos (ADM2) para todos os 43 países do shortlist ativo v2, replicando o método da v1 (que cobria 22 países LDC) para o universo ampliado.

## Entregável

`deliverables/district-level-map-v2.csv` — **15.404 linhas**, 43 países.

## Fonte de dados

**HDX COD-PS (Common Operational Dataset — Population Statistics)**
- URL padrão: `https://data.humdata.org/api/3/action/package_show?id=cod-ps-{iso3_lower}`
- Arquivo-alvo: `{iso3}_admpop_adm2_{year}.csv` ou equivalente XLSX
- Capturado em: 2026-10-13

## Cobertura por país

| Status | Países | Distritos |
|---|---|---|
| Dados v1 reutilizados (ADM2 real, fontes originais) | TZA, MDG, MWI, AGO, ZMB, SEN, NPL, SLE, LSO, LBR | 950 |
| HDX COD-PS novo — CSV com ADM2_PCODE | UGA, PAK, BGD, IDN, RWA, BEN, BRA, CIV, GHA, PHL, TGO, GTM, HND, ZAF, BOL, COL, ECU, SWZ, VNM, MEX, LKA, SLV, MAR, NAM, BWA, PRY, EGY, DOM, THA | ~13.479 |
| HDX COD-PS novo — XLSX com ADM2 | KEN (290), TGO (37) | 327 |
| ADM1 usado como proxy (sem ADM2 em HDX) | PER | 25 |
| Placeholder — dados não disponíveis em HDX | IND, BTN | 2 |

**Total: 15.404 linhas, 41/43 países com dados reais.**

## Gaps conhecidos

### India (IND) — crítico
- India não tem pacote `cod-ab-ind` ou `cod-ps-ind` no HDX
- Tem ~640 distritos (ADM2), chamados "districts" ou "zilas"
- **Impacto: 112M rurais pobres — 35% do TAM total — sem cobertura distrital**
- Fontes recomendadas para v3: Census India (censusindia.gov.in), GADM v4, ou dados do NITI Aayog

### Bhutan (BTN) — baixo impacto
- Não tem HDX COD; tem 20 dzongkhags (ADM2 equivalente)
- Rural poor: ~0,1M — impacto negligível no total
- Fontes recomendadas: National Statistics Bureau of Bhutan

### Peru (PER) — proxy
- HDX tem apenas ADM0 e ADM1 para Peru; sem ADM2 CSV/XLSX
- Usado ADM1 (25 regiões) como proxy
- Rural poor: ~0,9M
- Fontes recomendadas: INEI Peru (inei.gob.pe)

## Variantes de coluna tratadas

Os arquivos HDX COD-PS usam diferentes convenções de nomeação por idioma:
- Inglês: `ADM2_EN`, `ADM2_PCODE` (padrão UN)
- Francês: `ADM2_FR`, `ADM2_PCODE`
- Português: `ADM2_PT`, `ADM2_PCODE`
- Espanhol: `ADM2_ES`, `ADM2_PCODE`
- Pakistan (variante): `admin2Name_en`, `admin2Pcode`

O parser foi atualizado para detectar automaticamente todas as variantes.

## Dados rurais por distrito

- **Pakistan**: único país com `R_TL` (rural total) por distrito no HDX COD-PS → 131/131 distritos com dado rural
- **Demais países**: dado rural disponível apenas no nível país (do estudo World Bank); distribuição por distrito pode ser feita proporcionalmente à população total como próximo passo

## Comparação v1 vs. v2

| Métrica | v1 (22 países LDC) | v2 (43 países global) |
|---|---|---|
| Países | 22 | 43 |
| Distritos/unidades | 1.773 | **15.404** |
| Países com ADM2 real | 22 | **41** |
| Maior país | Tanzania (169 wards) | Brazil (5.570 municípios) |

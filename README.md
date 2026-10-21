# Karimu — Addressable Market Study

Sizing the global universe of rural communities in extreme poverty whose profile matches the operating
model Karimu has proven in Babati, Tanzania.

**Headline:** ~314M people in rural poverty across 43 countries · 16,383 districts mapped ·
~223,467 estimated communities.

## Read the report

- **Web (live HTML):** https://negociosbelezaai.github.io/karimu-addressable-market/
- **PDF:** [Karimu-Addressable-Market.pdf](Karimu-Addressable-Market.pdf)

## Raw data

All figures in the report trace to these CSVs. Each row carries its own source, capture date and criterion.

| File | What it is |
|---|---|
| [`data/country-market-map-v2.csv`](data/country-market-map-v2.csv) | 45 countries — the full funnel with rural/total poor, national poverty rate, rural share, CPI score and gap, conflict and exclusion flags. |
| [`data/district-level-map-v2.csv`](data/district-level-map-v2.csv) | 16,383 districts (ADM2) across the 43 active countries — population, rural share, administrative IDs/P-codes, parent hierarchy. |
| [`data/target-unit-map-v2.csv`](data/target-unit-map-v2.csv) | The community-scale model — how each district converts into ~223,467 target units (direct vs. modeled at 15k inhabitants). |
| [`data/corruption-cpi-2025.csv`](data/corruption-cpi-2025.csv) | Transparency International CPI 2025 scores and the gap versus Tanzania (CPI 40) used in the governance screen. |

Raw download URLs follow the pattern
`https://raw.githubusercontent.com/negociosbelezaai/karimu-addressable-market/main/data/<file>.csv`.

## Full project archive

Beyond the headline report and its four source CSVs, this repository also publishes the complete
working archive of the study so the analysis can be audited and reused end to end:

- [`deliverables/`](deliverables/) — every dataset produced across both methodology versions (country,
  province, district, ward and target-unit maps), the earlier report editions (HTML + PDF), and the
  data-processing scripts.
- [`research/`](research/) — the methodology and research notes behind each step: data sources,
  sub-national unit definition, province/district/ward construction, the rural-poverty disparity
  analysis, the corruption (CPI) screen and the v2 methodology revision.
- [`PROJECT-LOG.md`](PROJECT-LOG.md) — the chronological project log, from the first country map to the
  published report.

## Sources

World Bank (rural poverty US$3/day PPP 2021, June 2025 revision; rural population); Transparency
International CPI 2025; World Bank FCS list FY2025 (conflict); UCDP/PRIO Armed Conflict Dataset v26.1
(Uppsala University); HDX/OCHA COD-AB & COD-PS (administrative boundaries and P-codes); Census of India
2011; INEI Peru Censo Nacional 2017; NSB Bhutan Population & Housing Census 2017; ISO 3166-2.
Data collected October 2026.

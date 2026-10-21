# Conceito: Unidade-Alvo (ward-equivalente) — generalizável para todos os países

Data: 2026-10-01

## Motivação
A Karimu (Karimu International Help Foundation, karimufoundation.org, fundada 2008) atua hoje em 3 wards do Distrito Rural de Babati, Região de Manyara, Tanzânia: **Ayalagaya**, **Arri** e **Dabil**. A escolha de alvos futuros será feita neste nível (distrito/ward), não no nível país. Este documento define o conceito de forma usável para qualquer país, não só Tanzânia.

## Calibração (dado real, não estimado onde possível)
- **Arri**: 14.146 hab. (censo 2012) — [Wikipedia](https://en.wikipedia.org/wiki/Arri_(Tanzanian_ward))
- **Dabil**: 16.781 hab. (censo 2012) — Wikipedia/Wikidata
- **Ayalagaya**: ~50 km², 2.400 domicílios (população não confirmada em fonte primária nesta pesquisa; estimativa grosseira ~12.000 hab. a 5 hab./domicílio) — [karimufoundation.org/where-we-work](https://karimufoundation.org/where-we-work)
- Todas as três no mesmo distrito (Babati Rural, 4 divisões / 21 wards / 96 vilas — censo 2012).
- Hierarquia da Tanzânia: País → Região (31) → Distrito (169) → Divisão → **Ward** (menor unidade com liderança eleita) → Vila/Rua → Subúrbio/hamlet. [Subdivisions of Tanzania](https://en.wikipedia.org/wiki/Subdivisions_of_Tanzania)

Faixa observada: ~12k–17k habitantes.

## Definição proposta: "Unidade-Alvo"
A menor unidade sub-nacional **oficialmente reconhecida** (nome e fronteira definidos por governo ou instituto de estatística nacional) que:
1. Tipicamente tem **~5.000 a ~30.000 habitantes** (faixa alargada a partir da calibração real de 12-17k, para acomodar variância rural/urbana entre países).
2. Tem identidade comunitária/liderança local suficiente para ser alvo de intervenção direta (escola, posto de saúde, grupo de poupança) — não é um recorte estatístico arbitrário.

Dois critérios de corte:
- **Não grande demais**: perde a coesão comunitária que torna a intervenção direta eficaz (ex.: um county americano ou um distrito indiano inteiro, 100k+ hab.).
- **Não pequeno demais**: abaixo de ~2-3k raramente tem dado público de população e não sustenta a escala de um projeto tipo escola/posto de saúde.

**Importante**: o "nível administrativo" (Admin 1/2/3/4) usado para encontrar essa unidade **varia por país** — não existe um "nível N" único e comparável globalmente. O critério de seleção é sempre a faixa populacional + o papel funcional, nunca o número do nível.

## Precedente institucional
A União Europeia já resolveu exatamente este problema de comparabilidade entre hierarquias administrativas nacionais distintas: o sistema **NUTS/LAU** do Eurostat define regiões por **faixa populacional** (NUTS3: 150k-800k; NUTS2: 800k-3M) e usa **LAU (Local Administrative Unit)** para o nível município — não por contagem de nível hierárquico. Mesma lógica aplicada aqui, numa escala populacional menor (5k-30k em vez de 150k+).

## Exemplos de mapeamento por país

| País | Nome local da unidade-alvo | Nível típico (varia por país) |
|---|---|---|
| Tanzânia | Ward (Kata) | Admin 3 |
| Quênia | Ward | Admin 3 |
| Etiópia | Kebele | Admin 3/4 |
| Nigéria | Ward | Admin 3 |
| Índia | Gram Panchayat (rural) / Ward (urbano) | Admin 4 |
| Brasil | Município (nos menores; ~70% dos municípios já têm <20k hab.) | Admin 2 — não há subdivisão oficial com fronteira/governo próprio abaixo do município na maioria dos casos |
| UE (geral) | LAU / município | — (padrão Eurostat já existente) |
| EUA | County Subdivision / Census-designated place | Admin 3/4 |

## Identificador único — reaproveitar, não inventar
Padrão já existente, equivalente ao ISO3 usado na tabela de países:
- **P-code (Place code)**, do sistema **HDX COD-AB** (Common Operational Datasets - Administrative Boundaries, OCHA/ONU + institutos de estatística nacionais). Existe um "Global P-code List" consolidado, com p-code pai e nível por unidade, cobrindo a maior parte do mundo usado por ONGs humanitárias para exatamente este tipo de targeting.
- **Fallback**: GADM (códigos GID_1/2/3) para países sem COD-AB publicado — cobre o mundo todo, mas é mantido por projeto acadêmico, não estatística oficial (mesma hierarquia de confiabilidade documentada em `2026-10-01-data-sources-methodology.md` para população/pobreza).

## Gargalo conhecido (para v2)
Fronteira + nome da unidade é factível para quase todo país via COD-AB/GADM. **População por unidade-alvo é o gargalo real**: não existe uma API global equivalente ao World Bank para esse nível — é censo nacional país a país, com datas/metodologias heterogêneas. Montar essa segunda tabela para os ~195 países de uma vez é uma ordem de grandeza maior que a tabela de países. Recomendação: aplicar esse conceito primeiro ao subconjunto de países que sobrar do filtro da tabela 1 (população mínima + % pobreza + não estar em guerra — filtro ainda pendente), não aos 195 de uma vez.

## Validação com P-code real (2026-10-01)

Fonte: gazetteer oficial HDX COD-AB para Tanzânia — `cod-ab-tza` (resource `tza_admgz_20181019.xlsx`) e sua republicação em `cod-ps-tza` (resource `tza_gazetteer.xlsx`, metadata modificada em 2026, mas com os **mesmos 3.643 registros e os mesmos 21 wards de Babati** — ou seja, é republicação do mesmo levantamento de fronteiras de 2018, não uma atualização de fato). Mantido por Tanzania National Bureau of Statistics + UN OCHA ROSA.

| Ward | P-code | Hierarquia (prefixo embutido) | Status |
|---|---|---|---|
| Arri | `TZ2101111` | TZ → TZ21 (Manyara) → TZ2101 (Babati) → TZ2101111 | ✅ confirmado |
| Dabil | `TZ2101131` | TZ → TZ21 → TZ2101 → TZ2101131 | ✅ confirmado |
| Ayalagaya | — | — | ❌ **não existe no gazetteer oficial** |

### Achado: Ayalagaya é uma ward nova, mais recente que o último P-code oficial publicado
O distrito de Babati (TZ2101) tem só 21 wards no gazetteer oficial, sem Ayalagaya. Mas o **censo nacional de 2022** (via citypopulation.de, fonte: National Bureau of Statistics Tanzania, census 2022-08-23) já lista **Ayalagaya como ward própria, 11.935 hab.**, separada de "Dareda" (13.716 hab., `TZ2101123` no gazetteer oficial) — de onde ela foi provavelmente desmembrada. Arri e Dabil também têm número maior no censo 2022 (16.114 e 19.311) vs. 2012 (14.146 e 16.781), consistente com crescimento populacional normal, sem contradição.

**Implicação para o conceito**: datasets de P-code oficiais (COD-AB) atrasam em relação a divisões administrativas novas — wards são desmembradas com alguma frequência (crescimento populacional, redistritamento) e o P-code oficial só é publicado depois. Isso vai se repetir em outros países, não é uma particularidade da Tanzânia.

**Decisão (2026-10-01): atribuir ID provisório**, com um critério de reconhecimento fácil — ver convenção abaixo.

### Convenção de ID provisório

```
<p-code oficial do ancestral mais próximo>-PROV<n>
```

- **Ancestral mais próximo com P-code oficial**: a unidade-mãe de onde a nova unidade foi desmembrada (ward → distrito → região, nessa ordem de preferência — usa o nível mais específico que ainda tenha P-code real).
- **Marcador `-PROV`**: literal, maiúsculo, sempre precedido de hífen. **Critério de reconhecimento**: um P-code oficial do padrão COD-AB **nunca contém hífen ou letras além do prefixo de país** — então qualquer `unit_id` com hífen é, por definição, não-oficial. Isso é verificável por regex (`-PROV` no id) sem precisar consultar nenhuma tabela de referência.
- **`<n>`**: sequencial (1, 2, 3...), atribuído por ordem alfabética do nome entre as unidades-irmãs pendentes do mesmo pai, no momento em que cada uma é adicionada — nunca renumerado depois (uma unidade nova vinda do mesmo pai sempre recebe o próximo número, as existentes não mudam).

**Aplicado a Ayalagaya**: pai = Dareda (`TZ2101123`) → **`TZ2101123-PROV1`**

### Reconciliação quando o P-code oficial sair
Quando o HDX publicar uma gazetteer nova que inclua a unidade, substituir o `unit_id` pelo P-code oficial e registrar o ID provisório antigo num campo `superseded_provisional_id` (ou equivalente) na tabela — para qualquer relatório/pitch que já tenha citado o ID provisório continuar rastreável.

## Schema proposto para a próxima tabela (não construída ainda)
`unit_id (P-code oficial, ou provisório no formato <pcode-pai>-PROV<n>), is_official_id (yes/no), superseded_provisional_id (preenchido só na linha que recebeu o P-code oficial, depois de ter sido provisória), unit_name, local_unit_type (ward/kebele/commune/município/...), country_id (ISO3, FK), admin_level_used, parent_unit_name, parent_pcode, population, population_source, population_date_captured, population_data_year, poverty_rate_pct, poverty_source, poverty_date_captured, notes`

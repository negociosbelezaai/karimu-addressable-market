# Nível Distrito (ADM2) — resumo consolidado

Data: 2026-10-02
Entregável: `deliverables/district-level-map.csv` (1.773 linhas, 22 países, consolidado de 4 lotes)
Notas detalhadas por país: `2026-10-02-district-level-group{1,2,3,4}-notes.md`

## Validação de consistência (feita nesta sessão, não só pelos agentes)
- 1.773 linhas, 22 países (bate com o shortlist), **zero `unit_id` duplicado**.
- **Zero `parent_pcode` órfão**: todo distrito com `parent_pcode` preenchido aponta pra uma província que de fato existe em `province-level-map.csv` — cadeia país→província→distrito íntegra nos 4 lotes, checado programaticamente, não por amostra.
- 11 unidades com ID provisório (`<pcode-pai>-PROV<n>`): Timor-Leste (3), Camboja (5), Zâmbia (1), Senegal (1) — todas por redistritamento mais novo que o último P-code oficial publicado, mesmo padrão já visto em Ayalagaya (Tanzânia).
- 1 linha de nota para Tuvalu (sem tabela forçada — país não tem ADM2, confirmado, não presumido).
- **Incidente verificado**: o lote 1 reportou que um dos agentes, já em estado "concluído", continuou rodando e gerou uma segunda versão divergente dos dados do Timor-Leste a partir de uma fonte que "alucinou" números; o próprio agente percebeu, descartou a versão ruim e verificou a boa contra o PDF oficial da UNFPA (2022). Conferi por fora: os 67 registros de Timor-Leste no CSV final batem exatamente com o PDF (ex.: Aileu Vila=26.471, Hatulia A=20.305) — a autocorreção se sustentou. Registrado como risco de processo para lotes futuros: checar o resultado de um agente contra a fonte primária, não só aceitar o relatório final.

## Cobertura por país (1.773 distritos no total)

| País | ISO3 | Distritos | P-code oficial | Observação |
|---|---|---|---|---|
| Angola | AGO | 161 | 100% | — |
| Camboja | KHM | 203 | 197/203 | 6 provisórios (redistritamento recente) |
| Tanzânia | TZA | 169 | 100% | — |
| Moçambique | MOZ | 159 | 100% | 4 distritos com população `NA` na própria fonte (não omissão nossa) |
| Laos | LAO | 148 | 100% | — |
| Libéria | LBR | 136 | 100% | — |
| Madagascar | MDG | 119 | 100% | — |
| Zâmbia | ZMB | 116 | 115/116 | 1 provisório (Lusangazi) |
| Nepal | NPL | 77 | 100% | — |
| Lesoto | LSO | 78 | 100% (fronteira) | só 36/78 com população (reforma 2017 sem censo equivalente) |
| Timor-Leste | TLS | 67 | 64/67 | 3 provisórios |
| Senegal | SEN | 46 | 45/46 | 1 provisório (Keur Massar) |
| Gâmbia | GMB | 49 | 100% (fronteira) | só 41/49 com população (granularidade da fonte diverge) |
| Guiné-Bissau | GNB | 39 | 100% | ver divergência Bissau abaixo |
| Guiné | GIN | 34 | 100% | — |
| Kiribati | KIR | 36 | 100% | várias ilhas com população 0 (desabitadas, mantido da fonte) |
| Djibouti | DJI | 20 | 100% (fronteira, via GADM) | **0/20 com população confiável** — fonte secundária descartada por risco de dupla contagem |
| Malawi | MWI | 32 | 100% | — |
| Ilhas Salomão | SLB | 50 | 100% | — |
| Serra Leoa | SLE | 16 | 100% | — |
| Comores | COM | 17 | 100% | — |
| Gâmbia | — | (acima) | | |
| Tuvalu | TUV | — | n/a | país não tem ADM2 (confirmado) |

## Achados que valem atenção

1. **Divergência Guiné-Bissau (Bissau) — RECONCILIADA em 2026-10-02**: o nível província usava Wikipedia (387.909) e o nível distrito usava o PDF oficial do INE Guiné-Bissau (365.097, soma bruta das 8 sub-setores). Terceira fonte (citypopulation.de) resolveu: ela cita o próprio INE para 387.909 e registra que é um total **ajustado por omissão censitária** (não é só a soma bruta dos setores). Os dois números são do mesmo INE, só que em estágios diferentes do mesmo censo 2009 — não são fontes conflitantes. Adotado 387.909 (ajustado) como `population` principal em `district-level-map.csv` (unit_id `GW0800`), por ser a estimativa que o próprio INE considera corrigida, e para bater com o nível província. O valor bruto (365.097) foi preservado no campo `population_source`, não descartado. Atenção: a quebra rural/urbano (0% rural) dessa linha foi calculada sobre a base bruta, não sobre o total ajustado — sinalizado no `notes`.
2. **Guiné-Bissau é o único país com rural/urbano neste nível** — achado via relatórios oficiais do censo 2009 (INE), que o agente usou porque não havia outra opção de população; os outros 21 países não têm essa quebra no nível distrito (mesmo gap do nível província).
3. **Djibouti**: zero população confiável nas 20 sub-prefeituras — a única fonte secundária encontrada (citypopulation.de) tinha uma estrutura cidade-sede vs. zona periférica que não reconciliava sem risco de dupla contagem; o agente preferiu deixar em branco a estimar errado.
4. **Lesoto e Gâmbia**: fronteira oficial 100%, mas população parcial — reformas administrativas recentes (Lesoto 2017, redesenho de councils) sem censo subsequente que cubra as unidades novas.
5. **Zâmbia**: fronteiras oficiais (115 distritos) mais novas que o arquivo de população do HDX (74 distritos pré-2018) — agente trocou para citypopulation.de (censo 2022) pra cobrir todos; descobriu também que o agrupamento por província de alguma fontes não bate com o `parent_pcode` oficial (mantido o oficial).
6. **Kiribati**: Betio (ilha populosa, ~17k hab. por fontes externas) aparece com população 0 na fonte oficial — provavelmente contabilizada dentro de South Tarawa no censo; mantido 0, não corrigido (fonte oficial, ainda que contra-intuitivo).

## Próximo nível (ward/ADM3) — ainda não iniciado em escala
Confirmado neste lote: nenhum país tinha arquivo de população ADM3 em bulk no HDX (mesma limitação já documentada pra Tanzânia). Ward-level só é viável unidade-a-unidade (como fizemos com Arri/Dabil/Ayalagaya) — não em lote para os 22 países. Decisão de escopo pendente: esperar até que distritos específicos sejam priorizados, ou já tentar uma amostra piloto em 1-2 países antes de decidir o método em escala.

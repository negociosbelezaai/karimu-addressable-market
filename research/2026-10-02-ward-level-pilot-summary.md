# Piloto de nível Ward (ADM3) — Tanzânia (Babati) + Timor-Leste (Baguia)

Data: 2026-10-02
Entregável: `deliverables/ward-level-pilot.csv` (35 linhas: 25 wards de Babati/Tanzânia + 10 sucos de Baguia/Timor-Leste)
Notas: `research/2026-10-02-ward-level-pilot-tls-notes.md` (Timor-Leste). Tanzânia feita diretamente nesta sessão, sem agente separado.

## Objetivo do piloto
Testar se o nível ward (ADM3 / suco / unidade-alvo) é viável em escala para os 22 países do shortlist, antes de disparar para todos. Resultado: **sim, mas o gargalo mudou de lugar** — ver conclusão.

## Tanzânia — Babati (distrito completo, 25 wards)
- 21 wards com P-code oficial (gazetteer HDX 2018) + **4 com ID provisório**: Ayalagaya (`TZ2101123-PROV1`, já conhecida), e **3 wards novas descobertas neste piloto** — Kisangaji (`TZ2101-PROV1`), Qameyu (`TZ2101-PROV2`), Secheda (`TZ2101-PROV3`). Nenhuma das 3 teve ward-mãe específica identificável nesta pesquisa — usado o distrito (`TZ2101`) como ancestral mais próximo com P-code oficial.
- **Achado importante**: o padrão "ward nova, sem P-code oficial" não é uma exceção isolada (só Ayalagaya) — é recorrente. Babati cresceu de 21 para 25 wards reais entre 2018 e 2022 (+19%), confirmado por 3 fontes independentes por ward nova (citypopulation.de censo 2022, cadastro postal da Tanzânia, artigo acadêmico). Isso tem implicação direta pra escala: espere uma taxa de ~15-20% de IDs provisórios ao fazer isso pros outros países, não um caso raro.
- Uma entrada da fonte ("Tarangire National Park") foi excluída por não ser ward — é parque nacional sem população residente listado na mesma tabela administrativa.
- **Divergência não resolvida**: soma dos 25 wards (375.200, censo 2022) é ~14% menor que o total do distrito já registrado em `district-level-map.csv` (435.066, projeção 2020 do HDX COD-PS). Anos e metodologias diferentes (projeção vs. censo real) — não reconciliado, documentado como gap.

## Timor-Leste — Baguia (posto administrativo completo, 10 sucos)
- Posto escolhido: **Baguia** (`TL0304`, município de Baucau) — rural, fora de Dili.
- **10/10 sucos com P-code oficial** (gazetteer HDX `cod-ab-tls`) — nenhum provisório necessário neste posto (diferente do padrão visto na Tanzânia/Camboja).
- Fonte de população teve que mudar: o nível distrito usou o "Preliminary Results" do censo 2022 (só vai até posto administrativo); nível suco só existe no **Main Report** do censo 2022 (tabela 4.1).
- **Achado técnico importante**: essa tabela está **rasterizada como imagem** no PDF, não é texto selecionável — extração exigiu renderizar a página em PNG e ler visualmente (sem OCR disponível no ambiente do agente). Validação: soma dos 10 sucos (11.718) bate quase exatamente com o total do posto já registrado (11.725, diferença de 7 hab. = duas publicações do mesmo censo, preliminar vs. final) — confirma que a leitura visual não teve erro de transcrição.

## Conclusão do piloto: viável, mas o gargalo mudou
Nos dois países, fronteira + P-code não foram o problema (HDX cobre ADM3 em ambos). **População por ward/suco é que não vem em dataset estruturado** (CSV/XLSX) como nos níveis país/província/distrito — é só isso:
- Tanzânia: só achamos via citypopulation.de, página por distrito (não tem "todos os wards do país" num arquivo só).
- Timor-Leste: só achamos num PDF de 9 páginas **rasterizado como imagem**, exigindo leitura visual página a página.

**Isso significa**: ir para os 22 países inteiros no nível ward não é "rodar o mesmo script 22 vezes" — é um projeto de extração de dados bem mais manual/caro que os níveis anteriores. Recomendação, se decidirem prosseguir:
1. **Não repita a leitura manual posto-por-posto** (não escala — Timor-Leste sozinho tem 67 postos administrativos / 452 sucos).
2. Para Timor-Leste especificamente: vale investir uma vez em extrair as 9 páginas inteiras do Main Report (OCR ou leitura de imagem em lote) — processa os 452 sucos do país de uma vez, não um posto por vez.
3. Para os outros 20 países: esperado o mesmo padrão (fonte de população mais granular que distrito tende a existir só em formato não-estruturado — PDF de censo, página web por localidade). Melhor abordagem provável: priorizar por 1-2 distritos por país (os de maior % rural ou maior população, usando os dados que já temos), não tentar ward-level nacional completo.

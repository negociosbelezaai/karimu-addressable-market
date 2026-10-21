# Levantamento completo da unidade-alvo — passagem rápida (método misto)

Data: 2026-10-03
Entregável: `deliverables/target-unit-map.csv` (1.781 linhas, 22 países)

## Mudança de método (pedido explícito do Eduardo em 2026-10-02: "ir mais rápido, mesmo com imperfeições")
Até aqui, "unidade-alvo" vinha sendo tratada como sinônimo de "ward real, enumerado e com censo próprio" — o piloto (Tanzânia/Babati + Timor-Leste/Baguia) provou que isso não escala: população por ward só existe em fonte não-estruturada (PDF rasterizado, página web por distrito), exigindo pesquisa manual unidade a unidade.

Mudança: voltar ao que o conceito original já previa (`2026-10-01-target-unit-concept.md`) — unidade-alvo é definida por **faixa populacional (~5k-30k, banda de tolerância até 40k)**, não por um nível administrativo fixo. Aplicado **linha a linha** (não por país) sobre os 1.773 distritos que já tínhamos + as 9 ilhas de Tuvalu (único país sem ADM2):

- **População ≤ 40k**: o próprio distrito (ou ilha, no caso de Tuvalu) já é a unidade-alvo. Usado diretamente, sem pesquisa nova.
- **População > 40k**: grande demais para ser uma unidade-alvo direta. **Modelado, não enumerado**: população ÷ 15.000 (tamanho médio real de ward, calibrado em Babati/Tanzânia — 375.200 hab. / 25 wards = 15.008) = número estimado de unidades e seu tamanho médio. Isso é uma estimativa aritmética sobre dado que já tínhamos — não uma lista de wards reais com nome e fronteira.
- **População indisponível**: marcado `unresolved`, herdando os gaps já conhecidos (Djibouti inteiro, Lesoto pós-reforma, parte da Gâmbia).

Por que aplicar por LINHA e não por PAÍS: o piloto já mostrou que mesmo países "pequenos" têm distritos urbanos grandes (Dom Aleixo/Dili em Timor-Leste = 165.522 hab.; South Tarawa em Kiribati = 63.439 hab.) que precisariam de modelagem mesmo que o resto do país já esteja na faixa. Uma regra por país teria errado esses casos.

## Resultado

| Método | Linhas | O que significa |
|---|---|---|
| `direct` | 524 | Unidade real (distrito ou ilha), já no tamanho certo, usada como está |
| `modeled_split` | 1.180 | Distrito real grande demais — número de unidades-alvo é **estimado**, não enumerado |
| `unresolved` | 77 | Sem dado de população (gap pré-existente) |

**Total estimado de unidades-alvo no shortlist inteiro: ~20.141** (524 reais + soma das estimativas dos 1.180 distritos modelados). População total coberta pelas unidades-fonte com dado: ~303,8 milhões de habitantes.

## Por país (unidades-fonte, método)
Ver `deliverables/target-unit-map.csv` para o detalhe linha a linha. Resumo: Tanzânia, Guiné, Serra Leoa e Madagascar são 100% (ou quase) `modeled_split` — distritos grandes demais em todo o país. Kiribati, Ilhas Salomão, Timor-Leste, Libéria, Gâmbia e Guiné-Bissau são majoritariamente `direct` — distrito já é unidade-alvo na maior parte do país, com só a(s) área(s) urbana(s) precisando de modelagem.

## Limitações explícitas (aceitas de propósito, por pedido do Eduardo)
1. **`modeled_split` não tem nomes nem fronteiras reais** — é só "quantas unidades deste tamanho provavelmente existem", calculado por aritmética. Não serve pra apontar um ward específico no mapa; serve pra dimensionar o mercado endereçável (TAM) e comparar países/distritos por potencial.
2. **Calibração única (15.000) vem de 1 só país (Tanzânia)** — não validamos se o tamanho médio real de ward é parecido em Angola, Zâmbia, Madagascar etc. É um pressuposto de trabalho, não um fato verificado. Risco: se o tamanho real de ward variar muito por país (como já vimos entre Tanzânia ~15k e os sucos de Timor-Leste ~1,2k antes de reclassificá-los como `direct`), o número estimado de unidades pode estar sistematicamente errado pra cima ou pra baixo em países não-calibrados.
3. **77 linhas sem dado de população não entram na estimativa** — ver gaps já documentados (Djibouti, Lesoto pós-2017, parte da Gâmbia).
4. **Enumeração real (nomes, P-codes, censo próprio) continua reservada para quando Karimu escolher um distrito candidato específico** — já provamos que é viável (Babati, Baguia), só não escala pra todos de uma vez.

## Próximo passo sugerido
Esta tabela já é suficiente para comparar e ranquear os 22 países/distritos por tamanho de mercado endereçável (nº estimado de unidades-alvo × faixa de pobreza já conhecida por país). Quando Karimu apontar candidatos específicos, aplicar o método exaustivo (Babati/Baguia) só ali.

# Enumeração de wards — Tanzânia, Grupo 2 (Kigoma, Tabora, Singida, Geita, Mjini Magharibi)

Data: 2026-10-03
Entregável: `deliverables/ward-enum-tza-group2.csv` (688 wards)
Método: `research/2026-10-01-target-unit-concept.md` + `research/2026-10-02-ward-level-pilot-summary.md` (mesmo usado no piloto de Babati).
Fonte de wards/população: citypopulation.de, censo 2022-08-23, página "district - with wards" de cada distrito.
Fonte de P-code oficial: gazetteer HDX COD-AB `tza_admgz.xlsx`, aba `tza_admbnda_adm3_20181019` (2018).

## Totais do grupo
- **688 wards** no total: **557 oficiais** (P-code HDX 2018) + **131 provisórias** (`-PROV<n>`, ~19% do total — consistente com a taxa de 15-20% já observada no piloto de Babati).
- Nenhum distrito falhou completamente — todos os 20 distritos do grupo (Kigoma 8, Tabora 7, Singida 6, Geita 5) + as 2 unidades de Mjini Magharibi (Magharibi, Mjini) tiveram dados de wards extraídos com sucesso.
- Duas entradas excluídas da contagem por não serem wards (parque/reserva sem população, mesmo padrão de "Tarangire National Park" em Babati): **Moyawosi Game Reserve** (Kibondo) e **Kigosi National Park** (Bukombe).

## Por distrito

| Distrito | P-code | Wards | Oficiais | Provisórias | Soma wards | Pop. já registrada | Diferença |
|---|---|---|---|---|---|---|---|
| Kibondo | TZ1601 | 19 | 13 | 6 | 362.922 | 323.805 | +12,1% |
| Kasulu | TZ1602 | 21 | 19 | 2 | 537.767 | 391.170 | +37,5% |
| Kigoma | TZ1603 | 16 | 11 | 5 | 222.792 | 228.803 | -2,6% |
| Kigoma Ujiji Municipal | TZ1604 | 19 | 19 | 0 | 232.388 | 306.793 | -24,3% |
| Uvinza | TZ1605 | 16 | 13 | 3 | 458.353 | 509.126 | -10,0% |
| Buhigwe | TZ1606 | 20 | 15 | 5 | 240.005 | 337.504 | -28,9% |
| Kakonko | TZ1607 | 13 | 11 | 2 | 178.419 | 149.909 | +19,0% |
| Kasulu Town | TZ1608 | 15 | 8 | 7 | 238.321 | 230.686 | +3,3% |
| Nzega | TZ1401 | 36 | 31 | 5 | 574.498 | 605.795 | -5,2% |
| Igunga | TZ1402 | 35 | 26 | 9 | 546.204 | 491.597 | +11,1% |
| Uyui | TZ1403 | 30 | 24 | 6 | 562.588 | 548.431 | +2,6% |
| Urambo | TZ1404 | 18 | 16 | 2 | 260.322 | 263.616 | -1,2% |
| Sikonge | TZ1405 | 20 | 17 | 3 | 335.686 | 236.907 | +41,7% |
| Tabora Municipal | TZ1406 | 29 | 25 | 4 | 308.741 | 259.818 | +18,8% |
| Kaliua | TZ1407 | 28 | 21 | 7 | 678.447 | 623.691 | +8,8% |
| Iramba | TZ1301 | 20 | 17 | 3 | 328.912 | 433.723 | -24,2% |
| Singida | TZ1302 | 21 | 21 | 0 | 284.895 | 270.128 | +5,5% |
| Manyoni | TZ1303 | 19 | 19 | 0 | 279.069 | 414.903 | -32,7% |
| Singida Municipal | TZ1304 | 18 | 16 | 2 | 232.459 | 185.563 | +25,3% |
| Ikungi | TZ1305 | 28 | 26 | 2 | 411.262 | 351.799 | +16,9% |
| Mkalama | TZ1306 | 17 | 14 | 3 | 255.514 | 156.340 | +63,4% |
| Geita | TZ2501 | 37 | 28 | 9 | 1.035.214 | 1.069.531 | -3,2% |
| Nyang'hwale | TZ2502 | 15 | 12 | 3 | 225.803 | 189.354 | +19,2% |
| Mbogwe | TZ2503 | 17 | 16 | 1 | 362.855 | 215.125 | +68,7% |
| Bukombe | TZ2504 | 17 | 13 | 4 | 407.102 | 241.937 | +68,3% |
| Chato | TZ2505 | 23 | 22 | 1 | 584.963 | 512.566 | +14,1% |
| Magharibi | TZ5301 | 65 | 39 | 26 | 674.162 | 676.452 | -0,3% |
| Mjini | TZ5302 | 56 | 45 | 11 | 219.007 | 248.175 | -11,8% |

Nota sobre a diferença: como já documentado no piloto de Babati, a "população já registrada" em `district-level-map.csv` vem de projeção HDX COD-PS 2020, enquanto a soma dos wards vem do censo real 2022-08-23 (citypopulation.de) — são fonte e ano diferentes, a divergência (positiva ou negativa) é esperada e não foi reconciliada.

## Casos especiais / achados importantes

### Manyoni (TZ1303) — distrito-mãe perdeu wards para um novo distrito (Itigi)
A gazetteer oficial HDX 2018 lista 30 wards para Manyoni, mas o censo 2022 (citypopulation.de) só mostra 19 — todos batendo exatamente com um subconjunto da gazetteer (nenhuma ward nova, soma = população da fonte exatamente). As 11 wards remanescentes da gazetteer que não aparecem mais em Manyoni (`Idodyandole, Rungwa, Mgandu, Itigi Mjini, Ipande, Sanjaranda, Aghondi, Mwamagembe, Mitundu, Kitaraka, Itigi Majengo`) foram identificadas como tendo migrado para um **novo distrito "Itigi" (código 1307)**, criado depois de 2018 e confirmado na própria página-índice da região Singida (população 2022: 215.947) — **fora do escopo deste grupo** (não estava na lista de distritos atribuída). Não é erro de matching, é desmembramento administrativo real, documentado e não investigado further pois Itigi não pertence a este grupo.

### Mjini Magharibi (TZ5301 "Magharibi") — distrito oficial dividido em duas municipalidades no censo 2022
A gazetteer HDX 2018 lista só 2 distritos em Mjini Magharibi: `Magharibi` (TZ5301, 38 wards) e `Mjini` (TZ5302, 44 wards). No citypopulation.de (censo 2022), porém, "Magharibi" já aparece dividido em **duas municipalidades**: "Magharibi A Municipal" (329.645 hab., sem P-code oficial próprio neste levantamento) e "Magharibi B Municipal" (344.517 hab., manteve o código informal 5301). A soma das duas (674.162) bate quase exatamente com a população do distrito TZ5301 já registrada (676.452, diff -0,3%) — confirma que A+B juntas é o mesmo distrito "Magharibi" pré-divisão, não dois distritos novos.
**Tratamento adotado**: as wards de Magharibi A e Magharibi B foram casadas, juntas, contra a MESMA lista de 38 wards oficiais do gazetteer HDX para TZ5301 (pré-divisão), já que não existe pcode oficial publicado para a subdivisão A/B. Todas as 38 wards oficiais da gazetteer foram localizadas nessa fusão (0 remanescentes) — ou seja, a divisão A/B parece ter sido feita rearranjando as mesmas wards antigas entre as duas novas municipalidades, sem perda. Além disso, **26 wards novas** apareceram nessa área (15 do lado B, 11 do lado A) — a região urbana de Zanzibar cresceu bastante desde 2018, com subdivisão de wards antigas em várias novas (ex. os vários "Fuoni X", "Mtoni X"). Todas as 26 novas recebem ID provisório com base no distrito-pai oficial `TZ5301` (não foi possível identificar ward-mãe específica para cada uma dentro do escopo desta pesquisa).

### Kibondo (TZ1601) — outlier de população
A ward "Murungu" aparece com 84.449 habitantes no censo 2022, muito acima das demais wards do distrito (a maioria entre 7k-35k). Não foi possível confirmar/desconfirmar isso dentro do escopo desta tarefa (não há fonte alternativa consultada) — mantido como está na fonte primária (não se deve inventar número), mas sinalizado aqui como outlier a revisitar se o distrito virar alvo de interesse.

### Wards oficiais da gazetteer não encontradas no censo 2022 (além do caso Manyoni/Itigi)
Além das 11 wards de Manyoni (ver acima), ficaram sem contrapartida no censo 2022 (não foi encontrado nome igual nem fuzzy-match com confiança >=0,72):
- **Uvinza (TZ1605)**: `Simbo` (gazetteer) — não aparece na lista atual; 3 wards novas sem nome parecido apareceram no lugar (Basanza, Herembe, Mwakizega). Pode ser renomeação/fusão não confirmada.
- **Kasulu Town (TZ1608)**: `Kasulu Mjini` (gazetteer) — não aparece; 7 wards novas (centro urbano bastante subdividido: Heru Juu, Kimobwa, Kumnyika, Kumsenga, Murubona, Murusi, Mwilamvya) — plausivelmente Kasulu Mjini foi fatiada nessas 7, mas sem confirmação individual.
- **Nzega (TZ1401)**: 6 wards da gazetteer sem par no censo 2022 (`Nzega Mjini, Mbogwe, Miguwa, Itilo, Ijanija, Nzegandogo`) — e 5 wards novas sem fuzzy-match com confiança suficiente (Mbagwa, Mbutu, Mwantundu, Mwasala, Ugembe). Testado fuzzy a 0,6+ sem sucesso — tratadas como provisórias independentes, sem associação às antigas.
- **Geita (TZ2501)**: 7 wards da gazetteer sem par (`Kasamwa, Bung'wangoko, Bulela, Ihanamilo, Nyanguku, Mtakuja, Kalangalala`) — e 9 wards novas (Butundwe, Izumacheli, Ludete, Magenge, Nyalwanzaja, Nyamboge, Nyamwilolelwa, Nyaruyeye, Nyawilimilwa), sem fuzzy-match confiável entre os dois grupos.

Esses casos foram tratados de forma conservadora: nenhuma correspondência forçada abaixo do limiar de confiança (razão de similaridade >= 0,72 após normalização ortográfica); wards antigas sem par ficam apenas documentadas aqui (não entram no CSV, pois não têm população do censo atual); wards novas sem ward-mãe identificável recebem `<pcode do distrito>-PROV<n>`.

### Falhas de fonte
Nenhuma falha completa de distrito. Duas falhas pontuais de URL, resolvidas:
- O link "district" do índice regional (`/en/tanzania/admin/<regiao>/...`) não contém a tabela de wards — foi preciso seguir o link "... district - with wards" (ex. `/en/tanzania/lake/admin/1601__kibondo/`), que usa um prefixo de "zona" diferente por região (`lake` para Kigoma/Geita, `central` para Tabora/Singida, `zanzibar` para Mjini Magharibi).
- A entrada oficial `Nzega Town` (TZ1408) e `Itigi` (TZ1307) apareceram nos índices regionais mas não fazem parte da lista de distritos deste grupo — ignoradas corretamente.

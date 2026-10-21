# Disparidade real de pobreza rural vs. urbana — todos os 21 países com dado de pobreza

Data: 2026-10-03
Estende `2026-10-03-rural-poverty-disparity-tza-moz-mdg.md` (os 3 primeiros) para os outros 18 países do shortlist.

## Método (igual ao already feito para Tanzânia/Moçambique/Madagascar)
Para cada país, busquei a taxa de pobreza **rural** e **urbana** pela linha de pobreza **nacional** (pesquisa domiciliar oficial — HBS/IOF/EHCVM/IHS/LCMS, conforme o país), e usei a *razão* dessa disparidade para redistribuir o total de pobres já calculado pela linha **internacional** (US$3,00/dia, PPP 2021):

```
share_rural_ajustado = (%pop_rural × taxa_pobreza_rural) / (%pop_rural × taxa_pobreza_rural + %pop_urbana × taxa_pobreza_urbana)
```

## Fontes por país (R=rural, U=urbano, linha nacional, confiança)

| País | R | U | Fonte | Confiança |
|---|---|---|---|---|
| Zâmbia | 78,8% | 31,9% | LCMS 2022, Zambia Statistics Agency | alta (oficial, lido direto) |
| Madagascar | 79,9% | 55,5% | EPM 2022, INSTAT | alta |
| Moçambique | 70,9% | 47,6% | IOF 2019/20, INE | alta |
| Gâmbia | 76,7% | 34,4% | IHS 2020, GBoS (tabela 18) | alta (oficial, lido direto) |
| Serra Leoa | 73,9% | 34,8% | SLIHS 2018, Statistics Sierra Leone | alta (oficial, lido direto) |
| Libéria | 71,6% | 31,5% | HIES 2016/17, LISGIS | alta |
| Lesoto | 60,7% | 28,5% | HBS 2017 / WB Poverty Assessment 2019 | alta |
| Guiné-Bissau | 60,4% | 12,2% | EHCVM 2021 (via brief do WB) | **baixa — o próprio brief tem número inconsistente (21%/42% por sub-área urbana); não verificado no documento original** |
| Malawi | 56,6% | 19,2% | IHS5 2019/20, NSO Malawi | alta |
| Angola | 57,0% | 30,0% | IDREA 2018/19, INE (via imprensa) | média — PDF oficial não abriu, confirmado por fonte secundária |
| Guiné | 55,4% | 22,4% | EHCVM 2018/19, INS Guinée | alta (oficial, lido direto, pág. 32) |
| Senegal | 53,3% | 20,0% | EHCVM II 2021-22, ANSD | alta |
| Comores | 50,3% | 32,8% | EHCVM 2020 | alta |
| Timor-Leste | 45,5% | 18,4% | TLSLS 2024 (via imprensa) | média — PDF oficial não abriu |
| Djibouti | 78,4% | 28,2% | EDAM-IS 2017, linha moderada/global; "urbano" = só Djibouti-ville | média — PDF escaneado, urbano não cobre todas as cidades |
| Tanzânia | 31,3% | 15,8% | HBS 2017/18, NBS | alta |
| Laos | 23,8% | 7,0% | LECS 6 2018/19 (via convergência de buscas) | média — sem tabela-fonte confirmada |
| Nepal | 24,7% | 18,3% | NLSS IV 2022/23 | alta |
| Kiribati | 24,7%* | 19,5%* | HIES 2019/20 (KINSO/SPC) | **aproximado** — *"rural"=outer islands, "urbano"=South Tarawa, não divisão clássica |
| Tuvalu | 24,8%* | 27,5%* | HIES 2010 (via brief WB 2024) | **aproximado + dado de 2010** — *"rural"=outer islands, "urbano"=Funafuti; único país onde pobreza urbana > rural |
| Ilhas Salomão | — | — | não encontrado (número único achado era inconsistente, descartado) | **sem dado — manteve estimativa ingênua** |

## Resultado consolidado (21 países com dado de pobreza, 20 com ajuste + 1 naive)

| | Total | % do total de pobres |
|---|---|---|
| Pobres estimados (linha US$3/dia) | 151.486.526 | 100% |
| Rural — estimativa ingênua (uniforme) | 90.938.653 | 60,0% |
| **Rural — ajustada pela disparidade real** | **110.602.135** | **73,0%** |
| Diferença | +19.663.483 | +13 p.p. |

A correção aumenta a estimativa de pobres rurais em quase **19,7 milhões de pessoas** frente à ingênua — a maior parte concentrada em Tanzânia (+5,1M), Zâmbia (+3,2M), Moçambique (+2,5M), Angola (+2,2M) e Madagascar (+1,7M).

**Achado curioso**: Tuvalu é o único país onde a correção vai na direção oposta (-20, irrisório em termos absolutos) — a pobreza na capital (Funafuti) é ligeiramente maior que nas ilhas periféricas, invertendo o padrão visto em todos os outros 20 países.

## Limitações explícitas
1. **Duas métricas de pobreza diferentes** (nacional vs. US$3/dia internacional) combinadas via razão, não valor direto — mesma ressalva do arquivo anterior, vale para todos os 21.
2. **5 países com confiança reduzida**: Guiné-Bissau (inconsistência interna, não verificada no original), Timor-Leste/Laos/Angola/Djibouti (fonte secundária ou PDF não-extraível, não a tabela primária).
3. **Kiribati e Tuvalu**: "rural/urbano" aproximado por "ilhas periféricas vs. capital" — conceitualmente razoável pra essas nações insulares pequenas, mas não é a mesma categoria clássica usada nos outros países.
4. **Ilhas Salomão**: sem dado confiável encontrado — mantido na estimativa ingênua (provavelmente subestima o rural, como nos demais antes do ajuste).
5. Nenhum destes 21 números foi cruzado com uma fonte de disparidade medida *diretamente* na linha internacional de US$3/dia (não achamos essa quebra específica publicada) — a transferência de razão entre linhas de pobreza continua sendo a maior fonte de incerteza do método.

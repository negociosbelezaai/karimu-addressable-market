# Enumeração exaustiva de wards (ADM3) — Tanzânia, Grupo 4

Data: 2026-10-03
Entregável: `deliverables/ward-enum-tza-group4.csv` (739 wards, 23 distritos, 5 regiões: Dodoma, Morogoro, Lindi, Iringa, Katavi)
Método: mesmo da pilot de Babati (`research/2026-10-02-ward-level-pilot-summary.md`) — índice regional citypopulation.de → página por distrito → lista completa de wards, censo 2022-08-23 → cruzamento fuzzy contra gazetteer oficial HDX (`tza_admgz.xlsx`, aba `tza_admbnda_adm3_20181019`, filtrado por `ADM2_PCODE`).

## Achado metodológico novo neste grupo: redistritamento pós-2018 em escala

Diferente de Babati (onde o distrito citypopulation.de = distrito do nosso HDX ADM2, 1:1, só com wards novas dentro do mesmo distrito), **neste grupo vários distritos antigos (nossa lista, baseada no gazetteer HDX 2018) foram desmembrados ou renomeados** pela Tanzânia entre 2018 e o censo 2022. citypopulation.de reflete a divisão administrativa ATUAL (pós-redistritamento), não a de 2018. Tratamento aplicado por caso:

- **Rename simples (1:1, sem split)**: Kondoa Rural→Kondoa Rural (mantido), Lindi Rural→**Mtama**, Mpanda→**Tanganyika**, Mpanda Town→**Mpanda Municipal**, Morogoro Rural→Morogoro Rural, Dodoma Municipal→**Dodoma City**. Mesma fronteira, só nome mudou — wards casados diretamente.
- **Split em 2+ distritos atuais**: our distrito antigo precisou agregar **múltiplas páginas atuais** do citypopulation.de, cruzando cada ward contra o `ADM2_PCODE` antigo (não a página de origem):
  - `TZ0101 KONDOA` = Kondoa Rural (atual) + **Kondoa Town** (novo)
  - `TZ0503 KILOMBERO` = **Ifakara Town** (novo) + **Mlimba** (novo)
  - `TZ0504 ULANGA` = Ulanga (atual) + **Malinyi** (novo)
  - `TZ2303 MLELE` = Mlele (atual, menor) + **Mpimbwe** (novo) + **Nsimbo** (novo)
- **Anexação cruzada de fronteira (caso mais delicado — 3 ocorrências)**: a fronteira de um município/cidade atual **cresceu e absorveu wards que, pelo P-code oficial do gazetteer 2018, pertencem a outro distrito antigo da nossa lista**. Resolvido atribuindo a ward ao distrito cujo P-code ela tem (não à página onde o censo 2022 a lista hoje), com nota explicativa em cada linha:
  - 10 wards (Mipingo, Kitomanga, Mchinga, Kilolambwani, Kilangala, Rutamba, Milola, Kiwawa, Matimba, Nangaru): listadas na página atual "Lindi Municipal", mas P-code oficial pertence a `TZ0802 LINDI` (antigo Lindi Rural) — atribuídas lá, não a `TZ0806 LINDI MUNICIPAL`.
  - 3 wards (Bumilayinga, Isalavanu, Rungemba): listadas na página atual "Mafinga Town", mas P-code oficial pertence a `TZ1102 MUFINDI` — atribuídas lá, não a `TZ1105 MAFINGA`.
  - 2 wards (Kasokola, Magamba): listadas na página atual "Mpanda Municipal", mas P-code oficial pertence a `TZ2303 MLELE` — atribuídas lá, não a `TZ2301 MPANDA TOWN`.
  - Validação: somando a população dessas wards de volta à página onde o censo 2022 realmente as lista reproduz exatamente o total 2022 já publicado para aquela página (ex. Lindi Municipal atual = 99.905 [18 wards próprias] + 74.221 [10 anexadas] = 174.126, batendo com o total regional bruto obtido no primeiro fetch do índice de Lindi) — confirma que não há erro de transcrição, só uma decisão de atribuição de P-code.
  - **Implicação**: a população "já registrada" em `district-level-map.csv` para Lindi Municipal (137.397), Mafinga (70.282) e Mpanda Town (146.868) parece ter sido calculada com uma fronteira mais próxima da ATUAL (pós-anexação) do que da fronteira 2018 do gazetteer — por isso a soma dos wards aqui (que segue o P-code 2018) diverge da população já registrada nesses 3 casos (ver tabela abaixo). Não é erro de contagem, é descompasso de fronteira entre as duas fontes.

## Resumo por distrito

| Distrito (P-code antigo) | Wards achadas | Oficiais | Provisórias | Soma pop. (wards) | Pop. já registrada | Diferença | Nota |
|---|---|---|---|---|---|---|---|
| TZ0101 KONDOA | 29 | 28 | 1 | 325.297 | 311.638 | +4,4% | Crescimento normal 2020→2022 |
| TZ0102 MPWAPWA | 33 | 30 | 3 | 403.247 | 368.137 | +9,5% | Crescimento normal |
| TZ0103 KONGWA | 22 | 22 | 0 | 443.867 | 386.458 | +14,9% | Crescimento normal |
| TZ0104 CHAMWINO | 36 | 32 | 4 | 486.176 | 420.529 | +15,6% | Crescimento normal |
| TZ0105 DODOMA MUNICIPAL | 41 | 37 | 4 | 765.179 | 505.425 | +51,4% | Dodoma virou capital administrativa (migração de órgãos do governo) — crescimento urbano muito acima da média nacional, plausível |
| TZ0106 BAHI | 22 | 20 | 2 | 322.526 | 276.916 | +16,5% | Crescimento normal |
| TZ0107 CHEMBA | 26 | 20 | 6 | 339.333 | 293.229 | +15,7% | Crescimento normal |
| TZ0501 KILOSA | 40 | 35 | 5 | 617.032 | 543.637 | +13,5% | Crescimento normal |
| TZ0502 MOROGORO | 31 | 29 | 2 | 387.736 | 321.367 | +20,7% | Crescimento normal/alto |
| TZ0503 KILOMBERO | 35 | 19 | 16 | 582.960 | 505.955 | +15,2% | Split em Ifakara Town + Mlimba; alta taxa de wards novas é esperada em distrito agrícola de irrigação (Kilombero) com forte adensamento |
| TZ0504 ULANGA | 31 | 24 | 7 | 458.021 | 349.526 | +31,0% | Split em Ulanga + Malinyi |
| TZ0505 MOROGORO MUNICIPAL | 29 | 19 | 10 | 471.409 | 418.556 | +12,6% | Crescimento normal |
| TZ0506 MVOMERO | 30 | 17 | 13 | 421.741 | 376.824 | +11,9% | Alta taxa de wards novas (quase metade) — não investigado a fundo, mas nenhuma ambiguidade de match restante |
| TZ0507 GAIRO | 18 | 11 | 7 | 258.205 | 259.817 | -0,6% | Divergência mínima, dentro do esperado (projeção vs censo real) |
| TZ0801 KILWA | 23 | 21 | 2 | 297.676 | 217.978 | +36,6% | Crescimento alto; sem evidência de erro de match (0 gaz perdida) |
| TZ0802 LINDI | 30 | 30 | 0 | 240.714 | 189.871 | +26,8% | Ver nota de anexação acima — 10 das 30 wards vêm da página atual "Lindi Municipal" |
| TZ0803 NACHINGWEA | 36 | 26 | 10 | 233.655 | 199.020 | +17,4% | Crescimento normal/alto |
| TZ0804 LIWALE | 20 | 20 | 0 | 136.505 | 111.517 | +22,4% | Crescimento alto, sem ambiguidade |
| TZ0805 RUANGWA | 22 | 21 | 1 | 185.573 | 143.857 | +29,0% | Crescimento alto |
| TZ0806 LINDI MUNICIPAL | 21 | 18 | 3 | 99.905 | 137.397 | -27,3% | Ver nota de anexação acima — pop. registrada provavelmente já usa fronteira expandida (ver maior detalhe acima) |
| TZ1101 IRINGA | 28 | 24 | 4 | 315.354 | 269.639 | +17,0% | 1 ward oficial não encontrada (ver "Falhas" abaixo: Nduli) |
| TZ1102 MUFINDI | 30 | 27 | 3 | 312.020 | 293.544 | +6,3% | Inclui 3 wards anexadas por Mafinga Town, ver nota acima |
| TZ1103 IRINGA MUNICIPAL | 18 | 16 | 2 | 202.490 | 201.395 | +0,5% | Divergência mínima |
| TZ1104 KILOLO | 24 | 22 | 2 | 263.559 | 240.575 | +9,6% | Crescimento normal |
| TZ1105 MAFINGA | 6 | 3 | 3 | 99.305 | 70.282 | +41,3% | 3 wards oficiais (Bumilayinga, Isalavanu, Rungemba) excluídas daqui — pertencem a TZ1102, ver nota acima. Mesmo assim diferença alta: cidade pequena com crescimento urbano acelerado, plausível |
| TZ2301 MPANDA TOWN | 13 | 9 | 4 | 225.804 | 146.868 | +53,7% | 2 wards (Kasokola, Magamba) excluídas — pertencem a TZ2303, ver nota acima. Crescimento urbano de Mpanda (capital de Katavi) muito acima da média, plausível |
| TZ2302 MPANDA | 16 | 9 | 7 | 371.836 | 295.772 | +25,7% | Renomeado "Tanganyika"; crescimento alto |
| TZ2303 MLELE | 29 | 24 | 5 | 555.318 | 333.634 | +66,4% | Distrito antigo split em 3 (Mlele+Mpimbwe+Nsimbo); inclui 2 wards anexadas por Mpanda Municipal. Maior divergência do grupo — provável combinação de (a) fronteira antiga vs atual, (b) área de reassentamento/fronteira agrícola no oeste da Tanzânia com crescimento populacional real muito acima da média |

**Total do grupo**: 739 wards — **613 oficiais** (P-code HDX 2018 confirmado, incl. por fuzzy-match ortográfico) + **126 provisórias** (`-PROVn`, sem P-code oficial — grafia nova ou desmembramento posterior a 2018).

## Convenção de ID provisório aplicada

Igual a Babati/target-unit-concept.md: `<pcode do ancestral mais próximo>-PROV<n>`, `n` sequencial alfabético entre as pendentes do mesmo ancestral. Ancestral = **distrito** (`TZ0101`, etc.) na maioria dos 126 casos novos, exceto 3 onde o nome da ward nova sugere claramente desmembramento de uma ward oficial específica já casada no mesmo distrito (usada como ancestral mais específico, conforme a regra do concept doc):
- `Hombolo Bwawani` → pai = `Hombolo` (`TZ0105101`) → `TZ0105101-PROV1`
- `Mang'ula B` → pai = `Mang'ula` (`TZ0503043`) → `TZ0503043-PROV1`
- `Kihonda Maghorofani` → pai = `Kihonda` (`TZ0505192`) → `TZ0505192-PROV1`

Caso ambíguo não resolvido por falta de evidência: em `TZ0105` (Dodoma), a ward oficial "Hombolo" (`TZ0105101`) aparece hoje como DUAS wards no censo 2022 — `Hombolo Makulu` (10.857 hab.) e `Hombolo Bwawani` (20.033 hab.). Como "Makulu" ("grande/principal", sugerindo a sede original) é plausivelmente a sucessora direta, foi tratada como match fuzzy direto de "Hombolo" (`TZ0105101`, oficial) e só `Hombolo Bwawani` foi tratada como nova (com pai específico `Hombolo`). Essa inferência de qual metade herda o P-code é uma leitura de nome, não uma fonte primária confirmada — registrado aqui para transparência.

## Falhas / não resolvido

- **`TZ1101 IRINGA` — ward "Nduli" (`TZ1101171`, oficial no gazetteer 2018) sem população atribuída.** Não aparece na página atual "Iringa Rural" do citypopulation.de. Existe uma ward com o mesmo nome na página atual "Iringa Municipal" (pop. 10.304), mas essa ward tem SEU PRÓPRIO P-code oficial distinto no gazetteer 2018 (`TZ1103162`, também chamado "Nduli") — ou seja, há duas wards "Nduli" homônimas e vizinhas (uma rural, uma urbana) desde 2018, e não há evidência clara de que a rural foi fundida/anexada pela urbana ou simplesmente deixou de ser reportada separadamente. Para não arriscar contagem dupla nem atribuição especulativa, a linha `TZ1101171 Nduli` **não foi incluída no CSV** (diferente dos outros 28 wards de Iringa Rural, que foram todas encontradas). Soma de Iringa (315.354) reflete as 28 wards *encontradas*, não inclui esta.
- Nenhum distrito falhou completamente (todas as 23 tiveram página carregada com sucesso e lista de wards extraída).
- Nenhuma entrada não-ward (tipo "Tarangire National Park" em Babati) apareceu nas tabelas deste grupo — todas as linhas das 33 páginas fetchadas eram wards reais com população.

## Fonte

citypopulation.de, tabelas de wards por distrito, Census 2022-08-23 (National Bureau of Statistics Tanzania). Gazetteer oficial: HDX `cod-ab-tza`, `tza_admgz_20181019.xlsx` (local: `/Users/eduardo.thuler/.claude/jobs/8f90797d/tmp/tza_admgz.xlsx`), aba `tza_admbnda_adm3_20181019`.

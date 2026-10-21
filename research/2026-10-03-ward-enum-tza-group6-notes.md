# Enumeracao de wards (ADM3) - Tanzania, Grupo 6

Data: 2026-10-03
Entregavel: `deliverables/ward-enum-tza-group6.csv`
Regioes: Kilimanjaro (TZ03), Mtwara (TZ09), Mbeya (TZ12), Simiyu (TZ24), Kusini Unguja (TZ52) - 27 distritos

## Metodo
- Paginas-indice de regiao (citypopulation.de) para achar o link real de cada distrito.
- **Achado de metodo importante**: a pagina de distrito 'normal' (`/en/tanzania/admin/<regiao>/<code>__<slug>/`) NAO tem a tabela de wards - ela so tem o link 'District - with wards' apontando para uma pagina em outra zona geografica (`/en/tanzania/<zona>/admin/<code>__<slug>/`, zona = northern/coastal/southernhighlands/lake/zanzibar conforme a regiao). Teve que seguir esse link em cada um dos 27 distritos para pegar a tabela real.
- Tabela de wards extraida via HTML estatico (tabela `id="tl"`), nao via sumarizacao de modelo - mais confiavel para 679 linhas. Coluna de populacao confirmada como `Census 2022-08-23` (mesmo padrao do piloto Babati).
- Cruzamento com gazetteer oficial HDX (`tza_admgz.xlsx`, aba `tza_admbnda_adm3_20181019`), filtrado por `ADM2_PCODE` (formato com prefixo `TZ`, ex. `TZ0301` para Rombo - confirmado na planilha, diferente do exemplo do brief que sugeria sem prefixo).
- Match exato (nome normalizado) primeiro; depois fuzzy match (SequenceMatcher, corte >=0.85, calibrado pelos exemplos do piloto Babati: 'Qash'/'Qashi'=0.89, 'Bashnet'/'Bashneti'=0.93) resolvendo por melhor par global (nao por ordem de iteracao - corrigido um bug inicial em que 'Keni Aleni' roubava o match de 'Keni Mengeni' por similaridade parcial de prefixo).
- Excluidas linhas sem populacao na tabela da fonte (parques nacionais, reservas de caca, area de pantano) - mesmo padrao do 'Tarangire National Park' em Babati. Nesta rodada: Mtwara Rural Swamp Area (TZ0901), Serengeti National Park/Maswa Game Reserve (TZ2401, TZ2402, TZ2403), Kijereshi Game Reserve/Serengeti NP (TZ2405).

## Por distrito

| Distrito (regiao) | Wards achadas | Oficiais | Provisorias | Soma pop. (wards) | Pop. ja registrada | Diferenca |
|---|---|---|---|---|---|---|
| TZ0301 ROMBO (Rombo) [Kilimanjaro] | 28 | 21 | 7 | 275,314 | 284,110 | -3.1% |
| TZ0302 MWANGA (Mwanga) [Kilimanjaro] | 20 | 20 | 0 | 148,763 | 152,977 | -2.8% |
| TZ0303 SAME (Same) [Kilimanjaro] | 34 | 31 | 3 | 300,303 | 336,637 | -10.8% |
| TZ0304 MOSHI (Moshi) [Kilimanjaro] | 32 | 31 | 1 | 535,803 | 538,028 | -0.4% |
| TZ0305 HAI (Hai) [Kilimanjaro] | 17 | 12 | 5 | 240,999 | 259,383 | -7.1% |
| TZ0306 MOSHI MUNICIPAL (Moshi Urban) [Kilimanjaro] | 21 | 21 | 0 | 221,733 | 221,588 | +0.1% |
| TZ0307 SIHA (Siha) [Kilimanjaro] | 17 | 10 | 7 | 139,019 | 148,239 | -6.2% |
| TZ0901 MTWARA (Mtwara) [Mtwara] | 21 | 15 | 6 | 158,504 | 263,312 | -39.8% |
| TZ0902 NEWALA (Newala) [Mtwara] | 22 | 18 | 4 | 136,939 | 234,644 | -41.6% |
| TZ0903 MASASI (Masasi) [Mtwara] | 34 | 21 | 13 | 314,778 | 281,236 | +11.9% |
| TZ0904 TANDAHIMBA (Tandahimba) [Mtwara] | 32 | 30 | 2 | 299,073 | 261,876 | +14.2% |
| TZ0905 MTWARA MIKINDANI (Mtwara Urban) [Mtwara] | 18 | 15 | 3 | 146,772 | 120,742 | +21.6% |
| TZ0906 NANYUMBU (Nanyumbu) [Mtwara] | 17 | 14 | 3 | 204,323 | 175,212 | +16.6% |
| TZ0907 MASASI TOWN (Masasi  Township Authority) [Mtwara] | 14 | 10 | 4 | 137,585 | 120,943 | +13.8% |
| TZ1201 CHUNYA (Chunya) [Mbeya] | 20 | 16 | 4 | 344,471 | 398,156 | -13.5% |
| TZ1202 MBEYA (Mbeya) [Mbeya] | 28 | 25 | 3 | 371,259 | 372,045 | -0.2% |
| TZ1203 KYELA (Kyela) [Mbeya] | 33 | 20 | 13 | 266,426 | 281,985 | -5.5% |
| TZ1204 RUNGWE (Rungwe) [Mbeya] | 29 | 24 | 5 | 273,536 | 383,359 | -28.6% |
| TZ1207 MBARALI (Mbarali) [Mbeya] | 20 | 20 | 0 | 446,336 | 385,493 | +15.8% |
| TZ1208 MBEYA CITY (Mbeya Urban) [Mbeya] | 36 | 36 | 0 | 541,603 | 529,669 | +2.3% |
| TZ2401 BARIADI (Bariadi) [Simiyu] | 21 | 15 | 6 | 383,385 | 529,659 | -27.6% |
| TZ2402 ITILIMA (Itilima) [Simiyu] | 22 | 22 | 0 | 419,213 | 380,810 | +10.1% |
| TZ2403 MEATU (Meatu) [Simiyu] | 29 | 25 | 4 | 366,941 | 364,133 | +0.8% |
| TZ2404 MASWA (Maswa) [Simiyu] | 36 | 26 | 10 | 427,864 | 396,481 | +7.9% |
| TZ2405 BUSEGA (Busega) [Simiyu] | 15 | 13 | 2 | 282,167 | 246,683 | +14.4% |
| TZ5201 KATI (Kati) [Kusini Unguja] | 42 | 39 | 3 | 132,717 | 92,673 | +43.2% |
| TZ5202 KUSINI (Kusini) [Kusini Unguja] | 21 | 20 | 1 | 63,156 | 45,822 | +37.8% |

## Observacoes por distrito

### TZ0301 ROMBO (Rombo)
- 28 wards achadas na fonte (21 com P-code oficial, 7 provisorias). Soma = 275,314 hab. vs. populacao ja registrada 284,110 hab. (-3.1%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0301-PROVn`): Chala, Keni Aleni, Kisale Masangara, Kitirima, Nanjala, Reha, Shimbi Kwandele.
- Wards da gazetteer oficial HDX 2018 nao encontradas na listagem atual (3): Aleni, Kisale Msaranga, Nanjara Reha.

### TZ0302 MWANGA (Mwanga)
- 20 wards achadas na fonte (20 com P-code oficial, 0 provisorias). Soma = 148,763 hab. vs. populacao ja registrada 152,977 hab. (-2.8%).
- Variacoes de grafia resolvidas por fuzzy match: 'Kigonigoni' (citypop) = 'Kigoningoni' (gazetteer).

### TZ0303 SAME (Same)
- 34 wards achadas na fonte (31 com P-code oficial, 3 provisorias). Soma = 300,303 hab. vs. populacao ja registrada 336,637 hab. (-10.8%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0303-PROVn`): Bangalala, Gavao-Saweni, Tae.

### TZ0304 MOSHI (Moshi)
- 32 wards achadas na fonte (31 com P-code oficial, 1 provisorias). Soma = 535,803 hab. vs. populacao ja registrada 538,028 hab. (-0.4%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0304-PROVn`): Njia Panda.
- Variacoes de grafia resolvidas por fuzzy match: 'Kirua Vunjo Magharibi' (citypop) = 'KiruaVunjo Magharibi' (gazetteer); 'Kirua Vunjo Mashariki' (citypop) = 'KiruaVunjo Mashariki' (gazetteer); 'Kirua Vunjo Kusini' (citypop) = 'KiruaVunjo Kusini' (gazetteer); 'Mwika Kaskazini' (citypop) = 'MwikaKaskazini' (gazetteer).

### TZ0305 HAI (Hai)
- 17 wards achadas na fonte (12 com P-code oficial, 5 provisorias). Soma = 240,999 hab. vs. populacao ja registrada 259,383 hab. (-7.1%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0305-PROVn`): Bomang'ombe, Bondeni, Mnadani, Muungano, Romu.
- Wards da gazetteer oficial HDX 2018 nao encontradas na listagem atual (2): Machame Kusini, Hai Mjini.

### TZ0306 MOSHI MUNICIPAL (Moshi Urban)
- 21 wards achadas na fonte (21 com P-code oficial, 0 provisorias). Soma = 221,733 hab. vs. populacao ja registrada 221,588 hab. (+0.1%).

### TZ0307 SIHA (Siha)
- 17 wards achadas na fonte (10 com P-code oficial, 7 provisorias). Soma = 139,019 hab. vs. populacao ja registrada 148,239 hab. (-6.2%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0307-PROVn`): Donyomurwak, Kashashi, Kirua, Miti Mirefu, Naeny, Ormelili, Songu.
- Wards da gazetteer oficial HDX 2018 nao encontradas na listagem atual (2): Ivaeny, Kashisha.

### TZ0901 MTWARA (Mtwara)
- 21 wards achadas na fonte (15 com P-code oficial, 6 provisorias). Soma = 158,504 hab. vs. populacao ja registrada 263,312 hab. (-39.8%).
- Excluidas da contagem (nao sao ward): Mtwara Rural Swamp Area (Swamp Area).
- Wards novas (sem P-code oficial, ID provisorio `TZ0901-PROVn`): Lipwidi, Mangopachanne, Mkunwa, Moma, Msimbati, Nalingu.
- Wards da gazetteer oficial HDX 2018 que NAO aparecem na listagem atual de Mtwara em citypopulation.de (13): Kitaya, Kiromba, Njengwa, Nitekela, Nanyamba, Mtiniko, Mnima, Chawi, Namtumbuka, Kiyanga, Milango Minne, Mbembaleo, Mtimbwilimbwi. Hipotese mais provavel: desmembramento administrativo pos-2018 moveu essas wards para um novo distrito/cidade/town council que nao faz parte deste grupo de 27 (ex.: parte de Rungwe -> Busekelo; parte de Mtwara Rural -> Nanyamba Town; parte de Newala Rural -> Newala Town; parte de Bariadi Rural -> Bariadi Town; todos vistos no indice da regiao mas fora do escopo deste grupo).

### TZ0902 NEWALA (Newala)
- 22 wards achadas na fonte (18 com P-code oficial, 4 provisorias). Soma = 136,939 hab. vs. populacao ja registrada 234,644 hab. (-41.6%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0902-PROVn`): Mikumbi, Mnyeu, Mpwapwa, Muungano.
- Wards da gazetteer oficial HDX 2018 que NAO aparecem na listagem atual de Newala em citypopulation.de (10): Luchindu, Makote, Nanguruwe, Mkunya, Mcholi I, Namiyonga, Mnekachi, Mcholi II, Mtonya, Makonga. Hipotese mais provavel: desmembramento administrativo pos-2018 moveu essas wards para um novo distrito/cidade/town council que nao faz parte deste grupo de 27 (ex.: parte de Rungwe -> Busekelo; parte de Mtwara Rural -> Nanyamba Town; parte de Newala Rural -> Newala Town; parte de Bariadi Rural -> Bariadi Town; todos vistos no indice da regiao mas fora do escopo deste grupo).
- Variacoes de grafia resolvidas por fuzzy match: 'Chilangalanga' (citypop) = 'Chilangala' (gazetteer).

### TZ0903 MASASI (Masasi)
- 34 wards achadas na fonte (21 com P-code oficial, 13 provisorias). Soma = 314,778 hab. vs. populacao ja registrada 281,236 hab. (+11.9%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0903-PROVn`): Chikukwe, Chikundi, Chikunja, Lupaso, Makong’onda, Mijelejele, Mitesa, Mpeta, Mpindimbi, Msikisi, Namwanga, Nangoo, Ndanda.
- Wards da gazetteer oficial HDX 2018 nao encontradas na listagem atual (1): Mkundi.

### TZ0904 TANDAHIMBA (Tandahimba)
- 32 wards achadas na fonte (30 com P-code oficial, 2 provisorias). Soma = 299,073 hab. vs. populacao ja registrada 261,876 hab. (+14.2%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0904-PROVn`): Malopokelo, Mkwedu.
- Variacoes de grafia resolvidas por fuzzy match: 'Mdimbamnyoma' (citypop) = 'Mdimba Mnyoma' (gazetteer); 'Mihuta' (citypop) = 'Miuta' (gazetteer); 'Milingodi' (citypop) = 'Milongodi' (gazetteer).

### TZ0905 MTWARA MIKINDANI (Mtwara Urban)
- 18 wards achadas na fonte (15 com P-code oficial, 3 provisorias). Soma = 146,772 hab. vs. populacao ja registrada 120,742 hab. (+21.6%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0905-PROVn`): Magomeni, Mtawanya, Tandika.

### TZ0906 NANYUMBU (Nanyumbu)
- 17 wards achadas na fonte (14 com P-code oficial, 3 provisorias). Soma = 204,323 hab. vs. populacao ja registrada 175,212 hab. (+16.6%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0906-PROVn`): Kamundi, Kilimanihewa, Michiga.

### TZ0907 MASASI TOWN (Masasi  Township Authority)
- 14 wards achadas na fonte (10 com P-code oficial, 4 provisorias). Soma = 137,585 hab. vs. populacao ja registrada 120,943 hab. (+13.8%).
- Wards novas (sem P-code oficial, ID provisorio `TZ0907-PROVn`): Chanikanguo, Matawale, Mumbaka, Napupa.
- Wards da gazetteer oficial HDX 2018 nao encontradas na listagem atual (2): Mpindimbi, Mwenge.

### TZ1201 CHUNYA (Chunya)
- 20 wards achadas na fonte (16 com P-code oficial, 4 provisorias). Soma = 344,471 hab. vs. populacao ja registrada 398,156 hab. (-13.5%).
- Wards novas (sem P-code oficial, ID provisorio `TZ1201-PROVn`): Bwawani, Kasanga, Nkung'ungu, Upendo.
- Variacoes de grafia resolvidas por fuzzy match: 'Lupa Tingatinga' (citypop) = 'Lupatingatinga' (gazetteer).

### TZ1202 MBEYA (Mbeya)
- 28 wards achadas na fonte (25 com P-code oficial, 3 provisorias). Soma = 371,259 hab. vs. populacao ja registrada 372,045 hab. (-0.2%).
- Wards novas (sem P-code oficial, ID provisorio `TZ1202-PROVn`): Izyra, Mjele, Shizuvi.

### TZ1203 KYELA (Kyela)
- 33 wards achadas na fonte (20 com P-code oficial, 13 provisorias). Soma = 266,426 hab. vs. populacao ja registrada 281,985 hab. (-5.5%).
- Wards novas (sem P-code oficial, ID provisorio `TZ1203-PROVn`): Bondeni, Ibanda, Ipyana, Itunge, Mababu, Mbugani, Mikoroshoni, Mwanganyanga, Ndandalo, Njisi, Nkokwa, Nkuyu, Serengeti.
- Variacoes de grafia resolvidas por fuzzy match: 'Katumba Songwe' (citypop) = 'Katumbasongwe' (gazetteer).

### TZ1204 RUNGWE (Rungwe)
- 29 wards achadas na fonte (24 com P-code oficial, 5 provisorias). Soma = 273,536 hab. vs. populacao ja registrada 383,359 hab. (-28.6%).
- Wards novas (sem P-code oficial, ID provisorio `TZ1204-PROVn`): Iponjola, Itagata, Lupepo, Matwebe, Ndanto.
- Wards da gazetteer oficial HDX 2018 que NAO aparecem na listagem atual de Rungwe em citypopulation.de (13): Kandete, Luteba, Mpombo, Isange, Kabula, Lwangwa, Lufilyo, Itete, Kisegese, Lupata, Kambasegela, Kikole, Ikama. Hipotese mais provavel: desmembramento administrativo pos-2018 moveu essas wards para um novo distrito/cidade/town council que nao faz parte deste grupo de 27 (ex.: parte de Rungwe -> Busekelo; parte de Mtwara Rural -> Nanyamba Town; parte de Newala Rural -> Newala Town; parte de Bariadi Rural -> Bariadi Town; todos vistos no indice da regiao mas fora do escopo deste grupo).

### TZ1207 MBARALI (Mbarali)
- 20 wards achadas na fonte (20 com P-code oficial, 0 provisorias). Soma = 446,336 hab. vs. populacao ja registrada 385,493 hab. (+15.8%).
- Variacoes de grafia resolvidas por fuzzy match: 'Itamboleo' (citypop) = 'Itambaleo' (gazetteer).

### TZ1208 MBEYA CITY (Mbeya Urban)
- 36 wards achadas na fonte (36 com P-code oficial, 0 provisorias). Soma = 541,603 hab. vs. populacao ja registrada 529,669 hab. (+2.3%).
- Variacoes de grafia resolvidas por fuzzy match: 'Mbalizi Road' (citypop) = 'Mbalizi RD' (gazetteer).

### TZ2401 BARIADI (Bariadi)
- 21 wards achadas na fonte (15 com P-code oficial, 6 provisorias). Soma = 383,385 hab. vs. populacao ja registrada 529,659 hab. (-27.6%).
- Excluidas da contagem (nao sao ward): Serengeti National Park / Maswa Game Reserve (National Park).
- Wards novas (sem P-code oficial, ID provisorio `TZ2401-PROVn`): Banemhi, Gibishi, Ihusi, Itubukilo, Masewa, Mwasubuya.
- Wards da gazetteer oficial HDX 2018 que NAO aparecem na listagem atual de Bariadi em citypopulation.de (10): Nyangokolwa, Somanda, Bunamhala, Mhango, Guduwi, Nyakabindi, Isanga, Bariadi, Malambo, Sima. Hipotese mais provavel: desmembramento administrativo pos-2018 moveu essas wards para um novo distrito/cidade/town council que nao faz parte deste grupo de 27 (ex.: parte de Rungwe -> Busekelo; parte de Mtwara Rural -> Nanyamba Town; parte de Newala Rural -> Newala Town; parte de Bariadi Rural -> Bariadi Town; todos vistos no indice da regiao mas fora do escopo deste grupo).
- Variacoes de grafia resolvidas por fuzzy match: 'Mwadobana' (citypop) = 'Madobana' (gazetteer); 'Mwaubingi' (citypop) = 'Mwaubinge' (gazetteer).

### TZ2402 ITILIMA (Itilima)
- 22 wards achadas na fonte (22 com P-code oficial, 0 provisorias). Soma = 419,213 hab. vs. populacao ja registrada 380,810 hab. (+10.1%).
- Excluidas da contagem (nao sao ward): Serengeti National Park / Maswa Game Reserve (National Park).
- Variacoes de grafia resolvidas por fuzzy match: 'Ikindilo' (citypop) = 'Ikindiro' (gazetteer).

### TZ2403 MEATU (Meatu)
- 29 wards achadas na fonte (25 com P-code oficial, 4 provisorias). Soma = 366,941 hab. vs. populacao ja registrada 364,133 hab. (+0.8%).
- Excluidas da contagem (nao sao ward): Serengeti National Park / Maswa Game Reserve (National Park).
- Wards novas (sem P-code oficial, ID provisorio `TZ2403-PROVn`): Isengwa, Kabondo, Mbugayabanghya, Mbushi.

### TZ2404 MASWA (Maswa)
- 36 wards achadas na fonte (26 com P-code oficial, 10 provisorias). Soma = 427,864 hab. vs. populacao ja registrada 396,481 hab. (+7.9%).
- Wards novas (sem P-code oficial, ID provisorio `TZ2404-PROVn`): Bugarama, Busangi, Jija, Mataba, Mbaragane, Mwabaratulu, Mwabayanda, Sangamwalugesha, Shanwa, Sola.

### TZ2405 BUSEGA (Busega)
- 15 wards achadas na fonte (13 com P-code oficial, 2 provisorias). Soma = 282,167 hab. vs. populacao ja registrada 246,683 hab. (+14.4%).
- Excluidas da contagem (nao sao ward): Kijereshi Game Reserve / Serengeti National Park (Game Reserve).
- Wards novas (sem P-code oficial, ID provisorio `TZ2405-PROVn`): Imalamate, Nyashimo.

### TZ5201 KATI (Kati)
- 42 wards achadas na fonte (39 com P-code oficial, 3 provisorias). Soma = 132,717 hab. vs. populacao ja registrada 92,673 hab. (+43.2%).
- Wards novas (sem P-code oficial, ID provisorio `TZ5201-PROVn`): Kijibwemtu, Pete, Zawiyani.
- Wards da gazetteer oficial HDX 2018 nao encontradas na listagem atual (1): Michamvi.
- Variacoes de grafia resolvidas por fuzzy match: 'Kiboje Mwembeshauri' (citypop) = 'Kiboje Muembeshauri' (gazetteer); 'Ndijani Mwembepunda' (citypop) = 'Ndijani Muembe Punda' (gazetteer).

### TZ5202 KUSINI (Kusini)
- 21 wards achadas na fonte (20 com P-code oficial, 1 provisorias). Soma = 63,156 hab. vs. populacao ja registrada 45,822 hab. (+37.8%).
- Wards novas (sem P-code oficial, ID provisorio `TZ5202-PROVn`): Michamvi.
- Wards da gazetteer oficial HDX 2018 nao encontradas na listagem atual (1): Pete.

## Achados especiais

### Pete / Michamvi - possivel troca de fronteira distrital (Kati <-> Kusini, Zanzibar)
Em Kati (TZ5201), a ward 'Pete' aparece na listagem atual (censo 2022, pop. 2.108) sem match na gazetteer oficial de Kati. A gazetteer oficial HDX 2018, porem, TEM uma ward 'Pete' (`TZ5202131`) - só que registrada sob o distrito vizinho Kusini (TZ5202), nao Kati. Simetricamente, em Kusini a ward 'Michamvi' aparece na listagem atual (pop. 3.465) sem match na gazetteer oficial de Kusini, mas a gazetteer oficial TEM uma ward 'Michamvi' (`TZ5201361`) registrada sob Kati. Par exato (1 sobra de cada lado, nomes identicos, trocados). Interpretacao mais provavel: uma troca de fronteira distrital entre 2018 e 2022 moveu Pete de Kusini para Kati e Michamvi de Kati para Kusini. **Decisao**: por prudencia (o P-code codifica o distrito-pai no proprio prefixo), nao reatribuimos os P-codes oficiais cruzados - ambas tratadas como provisorias (`TZ5201-PROV2` e `TZ5202-PROV1`) ate reconciliacao futura, com a hipotese documentada no campo `notes` de cada linha.

### Masasi: 'Mpindimbi' - coincidencia de nome entre Masasi Rural e Masasi Town Authority
'Mpindimbi' aparece como ward nova (sem match) em Masasi Rural (TZ0903, pop. 8.689). A gazetteer oficial tem uma ward 'Mpindimbi' (`TZ0907043`), mas registrada sob o distrito vizinho Masasi Town Authority (TZ0907), que tambem nao usou essa entrada (ficou como gaz_unused la). Diferente do par Pete/Michamvi, aqui NAO ha uma troca simetrica limpa (Masasi Town tem 2 sobras - Mpindimbi e Mwenge - nao 1), entao tratamos como coincidencia de nome ou fronteira menos clara. Mantida como provisoria em TZ0903 sem reatribuicao cruzada.

## Padrao geral de divergencia de populacao (soma wards vs. populacao ja registrada)
Confirma o padrao ja documentado no piloto Babati (projecao HDX COD-PS 2020 vs. censo NBS 2022 sao fontes/anos diferentes) e acrescenta um segundo padrao novo neste grupo: **desmembramento administrativo pos-2018** explica as maiores divergencias (Mtwara -39.8%, Newala -41.6%, Rungwe -28.6%, Bariadi -27.6%, Kati +43.2%, Kusini +37.8%) - nestes casos o distrito oficial 'perdeu' populacao para um novo distrito/town council/city que se desmembrou dele e que NAO faz parte da populacao ja registrada original (que e mais antiga) nem deste grupo de 27 distritos. Ja Kati/Kusini sao o caso inverso: cidades-cidades menores (populacao ja registrada numeros antigos/baixos) com crescimento real + possivel troca de fronteira (ver achado especial acima).

## Falhas
Nenhum distrito falhou completamente - os 27 distritos do grupo foram encontrados e tiveram tabela de wards extraida com sucesso.
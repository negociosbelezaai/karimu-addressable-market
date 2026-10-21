# Enumeração de wards — Tanzânia, Grupo 5 (Arusha, Pwani, Ruvuma, Shinyanga, Kaskazini Unguja, Kusini Pemba)

Data: 2026-10-03
Entregável: `deliverables/ward-enum-tza-group5.csv` (659 wards, 29 distritos, 6 regiões)
Método: igual ao piloto de Babati (`research/2026-10-02-ward-level-pilot-summary.md`) — citypopulation.de censo 2022-08-23 para wards, cruzado com gazetteer oficial HDX 2018 (`tza_admbnda_adm3_20181019`) por `ADM2_PCODE` do distrito + fuzzy match de nome de ward.

Nenhum distrito falhou completamente — todos os 29 distritos listados na tarefa foram encontrados e processados.

## Achado estrutural mais importante: distritos "pai" divididos entre 2018 (gazetteer) e 2022 (censo atual)

Em pelo menos 4 distritos deste grupo, o pcode ADM2 oficial de 2018 cobria uma área que o governo da Tanzânia já dividiu em dois (ou mais) distritos administrativos reais por volta de 2016-2019, mas que o citypopulation.de só reflete na estrutura corrente (pós-divisão). Isso é visível porque, seguindo a própria página-índice da região (conforme instruído — nunca adivinhar URL), o pcode citypopulation que corresponde ao nosso ADM2_PCODE aponta para um distrito com NOME diferente e uma lista de wards bem mais curta que a do gazetteer:

- **TZ0601 Bagamoyo**: gazetteer tinha 22 wards; só 7 foram encontrados no Bagamoyo atual (11 wards, 7 batem + 4 novas). As 15 wards do gazetteer que sumiram (Msata, Miono, Mkange, Vigwaza, Talawanda, Bwilingu, Lugoba, Ubenazomozi, Kibindu, Pera, Msoga, Kimange, Mandera, Mbwewe) quase certamente foram para **Chalinze**, distrito novo que aparece na página-índice do Pwani mas que **não está na nossa lista de distritos do grupo** — portanto fora do escopo deste levantamento.
- **TZ0605 Rufiji**: gazetteer tinha 26 wards; só 11 batem no Rufiji atual (13 wards, 11 batem + 2 novas). As 15 wards que sumiram (Kibiti, Bungu, Mahege, Mchukwi, Mtunda, Ruaruke, Salale, Mbuchi, Kiongoroni, Maparoni, Dimani, Mtawanya, Mjawa, Mlanzi, Mwambao) quase certamente foram para **Kibiti**, novo distrito fora da nossa lista.
- **TZ1002 Songea** (Rural): 6 wards do gazetteer (Wino, Matumbi, Gumbiro, Mahanje, Mtyangimbole, Mkongotema) não aparecem na Songea Rural atual — provável migração para **Madaba**, distrito novo fora da lista.
- **TZ1003 Mbinga**: 10 wards do gazetteer (Utiri, Mbinga Mjini, Kilimani, Mbangamao, Kihungu, Kikolo, Luwaita, Myangayanga, Mpepai, Kitanda) não aparecem na Mbinga Rural atual — provável migração para **Mbinga Town**, distrito novo fora da lista.
- **TZ1704 Kahama**: o caso mais extremo. O gazetteer 2018 lista 35 wards sob "Kahama" (ADM2_PCODE TZ1704), incluindo uma ward chamada "Ushetu". A página-índice atual do Shinyanga não tem mais um distrito "Kahama" no código 1704 — tem **"Msalala"** (mesmo pcode 1704, usado por seguir o link da própria página conforme instruído) e um distrito totalmente novo, **"Ushetu"** (código 1706, fora da nossa lista), que virou um distrito de pleno direito com suas próprias ~20 wards. Das 35 wards do gazetteer, só 16 batem no Msalala atual; as outras 19 (Chona, Chambo, Kisuke, Mapamba, Bukomela, Ukune, Igunda, Kinamapula, Igwamanoni, Mpunze, Sabasabini, Idahina, Bulungwa, Nyankende, Ulewe, Ushetu, Uyogo, Ulowa, Ubagwe) foram para Ushetu.

**Implicação prática**: nestes 5 distritos, a tabela deste grupo cobre fielmente todas as wards do pcode ADM2 oficial **que ainda existem sob esse pcode hoje**, mas não cobre a área administrativa que se desmembrou para um distrito-irmão novo (Chalinze, Kibiti, Madaba, Mbinga Town, Ushetu) — nenhum desses 5 distritos novos estava na lista de distritos atribuída a este grupo, então ficaram fora do escopo por desenho, não por falha de busca. Fica registrado aqui para quem for reconciliar o nível distrito depois.

## Por distrito

### Região Arusha
- **TZ0201 Monduli**: 20 wards (15 oficiais + 5 provisórias: Lashaine, Lemooti, Mfereji, Migungani, Naalarami). Soma 227.585 vs. registrado 227.005 (+0,3%, bate bem).
- **TZ0202 Meru**: 26 wards (17 oficiais + 9 provisórias: Ambureni, Imbaseni, Majengo, Malula, Maruvango, Ngabobo, Nkoanekoli, Shambarai Burka, Uwiro). Excluída "Arusha National Park" (sem população). Soma 331.603 vs. registrado 312.524 (+6,1%).
- **TZ0203 Arusha City**: 25 wards (19 oficiais + 6 provisórias: Moivaro, Muriet, Olmoti, Osunyai Jr, Sakina, Sinoni). Soma 617.631 vs. registrado 536.007 (+15,2%, maior divergência do bloco Arusha — cidade em crescimento rápido, sem indício de split de distrito aqui).
- **TZ0204 Karatu**: 14 wards, todas oficiais (100% match com o gazetteer, nenhuma nova). Excluída "Marang Forest Reserve" (sem população). Soma 280.454 vs. registrado 292.100 (-4,0%).
- **TZ0205 Ngorongoro**: 28 wards (21 oficiais + 7 provisórias: Alaitolei, Engaresero, Eyasi, Kirangi, Misigiyo, Ngoile, Piyaya). Soma 273.549 vs. registrado 231.666 (+18,1%).
- **TZ0206 Arusha** (rural): 27 wards (20 oficiais + 7 provisórias: Ilboru, Kiutu, Laroi, Lemanyata, Lengijave, Oldonyowass, Tarakwa). Excluída "Meru Forest" (sem população). **Gap notável**: a ward oficial do gazetteer "Olkokola" (TZ0206021) não foi encontrada na lista de wards do censo 2022 — possivelmente renomeada ou fundida com outra; não incluída na tabela (sem dado de população, sem invenção de número). Soma 449.518 vs. registrado 412.383 (+9,0%).
- **TZ0207 Longido**: 18 wards (16 oficiais + 2 provisórias: Noondoto, Sinya). Soma 175.915 vs. registrado 178.768 (-1,6%, bate bem).

### Região Pwani
- **TZ0601 Bagamoyo**: 11 wards (7 oficiais + 4 provisórias: Kisutu, Makurunge, Mapinga, Nianjema). Ver nota de split acima (Chalinze). Soma 205.478 vs. registrado 408.198 (-49,7%, maior divergência negativa do grupo — explicada pelo split, não é erro).
- **TZ0602 Kibaha**: 14 wards (11 oficiais + 3 provisórias: Kawawa, Mtambani, Mtongani). Soma 123.367 vs. registrado 90.707 (+36,0% — zona de expansão peri-urbana de Dar es Salaam).
- **TZ0603 Kisarawe**: 17 wards (15 oficiais + 2 provisórias: Boga, Kazimzumbwi). Soma 159.226 vs. registrado 110.759 (+43,8%).
- **TZ0604 Mkuranga**: 25 wards (18 oficiais + 7 provisórias: Beta, Dondo, Kisegese, Mipeko, Msonga, Mwandege, Tengelea). Soma 533.033 vs. registrado 260.000 (**+105% — a maior divergência de todo o grupo**). Verificado diretamente na página do distrito (dois fetches independentes confirmaram o mesmo total e a mesma soma de wards batendo exatamente); não é erro de leitura. Mkuranga faz fronteira direta com Dar es Salaam e é conhecido por crescimento populacional explosivo pós-2012 por absorção de expansão urbana (ward Vikindu sozinha tem 118.210 hab., maior que o distrito inteiro registrado antes). Divergência real de dado, não de método.
- **TZ0605 Rufiji**: 13 wards (11 oficiais + 2 provisórias: Kipugira, Mohoro). Ver nota de split acima (Kibiti). Soma 159.906 vs. registrado 238.545 (-33,0%).
- **TZ0606 Mafia**: 8 wards, todas oficiais (100% match, nenhuma nova). Soma 66.180 vs. registrado 53.564 (+23,6%).
- **TZ0607 Kibaha Town**: 14 wards (11 oficiais + 3 provisórias: Sofu, Tangini, Viziwaziwa). Soma 265.360 vs. registrado 196.069 (+35,3%).

### Região Ruvuma
- **TZ1001 Tunduru**: 39 wards (35 oficiais + 4 provisórias: Chiwana, Majimaji, Namakambale, Tinginya). Soma 412.054 vs. registrado 360.350 (+14,3%).
- **TZ1002 Songea** (rural): 16 wards (11 oficiais + 5 provisórias: Kizuka, Liganga, Lilahi, Litapwasi, Parangu). Ver nota de split acima (Madaba). Soma 178.201 vs. registrado 191.415 (-6,9%).
- **TZ1003 Mbinga** (rural): 29 wards (24 oficiais + 5 provisórias: Amani Makoro, Lukarasi, Mhongozi, Muungano, Wukiro). Ver nota de split acima (Mbinga Town). Soma 285.582 vs. registrado 426.839 (-33,1%).
- **TZ1004 Songea Municipal**: 21 wards, todas oficiais (100% match, nenhuma nova). Soma 286.285 vs. registrado 290.520 (-1,5%, bate bem).
- **TZ1005 Namtumbo**: 21 wards (18 oficiais + 3 provisórias: Lisimonji, Mkongo gulioni, Msisima). Soma 271.368 vs. registrado 234.713 (+15,6%).
- **TZ1006 Nyasa**: 20 wards (15 oficiais + 5 provisórias: Linga, Lumeme, Mipotopoto, Mpepo, Upolo). Soma 191.193 vs. registrado 186.442 (+2,5%, bate bem).

### Região Shinyanga
- **TZ1701 Shinyanga Municipal**: 17 wards, todas oficiais (100% match, nenhuma nova). Soma 214.744 vs. registrado 187.876 (+14,3%).
- **TZ1702 Kishapu**: 29 wards (20 oficiais + 9 provisórias: Bupigi, Busangwa, Idukilo, Igaga, Maganzo, Mwasubi, Mwataga, Mwaweja, Ndoleleji). Soma 335.483 vs. registrado 320.311 (+4,7%).
- **TZ1703 Shinyanga** (rural): 26 wards, todas oficiais (100% match, nenhuma nova). Soma 468.611 vs. registrado 407.334 (+15,0%).
- **TZ1704 Kahama**: 18 wards (16 oficiais + 2 provisórias: Ikinda, Mwakata). Ver nota de split acima (Ushetu) — **maior divergência negativa do grupo em termos relativos de distrito "intacto"**: soma 378.214 vs. registrado 639.206 (-40,8%), majoritariamente explicada pela perda de ~19 das 35 wards originais para o novo distrito Ushetu.
- **TZ1705 Kahama Town**: 20 wards, todas oficiais (100% match, nenhuma nova). Soma 453.654 vs. registrado 339.957 (+33,4%).

### Região Kaskazini Unguja
- **TZ5101 Kaskazini A**: 44 wards/shehia (34 oficiais + 10 provisórias — a maior taxa de novas do grupo: Banda Kuu, Juga Kuu, Kipange, Kiungani, Matemwe Kaskazini, Matemwe Kusini, Mbuyutende, Mchangani, Mtakuja, Muwanda). Subdivisão de shehia em Zanzibar é conhecida por ser mais fina/volátil entre censos que ward continental. **Gap**: 2 wards do gazetteer (Nungwi, Kijini) não encontradas na lista atual — possivelmente renomeadas/fundidas, não incluídas sem dado. Soma 157.369 vs. registrado 128.663 (+22,3%).
- **TZ5102 Kaskazini B**: 31 wards/shehia (26 oficiais + 5 provisórias: Donge Pwani, Kiongwe Kidogo, Kisongoni, Kwagube, Majenzi). **Gap**: 3 wards do gazetteer (Donge Kipange, Donge Mchangani, Muwanda) não encontradas na lista atual. Soma 99.921 vs. registrado 121.062 (-17,5%).

### Região Kusini Pemba
- **TZ5501 Chake Chake**: 32 wards/shehia (28 oficiais + 4 provisórias: Gombani, Mchanga Mrima, Mjini Ole, Ole). **Gap**: 1 ward do gazetteer (Dodo) não encontrada. Soma 136.298 vs. registrado 116.657 (+16,8%).
- **TZ5502 Mkoani**: 36 wards/shehia (33 oficiais + 3 provisórias: Chole, Dodo, Mchakwe). Soma 135.052 vs. registrado 107.558 (+25,6%).

## Observação metodológica — Zanzibar
Em Kaskazini Unguja e Kusini Pemba a unidade local chamada na fonte é "shehia", não "ward" — mantido `local_unit_type=Ward` na tabela por consistência de schema com o resto do dataset (conforme instrução da tarefa), mas registrado aqui para quem for usar o nome local correto depois.

## Falhas
Nenhuma. Todos os 29 distritos tiveram página de índice e página de wards acessíveis via WebFetch, com lista completa de wards e total do distrito.

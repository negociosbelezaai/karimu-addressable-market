# Raw data collected from citypopulation.de (census 2022-08-23) for TZA ward-enum group 4
# Each old-district entry maps to one or more CURRENT citypopulation.de district pages
# (because several old ADM2 districts were split/renamed by Tanzania's post-2018 redistricting).

DISTRICTS = {
    "TZ0101": {
        "name": "KONDOA", "reg_pop": 311638,
        "sources": [
            ("Kondoa Rural", "citypopulation.de/en/tanzania/central/admin/0101__kondoa_rural/", [
                ("Bereko", 8223), ("Bumbuta", 10149), ("Busi", 9399), ("Changaa", 8436),
                ("Haubi", 14679), ("Hondomairo", 14481), ("Itaswi", 13790), ("Itololo", 7594),
                ("Kalamba", 14621), ("Keikei", 13454), ("Kikilo", 9620), ("Kikore", 15529),
                ("Kinyasi", 9872), ("Kisese", 14921), ("Kwadelo", 13504), ("Masange", 6556),
                ("Mnenia", 13056), ("Pahi", 15766), ("Salanka", 10675), ("Soera", 8597),
                ("Thawi", 11932),
            ]),
            ("Kondoa Town", "citypopulation.de/en/tanzania/central/admin/0108__kondoa_town/", [
                ("Bolisa", 3919), ("Chemchem", 8351), ("Kilimani", 9629), ("Kingale", 13152),
                ("Kolo", 5649), ("Kondoa Mjini", 26179), ("Serya", 9830), ("Suruke", 3734),
            ]),
        ],
    },
    "TZ0102": {
        "name": "MPWAPWA", "reg_pop": 368137,
        "sources": [
            ("Mpwapwa", "citypopulation.de/en/tanzania/central/admin/0102__mpwapwa/", [
                ("Berege", 12668), ("Chipogoro", 14515), ("Chitemo", 13876), ("Chunyu", 19190),
                ("Galigali", 5006), ("Godegode", 11150), ("Gulwe", 13189), ("Ipera", 9658),
                ("Iwondo", 13211), ("Kibakwe", 19968), ("Kimagai", 9777), ("Kingiti", 9213),
                ("Lufu", 5326), ("Luhundwa", 16424), ("Lumuma", 4339), ("Lupeta", 9795),
                ("Malolo", 7449), ("Mang'aliza", 6064), ("Massa", 16558), ("Matomondo", 11228),
                ("Mazae", 11011), ("Mbuga", 6745), ("Mima", 18138), ("Mlembule", 11335),
                ("Mlunduzi", 14342), ("Mpwapwa Mjini", 24670), ("Mtera", 14187), ("Nghambi", 11926),
                ("Pwaga", 15386), ("Rudi", 15440), ("Ving'hawe", 16311), ("Wangi", 7958),
                ("Wotta", 7194),
            ]),
        ],
    },
    "TZ0103": {
        "name": "KONGWA", "reg_pop": 386458,
        "sources": [
            ("Kongwa", "citypopulation.de/en/tanzania/central/admin/0103__kongwa/", [
                ("Chamkoroma", 18990), ("Chitego", 15434), ("Chiwe", 30099), ("Hogoro", 22777),
                ("Iduo", 15244), ("Kibaigwa", 50054), ("Kongwa", 15351), ("Lenjulu", 28622),
                ("Makawa", 11631), ("Matongoro", 11513), ("Mkoka", 16329), ("Mlali", 28218),
                ("Mtanana", 16435), ("Nghumbi", 15778), ("Ngomai", 14319), ("Njoge", 10757),
                ("Pandambili", 13079), ("Sagara", 28536), ("Sejeli", 27312), ("Songambele", 23342),
                ("Ugogoni", 22621), ("Zoissa", 7426),
            ]),
        ],
    },
    "TZ0104": {
        "name": "CHAMWINO", "reg_pop": 420529,
        "sources": [
            ("Chamwino", "citypopulation.de/en/tanzania/central/admin/0104__chamwino/", [
                ("Buigiri", 13853), ("Chamwino", 16424), ("Chiboli", 6849), ("Chilonwa", 9993),
                ("Chinugulu", 11125), ("Dabalo", 26241), ("Fufu", 6045), ("Handali", 12809),
                ("Haneti", 19635), ("Huzi", 12619), ("Idifu", 11977), ("Igandu", 8778),
                ("Ikombolinga", 6118), ("Ikowa", 8143), ("Iringa Mvumi Zamani", 9271),
                ("Itiso", 22547), ("Loje", 7916), ("Majeleko", 9244), ("Makang'wa", 8938),
                ("Manchali", 14884), ("Manda", 19144), ("Manzase", 16874), ("Membe", 14079),
                ("Mlowa Barabarani", 18975), ("Mlowa Bwawani", 13326), ("Mpwayungu", 19282),
                ("Msamalo", 16413), ("Msanga", 13992), ("Muungano", 13029), ("Mvumi Makulu", 8618),
                ("Mvumi Mission", 19367), ("Nghahelezi", 11341), ("Nghambaku", 10501),
                ("Nhinhi", 9507), ("Segala", 21348), ("Zajilwa", 16971),
            ]),
        ],
    },
    "TZ0105": {
        "name": "DODOMA MUNICIPAL", "reg_pop": 505425,
        "sources": [
            ("Dodoma City", "citypopulation.de/en/tanzania/central/admin/0105__dodoma_city/", [
                ("Chahwa", 6165), ("Chamwino", 21407), ("Chang'ombe", 39324), ("Chigongwe", 8933),
                ("Chihanga", 13605), ("Dodoma Makulu", 44013), ("Hazina", 10419),
                ("Hombolo Bwawani", 20033), ("Hombolo Makulu", 10857), ("Ihumwa", 24112),
                ("Ipagala", 49289), ("Ipala", 7663), ("Iyumbu", 7740), ("Kikombo", 11269),
                ("Kikuyu Kaskazini", 17376), ("Kikuyu Kusini", 11126), ("Kilimani", 9562),
                ("Kiwanja cha Ndege", 10333), ("Kizota", 30632), ("Madukani", 2066),
                ("Majengo", 4817), ("Makole", 10571), ("Makutupora", 19966), ("Matumbulu", 11169),
                ("Mbabala", 16929), ("Mbalawala", 11370), ("Miyuji", 36588), ("Mkonze", 41256),
                ("Mnadani", 44311), ("Mpunguzi", 13491), ("Msalato", 12905), ("Mtumba", 14673),
                ("Nala", 11715), ("Ng'hong'honha", 19173), ("Nkuhungu", 49327), ("Ntyuka", 13543),
                ("Nzuguni", 50454), ("Tambukareli", 10756), ("Uhuru", 1739), ("Viwandani", 4448),
                ("Zuzu", 10054),
            ]),
        ],
    },
    "TZ0106": {
        "name": "BAHI", "reg_pop": 276916,
        "sources": [
            ("Bahi", "citypopulation.de/en/tanzania/central/admin/0106__bahi/", [
                ("Babayu", 14737), ("Bahi", 31410), ("Chali", 14687), ("Chibelela", 12791),
                ("Chifutuka", 18604), ("Chikola", 18107), ("Chipanga", 13440), ("Ibihwa", 15118),
                ("Ibugule", 10957), ("Ilindi", 11969), ("Kigwe", 7201), ("Lamaiti", 18130),
                ("Makanda", 12186), ("Mpalanga", 14879), ("Mpamantwa", 18046), ("Mpinga", 12605),
                ("Msisi", 16994), ("Mtitaa", 12105), ("Mundemu", 10656), ("Mwitikira", 9281),
                ("Nondwa", 12079), ("Zanka", 16544),
            ]),
        ],
    },
    "TZ0107": {
        "name": "CHEMBA", "reg_pop": 293229,
        "sources": [
            ("Chemba", "citypopulation.de/en/tanzania/central/admin/0107__chemba/", [
                ("Babayu", 11331), ("Chandama", 10511), ("Chemba", 9730), ("Churuku", 9635),
                ("Dalai", 18195), ("Farkwa", 15616), ("Goima", 14985), ("Gwandi", 7328),
                ("Jangalo", 21713), ("Kidoka", 16378), ("Kimaha", 13435), ("Kinyamsindo", 7001),
                ("Kwamtoro", 17657), ("Lahoda", 20584), ("Lalta", 5781), ("Makorongo", 8640),
                ("Mondo", 10986), ("Mpendo", 11861), ("Mrijo", 27777), ("Msaada", 7314),
                ("Ovada", 8318), ("Paranga", 17613), ("Sanzawa", 15970), ("Songoro", 13078),
                ("Soya", 12868), ("Tumbakose", 5028),
            ]),
        ],
    },
    "TZ0501": {
        "name": "KILOSA", "reg_pop": 543637,
        "sources": [
            ("Kilosa", "citypopulation.de/en/tanzania/coastal/admin/0501__kilosa/", [
                ("Berega", 13196), ("Chanzulu", 14084), ("Dumila", 47237), ("Kasiki", 5317),
                ("Kidete", 15000), ("Kidodi", 12123), ("Kilangali", 17112), ("Kimamba A", 8025),
                ("Kimamba B", 7875), ("Kisanga", 19714), ("Kitete", 13229), ("Lumbiji", 9300),
                ("Lumuma", 18123), ("Mabula", 9597), ("Mabwerebwere", 9878), ("Madoto", 3555),
                ("Magole", 11752), ("Magomeni", 14374), ("Magubike", 14945), ("Maguha", 10389),
                ("Malolo", 13319), ("Mamboya", 15590), ("Masanze", 10941), ("Mbigiri", 13671),
                ("Mbumi", 4599), ("Mhenda", 9369), ("Mikumi", 31220), ("Mkwatani", 19128),
                ("Msowero", 30647), ("Mtumbatu", 24369), ("Mvumi", 23895), ("Parakuyo", 6638),
                ("Ruaha", 35067), ("Rudewa", 26169), ("Ruhembe", 18626), ("Tindiga", 14113),
                ("Ulaya", 14458), ("Uleling'ombe", 4787), ("Vidunda", 13628), ("Zombo", 11973),
            ]),
        ],
    },
    "TZ0502": {
        "name": "MOROGORO", "reg_pop": 321367,
        "sources": [
            ("Morogoro Rural", "citypopulation.de/en/tanzania/coastal/admin/0502__morogoro_rural/", [
                ("Bungu", 4536), ("Bwakila Chini", 31419), ("Bwakila Juu", 6776), ("Gwata", 9798),
                ("Kasanga", 7364), ("Kibogwa", 10929), ("Kibuko", 6485), ("Kibungo Juu", 6892),
                ("Kidugalo", 8939), ("Kinole", 13356), ("Kiroka", 14307), ("Kisaki", 28414),
                ("Kisemu", 10317), ("Kolero", 10360), ("Konde", 7146), ("Lundi", 10773),
                ("Matuli", 8265), ("Mikese", 23637), ("Mkambarani", 18388), ("Mkulazi", 6617),
                ("Mkuyuni", 14341), ("Mngazi", 13708), ("Mtombozi", 10247), ("Mvuha", 21478),
                ("Ngerengere", 15509), ("Selembala", 8802), ("Singisa", 14812), ("Tawa", 12166),
                ("Tegetero", 8528), ("Tomondo", 11503), ("Tununguo", 11924),
            ]),
        ],
    },
    "TZ0503": {
        "name": "KILOMBERO", "reg_pop": 505955,
        "sources": [
            ("Ifakara Town", "citypopulation.de/en/tanzania/coastal/admin/0509__ifakara_town/", [
                ("Ifakara", 13367), ("Katindiuka", 7365), ("Kibaoni", 29550), ("Kiberege", 17325),
                ("Kidatu", 27463), ("Kisawasawa", 9250), ("Lipangalala", 14387), ("Lumemo", 16893),
                ("Mang'ula", 6144), ("Mang'ula B", 8642), ("Mbasa", 19674), ("Michenga", 9945),
                ("Mkula", 10330), ("Mlabani", 15706), ("Msolwa Station", 9169), ("Mwaya", 28331),
                ("Sanje", 12777), ("Signal", 11351), ("Viwanjasitini", 22755),
            ]),
            ("Mlimba", "citypopulation.de/en/tanzania/coastal/admin/0503__mlimba/", [
                ("Ching'anda", 13527), ("Chisano", 10418), ("Chita", 27858), ("Idete", 11741),
                ("Igima", 22336), ("Kalengakelu", 14411), ("Kamwene", 18169), ("Masagati", 11092),
                ("Mbingu", 15180), ("Mchombe", 29875), ("Mlimba", 23984), ("Mngeta", 32409),
                ("Mofu", 18911), ("Namwawala", 19167), ("Uchindile", 3151), ("Utengule", 20307),
            ]),
        ],
    },
    "TZ0504": {
        "name": "ULANGA", "reg_pop": 349526,
        "sources": [
            ("Ulanga", "citypopulation.de/en/tanzania/coastal/admin/0504__ulanga/", [
                ("Chirombola", 6074), ("Euga", 4646), ("Ilonga", 6216), ("Iragua", 31787),
                ("Isongo", 4474), ("Ketaketa", 10290), ("Kichangani", 10953), ("Lukande", 8075),
                ("Lupiro", 22684), ("Mahenge", 8625), ("Mawasiliano", 4076), ("Mbuga", 17086),
                ("Milola", 17981), ("Minepa", 24360), ("Msogezi", 10906), ("Mwaya", 11617),
                ("Nawenge", 6601), ("Ruaha", 9319), ("Sali", 4663), ("Uponera", 5014),
                ("Vigoi", 7448),
            ]),
            ("Malinyi", "citypopulation.de/en/tanzania/coastal/admin/0508__malinyi/", [
                ("Biro", 18301), ("Igawa", 19236), ("Itete", 21196), ("Kilosa kwa Mpepo", 15956),
                ("Malinyi", 38714), ("Mtimbira", 22533), ("Ngoheranga", 19996), ("Njiwa", 18512),
                ("Sofi", 26090), ("Usangule", 24592),
            ]),
        ],
    },
    "TZ0505": {
        "name": "MOROGORO MUNICIPAL", "reg_pop": 418556,
        "sources": [
            ("Morogoro Municipal", "citypopulation.de/en/tanzania/coastal/admin/0505__morogoro_municipal/", [
                ("Bigwa", 16623), ("Boma", 8183), ("Chamwino", 28779), ("Kauzeni", 3225),
                ("Kichangani", 24184), ("Kihonda", 35579), ("Kihonda Maghorofani", 24887),
                ("Kilakala", 21758), ("Kingo", 2131), ("Kingolwira", 15823),
                ("Kiwanja cha Ndege", 12328), ("Luhungo", 3170), ("Lukobe", 56574),
                ("Mafiga", 12666), ("Mafisa", 25171), ("Magadu", 5989), ("Mazimbu", 19499),
                ("Mbuyuni", 4893), ("Mindu", 22447), ("Mji Mkuu", 3626), ("Mji Mpya", 7032),
                ("Mkundi", 37713), ("Mlimani", 5761), ("Mwembesongo", 28328), ("Mzinga", 1588),
                ("Sabasaba", 1764), ("Sultan Area", 2382), ("Tungi", 31830),
                ("Uwanja wa Taifa", 7476),
            ]),
        ],
    },
    "TZ0506": {
        "name": "MVOMERO", "reg_pop": 376824,
        "sources": [
            ("Mvomero", "citypopulation.de/en/tanzania/coastal/admin/0506__mvomero/", [
                ("Bunduki", 6464), ("Dakawa", 34810), ("Diongoya", 31421), ("Doma", 14358),
                ("Hembeti", 11332), ("Homboza", 8355), ("Kanga", 15757), ("Kibati", 18379),
                ("Kikeo", 8226), ("Kinda", 8313), ("Kweuma", 5911), ("Langali", 4522),
                ("Luale", 7316), ("Lubungo", 8488), ("Mangae", 8795), ("Maskati", 9982),
                ("Melela", 8920), ("Mgeta", 3789), ("Mhonda", 19278), ("Mkindo", 15523),
                ("Mlali", 23384), ("Msongozi", 5155), ("Mtibwa", 38287), ("Mvomero", 25654),
                ("Mziha", 14590), ("Mzumbe", 19677), ("Nyandira", 7801), ("Pemba", 14840),
                ("Sungaji", 18450), ("Tchenzema", 3964),
            ]),
        ],
    },
    "TZ0507": {
        "name": "GAIRO", "reg_pop": 259817,
        "sources": [
            ("Gairo", "citypopulation.de/en/tanzania/coastal/admin/0507__gairo/", [
                ("Chagongwe", 14391), ("Chakwale", 9744), ("Chanjale", 13952), ("Chigela", 10065),
                ("Gairo", 12295), ("Idibo", 12684), ("Italagwe", 15979), ("Iyogwe", 14528),
                ("Kibedya", 13082), ("Leshata", 21804), ("Madege", 12765), ("Magoweko", 19823),
                ("Mandege", 9625), ("Mkalama", 12532), ("Msingisi", 10231), ("Nongwe", 12770),
                ("Rubeho", 29034), ("Ukwamani", 12901),
            ]),
        ],
    },
    "TZ0801": {
        "name": "KILWA", "reg_pop": 217978,
        "sources": [
            ("Kilwa", "citypopulation.de/en/tanzania/coastal/admin/0801__kilwa/", [
                ("Chumo", 11424), ("Kandawale", 6165), ("Kibata", 11344), ("Kikole", 6448),
                ("Kinjumbi", 11587), ("Kipatimu", 16154), ("Kiranjeranje", 16375),
                ("Kivinjesingino", 32362), ("Lihimalyao", 13767), ("Likawage", 6917),
                ("Mandawa", 17160), ("Masoko", 21519), ("Miguruwe", 14958), ("Mingumbi", 11016),
                ("Miteja", 7301), ("Mitole", 3102), ("Namayuni", 8606), ("Nanjirinji", 16979),
                ("Njinjo", 11488), ("Pande Mikoma", 15038), ("Somanga", 18549),
                ("Songosongo", 5600), ("Tingi", 13817),
            ]),
        ],
    },
    "TZ0802": {
        "name": "LINDI", "reg_pop": 189871,
        "sources": [
            ("Mtama", "citypopulation.de/en/tanzania/coastal/admin/0802__mtama/", [
                ("Chiponda", 7007), ("Kiwalala", 16446), ("Longa", 3500), ("Majengo", 8324),
                ("Mandwanga", 13035), ("Mnara", 11590), ("Mnolela", 16260), ("Mtama", 5422),
                ("Mtua", 4236), ("Mtumbya", 2234), ("Nachunyu", 9753), ("Nahukahuka", 6886),
                ("Namangwale", 7404), ("Namupa", 6274), ("Navanga", 5129), ("Nyangamara", 9440),
                ("Nyangao", 11920), ("Nyengedi", 6514), ("Pangatena", 6992), ("Sudi", 8127),
            ]),
            # NOTE: these 10 wards carry official P-codes under TZ0802 (old Lindi Rural, HDX
            # gazetteer 2018) but by the 2022 census are reported on the citypopulation.de
            # "Lindi Municipal" page (current municipal boundary expanded and annexed them).
            # Attributed here (not to TZ0806) to match the gazetteer's official parent district.
            ("Lindi Municipal (wards annexed from old Lindi Rural boundary)",
             "citypopulation.de/en/tanzania/coastal/admin/0806__lindi_municipal/", [
                ("Mipingo", 8542), ("Kitomanga", 7045), ("Mchinga", 7856),
                ("Kilolambwani", 2913), ("Kilangala", 8112), ("Rutamba", 12801),
                ("Milola", 12516), ("Kiwawa", 2778), ("Matimba", 5754), ("Nangaru", 5904),
            ]),
        ],
    },
    "TZ0803": {
        "name": "NACHINGWEA", "reg_pop": 199020,
        "sources": [
            ("Nachingwea", "citypopulation.de/en/tanzania/coastal/admin/0803__nachingwea/", [
                ("Boma", 4073), ("Chiola", 6503), ("Chiumbati Shuleni", 5458), ("Kiegei", 5874),
                ("Kilimahewa", 3828), ("Kilimarondo", 6717), ("Kipara Mnero", 6013),
                ("Kipara Mtua", 5913), ("Lionja", 6599), ("Marambo", 10621), ("Matekwe", 5864),
                ("Mbondo", 11975), ("Mchonda", 2935), ("Mitumbati", 5985), ("Mkoka", 8363),
                ("Mkotokuyana", 4020), ("Mnero Miembeni", 10200), ("Mnerongongo", 5500),
                ("Mpiruka", 7470), ("Mtua", 7544), ("Nachingwea Mjini", 8537), ("Naipanga", 5038),
                ("Naipingo", 5562), ("Namapwia", 5604), ("Namatula", 5259), ("Nambambo", 4542),
                ("Namikango", 5047), ("Nang'ondo", 7600), ("Nangowe", 4635), ("Nditi", 5777),
                ("Ndomoni", 5845), ("Ngunichile", 5132), ("Raha leo", 2873), ("Ruponda", 7050),
                ("Stesheni", 12860), ("Ugawaji", 10839),
            ]),
        ],
    },
    "TZ0804": {
        "name": "LIWALE", "reg_pop": 111517,
        "sources": [
            ("Liwale", "citypopulation.de/en/tanzania/coastal/admin/0804__liwale/", [
                ("Barikiwa", 5320), ("Kiangara", 5647), ("Kibutuka", 5137), ("Kichonda", 5647),
                ("Kimambi", 3818), ("Likongowele", 14242), ("Lilombe", 6669), ("Liwale B", 11255),
                ("Liwale Mjini", 11731), ("Makata", 6812), ("Mangirirkiti", 6302),
                ("Mbaya", 9018), ("Mihumo", 7014), ("Mirui", 6468), ("Mkutano", 2379),
                ("Mlembwe", 3935), ("Mpigamiti", 3171), ("Nangando", 13098), ("Nangano", 3711),
                ("Ngongowele", 5131),
            ]),
        ],
    },
    "TZ0805": {
        "name": "RUANGWA", "reg_pop": 143857,
        "sources": [
            ("Ruangwa", "citypopulation.de/en/tanzania/coastal/admin/0805__ruangwa/", [
                ("Chibula", 4056), ("Chienjele", 11824), ("Chinongwe", 9356), ("Chunyu", 7638),
                ("Likunja", 10977), ("Luchelegwa", 5558), ("Makanjiro", 4002), ("Malolo", 9994),
                ("Mandarawe", 4613), ("Mandawa", 9868), ("Matambarale", 7511),
                ("Mbekenyera", 16531), ("Mbwemkuru", 5052), ("Mnacho", 8261),
                ("Nachingwea", 18343), ("Nambilaje", 10687), ("Namichiga", 7129),
                ("Nandagala", 7391), ("Nanganga", 6671), ("Narung'ombe", 6151), ("Nkowe", 6403),
                ("Ruangwa", 7557),
            ]),
        ],
    },
    "TZ0806": {
        "name": "LINDI MUNICIPAL", "reg_pop": 137397,
        "sources": [
            # 10 wards excluded here (Mipingo, Kitomanga, Mchinga, Kilolambwani, Kilangala,
            # Rutamba, Milola, Kiwawa, Matimba, Nangaru): same names appear verbatim on this
            # current page, but their official P-code parent per the 2018 HDX gazetteer is
            # TZ0802 (old Lindi Rural) -- attributed there instead, see note on TZ0802.
            ("Lindi Municipal", "citypopulation.de/en/tanzania/coastal/admin/0806__lindi_municipal/", [
                ("Chikonji", 6341), ("Jamhuri", 4797), ("Kitumbikwela", 5892),
                ("Makonde", 991), ("Matopeni", 3704),
                ("Mbanja", 3672), ("Mikumbi", 1906),
                ("Mingoyo", 8377), ("Mitandi", 2463), ("Mnazimmoja", 9539),
                ("Msanjihili", 4771), ("Mtanda", 6308), ("Mvuleni", 4809), ("Mwenge", 3290),
                ("Nachingwea", 3900), ("Ndoro", 1672), ("Ng'apa", 8425),
                ("Rahaleo", 1888), ("Rasbura", 10087),
                ("Tandangongoro", 4076), ("Wailes", 2997),
            ]),
        ],
    },
    "TZ1101": {
        "name": "IRINGA", "reg_pop": 269639,
        "sources": [
            ("Iringa Rural", "citypopulation.de/en/tanzania/southernhighlands/admin/1101__iringa_rural/", [
                ("Idodi", 13053), ("Ifunda", 18420), ("Ilolo Mpya", 8869), ("Itunundu", 13639),
                ("Izazi", 8764), ("Kalenga", 11491), ("Kihanga", 7506), ("Kihorogota", 8899),
                ("Kising'a", 9576), ("Kiwere", 11296), ("Luhota", 16319), ("Lumuli", 8463),
                ("Lyamgungwe", 11161), ("Maboga", 6035), ("Maguliwa", 15205), ("Mahuninga", 4994),
                ("Malengamakali", 9394), ("Masaka", 5631), ("Mboliboli", 7567), ("Mgama", 14937),
                ("Migoli", 15139), ("Mlenge", 14055), ("Mlowa", 12896), ("Mseke", 14131),
                ("Nyang'oro", 10643), ("Nzihi", 15419), ("Ulanda", 10736), ("Wasa", 11116),
            ]),
        ],
    },
    "TZ1102": {
        "name": "MUFINDI", "reg_pop": 293544,
        "sources": [
            ("Mufindi", "citypopulation.de/en/tanzania/southernhighlands/admin/1102__mufindi/", [
                ("Idete", 5822), ("Idunda", 6984), ("Ifwagi", 10393), ("Igombavu", 8101),
                ("Igowole", 18925), ("Ihalimba", 13028), ("Ihanu", 10063), ("Ihowanza", 12466),
                ("Ikongosi", 9136), ("Ikweha", 10066), ("Itandula", 14329), ("Kasanga", 8600),
                ("Kibengu", 18542), ("Kiyowela", 4678), ("Luhunga", 10424), ("Maduma", 5517),
                ("Makungu", 17393), ("Malangali", 6331), ("Mapanda", 13073),
                ("Mbalamaziwa", 9065), ("Mdabulo", 11399), ("Mninga", 15795), ("Mpanga", 775),
                ("Mtambula", 11232), ("Mtwango", 17445), ("Nyololo", 9448), ("Sadani", 9966),
            ]),
            # NOTE: official P-code parent per 2018 HDX gazetteer is TZ1102 (old Mufindi), but
            # 2022 census reports these on citypopulation.de's "Mafinga Town" page (current
            # Mafinga Town boundary expanded and annexed them). Attributed here, not to TZ1105.
            ("Mafinga Town (wards annexed from old Mufindi boundary)",
             "citypopulation.de/en/tanzania/southernhighlands/admin/1105__mafinga_town/", [
                ("Bumilayinga", 7299), ("Isalavanu", 8402), ("Rungemba", 7323),
            ]),
        ],
    },
    "TZ1103": {
        "name": "IRINGA MUNICIPAL", "reg_pop": 201395,
        "sources": [
            ("Iringa Municipal", "citypopulation.de/en/tanzania/southernhighlands/admin/1103__iringa_municipal/", [
                ("Gangilonga", 7892), ("Igumbilo", 10209), ("Ilala", 3759), ("Isakalilo", 20859),
                ("Kihesa", 22276), ("Kitanzini", 2543), ("Kitwiru", 20365), ("Kwakilosa", 7550),
                ("Makorongoni", 7061), ("Mivinjeni", 4454), ("Mkimbizi", 15020),
                ("Mkwawa", 15320), ("Mlandege", 4235), ("Mshindo", 1563), ("Mtwivila", 12466),
                ("Mwangata", 24673), ("Nduli", 10304), ("Ruaha", 11941),
            ]),
        ],
    },
    "TZ1104": {
        "name": "KILOLO", "reg_pop": 240575,
        "sources": [
            ("Kilolo", "citypopulation.de/en/tanzania/southernhighlands/admin/1104__kilolo/", [
                ("Boma la Ng'ombe", 13153), ("Dabaga", 8497), ("Ibumu", 8264), ("Idete", 7656),
                ("Ihimbo", 11536), ("Ilula", 14666), ("Image", 10857), ("Irole", 16408),
                ("Kimala", 7737), ("Kising'a", 6236), ("Lugalo", 13970), ("Mahenge", 6835),
                ("Masisiwe", 9272), ("Mlafu", 7013), ("Mtitu", 14280), ("Ng'ang'ange", 4398),
                ("Ng'uruhe", 12523), ("Nyalumbu", 20134), ("Nyanzwa", 7877),
                ("Ruaha Mbuyuni", 19543), ("Udekwa", 8594), ("Uhambingeto", 11915),
                ("Ukumbi", 14280), ("Ukwega", 7915),
            ]),
        ],
    },
    "TZ1105": {
        "name": "MAFINGA", "reg_pop": 70282,
        "sources": [
            # Bumilayinga, Isalavanu, Rungemba excluded here -- official P-code parent is
            # TZ1102 (old Mufindi), see note there.
            ("Mafinga Town", "citypopulation.de/en/tanzania/southernhighlands/admin/1105__mafinga_town/", [
                ("Boma", 32090), ("Changarawe", 11381),
                ("Kinyanambo", 21178),
                ("Sao Hill", 3799), ("Upendo", 25074), ("Wambi", 5783),
            ]),
        ],
    },
    "TZ2301": {
        "name": "MPANDA TOWN", "reg_pop": 146868,
        "sources": [
            # Kasokola, Magamba excluded here -- official P-code parent is TZ2303 (old Mlele),
            # see note there.
            ("Mpanda Municipal", "citypopulation.de/en/tanzania/southernhighlands/admin/2301__mpanda_municipal/", [
                ("Ilembo", 24395), ("Kakese", 21466), ("Kashaulili", 5537),
                ("Kawajense", 11138), ("Kazima", 25169), ("Majengo", 5399),
                ("Makanyagio", 12660), ("Misunkumilo", 19158), ("Mpanda Hotel", 9583),
                ("Mwamkulu", 16507), ("Nsemulwa", 33444), ("Shanwe", 22014),
                ("Uwanja wa Ndege", 19334),
            ]),
        ],
    },
    "TZ2302": {
        "name": "MPANDA", "reg_pop": 295772,
        "sources": [
            ("Tanganyika", "citypopulation.de/en/tanzania/southernhighlands/admin/2302__tanganyika/", [
                ("Bulamata", 23356), ("Ikola", 21978), ("Ilangu", 15117), ("Ipwaga", 15090),
                ("Isengule", 9605), ("Kabungu", 15697), ("Kapalamsenga", 18463),
                ("Karema", 8892), ("Kasekese", 33244), ("Katuma", 35018), ("Mishamo", 13723),
                ("Mnyagala", 31342), ("Mpandandogo", 22017), ("Mwese", 22171),
                ("Sibwesa", 38044), ("Tongwe", 48079),
            ]),
        ],
    },
    "TZ2303": {
        "name": "MLELE", "reg_pop": 333634,
        "sources": [
            ("Mlele", "citypopulation.de/en/tanzania/southernhighlands/admin/2303__mlele/", [
                ("Ilela", 16387), ("Ilunde", 24757), ("Inyonga", 25187), ("Kamsisi", 18219),
                ("Nsenkwa", 9528), ("Utende", 24740),
            ]),
            # NOTE: official P-code parent per 2018 HDX gazetteer is TZ2303 (old Mlele), but
            # 2022 census reports these on citypopulation.de's "Mpanda Municipal" page (current
            # municipal boundary expanded and annexed them). Attributed here, not to TZ2301.
            ("Mpanda Municipal (wards annexed from old Mlele boundary)",
             "citypopulation.de/en/tanzania/southernhighlands/admin/2301__mpanda_municipal/", [
                ("Kasokola", 5726), ("Magamba", 14234),
            ]),
            ("Mpimbwe", "citypopulation.de/en/tanzania/southernhighlands/admin/2304__mpimbwe/", [
                ("Chamalendi", 14178), ("Ikuba", 16588), ("Kasansa", 10785), ("Kibaoni", 28769),
                ("Majimoto", 52411), ("Mamba", 42847), ("Mbede", 19248), ("Mwamapuli", 14459),
                ("Usevya", 16153),
            ]),
            ("Nsimbo", "citypopulation.de/en/tanzania/southernhighlands/admin/2305__nsimbo/", [
                ("Ibindi", 13849), ("Itenka", 30190), ("Kanoge", 17399), ("Kapalala", 7207),
                ("Katumba", 30291), ("Litapunga", 16875), ("Machimboni", 5724),
                ("Mtapenda", 9277), ("Nsimbo", 8876), ("Sitalike", 22860), ("Ugala", 24645),
                ("Urwila", 13909),
            ]),
        ],
    },
}

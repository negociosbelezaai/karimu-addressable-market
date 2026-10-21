# Enumeração exaustiva nacional de wards — Tanzânia

Data: 2026-10-04
Entregável: `deliverables/ward-enum-tza-national.csv` (4.102 wards, todo o país) + 6 arquivos por grupo de regiões.

## Contexto da recuperação
Os agentes originais (grupo 1 e grupo 3) ficaram presos quase 2h num loop de coordenação (sub-agentes tentando endereçar um "parent" que não resolvia, re-pedindo os mesmos dados repetidamente) e no caso do Rukwa, num obstáculo técnico não resolvido (a página "normal" de distrito da citypopulation.de não tem tabela de wards — precisa do link "with wards" sob um caminho com zona geográfica, ex. `/en/tanzania/southernhighlands/admin/...`, descoberto pelo grupo 6 mas não propagado pro grupo 3). Os processos foram interrompidos.

**Recuperação**: a maior parte do trabalho já estava feita e só não tinha sido consolidada — recuperei 5 arquivos de região do grupo 1 (Tanga, Mara, Njombe, Kaskazini Pemba, Songwe) de arquivos temporários intactos, e 2 scripts de matching já prontos do grupo 3 (Kagera, Manyara) que só precisavam do arquivo de gazetteer (regenerado a partir do HDX já salvo localmente). Só Rukwa (4 distritos) precisou ser refeito do zero — feito diretamente, sem agente, em poucos minutos usando o padrão de URL já conhecido.

## Resultado nacional

| | Total |
|---|---|
| Wards enumeradas | **4.102** |
| Com P-code oficial (HDX 2018) | 3.418 (83,3%) |
| Provisórias (`-PROV<n>`, redistritamento recente) | 684 (16,7%) |
| Distritos cobertos | 169 de 169 |
| Soma de população (wards com dado) | 58.017.760 |
| Sem dado de população | 18 wards |

A taxa de 16,7% de wards provisórias bate com o padrão já esperado (~15-20%) desde o piloto em Babati — confirmado agora em escala nacional, não só uma amostra.

## Achados notáveis (por grupo, resumo)
- **Divisão distrital pós-2018 é comum**: Manyoni→Itigi, Mpanda→Mpanda+Mpimbwe+Nsimbo, Kilombero→Ifakara Town+Mlimba, Sengerema→Sengerema+Buchosa, Kahama→Kahama+Ushetu, Bagamoyo→Bagamoyo+Chalinze, Mbulu→Mbulu Rural+Mbulu Town (parcialmente fora do escopo original), entre outros. Documentado caso a caso, população não duplicada nem inventada.
- **Dar es Salaam**: os 3 distritos antigos (Kinondoni/Ilala/Temeke, 7.037.577 hab. registrados) viraram 5 municípios atuais (5.383.728 no censo 2022) — divergência de ~1,65M hab. entre a projeção 2020 do HDX e o censo real 2022, não erro de transcrição.
- **Crescimento periurbano real verificado**: Mkuranga (Pwani) +105% vs. registrado, checado em duas buscas independentes antes de aceitar.
- **Zanzibar**: troca de fronteira 1-para-1 entre Kati e Kusini (ward "Pete" e "Michamvi" trocaram de distrito entre 2018 e 2022).

## Integração no `target-unit-map.csv`
As 169 linhas de distrito da Tanzânia (antes 100% `modeled_split`, estimativa aritmética) foram substituídas pelas 4.102 wards reais, cada uma reclassificada pela mesma regra populacional (≤40k=direta, >40k=modelada) já usada no resto do projeto:

| Método | Linhas (Tanzânia) |
|---|---|
| Direta (real, dado de censo) | 3.941 |
| Modelada (ward real, mas grande demais — só 143 casos, principalmente áreas urbanas) | 143 |
| Sem dado | 18 |
| **Unidades-alvo estimadas (Tanzânia)** | **4.540** (antes: 3.904, só estimativa) |

Tanzânia agora é o único dos 22 países do projeto com enumeração 100% real no nível ward — todos os outros 21 continuam no método misto (direto onde o distrito já é pequeno, modelado onde é grande).

## Novo total agregado (todos os 22 países, pós-integração)
- Unidades-alvo estimadas: **20.777** (antes 20.141)
- Unidades-alvo estimadas, só nos 17 países ativos (pós-filtro de corrupção): **15.392**

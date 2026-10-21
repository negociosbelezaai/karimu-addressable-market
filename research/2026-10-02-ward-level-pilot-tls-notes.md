# Piloto nível ward (suco) — Timor-Leste

Data: 2026-10-02
Entregável: `deliverables/ward-level-pilot-tls.csv` (10 linhas, 1 posto administrativo)

## Posto administrativo escolhido: Baguia (TL0304, município de Baucau)

Critérios de escolha:
- **Rural, fora de Dili**: Baguia fica no município de Baucau, não tem componente urbano registrado no censo (evita o viés de pegar logo de cara um posto com capital/cidade).
- **Boa chance de dado de suco**: antes de escolher, confirmei que o HDX `cod-ab-tls` (`tls_admin_boundaries.xlsx`, aba `tls_admin3`) tem os 10 sucos de Baguia com P-code oficial completo (`TL030401`–`TL030410`, todos `valid_on 2020-09-11`, nenhum sem P-code).
- **Tamanho gerenciável para o piloto**: 10 sucos (a mediana entre os 67 postos; alguns postos chegam a 18 sucos, outros têm só 2).
- Evitei de propósito os postos de Dili (Vera Cruz, Nain Feto, Metinaro, Atauro, Dom Aleixo, Cristo Rei) — o enunciado pede isso para manter o foco rural do conceito de unidade-alvo.

## Fonte de população: Main Report do Censo 2022 (não a Preliminary Results já usada no nível distrito)

Achado importante: o pacote `cod-ps-tls` (já usado no nível distrito) **não tem** nível suco. O relatório "Preliminary Results" (usado em `district-level-map.csv`) também só vai até posto administrativo (Annex I/III). A tabela de suco só existe no relatório final e completo:

**Timor-Leste Population and Housing Census 2022 — Main Report** (General Directorate of Statistics / UNFPA), Table 4.1 "Population, by municipality, administrative post, suco, and by urban/rural location, sex" (páginas 70–78 do PDF).
URL: https://timor-leste.unfpa.org/sites/default/files/pub-pdf/final-main-report_tlphc-census_2022.pdf

Confirmei a existência e estrutura exata dessa tabela via busca web (não assumi — a Preliminary Results não tem suco, só a versão final tem).

### Limitação técnica encontrada: tabela é imagem, não texto selecionável
Baixei o PDF (204 páginas) e tentei extrair o texto da Table 4.1 com `pypdf` e `pdfplumber`: ambos retornaram só o título ("Table 4.1: Continued") — a tabela inteira (9 páginas, 452 sucos do país todo) está **rasterizada como imagem**, não como texto/células reais no PDF. Não havia `tesseract`/`pdftotext` instalados localmente e não tentei instalar via rede não confirmada.

**Solução usada**: renderizei as páginas relevantes para PNG em alta resolução (`PyMuPDF`, matriz 3x) e li os valores visualmente da imagem (capacidade de visão, não OCR automatizado). A página 86 do PDF (índice 0) já continha o posto Baguia inteiro, visível e legível, com todas as colunas (Total/Male/Female × Total/Urban/Rural).

**Risco assumido e mitigação**: leitura visual de tabela é suscetível a erro de transcrição linha-a-linha. Mitigação aplicada: somei os 10 valores de suco e conferi que batem **exatamente** com o total do posto Baguia mostrado na mesma linha da mesma tabela (11.718 = 11.718), o que és uma validação cruzada forte de que não houve erro de leitura de nenhum dos 10 valores.

## Os 10 sucos de Baguia

| Suco (nome no censo) | Nome no gazetteer oficial (se diferente) | P-code | População 2022 | Rural % |
|---|---|---|---|---|
| Afaloicai | (idêntico) | TL030401 | 791 | 100% |
| Alawa Craik | Alaua Craic | TL030402 | 1.939 | 100% |
| Alawa Leten | Alaua Leten | TL030403 | 985 | 100% |
| Defawasi | Defa Uassi | TL030408 | 908 | 100% |
| Hae Coni | Haeconi | TL030404 | 1.817 | 100% |
| Larisula | Lari Sula | TL030406 | 1.190 | 100% |
| Lavateri | (idêntico) | TL030409 | 1.657 | 100% |
| Osso Huna | Ossu-Huna | TL030405 | 549 | 100% |
| Samalari | (idêntico) | TL030407 | 1.521 | 100% |
| Uacala | (idêntico) | TL030410 | 361 | 100% |

Todos os 10 sucos têm P-code oficial (`is_official_id=yes`). **Nenhum caso de ID provisório foi necessário neste posto** — diferente do padrão visto em Tanzânia (Ayalagaya) e nos próprios postos administrativos de Timor-Leste (Hatulia A/B, Loré), onde unidades novas/desmembradas não tinham P-code ainda. Isso não invalida a convenção `-PROV<n>` (ela continua documentada e já aplicada noutros níveis) — só significa que Baguia, especificamente, não passou por nenhum desmembramento recente de suco.

Nenhum suco apareceu com componente urbano no Table 4.1 (colunas Urban = 0 em todas as 10 linhas) — por isso `rural_population = population` e `rural_population_pct = 100,0` em todas as linhas, com a mesma lógica já usada no nível distrito para postos fora de Dili.

## Validação: soma dos sucos vs. população do posto já registrada

- **Soma dos 10 sucos (Main Report, Table 4.1)**: 11.718 hab.
- **Total do posto Baguia na mesma tabela (Main Report)**: 11.718 hab. → **bate exatamente** (diferença = 0).
- **Valor já registrado em `deliverables/district-level-map.csv` para Baguia (TL0304)**: 11.725 hab., fonte "Preliminary Results" Annex I do mesmo censo 2022.
- **Diferença entre as duas fontes**: 11.725 − 11.718 = **7 habitantes (0,06%)**.

**Explicação da diferença (documentada, não escondida)**: não é suco faltante nem erro de soma — a soma dos sucos bate 100% com o total do mesmo relatório (Main Report). A diferença de 7 habitantes vem de os dois níveis terem usado **publicações diferentes do mesmo censo**: o nível distrito (`district-level-map.csv`) foi montado com a "Preliminary Results" (divulgada logo após o censo); este piloto de suco usa o "Main Report" (resultados finais, divulgado depois, com pequenas revisões/correções de apuração). Esse tipo de revisão pequena entre preliminar e final é esperado e normal em censos — já foi inclusive citado como fonte de diferença parecida entre o nível província (projeções COD-PS) e o nível distrito (contagem direta) nas notas anteriores.

**Recomendação para manter consistência futura**: se o piloto suco for escalado para os outros 66 postos, convém também atualizar `district-level-map.csv` para usar o Main Report (em vez da Preliminary Results) como fonte única, evitando esse tipo de diferença residual entre níveis. Não fiz essa atualização agora — está fora do escopo deste piloto, que é só validar viabilidade do nível suco.

## Avaliação honesta: viável em escala para os outros 66 postos?

**Parcialmente viável, mas com atrito real que não existia nos níveis país/província/distrito:**

1. **A tabela-fonte é uma imagem, não dado estruturado.** Nos níveis anteriores, bastava baixar um CSV/XLSX do HDX COD-PS e processar programaticamente — zero trabalho manual por unidade. Aqui, a única fonte com nível suco é uma tabela rasterizada de 9 páginas/452 sucos no Main Report. Sem OCR confiável instalado (tentei, não havia `tesseract` disponível no ambiente), a extração depende de **leitura visual página por página** — o que fiz manualmente para 1 posto (10 sucos, 1 página) é tratável, mas rodar isso para todos os 67 postos (452 sucos, ~9 páginas) exigiria ler e transcrever as 9 páginas inteiras com cuidado, o que é um trabalho de ordem de grandeza bem maior que os níveis anteriores — não é mais "baixar e processar arquivo", é "ler imagem e transcrever à mão, com checagem cruzada por soma em cada posto".
2. **Mitigação que reduz o risco, mas não o esforço**: a soma por posto bate exatamente com o total do mesmo posto na mesma tabela, então dá pra validar cada posto individualmente à medida que for lido — o risco de erro silencioso é baixo, mas o volume de trabalho de leitura não cai.
3. **Alternativa mais escalável, se decidirem prosseguir**: instalar OCR (ex.: `tesseract` via Homebrew, ou uma biblioteca de table-extraction mais robusta) e rodar sobre as 9 páginas da Table 4.1 de uma vez, extraindo os 452 sucos do país inteiro em um único lote — isso reduziria o custo marginal por posto a quase zero, mas depende de conseguir instalar essa ferramenta no ambiente (não tentei nesta sessão, por não ter acesso de rede/homebrew confirmado) e ainda exigiria conferência manual de uma amostra para validar a qualidade do OCR antes de confiar nos 452 valores.
4. **Comparação com os níveis anteriores**: a Tanzânia (piloto ward anterior) usou `citypopulation.de`, que é HTML raspável por fetch comum (sem OCR) — mais parecido com os níveis país/distrito em termos de esforço. Timor-Leste neste nível é o primeiro caso onde a fonte primária de população não é texto estruturado.

**Conclusão**: o nível suco **é factível e os dados são confiáveis quando obtidos** (fronteira/P-code via HDX, população via censo oficial, validação por soma funciona bem), mas o **método de extração não escala linearmente** como os níveis anteriores — exige ou (a) leitura manual posto a posto (viável para um piloto, trabalhoso para 66 postos), ou (b) investimento único em OCR/table-extraction para processar as 9 páginas do país inteiro de uma vez. Recomendo, se o projeto decidir escalar, ir pela opção (b) em lote único (todos os 452 sucos de uma vez, não posto por posto) — e não repetir o processo manual 66 vezes.

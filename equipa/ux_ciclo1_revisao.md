# Revisão UX, ciclo 1 lote 1 (base: screenshots/ciclo1; comparado com ux_ciclo1.md)

Visto: todos os 1366x768 "_tela"; A, B2, C, D1, D2 em 1920x1080 "_pagina". Não li erros.txt (item 7 assenta nas notas do Programador).

## 1. Os 12 problemas anteriores
1. Impacto abaixo da dobra: PARCIAL. A_tipica_1366x768_tela: título, veredicto, frase, 3 números e gráfico cabem (gráfico termina y~650); a comparação "Sem gestão vs. com DuoWatt" começa em y~712 e os números ficam fora do ecrã.
2. Gráfico/eixo X: PARCIAL. Horas em HH:MM e serão sombreado (OK), mas a área do gráfico ainda se estende desde 0 h: os dados ocupam só ~30% da largura à direita (x 1045-1285 em 1366) e ~70% fica vazio (todas as _tela e _pagina). O serão continua uma fatia estreita.
3. C e B2 sem gestão visível: RESOLVIDO no texto ("A gestão não é necessária...", "Mesmo com gestão excede o limite durante 40 min"), por baixo do veredicto. Residual: em C a legenda mostra "Sem gestão" sem curva visível (fica escondida atrás da azul).
4. Rótulos truncados/métricas: RESOLVIDO ("Min. acima do limite", "Min. sem água quente"; A_1920_pagina, bloco "Sem gestão vs. com DuoWatt").
5. Hierarquia: PARCIAL. Veredicto > 3 números é bom; mas "4 516 t CO2/ano" (e "22 580 t" em D2) continua a ser o maior número de impacto, na zona mais frágil; o 205 kg/ano do topo e o "Cenário adverso 109 kg/ano" são dois CO2 diferentes sem explicação.
6. Contraste/tamanho: PARCIAL. Limite a preto e grosso, rotulado: resolvido. Mas legenda do gráfico e captions ("Acima do limite = risco...", "O CO2 só desce...") continuam cinzento claro e pequenos (A_1920_pagina y~660 e ~873); eixos pequenos para 5 m.
7. Avisos de consola: RESOLVIDO segundo o Programador (erros.txt "sem erros"); não verificado por mim.
8. Deploy: RESOLVIDO (ausente em todas as capturas).
9. Avisos honestos: RESOLVIDO (1 linha azul + expander "Pressupostos e limites"). Ficam no fim da página, fora do ecrã.
10. Sidebar com 9 inputs: RESOLVIDO (3 à vista + expander "Avançado"; D1/D2 mostram-no aberto por causa da captura).
11. Sinal do custo: RESOLVIDO ("Poupança de custo 33 €/ano").
12. Estado B2 vazio: PARCIAL. Agora é caixa vermelha (B2_1920_pagina y~752), mas sem ação ("Aumentar para 6,9 kVA").

## 2. Problemas novos
- ALTA | Gráfico com 70% de área vazia à esquerda (qualquer _tela, zona do gráfico): desperdiça o espaço e encolhe o serão que é o argumento. R4. Fixar o domínio X em 17:00-23:00 (o limite deve ser rule com x1/x2 dentro do domínio, não com um intervalo 0-24 que alarga a escala).
- MÉDIA | Etiqueta "Limite 3,45 kW" colide com a linha tracejada vermelha e o sombreado do serão (A, B, B2, D1 1366 tela, x~1045-1150, y~465-490). R4. Pô-la à esquerda do serão (início do eixo).
- MÉDIA | D2: veredicto "Reserva de água insuficiente" (âmbar) com a frase "A gestão não é necessária: a casa aguenta sem ela" e nenhuma menção às 8 min sem água quente (D2_1366_tela, D2_1920_pagina). Parece contraditório. R3, R7. Frase deve citar o motivo do aviso.
- MÉDIA | A frase de margem "limite menos base menos indução" é jargão e dá "-150 W" (B2) sem leitura; em A quebra para 2 linhas ("1 372 / W."). R3. "Folga ao serão: 1 372 W" / "Faltam 150 W".
- BAIXA | Legenda do gráfico fraca e a ~14 px; a diferença entre as duas curvas deve ser rotulada diretamente ("Sem gestão" a vermelho junto ao pico). R4.
- BAIXA | Campos da sidebar (kVA, consumo) com texto minúsculo (~11 px, A_1366_tela). R6.

## 3. Pontuações (critérios como usados em ux_ciclo1.md: R3 clareza da mensagem/fluxo, R4 gráfico/dados legíveis, R7 impacto e honestidade)
- R3: 3,5/5. Para 4-5: texto de margem sem jargão; D2 explicar o aviso; B2 com ação concreta; impacto principal à vista sem scroll.
- R4: 3/5. Para 4-5: eixo X 17-23 h sem espaço vazio (serão ocupa ~1/3), etiqueta do limite fora do pico, legenda forte/rotulagem direta, eixos >= 16 px.
- R7: 3/5. Para 4-5: números de impacto (205 kg/casa, poupança) acima da dobra ou ao lado do veredicto; reduzir o peso de "4 516 t" e reconciliar 205 vs 109 kg; aviso de "valores por validar" visível sem scroll.

## 4. 1366x768 sem scroll: o fluxo percebe-se?
Parcialmente. Veredicto (cor + texto), "como a gestão resolve" (frase + pico sem gestão 4 078 W vs com DuoWatt 2 278 W + gráfico com a curva tracejada a ficar abaixo do limite) e CO2 por casa percebem-se sem scroll em A, B, B2, C, D1, D2. O impacto detalhado (minutos acima do limite 25 -> 0, água quente, custo) fica abaixo da dobra; a sidebar de 300 px continua aberta.

Ficheiros: equipa/ux_ciclo1_revisao.md; imagens em screenshots/ciclo1/.

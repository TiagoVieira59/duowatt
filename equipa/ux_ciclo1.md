# Auditoria UX, ciclo 1 (base: screenshots/ciclo0, app.py)

Nota: vi A (1366 tela+pagina), B/C/B2 (1920 pagina). D1/D2 e os restantes 1366 não foram abertos um a um; as conclusões assentam na estrutura comum (app.py) e nos cenários vistos.

## Validação dos achados do júri anterior
- Letra pequena e cinzenta: CONFIRMADO. Legendas, eixos, caption e rótulos das métricas ~12-13 px cinzento claro; ilegível a 5 m.
- Linha do limite pálida: CONFIRMADO. Azul-claro de 1-2 px (A_tipica_1366x768_tela, y~465; B_..._1920x1080_pagina, y~343 em px do viewer), mais fraca do que a curva e a legenda.
- Rótulos truncados: CONFIRMADO em 1366 ("Episódios acima da...", "Minutos acima do lim...", A_tipica_1366x768_pagina) e ainda em 1920 ("Episódios acima da potência contra...").
- Botão Deploy: CONFIRMADO (canto superior direito, todas as capturas).
- Avisos minúsculos no fundo: CONFIRMADO, mas o conteúdo (honestidade) deve ficar, só mais curto.
- Impacto fora do ecrã em 1366x768: CONFIRMADO. Na tela 1366x768 só se vê título, veredicto e gráfico; as métricas começam ~y 1050 (página).
- Serão (19:30-21:00) ocupa pouco: CONFIRMADO. Eixo 0-24 h; o pico ocupa ~8% da largura.
- C e B2 sem gestão visível: CONFIRMADO e é pior do que parece (ver P3).

## Problemas (prioridade | evidência | rubrica | sugestão)

1. ALTA | Impacto e comparação abaixo da dobra em 1366x768 (A_tipica_1366x768_tela vs _pagina; sidebar ocupa 300 px e título quebra em 2 linhas) | R3, R7 | Título numa linha curta; esconder sidebar por defeito (ou `initial_sidebar_state="collapsed"` e inputs em expander); um único bloco "resultado" acima da dobra (ver Layout).
2. ALTA | Gráfico: o interessante (serão) é uma fatia pequena; eixo X com decimais "7.0, 8.0... 24.0" em 1920 (C_..._pagina, zona inferior do gráfico), "24.0" cortado à direita; em 1366 "0..24" | R4, R6 | Restringir o eixo a 17:00-23:00 (ou 18-22) e formatar horas "19:30". Usar altair com `scale(domain=[..])` e `axis(format)`; sombrear 19:30-20:10.
3. ALTA | Cenários C e B2: gestão invisível. Em C (C_6_9kva_1920x1080_pagina) só há uma curva azul e uma linha de limite no topo, as vermelha/azul coincidem (pico 4 100 W bem abaixo de 6 900 W), legenda mostra "Sem gestão" sem curva. Em B2 (B2_..._pagina) as duas curvas coincidem acima do limite: a gestão não resolve e o gráfico não o diz | R3, R4 | Por cima do gráfico, uma frase de uma linha por cenário ("A gestão não é necessária: folga de 2,8 kW" / "Mesmo com gestão passa 40 min do limite"). Desenhar "Com DuoWatt" por cima, mais grosso, e "Sem gestão" tracejado atrás, para se verem as duas mesmo coincidentes.
4. ALTA | Rótulos truncados e 6 métricas pequenas em 2 colunas x 3 (A_tipica_1366x768_pagina, "Sem gestão vs. com DuoWatt") | R4, R6 | Encurtar: "Disparos", "Min. acima do limite", "Min. sem água quente". Mostrar só duas colunas (Sem / Com) com 2 números grandes cada (min. acima do limite; min. sem água quente); "episódios" corta-se ou funde-se.
5. MÉDIA | Hierarquia: o veredicto é grande (bom), mas competem com ele o título longo e o gráfico; os números de impacto (205 kg/ano) têm o mesmo peso que as métricas técnicas; a frase "4 516 t CO2/ano" é a maior, mas é o cenário mais frágil | R3, R6 | Ordem: veredicto, gráfico, 3 números-chave (disparos sem/com, água quente, CO2 por casa). O nacional passa a linha de texto secundária.
6. MÉDIA | Contraste/tamanho: captions e eixos cinza claro (<4,5:1 em texto pequeno), legenda do gráfico 12 px | R6 | CSS via `st.markdown("<style>")`: caption >= 16 px cor #444; eixos e legenda 14-16 px; `strokeWidth` 3 no Limite, cor forte (preto ou laranja) tracejada, com etiqueta direta "Limite 3,45 kW" em vez de legenda.
7. MÉDIA | Avisos de consola "Infinite extent for field 'Hora do dia' / 'value -- streamlit-generated'" (erros.txt, todos os cenários, repetidos até 3x por cenário) | R6 | Origem: st.line_chart/Vega-Lite a ser avaliado com dados vazios no primeiro render. Inofensivo, mas desaparece com `st.altair_chart` com domínio explícito (ponto 2) e dados longos (melt) em vez de wide.
8. MÉDIA | Botão "Deploy" e menu "⋮" visíveis (canto superior direito) | R6 | `.streamlit/config.toml`: `[client] toolbarMode="minimal"` ou `[ui] hideTopBar=true`; ou CSS a esconder `[data-testid=stToolbar]`.
9. MÉDIA | Avisos honestos: um parágrafo azul de 4 linhas, 12-13 px, no fundo (A_..._1920_pagina, y~970-1010) | R3, R7 | Cortar para 2 linhas legíveis e dar-lhe sítio fixo (rodapé); passar o detalhe para `st.expander("Pressupostos")`. Manter "valores por validar" visível.
10. BAIXA | Sidebar com 9 inputs; em demo só 2-3 mexem (kVA, indução, consumo). Slider "Casas a GPL..." e "Fator CO2" são ruído na demo | R3 | Deixar kVA, consumo, indução à vista; resto num expander "Avançado".
11. BAIXA | Texto de passagem de unidades: "Variação de custo 33 €/ano" sem sinal/sentido (poupa ou paga?) e "Cenário adverso" sem contexto (A_..._pagina) | R4 | "Custo extra: +33 €/ano" (conferir sinal com o Auditor de valores; não alterar fórmulas).
12. BAIXA | Estados quase vazios: B2 mostra só um `st.info` no lugar do impacto, sem hierarquia (B2_..._pagina, y~800) | R3 | Aviso a vermelho/âmbar com ação ("Aumentar para 6,9 kVA") em vez de info azul.

## Layout sugerido (acima da dobra, 1366x768, ~620 px úteis)
1. Título numa linha (<= 40 caracteres, ex. "DuoWatt: gás para elétrico, sem disparar") + veredicto (1 linha, grande).
2. Gráfico 17:00-23:00, altura ~320 px, limite grosso rotulado, serão sombreado.
3. Faixa de 3 números grandes a toda a largura: "Disparos: 1 -> 0", "Água quente: 0 min -> 0 min", "CO2 evitado: 205 kg/ano por casa".
Abaixo da dobra: tabela detalhada, cenário nacional, avisos. Sidebar recolhida por defeito (abre-se durante a demo para trocar B/C).

## Cortar
Botão Deploy/menu; legenda do gráfico (rotular direto); subtítulo "Potência ao longo do dia (W)" (fundir no gráfico); 4.º métrico "episódios" (redundante com minutos); caption do disjuntor (passar para tooltip/expander); sliders CO2 e adoção da vista principal.

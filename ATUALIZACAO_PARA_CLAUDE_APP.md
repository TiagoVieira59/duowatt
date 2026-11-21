# Atualização para o Claude da aplicação (colar numa conversa)

Atualização (21 nov 2026, ~01:15). O prompt autónomo que preparaste (PROMPT_Equipa_Autonoma_DuoWatt.md) foi executado pelo Claude Code, e esta mensagem resume o que mudou desde então. Responde-me em PT-PT.

1) CRITÉRIOS OFICIAIS (substituem a rubrica R1–R7): 1 provas do utilizador 20 %, 2 impacto mensurável 20 %, 3 solução e demonstração 15 %, 4 viabilidade técnica/económica/implementação 15 %, 5 originalidade e diferenciação 10 % (sábado 21 nov, 17:30); 6 pitch e perguntas 20 % (25 nov). Escala 1–5; só contam como prova dados REAIS recolhidos por nós. Regra: nunca inventar dados de utilizadores.

2) O QUE FOI FEITO (7 ciclos, tudo no git, branch main, tag "final"):
- App Streamlit com 4 separadores: Diagnóstico (veredicto: aguenta / aguenta com gestão / reserva de água insuficiente / precisa de mais potência; gráfico 17h–23h com e sem gestão; CO₂ e custo), Viabilidade (custo do DuoWatt ~200–280 € instalado, ou ~350–680 € com quadro novo, contra subir a potência 3,45→6,9 kVA, que custa 64–78 €/ano; equilíbrio 2,6–4,4 anos), Diferenciação (o que já existe: Legrand, Schneider, Shelly, SMA, simuladores ERSE/EDP; o que não afirmamos) e Provas do utilizador (só dados da Bosch, rotulados como secundários, e "Ainda sem dados" para a nossa equipa).
- Tabela de pressupostos com valor, fonte e classificação (confirmado/provável/derivado/hipótese).
- Documentos: INQUERITO.md (10 perguntas para Google Forms), ENTREVISTAS.md (3 guiões de 5 min), ferramentas/criar_formulario.gs (cria o Forms; NÃO testado), ferramentas/analisar_inquerito.py (CSV → números e gráficos que a app mostra), VIABILIDADE.md, DIFERENCIACAO.md, DEMO_GUIAO.md, PLANO_RECOLHA_PROVAS.md, RELATORIO_FINAL.md, PROGRESSO.md.
- 43 testes a passar (4 falhas esperadas, justificadas). Júri simulado (um modelo, só um guia): nota ponderada final 2,9/5 (C1=1, C2=3, C3=4, C4=4, C5=3).

3) NÚMEROS PRINCIPAIS (valores por omissão, derivados): casa de 3,45 kVA, 200 kWh/mês: sem gestão 25 min acima do limite (pico 4 078 W), com DuoWatt 0 min e 0 min sem água quente; 205 kg CO₂/casa/ano evitados pela eletrificação (109 kg no cenário adverso de 167 g/kWh); poupança de combustível ~33 €/ano; subir a potência → ~−30 €/ano; com DuoWatt ~+9 €/ano. A mensagem honesta é "descarboniza sem custar mais". O impacto atribuível ao DuoWatt é no máximo ~44 % das casas (proxy: contratos ≤3,45 kVA).

4) REGRAS DE HONESTIDADE: nunca "somos os primeiros", "sem eletricista", "sem obras", nem que os Tronic se ligam a um gestor de energia (nada encontrado). A gestão antidisparo já existe (Legrand, Schneider). Não encontrámos o diagnóstico gás→elétrico no momento da avaria, mas "não encontrado" não prova que não exista. 67 % das casas têm esquentador e só 17 % termoacumulador (INE 2020).

5) O QUE FALTA (só pessoas): recolher ≥30 respostas e 3 entrevistas (critério 1, +~0,5 na nota); validar com Mecânica (indução 1,8/3 kW e base ~600 W, sem fonte) e Contabilidade (custos de retalho, preço da garrafa 37 €); validar com um eletricista; confirmar o formato da entrega; preencher os campos [entre colchetes] do DEMO_GUIAO.md com dados reais.

6) COMO CORRER: cd "/home/tiago/Documentos/HACKATON SHIFTE" && .venv/bin/streamlit run app.py (localhost:8501). Retomar: "Lê PROGRESSO.md e continua". Entrega às 17:30; só correções de erros a partir das 14:00.

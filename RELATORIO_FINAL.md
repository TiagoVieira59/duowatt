# Relatório final da equipa autónoma (DuoWatt)

Estado: 21 nov 2026, de madrugada. Entrega às 17:30. Este relatório descreve o que foi feito, o que a equipa tem de validar e o que ainda depende de pessoas.

## 1. Avaliação (Júri simulado, critérios oficiais)
| Critério | Peso | Nota (1–5) |
|---|---|---|
| 1 Clareza do problema e provas do utilizador | 20 % | **1** |
| 2 Impacto mensurável | 20 % | 3 |
| 3 Solução e demonstração | 15 % | 3,5 |
| 4 Viabilidade técnica, económica e de implementação | 15 % | 4 |
| 5 Originalidade e diferenciação | 10 % | 3 |
| **Nota ponderada (sábado)** | | **2,78 / 5** |

O Júri é um modelo que só viu o enunciado, os screenshots e os documentos; é um guia, não uma previsão. Antes dos critérios oficiais, a rubrica interna dava ao ciclo 0 (linha de base) 3, 2, 3, 2, 3, 4, 3 em R1–R7; **não é comparável** com esta tabela (outros critérios e escala).
**O que mais subiria a nota:** recolha real de dados de utilizadores (inquérito + 3 entrevistas: cerca de +0,5 na nota ponderada), validação por um eletricista e pela Bosch (controlo externo nos Tronic), e entrevistar um instalador. Ver `PLANO_RECOLHA_PROVAS.md`.

## 2. O que mudou e porquê
- **Ciclo 0:** git, papéis dos agentes, captura automática de screenshots (Playwright no `.venv`), linha de base.
- **Ciclo 1:** layout legível em projetor a 1366×768 (veredicto, frase da potência e gráfico acima da dobra), gráfico do serão (17–23 h) com o limite rotulado, avisos honestos compactos, atribuição do impacto (o CO₂ vem da eletrificação; o DuoWatt desbloqueia a troca), extremos coerentes, higiene do modelo. Encontrou-se (e corrigiu-se) um bug do eixo X do gráfico que um agente tinha dado como resolvido.
- **Ciclo 2:** a conta do CO₂ explícita (gás 399 → elétrico 194 → evitado 205 kg), frase "placa + termoacumulador pedem X W", benefício atribuível ao DuoWatt (64–78 €/ano de termo de potência evitado) e limite superior do CO₂ atribuível (44 %, proxy).
- **Ciclo 3:** critérios oficiais, inquérito e guiões de entrevista, analisador do CSV do Forms (com testes sintéticos marcados), separador "Provas do utilizador" (dados da Bosch rotulados como secundários; "Ainda sem dados" para a equipa).
- **Ciclo 4:** `VIABILIDADE.md` e separador (custos com fontes, equilíbrio, efeito na fatura, próximos passos), `DIFERENCIACAO.md` e separador, tabela de pressupostos com fonte e classificação.
- **Ciclo 5:** polimento (legenda do gráfico, decimais com vírgula, citação legível), `DEMO_GUIAO.md`, `PLANO_RECOLHA_PROVAS.md` e script `criar_formulario.gs`.
- **Ciclo 6:** a app lê `dados/entrevistas.json` para mostrar as entrevistas da equipa sem mexer em código.

## 3. Decisões e valores que o Tiago/a equipa tem de validar
(Detalhe e fontes em `DECISOES.md`, `Parametros_Verificados.md` e `PESQUISA.md`.)
| Valor | Estado | Quem valida |
|---|---|---|
| Preço marginal da eletricidade 0,21 €/kWh (IVA 23 % acima de 200 kWh/mês) | derivado de tarifas ERSE 2026 | Contabilidade |
| Preço da garrafa de 13 kg: 37 € (cenário alto 42–43,5 €); a poupança varia ~10 €/ano por cada euro | último preço anunciado (ERSE, out 2026) | Contabilidade |
| CO₂ da eletricidade 107 g/kWh (APA 2023, média anual, não marginal); cenário adverso 167 g/kWh | confirmado / provável | Ciência Política, Mecânica |
| Eficiências (esquentador 0,82; elétrico 0,85) | fichas de fabricantes / derivado | Mecânica |
| Indução 1,8 kW (moderado) e 3 kW (intenso); base da casa = consumo ÷ 720 h | **pressupostos da equipa, sem fonte** | Mecânica (com 600 W de base o veredicto a 3,45 kVA com indução forte passa a "precisa de mais potência") |
| Termo de potência: 0,1917 €/dia (3,45 kVA) e 0,3659 €/dia (6,9 kVA) → 64 €/ano sem IVA | confirmado (Diretiva ERSE 4/2026); a coluna exata do PDF convém rever; IVA aplicável por verificar | Contabilidade |
| 44 % das casas ≤3,45 kVA (limite superior do CO₂ atribuível) | **proxy**: todos os contratos BTN (E-REDES, dados de 2023), não só domésticos nem só a GPL | Ciência Política |
| 67 % esquentador / 17 % termoacumulador | confirmado (INE, ICESD 2020) | |
| Custos do DuoWatt: material 172–222 €, mão de obra 30–60 €, quadro novo 150–400 € (total 200–280 € ou ~350–680 €) | preços de retalho e de plataformas, **não cotações** | Contabilidade, eletricista |
| Equilíbrio 2,6–4,4 anos (quadro adequado) ou 4,5–10,7 anos (quadro novo) | derivado | Contabilidade |
| Efeito na fatura: +33 €/ano trocando o gás; ~−30 €/ano subindo a potência; ~+9 €/ano com o DuoWatt amortizado a 10 anos | derivado; não inclui o aparelho novo | Contabilidade |

## 4. As 5 objeções mais prováveis do júri (Júri simulado) e respostas honestas
1. **"Sem provas próprias, o problema é assumido."** Verdade neste momento: só há os dados secundários da Bosch (68 %, 85 %, 60 %…). A equipa tem o plano pronto para recolher (inquérito + 3 entrevistas) e a app mostra os números assim que existirem. Se houver pouca amostra, dizer o n e que é indicativo.
2. **"Tudo é simulado; não há medições nem ensaio."** Correto: é um simulador com pressupostos explícitos. O primeiro passo proposto é um ensaio em bancada e a validação com um eletricista habilitado.
3. **"A gestão antidisparo já existe (Legrand, Schneider). Qual é a novidade?"** Não somos os primeiros a cortar cargas. A hipótese é o diagnóstico gás → elétrico no momento da avaria, ligado à venda do termoacumulador; não o encontrámos em nenhuma fonte, mas não encontrado não prova que não exista (a testar com instaladores).
4. **"67 % têm esquentador e o espaço não se resolve: só ataca 1 de 4 bloqueios."** É verdade. O DuoWatt resolve a potência; o espaço e a falta de instaladores ficam para outras peças (por exemplo, o trabalho da Mecânica).
5. **"Instalação de 200–680 € para ~8–9 €/ano de benefício; e o ganho da Bosch é incerto."** O argumento económico é evitar subir a potência (64–78 €/ano) e a mensagem é "descarboniza sem custar mais", não "poupa dinheiro". O benefício para a Bosch são hipóteses por validar com a Bosch.

## 5. Riscos e limitações conhecidos
- Segurança elétrica: a instalação exige um eletricista habilitado; normas, proteções e anti-legionela por validar.
- O disjuntor real tolera sobrecargas curtas, por isso "acima do limite" é risco de disparo, não certeza; kVA tratado como kW (fator de potência 1).
- A base da casa é plana (consumo mensal ÷ 720 h) e subestima o pico do serão.
- Os Tronic não têm controlo externo documentado: o corte seria por contactor.
- O CO₂ só desce se o gás for mesmo substituído; o DuoWatt tira um bloqueio mas a troca pode acontecer sem ele.
- O script `criar_formulario.gs` não foi testado (sem acesso a conta Google); se falhar, criar o Forms à mão com `INQUERITO.md`.
- Valores de custo de lojas e plataformas: nenhuma fonte indica a data de publicação.
- Os agentes verificaram a app por Playwright e por testes; um jurado humano pode ver coisas que escaparam (legibilidade no projetor real).

## 6. Como correr
- App: `cd "/home/tiago/Documentos/HACKATON SHIFTE" && .venv/bin/streamlit run app.py` (abre em http://localhost:8501).
- Testes: `python3 -I -m pytest -q test_impacto.py test_duowatt.py test_modelo_ciclo1.py ferramentas/teste_inquerito -p no:cacheprovider`.
- Screenshots: `.venv/bin/python ferramentas/capturar.py <nome>` (escreve em `screenshots/<nome>/`).
- Dados reais: `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv` (escreve em `dados/`); entrevistas: copiar `ferramentas/modelo_entrevistas.json` para `dados/entrevistas.json` e preencher.
- Retomar o trabalho: "Lê `PROGRESSO.md` e continua".

## 7. O que tem de acontecer antes das 17:30 (só a equipa pode)
Ver `PLANO_RECOLHA_PROVAS.md` e a checklist no fim de `DEMO_GUIAO.md`: criar e partilhar o inquérito, fazer as 3 entrevistas, confirmar valores com a Mecânica e a Contabilidade, e confirmar o formato da entrega (`PERGUNTAS.md`).

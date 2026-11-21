# Júri, ciclo 4 (screenshots ciclo4a)

Nota ponderada = (1x20 + 3x20 + 3,5x15 + 4x15 + 3x10) / 80 = **2,78 / 5**

| # | Critério | Nota | Evidência | O que subiria a nota |
|---|---|---|---|---|
| 1 | Problema e provas do utilizador (20 %) | **1** | Separador "Provas do utilizador" (A_tipica_*_provas.png): os 5 números são do enunciado (dados secundários) e "Provas da nossa equipa" diz "Ainda sem dados". INQUERITO.md e ENTREVISTAS.md são só guiões, sem uma resposta ou citação real. | Inquérito com 15-30 respostas reais e 3 entrevistas (A, B, C) reais, mostradas na app. Salta para 3-4. |
| 2 | Impacto mensurável (20 %) | **3** | Métricas concretas (pico 4 078 -> 2 278 W; 25 -> 0 min acima do limite; 205 kg CO2/ano; 33 EUR/ano), com pressupostos abertos. Mas é tudo simulado num cenário de demonstração, o CO2 vem da eletrificação e não do DuoWatt, e o "~44 % das casas" é um proxy. B2 mostra "n/d". | Ligar a métrica ao desafio com dados reais (potência contratada e equipamentos das casas inquiridas) e medir minutos acima do limite num ensaio. |
| 3 | Solução e demonstração (15 %) | **3,5** | Protótipo navegável e limpo, 4 separadores, 4 veredictos coerentes, gráfico claro, sem erros de consola (erros.txt). Perde pontos porque não responde a provas recolhidas (não há) e a demo assenta num único dia simulado. | Mostrar na app a resposta a uma objeção real (inquérito) e um caso real. |
| 4 | Viabilidade (15 %) | **4** | VIABILIDADE.md: lista de custos com fontes e classificação (confirmado / provável / hipótese), instalação 200-280 EUR, comparação a 10 anos, riscos honestos e 6 passos seguintes. Fraquezas: nada validado por eletricista ou pela Bosch; não se sabe se os Tronic aceitam controlo externo; 67 % das casas têm esquentador, não termoacumulador. | Entrevista real a um eletricista (perfil C) e resposta da Bosch sobre controlo externo. |
| 5 | Originalidade (10 %) | **3** | DIFERENCIACAO.md admite que gestão de cargas existe (Legrand, Schneider) e que a combinação "diagnóstico + gestão + canal Bosch" não está verificada. É uma adaptação de soluções conhecidas. | Testar o simulador da ERSE e o Heatpump Advisor e entrevistar um instalador. |

## 5 objeções mais prováveis (da mais perigosa)
1. Não têm nenhuma prova própria: inquérito e entrevistas por fazer, os números são nossos (Bosch). O problema é assumido.
2. Tudo é simulação com pressupostos da equipa; nenhum ensaio, nenhuma medição real de potência ou de água quente.
3. A gestão de cargas anti-disparo já existe no mercado; o que é novo, e é verdade?
4. A maioria das casas tem esquentador, não termoacumulador, e o problema do espaço (60 %) não é resolvido; o DuoWatt só ataca um dos quatro bloqueios.
5. Segurança e retorno: cortar o termoacumulador automaticamente exige eletricista; o custo (200-680 EUR) pode superar o ganho da família (a app admite que poupa ~8 EUR/ano, não mais) e a Bosch não ganha com o acessório.

## O que mais subiria a nota, por ordem
1. Recolha real (inquérito + 3 entrevistas) mostrada no separador Provas (critério 1: +2 a +3 pontos, ou +0,5 na nota ponderada).
2. Validação do eletricista e da Bosch (critério 4, e reforça o 3).
3. Ligar os números do critério 2 a dados reais recolhidos.
4. Verificar as ferramentas concorrentes (critério 5).
5. Cenário da demo com um caso real.

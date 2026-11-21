# Avaliação do Júri, ciclo0 (linha de base)

Materiais usados: enunciado Bosch, screenshots de ciclo0 (A, B, B2, C, D1, D2 em 1920x1080 "pagina"; A em 1366x768 "tela"), erros.txt. Sem guião de demo. Só avalio o que vejo.

## Notas (0 a 5)

| Critério | Nota | Justificação |
|---|---|---|
| R1 Impacto de CO2 mensurável | 3 | Há números concretos por casa (205 kg/ano, cenário adverso 109 kg/ano com 167 g/kWh) e extrapolação (1% de 2,2 M = 4 516 t, coerente com 22 000 x 205 kg). Mas o próprio ecrã admite que a troca "pode acontecer sem o DuoWatt", logo o CO2 não é atribuível ao produto. O 1% é arbitrário e 4 516 t é ~0,5% das 870 kt do enunciado, sem dizer. |
| R2 Viabilidade real | 2 | Não há custo do equipamento ("não inclui custo do equipamento"), nem como se instala, nem quem instala (bottleneck de 70 000 instaladores), nem espaço (60% com pouco espaço), nem o momento de compra urgente (85% recompra gás). Só ataca o bottleneck da potência contratada, e assume que a casa já tem termoacumulador. Aviso honesto de que já existe gestão de cargas no mercado (Schneider, ABB) enfraquece a novidade sem a substituir por um diferencial. |
| R3 Clareza da demo | 3 | Ordem de leitura boa de cima para baixo: título, veredicto, gráfico, sem gestão vs. com DuoWatt, impacto. Falta o "problema" (porque dispara o quadro) e o fecho da narrativa. Em 1366x768 só se vê título, veredicto e parte do gráfico; o impacto de CO2 fica fora do ecrã e exige scroll. A comparação só é visível nos cenários A e B; em C e B2 o ponto de gestão não aparece. |
| R4 UI/UX e projetor | 2 | Banner de veredicto grande e com cor (bom). Mas: eixos, legenda e rótulos de KPI em letra pequena e cinzenta, linha do limite azul-clara quase invisível, rótulos truncados ("Episódios acima da potência contra..."), eixo X com "0.0, 1.0" em decimais, sidebar Streamlit por defeito com "Deploy" visível, avisos honestos em letra minúscula no fundo. Muito espaço vazio abaixo. Sem destaque visual para "pausa do termoacumulador" no gráfico. |
| R5 Correção técnica (pelo que se vê) | 3 | Consistente: 25 min acima do limite batem com o pico vermelho (19:45 a 20:10); B2 mostra honestamente que a gestão não resolve (40 min em ambas as colunas) e esconde o impacto até aumentar potência. Dúvidas: em B o pico "com DuoWatt" fica a ~3 300 W, a ~150 W do limite de 3 450 (sem margem, sem comentário); em D1 a carga fica colada exatamente no limite de 2 300 W; "Variação de custo 33 €/ano" não diz se é poupança ou aumento; verdicto igual para casos com e sem necessidade de gestão sem explicar o que foi pausado e quando. |
| R6 Honestidade | 4 | Bloco "Avisos honestos" explícito (simulação ilustrativa, valores por validar, cenário de demonstração, sem custo de equipamento, concorrência referida), cenário adverso de CO2 e nota "fator é média anual, não marginal". Desconta: está pequeno e no fundo; o título do cenário fixo (indução 19:30, duche 19:45) é montado para dar o resultado e só aparece na letra miúda. |
| R7 Robustez | 3 | Sem crashes em nenhum extremo; B2 trata bem "precisa de mais potência". Falhas: D1 (0 garrafas) mostra verdicto positivo e "0 kg, 0 €, 0 t" sem explicar que não há gás a substituir; D2 (10,35 kVA, 8 pessoas, 50 garrafas) mostra 8 min sem água quente com banner âmbar, mas ainda anuncia 1 026 kg e 22 580 t evitados, o que é contraditório; 50 garrafas/ano não é plausível e infla o impacto. Consola: avisos "Infinite extent" do Vega em todos os cenários (inofensivos, mas indicam gráfico renderizado vazio num primeiro instante). |

## 5 objeções mais prováveis (da mais perigosa para a menos)

1. "Qual é o impacto de CO2 que é vosso?" O ecrã diz que a troca pode acontecer sem o DuoWatt; o CO2 mostrado é o da eletrificação, não o do produto. O contributo real (casas que só trocam por causa da gestão) não está estimado. O 1% e as 4 516 t são pressupostos soltos.
2. "Quanto custa e quem instala?" Sem preço do hardware, sem modelo de negócio, sem instalação (escassez de instaladores, 23% de visitas falhadas) e sem integração com o esquentador/termoacumulador existente. Sem isto, R2 não passa.
3. "Isto já existe." O próprio aviso cita Schneider e ABB; falta dizer o que o DuoWatt faz de diferente (por exemplo, integração Bosch/Tronic, termoacumulador compacto, zero obras).
4. "E os outros bloqueios do enunciado?" Espaço (40-60 cm, apartamentos), compra urgente (cold shower, 85% recompram gás) e sensibilização não aparecem. A solução assume casa com termoacumulador de 100 L, o oposto da casa que tem esquentador a gás.
5. "O cenário está feito à medida." Um único perfil fixo (duche às 19:45 a seguir à indução), margem de 150 W em B, carga colada ao limite em D1, e D2/D1 com resultados incoerentes (impacto positivo com falta de água; 0 kg com verdicto verde). A tolerância do disjuntor real é só uma nota minúscula.

## O que mais subiria a nota (por ordem)

1. Separar claramente o impacto atribuível ao DuoWatt (casas desbloqueadas pela gestão) do impacto geral da eletrificação, com a fonte do 1% e comparação com as 870 kt. Sobe R1 e R6.
2. Mostrar custo, instalação e encaixe no produto Bosch (retrofit sem obras, preço, quem instala, o que acontece na compra urgente). Sobe R2, a nota mais fraca e a que mais pesa em "viabilidade real".
3. Reorganizar o ecrã para projetor: texto e eixos maiores, linha do limite forte, rótulos sem truncar, impacto visível sem scroll em 1366x768, anotação direta no gráfico ("termoacumulador pausado 19:45 a 20:10"), esconder chrome do Streamlit, corrigir "Veredicto" para "Veredito" (PT-PT). Sobe R4 e R3.
4. Corrigir incoerências nos extremos: D1 sem gás deve dizer "sem gás para substituir"; D2 não deve celebrar CO2 com água quente em falta; limitar garrafas/ano a valores plausíveis; esclarecer o sinal de "Variação de custo". Sobe R7 e R5.
5. Guião de demo com ordem fixa: problema (quadro dispara) em A sem gestão, depois com gestão, depois veredicto B2 ("precisa de mais potência", honesto), depois impacto. Subir os avisos honestos para visíveis. Sobe R3 e R6.

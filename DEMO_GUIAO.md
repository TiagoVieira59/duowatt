# Guião da demo (2 a 3 minutos, PT-PT)

Estado: rascunho para a equipa, 21 nov 2026. Os números são os valores por omissão da app (derivados e por validar; ver o separador "Diagnóstico" → "Pressupostos"). **Campos entre [colchetes] são para preencher com dados reais da equipa; nunca inventar.**

## Antes de começar (2 minutos)
- Abrir a app: `cd "/home/tiago/Documentos/HACKATON SHIFTE" && .venv/bin/streamlit run app.py` e ligar o ecrã ao projetor (testar em 1366×768).
- Se já houver inquérito/entrevistas: correr `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv` e reiniciar a app (o separador "Provas do utilizador" passa a mostrar os dados da equipa).
- A app abre no **assistente**. Percurso da demo: responder com os valores pré-selecionados (3,45 kVA, 200 kWh, 3 pessoas, uso normal, 12 garrafas) → resultado → botão do relatório → «Modo detalhado» (a barra lateral já vem com as respostas).

## Roteiro
| Tempo | O que se diz | O que se clica |
|---|---|---|
| 0:00–0:25 **O problema** | "Em 2,2 milhões de casas portuguesas ainda se usa gás de garrafa. Segundo a Bosch, 85 % das substituições urgentes voltam a comprar gás. Falámos com [N] pessoas: [resultado-chave do inquérito] e [citação literal de uma entrevista]." *(se ainda não houver dados reais, dizer apenas os dados da Bosch e que a recolha está em curso)* | «Modo detalhado» → separador **Provas do utilizador** |
| 0:25–1:10 **O diagnóstico** | "Uma casa de 3,45 kVA que liga a placa de indução e o termoacumulador ao mesmo tempo passa o limite: 4 078 W contra 3 450 W durante 25 minutos. O DuoWatt pausa o aquecimento da água e a casa nunca passa o limite, sem ficar sem água quente." | Assistente → resultado (e depois **Diagnóstico** no modo detalhado): mostrar o veredicto "Aguenta com gestão" e o gráfico (a linha tracejada sem gestão, a azul com DuoWatt) |
| 1:10–1:40 **O limite honesto** | "Nem sempre chega. Com a placa mais forte e um consumo de base mais alto, a casa precisa mesmo de mais potência, e a app diz-nos quanta." | Assistente: 2,3 kVA, «Mais de 400 kWh», 6 pessoas, uso intenso (ou no modo detalhado: indução **Intenso** e consumo **432**) → veredicto "Precisa de mais potência" |
| 1:40–2:05 **O impacto** | "Trocar o gás por elétrico evita cerca de 205 kg de CO₂ por casa e ano, ou 109 kg com o cenário adverso da rede. Isto vem da eletrificação, não só do DuoWatt: o que o DuoWatt faz é tirar o bloqueio da potência, que no máximo afeta cerca de 44 % das casas (valor aproximado)." | Voltar a **Moderado / 200**, descer ao bloco "Impacto" |
| 2:05–2:40 **A viabilidade** | "Subir a potência para 6,9 kVA custa 64 a 78 € por ano. O DuoWatt custa cerca de 200 a 280 € instalado e compensa ao fim de 3 a 4 anos. Os custos são estimativas de retalho; o primeiro passo é validar com um eletricista e testar com instaladores da Bosch." | Separador **Viabilidade** |
| 2:40–3:00 **O que propomos** | "A gestão de cargas já existe e os simuladores de potência também. O que não encontrámos foi um diagnóstico, no momento da avaria, que diga se a casa aguenta passar a elétrico. É isso que propomos testar com a Bosch." | Separador **Diferenciação** |

## Perguntas prováveis e respostas honestas
1. **"Quanto CO₂ é do DuoWatt?"**: "A redução vem da eletrificação. O DuoWatt só conta onde a potência é o bloqueio: no máximo cerca de 44 % das casas (proxy, dados de todos os contratos BTN). É um limite superior, não uma previsão."
2. **"Quanto custa e quem instala?"**: "Estimamos 200 a 280 € (com quadro adequado) a 350 a 680 € (com quadro novo). Instala um eletricista habilitado. São preços de retalho, não uma cotação; o produto industrial é desconhecido."
3. **"Isto já existe."**: "A gestão antidisparo existe (Legrand, Schneider e outros). Não encontrámos o diagnóstico gás → elétrico no momento da avaria, mas não encontrado não prova que não exista; é o que queremos testar."
4. **"E o espaço, o esquentador?"**: "É verdade: 67 % das casas têm esquentador e só 17 % termoacumulador, e muitas não têm espaço. O DuoWatt não resolve o espaço; resolve a potência."
5. **"Os números batem?"**: "O enunciado fala em mais de 400 kg de CO₂ por casa, que é o que o gás emite. A eletricidade também emite, por isso o evitado é cerca de 205 kg (um pouco mais de metade), e menos se a rede for mais emissora."
6. **"Quem pagou os custos e quem validou?"**: "As estimativas vêm de preços de lojas portuguesas e de plataformas de orçamentos; a Contabilidade e a Mecânica devem confirmá-las."

## O que NÃO dizer
"Somos os primeiros", "ninguém faz isto", "sem eletricista", "sem obras", "os Tronic ligam-se a um gestor de energia", "poupa muito dinheiro" (a poupança é ~33 €/ano; a mensagem é "descarboniza sem custar mais"), e **nunca** apresentar dados de utilizadores que não sejam reais.

## Checklist antes de ir ao palco
- [ ] Dados do inquérito (≥30 respostas) e 3 entrevistas feitos e inseridos no separador Provas
- [ ] Mecânica confirmou a potência da indução e a base da casa (0,6 kW ao serão?)
- [ ] Contabilidade confirmou os custos e o preço da garrafa
- [ ] Formato exato da entrega confirmado (ver PERGUNTAS.md)
- [ ] Testada a demo no projetor e em 1366×768


## Novo fluxo (noite 2)
Assistente (5 perguntas) → resultado (veredicto, 3 números) → **descarregar o relatório** (mostrar o HTML: é o que a família leva ao instalador) → modo detalhado (gráfico, viabilidade, diferenciação, provas). Os números são os mesmos nos dois modos.

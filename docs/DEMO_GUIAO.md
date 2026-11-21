# Guião da demo (2 a 3 minutos, PT-PT)

Estado: 21 nov 2026. Simulação ilustrativa; valores por validar num piloto. Entre `[colchetes]` só dados reais da equipa; nunca inventar. Navegação por "Seguinte" / "Anterior". Antes: abrir a app uns minutos antes (adormece sem uso) e testar no projetor.

| Tempo | Ecrã | O que se diz | O que se clica |
|---|---|---|---|
| 0:00–0:50 | **1. O problema** | "Ao fim da tarde, o cilindro está a aquecer e a máquina da roupa liga. Cada um sozinho é normal, juntos passam o limite da casa e a luz vai abaixo. É por isto que muitas famílias continuam no gás, e 85 % das trocas urgentes de esquentador voltam a ser gás." | "Ligar a máquina da roupa": a barra sobe, passa a linha do limite, aparece "A luz foi abaixo". |
| 0:50–1:50 | **2. Com DuoWatt** | "O mesmo cenário, com o kit: um sensor no quadro e um módulo no cilindro, ligados localmente, sem internet. Antes de a luz ir abaixo, o cilindro pausa. A luz mantém-se, e o cilindro tem água quente guardada: ninguém nota a pausa. A família evita subir a potência: cerca de 64 a 78 € por ano." | Carregar em "Seguinte" e repetir o botão; mostrar "em pausa", "A luz mantém-se" e o gráfico com e sem DuoWatt. |
| 1:50–2:40 | **3. O que muda** | "Para a Bosch, o kit completa o Tronic e transforma trocas gás por gás em vendas de cilindro. Por casa, são cerca de 246 kg de CO₂ por ano; se 1 % das casas a gás trocarem, cerca de 5 400 toneladas. O CO₂ desce porque a casa sai do gás; o DuoWatt tira a barreira que a impedia." | Apontar os 2 números grandes, o diagrama de 3 caixas e a tabela de concorrência; abrir "Para saber mais" só se perguntarem. |
| 2:40–3:00 | fecho | **"Garantia sem apagões."** | Nenhum. |

Números: 246 kg/casa/ano e ~5 419 t (derivados de `impacto.py`, 12 garrafas, 107 g/kWh); cenário adverso 131 kg e ~2 881 t. 64–78 €/ano é estimativa (`NEGOCIO.md`).

## Perguntas prováveis
1. **"O 5501i já tem programação; não chega?"** A programação usa horas fixas; a máquina da roupa pode ligar a qualquer hora. O DuoWatt reage ao que está a acontecer, sem a família fazer nada.
2. **"Isto já existe?"** Pelo que vimos, existe gestão antidisparo (Schneider, Legrand, Delta Dore, Shelly), mas em mercado francês, com hub ou para entusiastas. A nossa proposta: par emparelhado, pago pela Bosch, vendido na avaria.
3. **"Quanto custa?"** `[a preencher pela Contabilidade]`.
4. **"E se a casa passar o limite sem o cilindro?"** Não resolvemos; a promessa é que o cilindro nunca é a causa do apagão.
5. **"Quanto é do DuoWatt?"** O CO₂ vem de sair do gás; o DuoWatt retira o medo da potência. Não é previsão, é cenário.

## O que NÃO dizer
"Somos os primeiros", "a Bosch não tem" (dizer "pelo que vimos na gama Tronic"), "sem eletricista", "sem obras", que os Tronic se ligam a um gestor de energia, e nunca dados de utilizadores que não sejam reais.

# Guia da equipa DuoWatt (para ler no telemóvel)

Entrega: **sábado 21 nov, 18:30** (tudo no GitHub às 18:00). Pitch a 25 nov.

## 1. O DuoWatt em 1 parágrafo
O DuoWatt é um kit que completa os cilindros elétricos Bosch: pausa o cilindro sozinho antes de a luz ir abaixo, para que as casas com esquentador a gás passem para elétrico sem medo e sem aumentar a potência. São 2 peças emparelhadas: um sensor no quadro e um módulo no cilindro, a falar localmente, sem internet. É só software e simulação: não há protótipo físico. Slogan: **"Garantia sem apagões"**.

## 2. As 2 user stories
- **US1, a família:** quero passar para um cilindro elétrico sem que a luz vá abaixo, para deixar o gás sem pagar mais pela potência. (Evita ~64–78 €/ano de subir a potência; estimativa.)
- **US2, a Bosch e o instalador:** numa troca urgente de esquentador, quero oferecer um cilindro com garantia sem apagões, para vender um cilindro em vez de outro esquentador a gás.

## 3. Como é a demo (3 ecrãs, 2–3 min)
1. **O problema:** cilindro a aquecer e máquina da roupa a ligar; a barra passa o limite e "a luz foi abaixo".
2. **Com DuoWatt:** o cilindro pausa, "a luz mantém-se", ninguém fica sem água quente; evita ~64–78 €/ano.
3. **O que muda:** CO₂ por casa/ano (~246 kg; 131 kg no cenário adverso), 1 % das casas a gás (~5 400 t/ano), como funciona, concorrência, "para a Bosch".
Guião completo em `docs/DEMO_GUIAO.md`; produto em `docs/PRODUTO.md`.

## 4. Números principais
| Número | Valor | Estado |
|---|---|---|
| Casas a gás de garrafa | 2,2 milhões | Enunciado Bosch |
| Trocas urgentes "gás por gás" | 85 % | Enunciado Bosch |
| CO₂ evitado por casa/ano | ~246 kg (adverso ~131; 12 garrafas) | Derivado (APA 2023) |
| Cenário nacional 1 % | ~5 419 t/ano (adverso ~2 881) | Derivado; adoção é pressuposto |
| Subir de 3,45 para 6,9 kVA | 64–78 €/ano | Estimativa (ERSE); IVA por verificar |
| Cenário da demo | cilindro 1,5 kW + máquina 2 kW + base 0,6 kW ≈ 4,1 kW | Pressupostos |
| Regras de controlo | desligar a 90 %, religar a 80 %, pausa máx. 30 min | Pressupostos |

## 5. O que falta e quem faz
Somos 4, de áreas diferentes: **Multimédia e Tecnologias de Comunicação**, **Informática** (Tiago), **Engenharia Mecânica** e **Mestrado em Contabilidade e Controlo de Gestão**.

| Perfil | Tarefa | Prazo |
|---|---|---|
| Contabilidade e Controlo de Gestão | Negócio: preencher `docs/NEGOCIO.md` (custo do kit, preço à Bosch, conta de equilíbrio). Nada de inventar: onde não houver fonte, deixar `[a preencher]` | 13:00 |
| Multimédia e Tecnologias de Comunicação | Deck do pitch (a partir dos 3 ecrãs e de `docs/PRODUTO.md`); rever a demo no telemóvel | 14:00 |
| Engenharia Mecânica | Validar os pressupostos: potência da máquina da roupa, base da casa, cilindro 1,5 kW, segurança de pausar o cilindro | 13:00 |
| Informática (Tiago) | Demo, imagem 3D concetual e publicação da app | 18:00 tudo no GitHub; 18:30 entregar |
| Todos | Provas no fim: se houver respostas ou entrevistas reais, entram em `dados/`; nunca inventar | até à entrega |

## 6. O que nunca dizer
"Somos os primeiros"; "sem eletricista"; "sem obras"; "a Bosch não tem" (dizer "pelo que vimos na gama Tronic"); que os Tronic se ligam a um gestor de energia; preços que ninguém calculou; dados de utilizadores que não sejam reais.

## 7. As 5 perguntas prováveis do júri
| Pergunta | Resposta honesta |
|---|---|
| O 5501i já tem programação; não chega? | A programação usa horas fixas; a máquina da roupa pode ligar a qualquer hora. O DuoWatt reage ao que está a acontecer. |
| Isto já existe? | Pelo que vimos, existe gestão antidisparo (Schneider, Legrand, Delta Dore, Shelly), mas com hub, em França ou para entusiastas. Nós propomos um par emparelhado, pago pela Bosch, vendido na avaria. |
| Quanto custa e quem paga? | A Bosch (B2B). Preços: `[a preencher pela Contabilidade]`. A família evita ~64–78 €/ano. |
| E se a casa passar o limite sem o cilindro? | Não resolvemos. A promessa é que o cilindro nunca é a causa do apagão. |
| Quanto CO₂ é do DuoWatt? | O CO₂ desce porque a casa sai do gás; o DuoWatt tira a barreira. ~246 kg por casa/ano; 1 % das casas: ~5 419 t/ano (cenário, não previsão). |

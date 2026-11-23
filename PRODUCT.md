# PRODUCT.md — App de demonstração DuoWatt

## O que é
DuoWatt é um kit de duas peças instaladas com o cilindro elétrico, na troca do esquentador a gás:
1. **Sensor no quadro** (pinça de corrente): mede a casa toda, ≥ 10 leituras/s.
2. **Ficha inteligente no cilindro**: pausa e retoma o cilindro.
Falam por rádio local encriptado, sem internet. Se o rádio falhar 5 s, o cilindro volta ao normal (modo seguro).

Esta app é o **«modo ligado»** (Wi-Fi opcional) e a **demonstração ao vivo do pitch** (Hackathon@ShiftE 2026). A proteção funciona sem app.

## Promessa (a única)
«O cilindro nunca é a causa do apagão.» Se a casa passa o limite **sem** o cilindro, o DuoWatt não resolve.

## Regras de controlo
Pausa a 90 % do limite; retoma com corrente + cilindro < 80 % e pausa mínima de 1 min; pausa máxima 30 min; reação < 1 s (meta); nunca mexe noutros aparelhos.

## Para quem
- A **família** no modo ligado: quer saber, num relance, se a casa está folgada e porque o cilindro parou.
- O **júri** no pitch: vê a demo num projetor (1280×720) ou abre pelo QR no telemóvel.

## Tom
Claro, calmo, honesto. Casa, energia, confiança. Nada de «gaming» nem «crypto». PT-PT.

## Honestidade (não negociável)
- «Simulação» sempre visível. Dados do histórico/consumo: «Dados de exemplo».
- O sensor não sabe que aparelho ligou: «um aparelho grande ligou».
- Sem temperatura da água. Sem Bosch (nome, logótipo, cores, tipografia).
- Estimativas com «≈» ou «estimativa». Números só de `src/data/facts.ts`.
- Frases proibidas: «sem obras», «sem eletricista», «somos os primeiros», «a Bosch não tem», «nunca mais falta a luz», «evita todos os disparos», «porta HAN», «overhead».

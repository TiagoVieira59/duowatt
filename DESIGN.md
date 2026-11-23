# DESIGN.md — direção visual

**Ideia:** «luz de casa ao serão». Papel quente, tinta verde-escura, uma luz âmbar. Calma e confiança; legível ao fundo da sala.

## Paleta (tokens em `src/styles/tokens.css`)
- Fundo `#F6F1E7` · superfície `#FFFDF8` · tinta `#1D2B26` · tinta suave `#4B5B54` (≥ 4,5:1 sobre o fundo).
- Marca: verde-floresta `#1F5E46`.
- **Estados do medidor, distintos em luminosidade (não só em tom):**
  - Folgada: fundo claro `#DCEFE3`, texto `#123D2B`.
  - Perto do limite: fundo médio `#F2C94C`, texto `#3B2A00`.
  - Acima do limite: fundo escuro `#5A1230`, texto `#FFF6F0`. Acima de 100 %: anel pulsante + «Acima do limite».
  - Apagão: `#0B0B0C`.
- Sem o vermelho nem o azul da Bosch.

## Tipografia (self-hosted, 2 famílias)
- **Manrope** (UI e texto), **Fraunces** (números grandes e legenda do apresentador). `font-variant-numeric: tabular-nums` nos números.
- Painel ≥ 22 px a 1280×720; números-chave ≥ 48 px.

## Forma
Raios 14/22 px; espaçamento base 4 px; sombras suaves e quentes; sem cartões aninhados.

## Movimento
150–300 ms nas transições; spring suave no medidor; 19:05 coreografado: pico → indicador de reação → cartão «Em pausa» → medidor desce → legenda. `prefers-reduced-motion`: sem movimento grande, apagão = corte para escuro.

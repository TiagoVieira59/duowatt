# DESIGN.md — direção visual

Fonte: ecrãs do Figma «Hackaton_Simulador (Tiago)» (PNG exportados). Neutro, limpo, cartões brancos grandes.

- **Fundo** `#F5F5F5`; cartões brancos, raio 28 px, sombra suave; tinta `#111`, texto secundário `#6B6B6B`.
- **Tipografia:** Inter (única família, self-hosted); títulos 800 com tracking −0,035em; números tabulares.
- **Estados do medidor (luminosidade distinta):** Folgada = cartão branco + pílula verde; Perto do limite = cartão âmbar claro `#FFEFC2` + pílula âmbar; Acima do limite = cartão escuro `#131313` + pílula vermelha. Sempre com texto.
- **Pílulas:** verde (A aquecer, Folgada), âmbar (Em pausa), vermelha (Parado, Acima), cinzenta (contadores). Cores de texto escurecidas face ao Figma para cumprir 4,5:1.
- **Barra de separadores:** painel flutuante com ícones em quadrados arredondados; ativo preto com ícone branco.
- **Logótipo:** wordmark «duo ⧓ watt» da equipa (SVG inline). Nota: o laço é vermelho `#E00000`, como no Figma; ver DECISOES.md.
- **Movimento:** 150–300 ms; spring no medidor; `prefers-reduced-motion` respeitado.

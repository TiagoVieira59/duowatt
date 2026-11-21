# Auditoria UX v2

Screenshots: `screenshots/ecra{1,2,3}_{390,1920}.png` e `ecra1_antes_{390,1920}.png`. Sem scroll horizontal (scrollWidth = largura em todos os ecrãs).

## Corrigido em app.py (cena())
- Rótulos "Cilindro" e "Máquina da roupa" eram brancos sobre fundo creme (ecrã 1 antes do clique e ecrã 2): invisíveis. Agora escuros com a luz acesa, brancos com a casa escura.
- "Máquina da roupa" saía da casa a 390 px (cortado). Máquina deslocada 20 px para a esquerda.

## Verificado
- Ícones: cilindro, máquina de porta redonda, lâmpada reconhecíveis; rótulos sans-serif ~18 px.
- Ecrã 1: casa escura, lâmpada apagada, "A luz foi abaixo" em grande, barra vermelha sem percentagens.
- Ecrã 2: selo "em pausa", lâmpada acesa, "A luz mantém-se", barra verde, gráfico com limite tracejado.
- Ecrã 3: sem placeholders; tabela de concorrência; conta de impacto em 3 linhas.
- Não especialista: percebe cada ecrã em <30 s (ecrã 3 é denso, mas o topo diz o essencial).

## Por decidir (não alterado)
- "~5419 t" sem espaço: `formato.pt` só separa milhares a partir de 10 000 (norma PT, testado em tests/test_formato.py). O pedido esperava "5 419 t"; mudar exige alterar o teste.
- Cabeçalhos da tabela e coluna da esquerda em cinzento claro: contraste baixo (baixa prioridade).
- Seta "ligação local, sem internet" parte em 3 linhas a 390 (aceitável).
- Screenshots a 390 feitos com viewport de altura 2200 (o Streamlit rola num contentor interno).

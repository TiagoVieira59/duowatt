
## Polimento (P1-P4), só app.py
- P1: séries do gráfico a 10 anos encurtadas (DuoWatt / Subir potência (sem IVA) / (com IVA)), legenda em baixo, labelLimit=400 (o corte vinha do limite por omissão de 160 px). Verificado nos screenshots ciclo5a a 1366x768 e 1920x1080.
- P2: material (.2f) passa a usar a função existente vir(); restantes valores já usavam vírgula ou são inteiros. Valores inalterados. Campo numérico da barra lateral (0.210) segue o formato do navegador, não alterado.
- P3: citação com cor #222, 18 px, itálico e barra lateral (CSS).
- P4: nota no topo de Viabilidade, Diferenciação e Provas.
- Testes: 38 passed, 4 xfailed; capturar.py ciclo5a: sem erros nem avisos.

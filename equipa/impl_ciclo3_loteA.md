# Implementação ciclo 3, lote A

- Branch `ciclo-3` (já existia; estava-se em `ciclo-2`, mudou-se para `ciclo-3`). Sem merge.
- A1: `ferramentas/analisar_inquerito.py <csv> [--saida dados/]` gera `inquerito_resumo.json/.md` e `graficos/P<n>.png` (matplotlib, adicionado ao requirements e ao .venv). Erros claros em PT-PT para ficheiro inexistente, vazio, só cabeçalho e sem colunas P<n>; colunas em falta avisadas; respostas em branco ignoradas (n por pergunta). P1/P6: opções desconhecidas agrupadas em "Outra" (contada uma vez por pessoa).
- A2: `ferramentas/teste_inquerito/` com CSV SINTÉTICO (8 linhas inventadas, marcadas no nome, na coluna de carimbo e no README) e pytest (saída em tmp_path; usa o python do .venv por causa do matplotlib).
- A3: `app.py` com `st.tabs` Diagnóstico (conteúdo igual, só indentado) e Provas do utilizador (cartões Bosch com fonte; bloco da equipa lê `dados/inquerito_resumo.json`, senão mostra "Ainda sem dados..."). `DUOWATT_DADOS` permite apontar a outra pasta (só para testes).
- Verificação: pytest verde; `capturar.py ciclo3a` sem erros; a 1366x768 o separador Diagnóstico mostra veredicto, frase, métricas e gráfico sem scroll (altura do gráfico mantida em 240). Ramo com JSON testado com AppTest e uma pasta temporária fora de `dados/` (apagada); `dados/` só tem `.gitkeep`.
- Não alterados: duowatt.py, valores, fórmulas, veredicto.

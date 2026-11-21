# Implementação ciclo 1, lote 3 (I6-I9), só `app.py`

- I6: `xs = alt.Scale(domain=[17, 23], zero=False, nice=False)` partilhada por eixo, retângulo do serão e rótulo. Verificado em Playwright (1366x768): ticks 17:00 em x=459 e 23:00 em x=1240, sem tick 0:00; os dados ocupam a largura toda.
- I7: etiqueta do limite alinhada à direita (22,95 h); "Sem gestão" a 8 px tracejado atrás, "Com DuoWatt" a 4 px à frente.
- I8: "Folga com a placa ligada: X W" / "Faltam X W para a placa ligada caber"; rótulos "CO2 evitado por casa (<fator> g/kWh)" e "No pior cenário (167 g/kWh)"; toneladas nacionais em `st.caption` (mantém "não atribuído ao DuoWatt").
- I9: legenda com `labelColor="#222"` (16 px); CSS para input/select/radio da sidebar a 16 px #222.
- Sem alterações a duowatt.py, impacto.py, valores ou veredicto; avisos mantidos.
- Verificação: pytest 32 passed, 4 xfailed (os mesmos); `capturar.py ciclo1c` -> "sem erros nem avisos".

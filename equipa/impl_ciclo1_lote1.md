# Implementação ciclo 1, lote 1 (I1, I2, I3)

## Alterado
- `app.py`: título curto; veredicto (h4) + frase por cenário + margem em W (limite - base - indução); 3 números (pico sem gestão, pico com DuoWatt, CO2 evitado por casa; "n/d" se precisa de mais potência); gráfico Altair 17:00-23:00 (horas HH:MM, limite a 4 px rotulado, serão 19:30-20:10 sombreado, "Sem gestão" tracejado atrás de "Com DuoWatt"); métricas 2 por coluna sem "episódios"; CSS (texto >= 16 px, eixos 14 px, cinzento #222/#333); avisos: `st.info` de 2 linhas + expander "Pressupostos e limites".
- Sidebar aberta com kVA, consumo e indução à vista; restantes entradas no expander "Avançado".
- `.streamlit/config.toml`: `toolbarMode = "minimal"`.
- `ferramentas/capturar.py`: abre o expander "Avançado" antes de preencher pessoas/garrafas.
- Extra mínimo de apresentação: "Variação de custo" passou a "Poupança de custo"/"Custo extra" conforme o sinal (mesmo valor, sem mexer em fórmulas).
- Sem alterações a duowatt.py, impacto.py, valores ou veredicto.

## Verificação
- pytest test_impacto + test_duowatt: 8 passed.
- capturar.py ciclo1: erros.txt = "sem erros nem avisos" (após corrigir um aviso Vega "Conflicting legend property").
- Medido por Playwright em 1366x768 (cenário A): gráfico termina em y=668 (< 768); título, veredicto, 3 números e gráfico acima da dobra.

## Não consegui / por saber
- Não vi imagens (Auditor UX). Os avisos ficam no fim da página, não fixos no rodapé (não cabem acima da dobra).
- Sidebar mantém 300 px de largura em 1366.

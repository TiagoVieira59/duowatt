# Implementação ciclo 2, lote 2 (J5a-e, J8, J9)
- J5a: impacto.py com TERMO_POTENCIA_EUR_DIA e custo_subir_potencia (3,45→6,9 = 63,6 €/ano); teste novo.
- J5b: frase do termo de potência (3,45 kVA, veredicto 'aguenta com gestão'); 'mais/menos do que' comparado em código.
- J5c: QUOTA_ATE_3_45_KVA = 0,44 (proxy) e legenda 'Limite superior ... proxy'.
- J5d: nota INE/ICESD 2020 (67 %/17 %) em 'Pressupostos e limites'.
- J5e: 3 entradas em DECISOES.md, 'para o Tiago validar'.
- J8: rótulos curtos (CO2 evitado, Poupança, Min. acima, Min. sem água) com help; Playwright 1366×768 e 1920×1080: nenhum scrollWidth > clientWidth.
- J9: captions a #222, 16 px, opacity 1; getComputedStyle confirma rgb(34,34,34)/16px.
Verificação: pytest 33 passed, 4 xfailed; capturar.py ciclo2b: 'sem erros nem avisos'.
Não alterados: duowatt.py, veredicto, valores por omissão, fórmulas.

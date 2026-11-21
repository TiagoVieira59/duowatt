# Implementação ciclo 2, lote 1 (J1, J2, J3, J4, J6, J7)
- J1: frase "Placa + termoacumulador juntos pedem X W; o limite é Y W" (X = base + indução + P_TERMO_W).
- J2: linha "CO2: gás X kg/ano → elétrico Y kg/ano → evitado Z kg/ano" na secção de impacto (dict de impacto_casa).
- J3: capturar.py: D2 com 20 garrafas; Enter + Tab depois de cada campo numérico.
- J4: gráfico a 240 px; uma linha de 6 métricas (picos, CO2 evitado, poupança, minutos "sem → com"); fonte das métricas 1,6 rem. A 1366×768 (cenário A) o fundo das métricas fica a 344 px (< 768).
- J6: veredicto "reserva de água insuficiente" tem frase própria (aumentar o depósito).
- J7: "precisa de mais potência" acrescenta a menor potência de [2,3; 3,45; 6,9; 10,35] kVA com limite ≥ pico com DuoWatt (ou "nem a maior chega").
Verificação: pytest 32 passed, 4 xfailed; capturar.py ciclo2a: "sem erros nem avisos"; Playwright confirma métricas e CO2/poupança dentro dos 768 px.
Não alterados: duowatt.py, impacto.py, fórmulas, veredicto, avisos e atribuições.

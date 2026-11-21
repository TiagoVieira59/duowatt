# Implementação ciclo 4, lote B (branch ciclo-4)

- impacto.py: constantes novas com fonte/classificação (custo do material, mão de obra, quadro novo, IVA da potência, 10 anos; valores por omissão de impacto_casa expostos como constantes, mesmos valores) e funções `custo_duowatt` e `anos_equilibrio`. Testes novos em test_impacto.py.
- app.py: separadores Viabilidade (seletor de quadro, métricas, tabela de custos, gráfico Altair a 10 anos, efeito na fatura calculado, 4 passos, 3 riscos) e Diferenciação (tabela, caixas, pitch). Expander "Pressupostos e limites" passou a tabela Valor | Fonte | Classificação lida das constantes.
- ferramentas/capturar.py: screenshots de Viabilidade e Diferenciação (cenário A, 1920×1080 e 1366×768) e deteção Playwright de rótulos/valores de métricas cortados.
- Verificação: pytest verde (38 passed, 4 xfailed); capturar.py ciclo4a: "sem erros nem avisos" (inclui a verificação de métricas cortadas).
- Nota: com quadro novo, a soma das constantes dá ~352–682 €, não os ~370–620 € de VIABILIDADE.md (a soma 200–280 + 150–400 é ~350–680): a app mostra o valor calculado; convém corrigir o documento. Com os valores por omissão a fatura com DuoWatt dá ~+9 €/ano (ponto médio), não +8.

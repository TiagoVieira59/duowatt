# Implementação ciclo 6
- app.py: separador "Provas do utilizador" lê `dados/entrevistas.json` (DUOWATT_DADOS) e mostra "Entrevistas da equipa (N)" em cartões (perfil, data, citação entre «», facto). Ignora entradas vazias ou com '[' ; JSON inválido mostra aviso; sem ficheiro não mostra nada.
- ferramentas/modelo_entrevistas.json: 3 placeholders A/B/C + entrada `_instrucoes`.
- test_entrevistas.py: 4 testes (válido, inválido, '[' ignorado, inexistente), dados sintéticos em tmp_path.
- PLANO_RECOLHA_PROVAS.md: passo 5 atualizado.
- Verificação: pytest 42 passed, 4 xfailed; capturar.py ciclo6a: "sem erros nem avisos"; dados/ só com .gitkeep.

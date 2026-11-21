# HANDOFF (porta de entrada para uma sessão nova)

**Estado (21 nov 2026):** demo de 3 ecrãs feita (`app.py`), simulação (`duowatt.py`), documentos em `docs/`. Tag `entrega-21nov`.
**Conceito:** kit de 2 peças (sensor no quadro + módulo no cilindro) que pausa o cilindro a ~90 %, religa a <80 %, pausa máx. 30 min, modo seguro sem sensor. Fonte de verdade: `docs/referencia/PROMPT_Kit_DuoWatt_Final.md`, resumo em `docs/PRODUTO.md`.

## Comandos
- Testes: `python3 -I -m pytest -q tests -p no:cacheprovider` (com streamlit instalado corre também `tests/test_app.py`)
- App: `.venv/bin/streamlit run app.py`
- Guia da equipa em Word: `.venv/bin/python ferramentas/md_para_docx.py docs/GUIA_EQUIPA.md docs/GUIA_EQUIPA.docx`
- Publicar: `DEPLOY.md`

## Falta
- Tiago: adicionar `assets/produto_3d.png`; publicar (DEPLOY.md); enviar `docs/GUIA_EQUIPA.docx`.
- Contabilidade: preencher `docs/NEGOCIO.md` e o texto "[números de negócio…]" do ecrã 3 em `app.py`.
- Multimédia: deck. Todos: provas (inquérito/entrevistas, `docs/provas/`); o Júri deu 1/5 a esse critério.
- Júri independente (`equipa/juri_final.md`): 2,31/5; melhorias: tirar placeholders, mostrar a conta do impacto, bloco "o que falta validar".

## Mapa
`app.py duowatt.py impacto.py formato.py` · `tests/` · `ferramentas/` · `docs/` (+`provas/`, `referencia/`) · `screenshots/` · `equipa/` · `dados/` (só dados reais).
Regras: `CLAUDE.md`. Decisões: `DECISOES.md`. Dúvidas: `PERGUNTAS.md`.

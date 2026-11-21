# HANDOFF (começa aqui numa sessão nova)

## Estado em 5 linhas
- Projeto DuoWatt, Hackathon@ShiftE 2026, desafio Bosch. Entrega **21 nov 17:30**; congelamento às **14:00** (só correções de erros).
- Tag `final-noite2`; testes: 46 a passar, 4 xfail justificados.
- A app (Streamlit) abre num assistente de 5 perguntas → resultado → relatório HTML para o instalador; «Modo detalhado» tem gráficos, viabilidade, diferenciação e provas.
- Júri simulado: 2,9/5 (C1=1, C2=3, C3=4, C4=4, C5=3); facilidade 4/5. O C1 só sobe com dados reais.
- Responde sempre em PT-PT. Regras no `CLAUDE.md` (nunca inventar dados de utilizadores).

## Decisões tomadas
Conceito fixo (diagnóstico gás→elétrico + gestão que pausa o termoacumulador); stack Python/Streamlit; push para o GitHub autorizado (sem `--force`); identidade visual neutra, sem imitar a Bosch; relatório do instalador é a única funcionalidade nova autorizada.
## Decisões pendentes
`PERGUNTAS.md` (formato da entrega, quem valida custos, retoma automática n.º 7).

## O que mudou na noite 2 (resumo de `DECISOES.md`)
Forms (`ferramentas/criar_formulario.gs`, `FORMS_INSTRUCOES.md`); formato PT-PT (`formato.py`); `UX_PESQUISA.md`; `assistente.py` (lógica pura testável + ecrãs); relatório HTML; modo detalhado herda as respostas; `GUIA_EQUIPA.md/.docx`.

## Próximos passos até às 17:30
1. Tiago executa o script do Forms (`FORMS_INSTRUCOES.md`), preenche o link no `GUIA_EQUIPA.md` e envia o guia pelo WhatsApp.
2. Recolher ≥30 respostas e 3 entrevistas; correr o analisador; copiar `ferramentas/modelo_entrevistas.json` para `dados/entrevistas.json` com citações literais.
3. Mecânica/Contabilidade confirmam os valores (lista em `RELATORIO_FINAL.md` §3).
4. Rever a demo (`DEMO_GUIAO.md`) em telemóvel e projetor; preencher os campos `[entre colchetes]` só com dados reais.
5. Às 14:00 congelar; às 17:30 entregar (formato por confirmar).

## Comandos
- App: `.venv/bin/streamlit run app.py` (http://localhost:8501)
- Testes: `python3 -I -m pytest -q test_formato.py test_assistente.py test_impacto.py test_duowatt.py test_modelo_ciclo1.py test_entrevistas.py ferramentas/teste_inquerito -p no:cacheprovider`
- Inquérito: `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv`
- Guia em Word: `.venv/bin/python ferramentas/md_para_docx.py GUIA_EQUIPA.md GUIA_EQUIPA.docx`

## Mapa de ficheiros
- **Ler:** `CLAUDE.md`, `PROGRESSO.md`, `CRITERIOS_AVALIACAO.md`, `CONTEXTO_Projeto_DuoWatt.md`, `RELATORIO_FINAL.md`, `DEMO_GUIAO.md`, `PERGUNTAS.md`.
- **Código:** `app.py` (modo detalhado), `assistente.py`, `duowatt.py`, `impacto.py`, `formato.py`, `ferramentas/`.
- **Ignorar:** `equipa/` (históricos de agentes), `screenshots/` antigos, `PROMPT_*.md`, `BACKLOG.md`, PDFs e .docx da equipa (não editar).

# HANDOFF (começa aqui numa sessão nova)

## Estado
- DuoWatt, Hackathon@ShiftE 2026, desafio Bosch. Entrega **21 nov 17:30**; congelamento às **14:00** (só correções de erros). PT-PT sempre; regras no `CLAUDE.md` (nunca inventar dados de utilizadores).
- Tag `final-noite2b`. Testes: 47 a passar, 4 xfail justificados.
- App Streamlit: assistente de 5 perguntas → resultado (veredicto, 3 números, tabela de impacto 1/5/10 %, relatório HTML para o instalador) → «Modo detalhado» (gráfico, viabilidade com plano por fases, diferenciação, provas).
- Júri simulado: ver `equipa/juri_noite2b.md` e `RELATORIO_FINAL.md` §0. O C1 (provas) só sobe com dados reais.

## Decisões
Conceito fixo; push autorizado (sem `--force`); 12 garrafas por omissão em tudo; botões verde-petróleo (sem imitar a Bosch). Pendentes: `PERGUNTAS.md` (formato da entrega, quem valida custos, retoma automática n.º 7).

## Próximos passos até às 17:30
1. Executar o script do Forms (`FORMS_INSTRUCOES.md`), pôr o link no `GUIA_EQUIPA.md` e enviar o guia (`.docx`) pelo WhatsApp.
2. ≥30 respostas + 3 entrevistas; correr o analisador; `dados/entrevistas.json` com citações literais.
3. Eng. Mecânica / Contabilidade e Controlo de Gestão / eletricista validam os valores (lista em `RELATORIO_FINAL.md` §3 e `VIABILIDADE.md` §8).
4. Ensaiar a demo (`DEMO_GUIAO.md`) em telemóvel e projetor. 14:00 congelar; 17:30 entregar.

## Comandos
- App: `.venv/bin/streamlit run app.py`
- Testes: `python3 -I -m pytest -q test_formato.py test_assistente.py test_impacto.py test_duowatt.py test_modelo_ciclo1.py test_entrevistas.py ferramentas/teste_inquerito -p no:cacheprovider`
- Inquérito: `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv`
- Guia Word: `.venv/bin/python ferramentas/md_para_docx.py GUIA_EQUIPA.md GUIA_EQUIPA.docx`

## Ficheiros
- **Ler:** `CLAUDE.md`, `PROGRESSO.md`, `CRITERIOS_AVALIACAO.md`, `IMPACTO.md`, `VIABILIDADE.md`, `DIFERENCIACAO.md`, `DEMO_GUIAO.md`, `PERGUNTAS.md`, `DECISOES.md`.
- **Código:** `app.py` (modo detalhado), `assistente.py`, `duowatt.py`, `impacto.py`, `formato.py`, `ferramentas/`.
- **Ignorar:** `equipa/`, `screenshots/` antigos, `PROMPT_*.md`, `BACKLOG.md`, PDFs e .docx da equipa (não editar).

# DuoWatt: garantia sem apagões

Hackathon@ShiftE 2026, desafio Bosch. Kit que completa os cilindros elétricos Bosch: pausa o cilindro sozinho antes de a luz ir abaixo, para que casas com esquentador a gás passem para elétrico sem aumentar a potência.

## Correr
```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py
python3 -I -m pytest -q tests -p no:cacheprovider
```
Publicar: ver `DEPLOY.md`.

## Mapa da pasta
| Caminho | O que é |
|---|---|
| `app.py`, `duowatt.py`, `impacto.py`, `formato.py` | Demo (Streamlit), simulação, impacto, formatação PT-PT |
| `tests/` | Todos os testes |
| `ferramentas/` | Inquérito (analisar, criar formulário), capturas, conversão para .docx |
| `docs/` | Produto, arquitetura, concorrência, negócio, impacto, guião, guia da equipa |
| `docs/provas/`, `docs/referencia/` | Recolha de provas; PDFs e documentos da equipa/organização |
| `dados/` | Só dados reais (vazio até haver respostas) |
| `HANDOFF.md`, `PROGRESSO.md`, `DECISOES.md`, `PERGUNTAS.md` | Estado e decisões |

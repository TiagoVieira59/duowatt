# DuoWatt

Hackathon@ShiftE 2026 (Universidade de Aveiro) · Desafio Bosch: "Decarbonizing 2.2M Homes". Entrega: **21 nov 2026, 17:30**; pitch a 25 nov.

**A ideia:** um diagnóstico "a minha casa tem potência para trocar o gás por elétrico?" (aguenta / aguenta com gestão / reserva de água insuficiente / precisa de mais potência) mais uma gestão que pausa o termoacumulador enquanto se usa a placa de indução, para uma casa de 3,45 kVA não disparar. Só software e simulação; complemento dos termoacumuladores Tronic da Bosch.

## Por onde começar (para pessoas e para o Claude)
1. `PROGRESSO.md`: estado atual, notas do Júri simulado e próximo passo.
2. `CONTEXTO_Projeto_DuoWatt.md`: decisões da equipa e regras.
3. `CRITERIOS_AVALIACAO.md`: critérios oficiais e pesos.
4. `RELATORIO_FINAL.md`: o que foi feito, valores a validar, objeções do júri e respostas.

## Correr a app
```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run app.py        # abre em http://localhost:8501
```

## Testes
```bash
python3 -I -m pytest -q test_impacto.py test_duowatt.py test_modelo_ciclo1.py test_entrevistas.py ferramentas/teste_inquerito -p no:cacheprovider
```
(os testes do inquérito e das entrevistas chamam o `.venv`, por isso criar o ambiente primeiro; 4 falhas esperadas, justificadas, dependem de decisões da equipa)

## Estrutura
| Ficheiro ou pasta | O que é |
|---|---|
| `app.py` | Demo Streamlit: Diagnóstico, Viabilidade, Diferenciação, Provas do utilizador |
| `duowatt.py` | Simulador de potência de 24 h e veredicto |
| `impacto.py` | CO₂ e custo, gás contra elétrico; constantes com fonte e classificação |
| `VIABILIDADE.md`, `DIFERENCIACAO.md`, `DEMO_GUIAO.md` | Documentos de entrega e de pitch |
| `INQUERITO.md`, `ENTREVISTAS.md`, `PLANO_RECOLHA_PROVAS.md` | Recolha de provas do utilizador (critério 1) |
| `Parametros_Verificados.md`, `PESQUISA.md`, `DECISOES.md` | Valores com fonte e decisões |
| `ferramentas/` | Captura de screenshots, analisador do inquérito, script do Google Forms |
| `dados/` | Resultados reais do inquérito e das entrevistas (vazio até haver dados reais) |
| `equipa/` | Papéis e relatórios dos agentes de apoio |
| `screenshots/` | Capturas automáticas (a pasta `final/` é o estado de entrega) |

## Dados reais (critério 1)
Nunca se inventam dados de utilizadores. Depois de recolhidos: `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv` (escreve em `dados/`), e para as entrevistas copiar `ferramentas/modelo_entrevistas.json` para `dados/entrevistas.json`. Ver `PLANO_RECOLHA_PROVAS.md`. O CSV bruto na raiz não é versionado.

## Notas
O repositório é privado e contém os PDFs e .docx fornecidos pela organização e pela equipa; se vier a ser público, retirar esses ficheiros.

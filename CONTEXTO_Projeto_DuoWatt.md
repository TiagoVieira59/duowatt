# Contexto do projeto DuoWatt (para outra sessão do Claude)

Estado em 21 nov 2026, de manhã. Língua de trabalho: **português europeu (PT-PT)**.

## 1. O que é
Hackathon@ShiftE 2026 (Universidade de Aveiro), desafio **Bosch**: "Decarbonizing 2.2M Homes". Substituir o gás (GPL) no aquecimento de água e na cozinha em ~2,2 M de casas portuguesas. O júri valoriza a solução mais viável na vida real e o impacto de CO₂ mensurável. **Entrega: 21 nov 2026, 17:30.**

Equipa de 5: Eng. Informática (o utilizador, Tiago), Eng. Mecânica, Contabilidade e Controlo de Gestão (mestrado), Multimédia e Tecnologias da Comunicação, Ciência Política. O Tiago fica com a parte de software.

## 2. Decisões já tomadas
- **Conceito fixo: DuoWatt.** Não mudar de conceito. A alternativa "RetroFit Bridge + FitGauge" (interface mecânica, no docx "Propostas_Inovacao...") é da Mecânica e **não se implementa**; só se pode propor noutro ficheiro, nunca no código.
- **Dois passos:** (1) **diagnóstico** "a casa tem potência para passar de gás a elétrico?" → "aguenta" / "aguenta com gestão" / "reserva de água insuficiente" / "precisa de mais potência"; (2) **gestão**: um controlador pausa o termoacumulador enquanto há indução, para a casa de 3,45 kVA não disparar.
- **Posicionamento:** complemento dos termoacumuladores Tronic da Bosch (não produto concorrente).
- **Só software/simulação**, sem hardware e sem sensores. Entradas (da fatura): potência contratada, tarifa/preço e consumo mensal; mais nº de pessoas e garrafas de gás por ano.
- **Stack:** Python + Streamlit.
- **Mensagem honesta:** o benefício em € é pequeno (~33 €/ano nos valores atuais); o argumento principal é "descarboniza sem custar mais".
- O PRD_Rascunho antigo está desatualizado e vai ser apagado: ignorar.
- Modo de trabalho pedido pelo Tiago: **o Claude escreve o código todo; o Tiago decide**. Sem perguntas de escolha múltipla; perguntas curtas em texto.

## 3. O que já está feito (pasta do projeto)
| Ficheiro | O que é |
|---|---|
| `duowatt.py` | Simulador de 24 h (1 min/passo): consumo, indução, termoacumulador 2 kW com reserva de água, regra de gestão com pausa mínima de 5 min, `veredicto()`. |
| `impacto.py` | CO₂ e custo gás vs. elétrico por casa, e extrapolação para as 2,2 M de casas. |
| `app.py` | Demo Streamlit: entradas, veredicto, gráfico do dia com e sem gestão, métricas, impacto e avisos. |
| `test_duowatt.py`, `test_impacto.py` | 8 testes (todos a passar). |
| `Parametros_Verificados.md` | Valores pesquisados com fonte e classificação (feito por um subagente de pesquisa). |
| `Parametros_Simulador.md` | Primeira lista de parâmetros (anterior; o link da APA lá dentro está partido). |
| `Ficha_DuoWatt_Proposta_Equipa.md` | Ficha de uma página para a equipa. |
| `.venv/` | Ambiente com Streamlit. |

Correr a demo: `cd "/home/tiago/Documentos/HACKATON SHIFTE" && .venv/bin/streamlit run app.py`
Correr testes: `python3 -I -m pytest -q test_impacto.py test_duowatt.py -p no:cacheprovider`

Foi usada uma equipa de 3 subagentes (interface, verificação de valores, revisão) e já terminou; o revisor apontou 8 pontos e os mais claros já foram corrigidos.

## 4. Valores por omissão atuais (a validar)
- Limite: kVA tratado como kW. Termoacumulador 2 000 W (Tronic 4001 T, 80 L ou mais). Indução 1,8 kW (moderado) ou 3 kW (intenso). Base da casa = consumo mensal ÷ 720 h (plana).
- CO₂: GPL ~0,227 kg/kWh (2,9 kg/kg); eletricidade 107 g/kWh (APA 2023, média anual), cenário adverso 167 g/kWh.
- Preço da garrafa 13 kg: 37 €; eletricidade 0,21 €/kWh (marginal); eficiência esquentador 0,82; eficiência elétrica 0,85.
- Resultado com 10 garrafas/ano: ~205 kg CO₂ evitados/casa (109 kg no cenário adverso), ~33 €/ano; cenário nacional com 1 % de adoção: ~4 500 t CO₂/ano.

## 5. O que NÃO fazer / regras de honestidade
- Não afirmar "somos os primeiros", "sem eletricista", "sem obras", nem que os Tronic se ligam a um gestor de energia (não encontrado na documentação).
- A gestão de cargas já existe no mercado (Schneider Wiser, ABB). Não encontrámos uma ferramenta pública da Bosch que faça este diagnóstico, **o que não prova que não exista**.
- O CO₂ só desce se o gás for mesmo substituído; o DuoWatt tira o bloqueio da potência, não causa a troca sozinho.
- Cada valor novo leva **fonte e classificação** (confirmado / provável / não encontrado). **Não mudar valores por omissão sem o assinalar.**
- Não editar os PDFs nem os .docx da equipa.

## 6. Por confirmar / em aberto
- Base da casa de ~600 W ao serão (sem fonte; com indução de 3 kW o veredicto a 3,45 kVA passa a "precisa de mais potência"). Pedir valor à Mecânica.
- Potência real da indução (1,8 kW é um uso moderado; a placa de 4 zonas tem ~7,2 kW nominais).
- Preço da garrafa (37 € vs. 42–43,5 €), preço por escalões da eletricidade, fator de CO₂ oficial.
- Se o Heatpump Advisor da Bosch pergunta a potência contratada (só se leram descrições; experimentar a ferramenta).
- Prazo útil de trabalho e hora de parar (**por decidir pelo Tiago**), formato exato da entrega, identidade visual/paleta do colega de Multimédia (**por decidir**).
- Falta ainda: guião do pitch (demo de 2–3 minutos, em PT-PT, legível num projetor) e ver a demo no browser (ainda só foi testada sem interface).

## 7. Respostas rápidas às 8 perguntas
1. **Conceito fechado?** Sim, DuoWatt. Alternativas só como proposta em ficheiro à parte.
2. **Hora limite:** por decidir pelo Tiago. Entrega às 17:30; propõe-se parar cedo, deixar `PROGRESSO.md` e uma app estável.
3. **Tokens:** a fase de subagentes já passou; o resto cabe numa sessão só, por fases.
4. **Ponytail:** é uma skill/plugin já instalada na sessão do Tiago ("ponytail:ponytail", modo de programador preguiçoso: a menor alteração que resolve a tarefa, sem funcionalidades a mais). Não há link; usar `/ponytail-help` na sessão que a tem.
5. **Ver a app:** só foi testada com `streamlit.testing.v1.AppTest` e arranque do servidor; nunca num browser. Playwright headless é uma boa opção (não instalado).
6. **Segurança:** a pasta **não** é um repositório git. Fazer `git init` e um commit antes de qualquer trabalho autónomo. Não mexer fora da pasta nem nos PDFs/.docx. Desligar a suspensão do PC é decisão do Tiago.
7. **Para quem é:** demo de 2–3 minutos para o júri, PT-PT, projetor. Pitch e identidade visual ficam com o colega de Multimédia; paleta/logo por receber.
8. **Honestidade e pesquisa:** ver secção 5.

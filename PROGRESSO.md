# PROGRESSO (para retomar: "Lê PROGRESSO.md e continua")

Prompt da missão: `PROMPT_Equipa_Autonoma_DuoWatt.md`. Fonte de verdade do projeto: `CONTEXTO_Projeto_DuoWatt.md`. Entrega: 21 nov 2026, 17:30 (a partir das 14:00, só correções de erros).

## Estado do `main`
- Tag `estavel-3` (21 nov, ~00:55). Testes: 36 a passar, 4 xfail justificados. Na app: separadores 'Diagnóstico' e 'Provas do utilizador' (só dados da Bosch rotulados como secundários; a parte da equipa mostra 'Ainda sem dados' até haver `dados/inquerito_resumo.json`).
- Documentos na pasta: `CRITERIOS_AVALIACAO.md`, `INQUERITO.md`, `ENTREVISTAS.md`, `VIABILIDADE.md`, `DIFERENCIACAO.md`, `PESQUISA.md` (fontes e classificações), `ferramentas/analisar_inquerito.py` (+ testes com CSV sintético, claramente marcado).
- Para a equipa humana (manhã): criar o Google Forms (`INQUERITO.md`), recolher ≥30 respostas, fazer 3 entrevistas (`ENTREVISTAS.md`), exportar o CSV e correr `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv` (escreve em `dados/`; a app passa a mostrar os números).

## Ciclo atual
- Ciclo 4 (branch `ciclo-4`): Programador a acrescentar os separadores 'Viabilidade' e 'Diferenciação' e a tabela de pressupostos citados (item B2/B3). Depois: Júri com a rubrica oficial, `DEMO_GUIAO.md`, `RELATORIO_FINAL.md`.

## Rubrica oficial (ver `CRITERIOS_AVALIACAO.md`; escala 1–5; pesos 20/20/15/15/10; a 6 é só a 25 nov)
| Critério | Peso | Última avaliação do Júri |
|---|---|---|
| 1 Clareza do problema e provas do utilizador | 20 % | por avaliar com a nova rubrica (sem dados reais de utilizadores: 1–2 até a equipa recolher) |
| 2 Impacto mensurável | 20 % | por avaliar |
| 3 Solução e demonstração | 15 % | por avaliar |
| 4 Viabilidade técnica, económica e de implementação | 15 % | por avaliar |
| 5 Originalidade e diferenciação | 10 % | por avaliar |
(Avaliações antigas R1–R7 em `equipa/juri_ciclo0.md` e `equipa/juri_ciclo1.md`: já não se usam.)

## Prioridades novas (recebidas a 21 nov)
A provas do utilizador (INQUERITO.md, ENTREVISTAS.md, `ferramentas/analisar_inquerito.py`, espaço na app só com dados da Bosch enquanto não houver dados reais) · B viabilidade (custos reais, VIABILIDADE.md) · C diferenciação (concorrentes, DIFERENCIACAO.md) · D impacto com pressupostos visíveis e citados · E UI com menos peso · DEMO_GUIAO.md depois.

## Próximo passo
Fechar o lote 2 do ciclo 2 (branch `ciclo-2`), integrar se verde e depois A, B, C, D, E (ver acima). Investigador (custos) a correr.

## Decisões pendentes
Ver `PERGUNTAS.md`.

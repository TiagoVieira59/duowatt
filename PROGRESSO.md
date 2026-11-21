# PROGRESSO (para retomar: "Lê PROGRESSO.md e continua")

Prompt da missão: `PROMPT_Equipa_Autonoma_DuoWatt.md`. Fonte de verdade do projeto: `CONTEXTO_Projeto_DuoWatt.md`. Entrega: 21 nov 2026, 17:30 (a partir das 14:00, só correções de erros).

## Estado do `main`
- Tag `final` (ciclo 6) + commits da noite 2. Testes: 44 a passar, 4 xfail justificados. App: 'Diagnóstico' e 'Provas do utilizador' (só dados Bosch, rotulados, até haver `dados/inquerito_resumo.json`).
- Noite 2: Fase 1 (Forms: `ferramentas/criar_formulario.gs`, `FORMS_INSTRUCOES.md`) feita; Fase 2 (retoma automática) bloqueada por permissões, ver `PERGUNTAS.md` n.º 7; Fase 3 (formato PT-PT em `formato.py`) feita.
- Para a equipa humana: criar o Forms, ≥30 respostas, 3 entrevistas, `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv`.

## Ciclo atual
- **Concluído.** `main` na tag `final` (ciclo 6 integrado). Falta o que depende de pessoas: dados reais (`PLANO_RECOLHA_PROVAS.md`), validações da Mecânica/Contabilidade/eletricista/Bosch, formato da entrega (`PERGUNTAS.md`). Para retomar: 'Lê PROGRESSO.md e continua'.

## Rubrica oficial (ver `CRITERIOS_AVALIACAO.md`; escala 1–5; pesos 20/20/15/15/10; a 6 é só a 25 nov)
| Critério | Peso | Júri ciclo 4 (1–5) |
|---|---|---|
| 1 Clareza do problema e provas do utilizador | 20 % | **1** (sem dados reais de utilizadores; só guiões de recolha) |
| 2 Impacto mensurável | 20 % | 3 (métricas concretas mas simuladas; o CO₂ vem da eletrificação, não do DuoWatt) |
| 3 Solução e demonstração | 15 % | **4** (final; era 3,5) |
| 4 Viabilidade técnica, económica e de implementação | 15 % | 4 (custos com fontes, equilíbrio, próximos passos; nada validado por eletricista ou Bosch) |
| 5 Originalidade e diferenciação | 10 % | 3 (adaptação de soluções conhecidas) |
**Nota ponderada final: 2,9 / 5** (ciclo 4: 2,78). Avaliação final em `equipa/juri_final.md`. O Júri diz que o que mais subiria a nota é a recolha real (inquérito 15–30 respostas + 3 entrevistas, +0,5 na ponderada), depois a validação por eletricista e pela Bosch. Ver `PLANO_RECOLHA_PROVAS.md` e `equipa/juri_ciclo4.md`.
(Avaliações antigas R1–R7 em `equipa/juri_ciclo0.md` e `equipa/juri_ciclo1.md`: já não se usam.)

## Prioridades novas (recebidas a 21 nov)
A provas do utilizador (INQUERITO.md, ENTREVISTAS.md, `ferramentas/analisar_inquerito.py`, espaço na app só com dados da Bosch enquanto não houver dados reais) · B viabilidade (custos reais, VIABILIDADE.md) · C diferenciação (concorrentes, DIFERENCIACAO.md) · D impacto com pressupostos visíveis e citados · E UI com menos peso · DEMO_GUIAO.md depois.

## Próximo passo
Noite 2, Fase 4 (`UX_PESQUISA.md`) e Fase 5 (assistente para a família, relatório, modo detalhado; máx. 3 ciclos), depois fecho §8 do `PROMPT_Noite_2_DuoWatt.md`.

## Decisões pendentes
Ver `PERGUNTAS.md`.

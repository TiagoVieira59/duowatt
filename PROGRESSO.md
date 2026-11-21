# PROGRESSO (para retomar: "Lê PROGRESSO.md e continua")

Prompt da missão: `PROMPT_Equipa_Autonoma_DuoWatt.md`. Fonte de verdade do projeto: `CONTEXTO_Projeto_DuoWatt.md`. Entrega: 21 nov 2026, 17:30 (a partir das 14:00, só correções de erros).

## Estado do `main`
- Tag `estavel-1` (ciclo 1 integrado, 00:38 de 21 nov). Testes: 32 a passar, 4 xfail justificados (dependem de decisões: base ao serão de 600 W, pessoas vs garrafas, etc.). App vista em browser nos 6 cenários; `erros.txt` = sem erros nem avisos.
- O que mudou no ciclo 1: layout para 1366×768 (veredicto, frase, 3 números e gráfico acima da dobra), gráfico Altair 17:00–23:00 com limite rotulado e serão sombreado, avisos honestos compactos, atribuição do impacto (o CO₂ vem da eletrificação; o DuoWatt desbloqueia a troca), extremos coerentes, higiene do modelo.

## Ciclo atual
- Ciclo 1 fechado. Júri do ciclo 1 a avaliar `screenshots/ciclo1c/` (resultado em `equipa/juri_ciclo1.md`). Próximo: ciclo 2 (backlog em `BACKLOG.md`), branch `ciclo-2` a partir do `main`.

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

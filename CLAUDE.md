# CLAUDE.md (instruções para qualquer Claude que abra este repositório)

Projeto DuoWatt, Hackathon@ShiftE 2026, desafio Bosch. Responde sempre em **português europeu (PT-PT)**.

## Começa por aqui
1. Lê `HANDOFF.md` (estado, decisões, comandos, mapa da pasta).
2. Lê `PROGRESSO.md` e `docs/PRODUTO.md` (conceito) e `docs/CRITERIOS_AVALIACAO.md`.

## Conceito fixo
DuoWatt = kit de 2 peças (sensor no quadro + módulo de controlo do cilindro) que completa os cilindros elétricos Bosch: pausa o cilindro antes de a luz ir abaixo (desliga a ~90 %, religa a <80 %, pausa máx. 30 min, modo seguro sem sensor). Só software/simulação, nada de hardware. A fonte de verdade é `docs/referencia/PROMPT_Kit_DuoWatt_Final.md`.

## Regras (não negociáveis)
- **Nunca inventar dados de utilizadores**, citações, resultados de inquérito, preços ou números de negócio (`[a preencher pela Contabilidade]`). Dados reais só em `dados/`.
- Nunca "somos os primeiros", "sem eletricista", "sem obras", nem que os Tronic se ligam a um gestor de energia. Nunca "a Bosch não tem": usar "pelo que vimos na gama Tronic".
- Todo o número novo leva fonte e classificação (confirmado / provável / derivado / pressuposto).
- Sem logótipo, cores ou tipografia da Bosch.
- `main` fica sempre demonstrável: testes verdes e app a arrancar sem erros.
- Não editar os PDFs nem os .docx da equipa (em `docs/referencia/`).

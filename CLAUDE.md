# CLAUDE.md — DuoWatt (app de demonstração)
Responde em PT-PT. Código/comentários em inglês; texto visível em PT-PT.

## Comandos
`npm run dev` · `npm test` · `npm run typecheck` · `npm run build` · `npm run preview`

## Estrutura
- `src/data/facts.ts`: **únicos** números permitidos (valor, tipo, fonte). A UI nunca escreve números à mão.
- `src/data/serao.ts`, `exemplo.ts`: cenário (18:30–21:00) e dados de exemplo.
- `src/domain/controller.ts`: lógica pura `decide(...)`; `simulation.ts` corre o cenário nos dois modos.
- `src/presenter/`: modo apresentação (≥ 1024 px). `src/app/`: a app dentro do telemóvel.
- `entregaveis/`: vídeo, GIF, QR.

## Regras de honestidade
- «Simulação» sempre visível; dados de exemplo com «Dados de exemplo»; estimativas com «≈».
- «Um aparelho grande ligou», nunca o nome do aparelho. Sem temperatura da água. Sem Bosch.
- Frases proibidas: ver PRODUCT.md.
- Sem backend, router nem CDNs; fontes via `@fontsource`.
- `main` com testes verdes e build limpo. Decisões em `DECISOES.md`.

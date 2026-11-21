# Plano de recolha de provas (para a equipa, sábado de manhã)

**Porquê:** o critério 1 (clareza do problema e provas do utilizador) pesa **20 %** da nota de sábado. O último Júri deu **1 em 5**, porque ainda não há dados reais da equipa. É o maior ganho possível, e só a equipa o pode fazer. Estimativa do ganho: +0,5 na nota ponderada (do Júri) com 15–30 respostas e 3 entrevistas.

## Quem faz o quê (sugestão; ajustar à equipa)
| Quem | Tarefa | Tempo |
|---|---|---|
| Informática | Correr o script `ferramentas/criar_formulario.gs` (ver o cabeçalho do ficheiro) e partilhar o link no grupo | 5 min |
| Todos | Partilhar o link: família, vizinhos, condomínio, colegas de residência, redes sociais, grupos de moradores (meta: 30 respostas; mínimo útil: 15) | 20 min |
| Mecânica + Contabilidade | Entrevista perfil C (eletricista): `ENTREVISTAS.md` | 15 min |
| Ciência Política + Multimédia | Entrevista perfil A (morador com gás de garrafa) e perfil B (loja ou instalador de esquentadores; por exemplo, ir a uma loja de eletrodomésticos ou de material elétrico) | 30 min |
| Informática | Exportar o CSV, correr o analisador, reiniciar a app e colar os números no pitch | 10 min |

## Passos técnicos (Informática)
1. Em https://script.google.com: novo projeto, colar `ferramentas/criar_formulario.gs`, executar `criarFormulario`. (Alternativa: criar o Forms à mão com `INQUERITO.md`.) O script não foi testado, e se falhar basta criar à mão.
2. Respostas → Ficheiro → Transferir → .csv.
3. Na pasta do projeto: `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv` (escreve em `dados/`).
4. Reiniciar a app: o separador "Provas do utilizador" passa a mostrar n, os números principais e os gráficos.
5. Entrevistas: preencher uma ficha de `ENTREVISTAS.md` por entrevista (citações literais, sem editar). Guardar as fichas no repositório (pasta `dados/entrevistas/`).

## O que dizer no pitch (só com dados reais)
- "Perguntámos a [N] pessoas com gás de garrafa: [X %] nunca pensaram em trocar, [Y %] já tiveram o quadro a disparar, [Z %] comprariam outro aparelho a gás se avariasse hoje."
- "Falámos com [um eletricista, um instalador, um morador]: [citação literal]."
- Se houver menos de 30 respostas: dizer o n e que as percentagens são indicativas.

## Regras
- Nunca preencher o formulário em nome de outras pessoas nem inventar respostas ou citações.
- Anónimo: sem nomes nem emails.
- Se os resultados contradisserem a nossa ideia (por exemplo, ninguém quer o dispositivo), **dizê-lo**. É isso que o júri valoriza, e a app foi feita para o mostrar.

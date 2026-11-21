# UX_PESQUISA: regras de interface para o DuoWatt

Pesquisa feita a 21 nov 2026. Só entram regras que li nas fontes indicadas.
Classificação: **confirmado** = lido na fonte; **provável** = de snippet de pesquisa ou inferência; **hipótese** = decisão nossa.

Não consegui ler: o PDF da ERSE sobre potência contratada (ilegível via WebFetch) e a página "Use clear language" do GOV.UK.

---

## 1. GOV.UK Design System (confirmado)

**Uma pergunta por página.**
"Asking just one question per question page helps users understand what you're asking them to do."
Fonte: https://design-system.service.gov.uk/patterns/question-pages/
Se houver perguntas relacionadas numa página, usar título em forma de afirmação. Pedir cada informação só uma vez por percurso.
**Como se aplica ao DuoWatt:** cada uma das 4 perguntas num ecrã próprio, com contador "Pergunta 2 de 4". O relatório não volta a perguntar o que já foi respondido.

**Mensagens de erro.**
"explain what went wrong and how to fix it." Linguagem simples, positiva, direta. Evitar "An error occurred" e "Select an option". Não usar "you forgot" nem "sorry". A mesma frase no campo e no resumo.
Fonte: https://design-system.service.gov.uk/components/error-message/
Resumo de erros: "Always show an error summary when there is a validation error, even if there's only one." Título "There is a problem.", link ao campo com erro, foco movido para o resumo, "Error: " no `<title>`.
Fontes: https://design-system.service.gov.uk/components/error-summary/ e https://design-system.service.gov.uk/patterns/validation/
**Como se aplica ao DuoWatt:** kVA a zero ou vazio mostra "Indique a potência contratada, por exemplo 3,45 kVA. Está na fatura de eletricidade." Mesma frase no campo e no resumo.

**Página de resultado / confirmação.**
Deve dizer que a tarefa está concluída, o que acontece a seguir e quando, a quem contactar se algo correr mal, e uma forma de guardar registo (por exemplo, PDF). Confirmation pages "reassure users that they have completed a transaction". Não colocar links ou botões dentro do painel de confirmação sem garantir contraste de 3:1.
Fonte: https://design-system.service.gov.uk/patterns/confirmation-pages/
**Como se aplica ao DuoWatt:** o veredicto é a página de resultado. Tem de dizer o próximo passo (falar com o instalador), o relatório de 1 página é o registo a descarregar, e há um contacto de ajuda.

---

## 2. As 10 heurísticas de Nielsen (confirmado; tradução nossa)

Fonte: https://www.nngroup.com/articles/ten-usability-heuristics/

1. Visibilidade do estado do sistema
2. Correspondência entre o sistema e o mundo real
3. Controlo e liberdade do utilizador
4. Consistência e padrões
5. Prevenção de erros
6. Reconhecimento em vez de memorização
7. Flexibilidade e eficiência de utilização
8. Design estético e minimalista
9. Ajudar a reconhecer, diagnosticar e recuperar de erros
10. Ajuda e documentação

**Como se aplica ao DuoWatt:** (1) barra de progresso nas 4 perguntas; (2) "potência contratada" com a palavra da fatura; (3) botão "Voltar" e "Recomeçar" sempre visíveis; (4) mesmos nomes de campo no ecrã e no relatório; (5) limites nos campos (ex.: pessoas entre 1 e 12, hipótese); (6) ajuda visível por baixo de cada pergunta, sem obrigar a memorizar; (7) atalho para quem já sabe o kVA, mas sem ser obrigatório; (8) veredicto primeiro, detalhe depois; (9) erro em linguagem simples com a correção; (10) ajuda curta e no sítio certo.

---

## 3. WCAG 2.2 AA (confirmado, salvo indicação)

Fontes: https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html ; https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html

- **1.4.3 Contraste (AA):** "at least 4.5:1" para texto; 3:1 para texto grande.
- **1.4.4 Redimensionar texto (AA):** texto amplia-se até 200% "without loss of content or functionality". Nenhum critério lido fixa um tamanho mínimo em px.
- **2.4.7 Foco visível (AA):** "the keyboard focus indicator is visible".
- **2.4.11 Foco não obscurecido (AA):** o componente focado não pode ficar "entirely hidden due to author-created content".
- **2.5.8 Tamanho dos alvos (AA):** mínimo 24 × 24 CSS px, com exceções (espaçamento, texto em linha, etc.).
- **2.5.5 Tamanho dos alvos (AAA):** 44 × 44 CSS px. O critério AA usa 24 px; os 44 px são o critério AAA. Tratamos 44 px como recomendação nossa.
- **1.4.10 Reflow (AA):** conteúdo a 320 CSS px de largura, sem scroll horizontal.
- **1.4.12 Espaçamento do texto (AA):** altura de linha ≥ 1,5×; espaço entre parágrafos ≥ 2×; letras ≥ 0,12×; palavras ≥ 0,16×.
- **3.3.1 Identificação de erros (A):** o item em erro é identificado e "described to the user in text".
- **3.3.2 Rótulos ou instruções (A):** "Labels or instructions are provided when content requires user input."

**Como se aplica ao DuoWatt:** contraste 4,5:1 no veredicto e nas cores de estado (verde/vermelho/amarelo); botões com 44 px de altura (recomendação); foco visível no Streamlit (não tapar com barras fixas); 320 px sem scroll horizontal; rótulo visível em cada campo, não só placeholder; erro escrito em texto, não só a cor.

---

## 4. Linguagem simples

- **Frase de referência:** "The message must be in plain English, use positive language and get to the point." Fonte: https://design-system.service.gov.uk/components/error-message/
- **kVA:** a DECO indica a unidade como "quilovolts-ampere (kVA)" e diz que a potência contratada "Está relacionada com o uso simultâneo de aparelhos e a sua potência". A DECO não explica o termo mais do que isto. Fonte: https://www.deco.proteste.pt/casa-energia/eletricidade-gas/dicas/fatura-eletricidade-como-ler-cada-campo-saber-que-esta-pagar. Regra "nunca kVA sem explicar": **decisão nossa**.
- **Onde encontro na fatura:** na fatura da DECO, a potência contratada é o item 3, com o valor diário e o número de dias do período. O layout varia de comercializador para comercializador (**provável**; a fonte da ERSE não foi lida).

**Como se aplica ao DuoWatt:** o campo diz "Potência contratada (kVA)" e, por baixo, "Está na fatura, na linha 'Potência contratada'. Exemplo: 3,45 kVA." Ao lado, um "Onde encontro isto na fatura?" aberto por clique, com a frase "procure 'Potência contratada'". Os textos de ajuda para placa de cozinha e garrafas são **hipótese**, a testar com utilizadores.

---

## 5. Telemóvel primeiro, 390 × 844 (confirmado na largura; provável na altura)

- **Largura 390 CSS px:** a lista de viewports indica "390: iPhone 12/12 Pro/13/13 Pro/14", com `width=device-width`. Fonte: https://firt.dev/notes/viewports
- **Altura 844:** veio de snippets de pesquisa, sem página lida (**provável**). A altura útil muda com a barra do browser, por isso serve como base de teste, não como garantia.

**Como se aplica ao DuoWatt:** desenhar primeiro a 390 px de largura e testar também a 320 px (critério 1.4.10). Um só botão principal por ecrã, na parte de baixo, ao alcance do polegar.

---

## 6. Oito regras de implementação

1. Uma pergunta por ecrã Streamlit, com contador "Pergunta n de 4".
2. Erro: resumo no topo com "Há um problema", frase igual no campo, diz o que falhou e como corrigir. Sem "sorry" nem "você esqueceu".
3. Cada campo tem rótulo visível e ajuda curta por baixo. O placeholder não conta como rótulo.
4. Texto com contraste de pelo menos 4,5:1. Verificar as cores de estado com um validador.
5. Alvos com pelo menos 24 px; botões principais com 44 px.
6. Foco visível em todos os controlos; nada fixo a tapar o foco.
7. Layout sem scroll horizontal a 320 px; testar 390 × 844 primeiro.
8. kVA sempre com explicação na mesma linha, "Onde encontro na fatura?" sempre disponível, e o resultado com próximo passo e registo para descarregar.

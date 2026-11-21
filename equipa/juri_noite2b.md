# Júri independente, noite 2b (entrega 21 nov)

Fontes lidas: CRITERIOS_AVALIACAO.md, enunciado, 8 screenshots, IMPACTO.md, VIABILIDADE.md, DIFERENCIACAO.md.

## Notas (1-5)
| Critério | Peso | Nota | Justificação |
|---|---|---|---|
| C1 Problema e provas do utilizador | 20 | 1 | Nos documentos lidos não há entrevistas, inquérito nem observação; o problema assenta nos números do enunciado e em pesquisa web. Sem dados reais não passa de 1. |
| C2 Impacto mensurável | 20 | 4 | Métrica concreta (casas desbloqueadas, t CO2, % das 870 kton, M€), pressupostos classificados, sensibilidade e limites honestos (2,7 % com 10 % de adoção). Perde por a adoção e o teto de 44 % serem hipótese/proxy. |
| C3 Solução e demonstração | 15 | 3 | Protótipo navegável e coerente (5 perguntas, veredicto, modo detalhado). Não responde a provas recolhidas (não há) e nos screenshots de projetor há widgets em branco. |
| C4 Viabilidade | 15 | 4 | Custos com fonte, comparação a 10 anos, fases, riscos e passos para a Bosch. Falta validação de segurança, anti-legionela e custo industrial. |
| C5 Originalidade | 10 | 3 | A equipa admite "adaptação de soluções conhecidas"; concordo. |

**Nota ponderada = (1×20 + 4×20 + 3×15 + 4×15 + 3×10) ÷ 80 = 235 ÷ 80 = 2,94 / 5.**
Com C1 = 3 (algumas entrevistas reais) seria 3,19; com C1 = 4, 3,44.

**Facilidade para pessoa comum: 4/5.** Telemóvel claro, 5 perguntas, "Não sei", ajuda para a fatura, resultado em linguagem simples. Tira ponto: resultado longo e denso, tabela estreita com "0,3 %" a partir em linhas, jargão (kVA, termoacumulador).

## Problemas de impacto alto e rápidos (por ordem)
1. **C1 sem dados reais.** Recolher já (mesmo 5-10 respostas ou 2-3 entrevistas, incl. um instalador) e pôr só em `dados/`, com as conclusões ligadas ao veredicto. É 20 % do peso e a única nota 1. Se não der, dizer abertamente que a recolha é o próximo passo e não inventar nada.
2. **Screenshots de projetor com elementos em branco.** No passo 1 as opções de potência e os botões não aparecem; no resultado extremo a tabela de impacto está vazia. Verificar se é só captura antes de carregar, ou erro real; num projetor isto mata a demo.
3. **Resultado extremo confuso.** Mostra "14 min sem água (sem gestão: 3 min)", ou seja, a gestão parece piorar. Explicar numa linha (a pausa do termoacumulador é o que custa água quente) ou esconder a comparação neste caso. Dá também "Sem estimativa" para o custo, apesar de o VIABILIDADE ter 6,9 kVA (~64-78 €/ano); mostrar o valor ou dizer o que fazer a seguir.
4. **Resultado móvel denso.** Mover a tabela 1/5/10 % para um "ver impacto nacional" recolhido, ou dar-lhe colunas legíveis; manter só o veredicto, 3 cartões e o botão do relatório à vista.
5. **Números inconsistentes entre ecrã e documentos.** O ecrã diz 202-282 € e o VIABILIDADE ~200-280 €; alinhar arredondamentos para não parecer erro perante o júri.

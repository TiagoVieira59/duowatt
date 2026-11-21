# Júri Bosch: avaliação final (21 nov 2026)

Materiais lidos: PDF do desafio, CRITERIOS_AVALIACAO.md, PRODUTO.md, screenshots ecra1-3 (1920) e ecra1 (390). Código, outros documentos e equipa/ não foram lidos.

## Notas (escala 1-5)
| # | Critério | Peso | Nota | Justificação (evidência) | O que faria subir |
|---|---|---|---|---|---|
| 1 | Problema e provas do utilizador | 20 % | **1** | PRODUTO.md só cita o enunciado Bosch (85 %, INE 2020), dados secundários. Nada de entrevistas, inquérito ou observação feita pela equipa. | Qualquer dado real, mesmo pequeno (ex.: 5 entrevistas curtas a famílias com 3,45 kVA / a instaladores), apresentado como tal. |
| 2 | Impacto mensurável | 20 % | **3** | Métricas concretas: ~246 kg CO₂/casa/ano (131 no cenário adverso), ~5 419 t/ano a 1 %, 64-78 €/ano evitados; pressupostos rotulados (PRODUTO.md, ecra2/3). Mas o 1 % é arbitrário, a ligação ao "870 kton" do desafio é indireta (o CO₂ vem de a casa sair do gás, não do kit) e não há taxa de conversão suportada. | Ligar a uma conta explícita: trocas urgentes/ano × % que o kit converte de gás por gás → CO₂; mostrar o intervalo. |
| 3 | Solução e demonstração | 15 % | **3** | Demo navegável de 3 ecrãs, coerente e clara (119 % "a luz foi abaixo" → 75 % "cilindro em pausa"). Mas: ilustração com rótulos em serifa por defeito, "Imagem concetual a adicionar", "[números de negócio a preencher pela Contabilidade]" visíveis no ecrã 3, e a demo não responde a provas recolhidas (não existem). | Remover placeholders; uniformizar tipografia do SVG. |
| 4 | Viabilidade técnica/económica/implementação | 15 % | **2** | Técnica plausível (sensor + relé, regra 90/80/30, modo seguro) e próximos passos (piloto, integração 5501i, CE). Mas sem custo do kit, preço, margem nem payback: "a preencher". Segurança "por validar"; tempo de corte do contador é pressuposto. | Estimativa de custo/benefício, mesmo grosseira e rotulada como pressuposto. |
| 5 | Originalidade e diferenciação | 10 % | **3** | Tabela de concorrência honesta (quem paga, quando vende, sem hub/app); reconhece que a tecnologia já existe (Shelly, Schneider...). Adaptação interessante, não abordagem nova. | Manter a honestidade; reforçar o canal Bosch/instalador na avaria. |

**Nota ponderada = (1×20 + 3×20 + 3×15 + 2×15 + 3×10) ÷ 80 = 185 ÷ 80 = 2,31 / 5**

## 5 perguntas mais prováveis do júri e respostas sugeridas
1. **Que utilizadores ouviram? Como sabem que o medo do apagão é real?**
   Resposta: "Ainda não temos dados nossos de utilizadores; partimos do enunciado Bosch (60 % das compras são urgentes, 85 % de gás por gás, limites de 3,45/6,9 kVA) e do caso de uso de 3,45 kVA. O primeiro passo do piloto é validar o medo com famílias e instaladores." Não inventar nada.
2. **O desafio fala de espaço (60 %) e falta de instaladores (70 000). O que resolve?**
   Resposta: "Resolve só a barreira da potência contratada. Não resolve o espaço: 67 % têm esquentador e 17 % termoacumulador (INE 2020), e assumimos esse limite. Também precisa de eletricista habilitado, por isso a venda deve vir do instalador Bosch na troca."
3. **Quanto custa o kit e quem ganha dinheiro?**
   Resposta: "Cliente é a Bosch (B2B): troca uma venda de esquentador a gás por uma de cilindro. Os custos do kit ainda não estão fechados, são o próximo passo com a Contabilidade e a Bosch. Para a família o ganho é não pagar a subida de potência (~64-78 €/ano, estimativa)."
4. **De onde vêm as 5 419 t e os 246 kg? É credível?**
   Resposta: "São derivados: CO₂ evitado quando a casa sai do gás (12 garrafas/ano), com cenário adverso de 131 kg; o 1 % das casas a gás é um cenário ilustrativo, não uma previsão. O DuoWatt tira a barreira, não é ele que reduz o CO₂ sozinho."
5. **Isto já existe (gestores de carga) e a Bosch não pode fazê-lo sozinha?**
   Resposta: "Existe em quadros e hubs; a nossa diferença é o par emparelhado para o cilindro, pago pela Bosch e vendido na avaria. Sim, a Bosch pode integrá-lo no Tronic 5501i: é a evolução prevista; o kit valida a regra num piloto."

## 3 melhorias rápidas (≤ 30 min)
1. **Retirar os placeholders visíveis no ecrã 3** ("Imagem concetual a adicionar", "[números de negócio... Contabilidade]"): trocar por um diagrama simples ou remover, e por uma linha de "custo/preço: pressuposto a validar no piloto" com um intervalo rotulado. Sobe c3 e c4.
2. **Mostrar a conta do impacto em 3 linhas** (trocas urgentes → % convertida → kg CO₂, com cenário base e adverso) e dizer explicitamente que o 1 % é cenário. Sobe c2 de forma credível.
3. **Declarar a evidência na própria demo/pitch**: um bloco "O que sabemos / o que falta validar" com fontes (enunciado, INE) e o plano de piloto, sem inventar utilizadores. Protege contra a pergunta 1 e a credibilidade (c1 continua baixo, mas honesto). Corrigir também a fonte serifada dos rótulos "a aquecer"/"em pausa" no SVG.

# Júri noite 2, ciclo 2 (critérios 1 a 5)

Base: juri_final.md, PROGRESSO.md, UX_PESQUISA.md, screenshots/noite2 (móvel 390×844, portátil 1366×768, projetor 1920×1080). `dados/` está vazio: continua sem dados reais de utilizadores.

| # | Critério | Antes | Agora | Evidência |
|---|---|---|---|---|
| 1 | Problema e provas do utilizador (20 %) | 1 | **1** | Sem inquérito nem entrevistas; só guiões e números secundários da Bosch. O assistente não altera isto. Não se aceita nenhum dado inventado. |
| 2 | Impacto mensurável (20 %) | 3 | **3** | 246 kg CO2/ano, 64-78 €/ano, payback 2,6-4,4 anos, com "estimativa, sem validação". Mas o CO2 vem da eletrificação e não do DuoWatt (a app admite-o), e a adoção e a proporção de casas continuam sem dado real. |
| 3 | Solução e demo (15 %) | 4 | **4** (4,25 a arredondar) | Protótipo navegável em telemóvel e computador, veredicto primeiro, relatório para o instalador, modo detalhado com gráfico. Não chega a 5 porque não responde a provas recolhidas, que não existem. |
| 4 | Viabilidade (15 %) | 4 | **4** | Sem alterações. Falta validação de eletricista e da Bosch. |
| 5 | Originalidade (10 %) | 3 | **3** | Relatório na diferenciação ajuda, mas a anterioridade continua por verificar. |

**Nota ponderada = (1×20 + 3×20 + 4×15 + 4×15 + 3×10) ÷ 80 = 2,9 / 5** (igual). A noite 2 melhorou a usabilidade, não a pontuação: o teto está nos dados reais.

## Facilidade para uma pessoa comum: 4 / 5
Uma pergunta por ecrã, barra "Passo 1 de 5", ajuda "procure Potência contratada na fatura", opção "Não sei", "Não guardamos nada", veredicto em frase simples, botão de descarregar relatório. Perde um ponto por: botão "Voltar" quase invisível no passo 1 (cinzento claro sobre branco, contraste fraco); texto pequeno e cinzento nos avisos; no modo detalhado "Poupança 40 €/ano" convive com "evita 64-78 €/ano" no resultado (parecem contradizer-se sem explicação); o modo detalhado em 1366×768 mostra "Min. sem água 0→0" cortado pela barra de ferramentas do gráfico; termos como "kVA", "termoacumulador" e "disparo" sem glossário no resultado; "n/d" nos cartões do caso extremo é seco (o veredicto é bom, mas os cartões vazios parecem erro). O ecrã de 1920×1080 aproveita só uma coluna estreita, o que é aceitável.

## 5 itens de maior impacto (por ordem)
1. **Recolher dados reais** (inquérito 30 ou mais, 3 entrevistas, eletricista) e inseri-los em `dados/` e no separador Provas: C1 de 1 para 3-4 (+0,5 a 0,75 na ponderada). Só a equipa humana pode fazer; nada substitui isto.
2. **Dado real da proporção de casas a GPL com 3,45 kVA** e adoção sustentada (E-REDES/ERSE, inquérito): C2 de 3 para 4.
3. **Validação por eletricista e pela Bosch** (controlo externo do Tronic, segurança): C4 de 4 para 5.
4. **Verificar anterioridade** (Heatpump Advisor, ERSE, Legrand/Schneider) e perguntar a um instalador sobre o momento da avaria: C5 de 3 para 4.
5. **Resolver a incoerência 40 €/ano vs 64-78 €/ano** (e a lacuna do esquentador/espaço, 67 % e 60 %) com uma frase explicativa: protege C2 e C3 contra a objeção do júri a 25 nov.

## Impacto baixo (não fazer antes de 1 a 5)
- Contraste do botão "Voltar" e tamanho do texto cinzento (corrigir só se houver tempo, são erros e não funcionalidades).
- Posição da barra de ferramentas do gráfico sobre "0→0".
- Substituir "n/d" por frase mais amigável.
- Mais ecrãs ou animações; layout para projetor; novos separadores.
- Glossário de termos (útil, mas não altera nenhum critério).

Nota: a partir das 14:00 de 21 nov só correções de erros; os itens 1 a 4 dependem de pessoas, não de código.

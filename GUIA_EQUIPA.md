# Guia da equipa DuoWatt (para ler no telemóvel)

Entrega: **sábado 21 nov, 17:30**. Às **14:00** a app congela: depois disso só se corrigem erros. Pitch a 25 nov.

## 1. O DuoWatt numa frase e num parágrafo
**Numa frase:** uma ferramenta que, no dia em que o esquentador a gás avaria, diz à família se a casa aguenta passar a elétrico sem aumentar a potência contratada.

**Num parágrafo:** muitas casas têm 3,45 kVA. Se ligarem ao mesmo tempo a placa de indução e o termoacumulador, o quadro dispara. O DuoWatt faz duas coisas: (1) diagnostica a casa em 5 perguntas simples e dá um veredicto; (2) propõe uma gestão de potência que pausa o termoacumulador quando a casa está no limite, para não ser preciso subir o contrato. No fim, a família descarrega um relatório de uma página para levar ao instalador. É só software e simulação: não há protótipo físico nem nada validado por um eletricista.

## 2. O desafio da Bosch e os critérios
Desafio: ajudar os portugueses a trocar o gás por elétrico (2,2 milhões de casas ainda usam gás de garrafa).

| # | Critério | Peso |
|---|---|---|
| 1 | Clareza do problema e provas do utilizador | 20 % |
| 2 | Impacto mensurável | 20 % |
| 3 | Solução e demonstração | 15 % |
| 4 | Viabilidade técnica, económica e de implementação | 15 % |
| 5 | Originalidade e diferenciação | 10 % |
| 6 | Pitch e perguntas (só a 25 nov) | 20 % |

O critério 1 só sobe com **dados reais** que nós recolhermos. É a maior alavanca que temos.

## 3. O que está feito
- App em Streamlit: assistente de 5 perguntas, página de resultado com veredicto, 3 números e tabela de impacto (casas desbloqueadas, CO₂, % das 870 kton), relatório para o instalador, e um «modo detalhado» com gráficos, custos, diferenciação e provas.
- Inquérito pronto (Google Forms) e guiões de 3 entrevistas.
- Documentos de impacto (IMPACTO.md), custos e plano por fases (VIABILIDADE.md) e concorrentes (DIFERENCIACAO.md), cada número com fonte.
- Screenshots: pasta `screenshots/final/` (resultado no telemóvel e no portátil).

## 4. Números principais e o que falta validar
| Número | Valor | Estado |
|---|---|---|
| Casas a gás de garrafa | 2,2 milhões | Enunciado Bosch |
| CO₂ evitado por casa | ~246 kg/ano (pior cenário ~131; 12 garrafas por ano) | Derivado (APA 2023); vem da eletrificação, não só do DuoWatt |
| Subir de 3,45 para 6,9 kVA | 64–78 €/ano | Derivado (ERSE); IVA por verificar |
| DuoWatt instalado | ~202–282 € | Derivado; mão de obra é hipótese |
| Tempo até compensar | ~3–4 anos | Derivado |
| Casas com ≤3,45 kVA | ~44 % | Proxy (E-REDES), inclui não domésticos |
| Impacto atribuível com 1 / 5 / 10 % de adoção | ~2 400 / ~11 900 / ~23 800 t CO₂/ano (0,3 / 1,4 / 2,7 % das 870 kton) | Derivado; adoção é hipótese (ver IMPACTO.md) |
| Mercado da Bosch | 60 M€/ano (enunciado); 0,3 / 1,3 / 2,6 M€ proporcionais | Hipótese de proporcionalidade |

**Por validar:** segurança elétrica (eletricista habilitado), se algum Tronic aceita controlo externo (não encontrámos), preços de mão de obra, potência real da placa de indução, consumo de base da casa.

## 5. A equipa e o que cada pessoa faz hoje
Somos 4, de áreas diferentes: **Multimédia e Tecnologias de Comunicação**, **Informática** (Tiago), **Engenharia Mecânica** e **Mestrado em Contabilidade e Controlo de Gestão**.

| Perfil | Tarefa | Prazo |
|---|---|---|
| Todos | Partilhar o link do inquérito (texto em FORMS_INSTRUCOES.md) em 5 grupos e com 5 pessoas | 12:00 |
| Engenharia Mecânica | Confirmar potência da placa de indução (1,8 / 3 kW), consumo de base ao serão e se o termoacumulador pode ser pausado com segurança; se conseguir, falar com um eletricista ou instalador (guião C/B em ENTREVISTAS.md) | 13:00 |
| Contabilidade e Controlo de Gestão | Confirmar custos: garrafa (37 €), mão de obra do eletricista, preço do termo de potência e IVA; rever as contas de equilíbrio em VIABILIDADE.md | 13:00 |
| Multimédia e Tecnologias de Comunicação | Rever a app no telemóvel (cores, legibilidade, texto), fazer 2 entrevistas a moradores com os guiões em ENTREVISTAS.md (citações literais) e preparar os slides/pitch | 13:30 |
| Informática (Tiago) | Exportar o CSV, correr `analisar_inquerito.py`, colar entrevistas em `dados/entrevistas.json`, rever a app e fazer a entrega | 14:00 congelar; 17:30 entregar |

As 3 entrevistas (morador, instalador/loja, eletricista) repartem-se assim por não termos ninguém de Ciências Sociais: podem trocar entre vocês, o importante é serem feitas e escritas palavra por palavra.

## 6. Como recolher as provas
- **Link do Forms:** [o Tiago cola aqui o link depois de executar o script]
- **Meta:** 30 respostas (mínimo útil: 15) e 3 entrevistas (1 por perfil).
- **Guiões das entrevistas:** em `ENTREVISTAS.md`. Escrever o que a pessoa disse, palavra por palavra. Nunca inventar nem «arredondar» respostas.

## 7. O que nunca dizer, e as 5 perguntas prováveis
**Nunca dizer:** «somos os primeiros»; «ninguém faz isto»; «sem eletricista»; «sem obras»; que os Tronic se ligam a um gestor de energia; que o DuoWatt poupa muito dinheiro (a mensagem é descarbonizar sem custar mais); dados de utilizadores que não sejam reais.

| Pergunta | Resposta honesta |
|---|---|
| Quanto CO₂ é do DuoWatt? | A redução vem de trocar gás por elétrico. O DuoWatt retira o bloqueio da potência, que afeta no máximo ~44 % das casas (limite superior). |
| Quanto custa e quem instala? | ~202–282 €, instalado por eletricista habilitado. São preços de retalho, não uma cotação. |
| Isto já existe? | A gestão antidisparo existe (Legrand, Schneider). Não encontrámos um diagnóstico gás → elétrico no momento da avaria, mas não encontrar não prova que não exista. |
| E o espaço e o esquentador? | 67 % das casas têm esquentador e só 17 % termoacumulador; muitas não têm espaço. O DuoWatt resolve a potência, não o espaço. |
| Onde estão as provas? | [N] respostas e [N] entrevistas da equipa; os dados da Bosch são secundários. Se ainda não houver, dizê-lo. |

## 8. Perguntas em aberto para decidir
1. Qual é o formato exato da entrega das 17:30 (documento, link, vídeo, protótipo)? E o que se apresenta a 25 nov?
2. Quem confirma os custos e a segurança elétrica antes das 14:00?
3. Há paleta ou logo da equipa para a app? (Não pode imitar a marca Bosch.)

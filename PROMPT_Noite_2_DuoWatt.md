# Missão (noite 2): DuoWatt pronto para o júri e para pessoas comuns

Lê primeiro o `PROGRESSO.md`, o `CRITERIOS_AVALIACAO.md` e o `CLAUDE.md` (regras não negociáveis, que continuam em vigor). Tudo em PT-PT. Mantém o mesmo método de equipa do `PROMPT_Equipa_Autonoma_DuoWatt.md` (coordenador + agentes, ciclos, júri independente, `main` sempre demonstrável), com as alterações abaixo.

O Tiago vai dormir e acorda às **08:30**. Trabalhas sozinho até concluíres o que está aqui, ou até às **08:00** (o que vier primeiro). A partir daí não começas nada novo: fazes o fecho (§8). O congelamento das 14:00 mantém-se.

---

## 1. Objetivo

Levar a nota ponderada do júri (critérios oficiais 1 a 5) o mais alto possível, e tornar a app **amigável para pessoas comuns**. Nota de partida: 2,9/5 (C1=1, C2=3, C3=4, C4=4, C5=3).

Sê honesto sobre o teto: o **C1 (provas do utilizador) não sobe com software**, só com dados reais. O teu trabalho no C1 é tornar a recolha fácil (Forms) e a integração automática.

---

## 2. Decisões do Tiago (já tomadas)

- **Utilizador principal:** a família, no momento da avaria do esquentador. O ecrã principal é um **assistente passo a passo** para ela. Os gráficos e os números técnicos ficam num **"Modo detalhado"** para o júri e para o instalador.
- **Funcionalidade nova autorizada (só esta):** no fim do diagnóstico, um **relatório de uma página** para descarregar ou imprimir, para a família levar ao instalador (veredicto, o que é preciso, pressupostos, CO₂ e custo). Ataca o bloqueio "troca à pressa na avaria" e o critério 5.
- **Push para o GitHub autorizado:** `git push origin main --tags` no fim de cada ciclo estável. Nunca `--force`. Nunca reescrever histórico.
- **Identidade visual:** escolhes tu um estilo neutro e profissional. **Proibido imitar a marca Bosch** (logo, vermelho oficial, tipografia da marca): não pode parecer um produto oficial da Bosch.
- **Stack:** fica em Python + Streamlit. Tema próprio, CSS, `st.session_state` para o assistente. Se o Streamlit limitar mesmo, regista em `ALTERNATIVAS.md`.
- **A equipa recebe os documentos pelo WhatsApp.**

---

## 3. Ordem de trabalho (por prioridade; não saltes fases)

### Fase 1: Google Forms (URGENTE, primeiro de tudo, ~15 min)
O Tiago vai executar o script **antes de dormir**, para as respostas chegarem durante a noite.
1. Revê e corrige `ferramentas/criar_formulario.gs` (Google Apps Script, `FormApp`). As perguntas vêm do `INQUERITO.md`. Valida com cuidado a sintaxe e os tipos de pergunta, porque não o podes executar.
2. O formulário tem de ser **anónimo**: não pede nome, email nem morada. No início, um texto curto de consentimento e finalidade (hackathon da Universidade de Aveiro, dados só para este trabalho, respostas anónimas).
3. O script deve, no fim, registar (`Logger.log`) o **link de resposta** e o **link de edição**, e ligar as respostas a uma Google Sheet.
4. Cria `FORMS_INSTRUCOES.md`, com no máximo 6 passos: abrir script.google.com, novo projeto, colar, executar, autorizar, copiar o link. Inclui um **texto pronto para o WhatsApp** a pedir respostas (curto e simpático, a dizer que são 2 minutos e é para quem tem gás de garrafa ou esquentador).
5. Confirma que `ferramentas/analisar_inquerito.py` lê o CSV exportado **exatamente com os títulos das colunas** que este formulário gera. Se não, corrige-o e testa-o com um CSV sintético marcado como sintético.
6. Commit, push, e escreve no chat: **"Tiago: o Forms está pronto, vê FORMS_INSTRUCOES.md."** Depois continua sem esperar resposta.

### Fase 2: Retoma automática depois do limite do plano (~10 min)
O limite do plano Pro repõe às **03:50**. Quando o limite chega, esta sessão pára e não recomeça sozinha. Prepara uma retoma:
1. Encontra o executável do Claude Code: `which claude`, `claude --version`; se não estiver no PATH, procura em `~/.vscode/extensions/anthropic.claude-code-*/` e `~/.local/bin/`. Se não o encontrares, regista em `PERGUNTAS.md` e salta esta fase.
2. Se o encontrares, cria `ferramentas/retomar.sh`, que:
   - usa caminhos absolutos (o cron tem um PATH mínimo);
   - entra na pasta do projeto;
   - só corre se existir o ficheiro `.retomar_ativo` e não existir `.retomar_lock` (cria o lock ao começar e apaga-o no fim);
   - corre o Claude Code em modo não interativo com o prompt "Lê PROGRESSO.md e o PROMPT_Noite_2_DuoWatt.md e continua do ponto em que ficaste. Não repitas o que já está feito.", pré-autorizando só as ferramentas necessárias (`--allowedTools` com Read, Edit, Write, Bash, WebSearch, WebFetch e a de subagentes). **Não** uses `--dangerously-skip-permissions`;
   - escreve o resultado em `ferramentas/retomar.log`.
3. Agenda com `crontab` duas execuções únicas: **03:55** e **05:30** (a segunda cobre o caso de a primeira também bater no limite). Testa o script uma vez com um prompt mínimo ("responde só OK") para confirmar que arranca.
4. Quando concluíres a missão, **apaga o `.retomar_ativo` e remove as entradas do crontab**, para nada voltar a correr.

### Fase 3: Correções pendentes (~20 min)
1. Formatação PT-PT: uma função única (espaço nos milhares, vírgula nos decimais) usada em toda a app. Hoje aparece "2 2 M" e "≤3 45 kVA" (o `.replace(",", " ")` é aplicado à frase inteira, linhas ~97, 112, 113, 175, 180 e 199 do `app.py`). Teste para a função.
2. Eixo Y do gráfico em formato PT-PT ("5 000", não "5,000").
3. `PROGRESSO.md`: as secções "Estado do main" e "Próximo passo" contradizem-se (estavel-3 vs. final vs. "fechar lote 2"). Reescreve-as com o estado real.

### Fase 4: Pesquisa de UX (agente Investigador + Auditor UX, ~20 min)
Escreve `UX_PESQUISA.md` com as regras que vais aplicar, cada uma com fonte. No mínimo:
- **GOV.UK Design System:** padrão "uma pergunta por página", linguagem simples, mensagens de erro, página de resultado.
- **Heurísticas de Nielsen** (as 10).
- **WCAG 2.2 AA:** contraste, tamanho do texto, foco, rótulos, alvos de toque.
- **Linguagem simples para o público:** nunca "kVA" sem explicação; sempre "onde encontro isto na fatura".
- **Telemóvel primeiro:** a família está ao telemóvel, com o esquentador avariado.
Para cada regra, diz como se aplica ao DuoWatt.

### Fase 5: Redesign da app (ciclos, o grosso da noite)
**Ecrã principal: assistente para a família.**
- Barra de progresso ("Passo 2 de 4") e botões "Voltar"/"Continuar".
- Uma pergunta por passo, com ajuda contextual ("Na sua fatura de eletricidade, procure 'Potência contratada'"), valores típicos pré-selecionados e uma opção "Não sei" com um valor por omissão explicado.
- Perguntas sugeridas (ajusta se a pesquisa o justificar): potência contratada; quantas pessoas vivem na casa; como cozinha / que placa pensa ter; quantas garrafas de gás gasta por ano (com ajuda: "uma por mês = 12"). O consumo mensal pode ter um "Não sei" com o valor típico.
- **Página de resultado:** veredicto grande, em linguagem simples ("A sua casa consegue passar para elétrico sem aumentar a potência, se o termoacumulador for gerido"), 3 números grandes (CO₂ evitado, custo por ano vs. subir a potência, minutos sem água quente), "o que fazer a seguir" e o botão do **relatório** (§2).
- **Modo detalhado** (separador ou interruptor): o que existe hoje (gráfico do serão, métricas, viabilidade, diferenciação, provas, pressupostos), também melhorado.
- O assistente e o resultado têm de usar **exatamente** as mesmas funções de `duowatt.py`/`impacto.py`. Os números não podem divergir entre modos.

**Para o júri (critérios 2 a 5):**
- C2: um número de impacto principal, claro, com pressupostos visíveis e o cenário adverso.
- C3: a demo responde às provas. O separador "Provas" mostra os dados reais quando existirem em `dados/`, e liga cada prova à funcionalidade que ela justifica.
- C4: custos, equilíbrio e próximos passos concretos para a Bosch, fáceis de ler.
- C5: o relatório para o instalador e o diagnóstico no momento da avaria são a diferença. Mostra-o honestamente face aos concorrentes.

**Verificação de cada ciclo** (para além da do prompt anterior):
- Screenshots em **390×844 (telemóvel)**, 1366×768 e 1920×1080.
- Percorrer o assistente de ponta a ponta com Playwright, incluindo "Voltar", "Não sei" e entradas extremas.
- Testes verdes. Nenhum texto em inglês na UI.
- Commit, tag `estavel-N`, push.

### Fase 6: Júri e paragem
Como antes, o Júri é independente e avalia pelos **critérios oficiais** e respetivos pesos (`CRITERIOS_AVALIACAO.md`), em computador e em telemóvel. Pede-lhe também uma nota de 1 a 5 de "facilidade para uma pessoa comum". Paras quando o Júri der 4 ou mais em C2 a C5 e na facilidade, e o último ciclo só tiver itens de impacto baixo; ou quando dois ciclos seguidos não subirem notas; ou às 08:00.

---

## 4. Regras que se mantêm

Todas as do `CLAUDE.md`. Em especial: nunca inventar dados de utilizadores (nem nos screenshots, nem nos exemplos, nem no guião); nunca "somos os primeiros", "sem eletricista", "sem obras", nem que os Tronic se ligam a um gestor de energia; números novos com fonte e classificação; valores por omissão alterados registados em `DECISOES.md`; não editar PDFs nem `.docx` da equipa.

---

## 5. Gestão de tokens (plano Pro)

Igual ao prompt anterior: contexto do coordenador pequeno, agentes em sonnet (Investigador em haiku), nunca opus nos agentes, no máximo 2 em paralelo, resumos de 10 linhas, imagens só para o Auditor UX e o Júri, ponytail no código. `PROGRESSO.md` atualizado e push no fim de **cada** ciclo: é dele que a retoma automática depende.

---

## 6. Comunicação

O Tiago está a dormir: **não faças perguntas no chat** (exceto a mensagem da Fase 1). Tudo o que precisar de decisão vai para `PERGUNTAS.md`, e tu escolhes a opção mais prudente e continuas.

---

## 7. Documentos para a equipa e handoff

Só no fecho (§8), quando o trabalho estiver concluído.

**A) Guia da equipa** (para os 4 colegas, que não são de Informática; vai ser enviado pelo WhatsApp):
- `GUIA_EQUIPA.md` no repositório **e** `GUIA_EQUIPA.docx` (gerado com `python-docx`, bem formatado: títulos, tabelas, fácil de ler no telemóvel).
- Conteúdo, em linguagem simples:
  1. O DuoWatt numa frase e num parágrafo.
  2. O desafio da Bosch e os critérios de avaliação, com pesos.
  3. O que está feito (com 2 ou 3 screenshots da app).
  4. Os números principais e de onde vêm, com o que ainda está por validar.
  5. **O que cada pessoa tem de fazer hoje**, por perfil (Mecânica, Contabilidade, Multimédia, Ciência Política, Informática), com prazos até às 14:00 (congelamento) e às 17:30 (entrega).
  6. Como recolher as provas: link do Forms (campo para o Tiago preencher), meta de respostas, guiões das entrevistas.
  7. O que **nunca** dizer ao júri (regras de honestidade) e as 5 perguntas prováveis do júri, com respostas.
  8. Perguntas em aberto para a equipa decidir.

**B) Handoff para uma sessão nova do Claude:** `HANDOFF.md`, com **no máximo ~120 linhas**, para começar uma sessão limpa só com ele:
- Estado em 5 linhas (tag, testes, o que a app faz).
- Decisões tomadas e decisões pendentes (com remissão para `PERGUNTAS.md`).
- O que mudou esta noite (resumo de `DECISOES.md`).
- Os próximos passos, por ordem, até às 17:30.
- Comandos (correr app, testes, analisar o inquérito).
- Mapa dos ficheiros: o que ler e o que ignorar.
Atualiza o `CLAUDE.md` para apontar primeiro para o `HANDOFF.md`, e o `ATUALIZACAO_PARA_CLAUDE_APP.md` passa a dizer só "o Claude da app lê o repositório GitHub; começar pelo HANDOFF.md".

---

## 8. Fecho

1. Guia da equipa (`.md` e `.docx`) e `HANDOFF.md` (§7).
2. `RELATORIO_FINAL.md` atualizado: notas do júri antes e depois, o que mudou, o que o Tiago tem de validar.
3. `DEMO_GUIAO.md` atualizado para o novo fluxo (assistente → resultado → modo detalhado), com campos `[entre colchetes]` só onde faltarem dados reais.
4. Screenshots finais em `screenshots/final/` (telemóvel, portátil, projetor).
5. Testes verdes, app a arrancar sem erros, servidor desligado.
6. **Apagar `.retomar_ativo` e remover as entradas do crontab.**
7. Commit, tag `final-noite2`, `git push origin main --tags`.
8. Última mensagem no chat: 5 linhas com o resultado e o que o Tiago tem de fazer ao acordar.

**Começa pela Fase 1.**

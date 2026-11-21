# Missão final: DuoWatt como kit que completa os cilindros Bosch (demo, documentos e organização)

Hackathon@ShiftE 2026 · Desafio Bosch · **Entrega até às 18:30 de hoje (21 nov 2026)** · Pitch a 25 nov.
Língua: **português europeu (PT-PT)** em tudo (UI, código, comentários, documentos, commits).

Este prompt **substitui** os anteriores (`PROMPT_Equipa_Autonoma_DuoWatt.md`, `PROMPT_Noite_2_DuoWatt.md`) e o conceito antigo. Onde houver conflito com qualquer ficheiro do repositório, **vale este prompt**.

---

## 0. Como trabalhas

- És o **coordenador** de uma pequena equipa de agentes (§6). Planeias, decides, integras e verificas.
- Trabalhas **sozinho do princípio ao fim**. O Tiago não vai responder durante o trabalho.
- **Nunca termines a tua vez antes do fecho (§9).** Uma mensagem tua sem chamar ferramentas a seguir faz-te parar. Não escrevas mensagens de estado no chat: o estado vai para `PROGRESSO.md` e para os commits. A única mensagem final é a do §9.
- Dúvidas vão para `PERGUNTAS.md`; escolhes a opção mais prudente e continuas. **Nunca perguntas de escolha múltipla.**
- **Horário:** às **17:45** começas o fecho, mesmo que haja coisas por fazer. Às **18:00** tem de estar tudo no GitHub. Às 18:30 a equipa entrega.
- O `main` fica **sempre demonstrável**: testes verdes e app a arrancar sem erros. Faz commit e `git push origin main` no fim de cada fase. Nunca `--force`.

---

## 1. O conceito (fonte de verdade)

### Numa frase
> **O DuoWatt é um kit que completa os cilindros elétricos Bosch: pausa o cilindro sozinho antes de a luz ir abaixo, para que as casas com esquentador a gás possam passar para elétrico sem medo e sem aumentar a potência.**

### Problema
Quem tem esquentador a gás não muda para cilindro elétrico com medo de que a luz vá abaixo (e por achar que, para o evitar, teria de aumentar a potência contratada, pagar mais e tratar de burocracias).

### O kit (2 peças, vendidas juntas e emparelhadas de fábrica)
1. **Sensor no quadro elétrico:** mede o consumo total da casa em tempo real.
2. **Módulo de controlo do cilindro:** tomada de potência ou relé, conforme a instalação. **Evolução com a Bosch:** integrado no próprio Tronic 5501i (que já tem Wi-Fi), e o kit passa a ser só o sensor.

### Como funciona
- Comunicação **local e direta** entre as duas peças, **sem internet**.
- Quando o consumo da casa passa **~90 % do limite**, o cilindro é **desligado de imediato** (antes de o disjuntor ou o contador cortarem).
- Volta a ligar quando o consumo desce abaixo de **~80 %** do limite.
- **Pausa máxima de 30 min seguidos** (prioridade à água quente).
- **Se o sensor deixar de comunicar**, o cilindro volta ao funcionamento normal (fica como estaria sem o DuoWatt).
- **Ninguém fica sem água quente:** o cilindro tem água quente guardada, por isso uma pausa de alguns minutos não se nota.
- **Tempo de reação:** a norma dos disjuntores domésticos (EN 60898) dá **segundos a minutos** de tolerância para estes excessos (1,13× não dispara em 1 h; 1,45× dispara em menos de 1 h; 2,55× dispara entre 1 e 60 s). O tempo real do contador inteligente fica como **pressuposto a validar num piloto com a Bosch**.
- **Limite assumido:** se a casa passar o limite **mesmo sem o cilindro**, o DuoWatt não resolve. Promessa exata: *"o cilindro nunca é a causa do apagão"*.

### O que o DuoWatt NÃO tem (não implementar, não mencionar como funcionalidade)
Sem app para a família, sem avisos, sem histórico, sem porta HAN, sem sensor de temperatura, sem assistente de perguntas, sem relatório. **Nada de hardware** a construir: o protótipo é a simulação de software.

### Fator wow (o que a gama Tronic não tem)
Os Tronic já sabem **quando a família precisa de água quente** (o 5501i tem Wi-Fi, app HomeCom Easy, modos Smart/Eco/manual/programado, aprende hábitos). **Não sabem o que se passa no resto da casa.** O DuoWatt acrescenta isso: o cilindro pausa sozinho quando a casa está no limite. *"O DuoWatt é a peça que falta aos cilindros Bosch para conquistarem as casas que hoje continuam no gás."*
Pergunta provável do júri: *"O 5501i já tem programação; não chega?"* Resposta: a programação usa horas fixas, a vida real não (a máquina da roupa pode ligar a qualquer hora). O DuoWatt reage ao que está realmente a acontecer, sem a família fazer nada.
Escrever sempre *"pelo que vimos na gama Tronic"*, nunca *"a Bosch não tem"*.

### Negócio
- **O cliente é a Bosch** (B2B): compra os kits e inclui-os no Tronic ou vende-os como opção na troca do esquentador.
- **Benefício para a Bosch:** transforma trocas "gás por gás" (85 % das trocas urgentes, segundo o enunciado) em vendas de cilindro; diferencia os Tronic; ajuda as metas de descarbonização.
- **Benefício para a família:** não precisa de subir a potência (3,45 → 6,9 kVA custa ~64–78 €/ano, valor já em `VIABILIDADE.md`, marcado como estimativa).
- **Preços e custos do kit:** estão a ser calculados pelo colega de Contabilidade. **Não inventes preços.** Usa campos `[a preencher pela Contabilidade]`.
- **Slogan:** **"Garantia sem apagões"**.

### Concorrência (pesquisa já feita; usa estes factos, não repitas a pesquisa)
| Concorrente | O que faz | Preço encontrado | Limitação |
|---|---|---|---|
| Schneider Electric, Wiser Home | Função "Anti-Tripping Management": desliga o termoacumulador para o disjuntor não disparar; notifica quando não pode aquecer | Não encontrado | Precisa de hub Wiser + módulo; documentação para FR, UK, NO; venda em PT/ES não confirmada |
| Legrand, Délesteur connecté (Drivia with Netatmo) | Mede a casa no quadro e corta aparelhos por prioridade, com app | 146,54 € (produto, PVP com IVA); desde 290 € instalado | Mercado francês; precisa de pack de arranque "with Netatmo" |
| Delta Dore | Pioneiro: inventou o primeiro delestador em 1976; gestores de energia com delestador | Tywatt 1000: 372 €; Tybox 2020: 766,33 € | França; produto completo e caro |
| Shelly | DIY: medidor no quadro + relé, com scripts | Tomada Plug M Gen3: 12,90 €; Pro 1PM: 75,79 € | Para entusiastas; tomadas comuns com limites baixos (Plug S Gen3: 2500 W) |
| Ariston | Aviso "Shower Ready" no telemóvel | Incluído no cilindro | Só aviso; não gere potência |

Fontes: productinfo.schneider-electric.com (Wiser Home, Anti-Tripping Management); legrand.fr (ref. 199120); espace-aubade.fr e domomat.com (Delta Dore); shelly.com; mediamarkt.es (Ariston); bosch-homecomfort.com/pt (Tronic 5501i T e 4000 T).
**Diferenciação** (nunca "somos os primeiros"): quem paga (a Bosch, não a família), quando se vende (na avaria do esquentador, pelo mesmo instalador), simplicidade (2 peças emparelhadas, sem hub, sem app, sem internet), mercado (Portugal e Espanha: 3,45 kVA, botijas de gás) e integração com os Tronic.

---

## 2. As duas user stories (a demo é construída à volta delas)

**US1, a família**
> Como família com esquentador a gás e 3,45 kVA, quero passar para um cilindro elétrico sem que a luz vá abaixo, para deixar o gás sem pagar mais pela potência.

Critérios de aceitação na demo:
- Cenário único e simples: **ao fim da tarde, o cilindro (Tronic 5501i, 1,5 kW) está a aquecer e a máquina da roupa liga** (fase de aquecimento ~2 kW durante ~20 min, *pressuposto*), com a base da casa a ~0,6 kW (*pressuposto*). Total sem DuoWatt ≈ 4,1 kW > 3,45 kVA.
- **Sem DuoWatt:** o consumo passa o limite e a luz vai abaixo.
- **Com DuoWatt:** o cilindro pausa, o consumo fica abaixo do limite, a luz mantém-se e **não há minutos sem água quente**.
- Número que importa: **evita ~64–78 €/ano** (não sobe a potência).
- Opcional, só se sobrar tempo: segundo cenário com a placa de indução ao jantar.

**US2, a Bosch (e o instalador)**
> Como instalador da Bosch, numa troca urgente de esquentador, quero oferecer um cilindro com garantia sem apagões, para vender um cilindro em vez de outro esquentador a gás.

Critérios de aceitação na demo:
- **CO₂ evitado por casa por ano** (com 12 garrafas/ano, o valor já usado na app) e **um cenário nacional** ("se 1 % das casas a gás trocarem…"), com o cenário adverso da rede indicado de forma discreta.
- Porque interessa à Bosch (texto curto) + espaço para os números de negócio `[a preencher pela Contabilidade]`.
- Como funciona (diagrama simples) e concorrência (tabela curta).

---

## 3. A demo (Streamlit): 3 ecrãs para um júri NÃO especialista

### Princípios (obrigatórios)
- **Uma ideia por ecrã.** Linguagem do dia a dia: "o limite da sua casa", "a luz vai abaixo". Nunca "kVA" ou "W" sem explicação; de preferência, não os mostrar.
- **No máximo 3 números grandes em toda a demo** (1 no ecrã 2, 2 no ecrã 3). Tudo o resto em texto simples ou num expansor "Para saber mais".
- **Visual primeiro:** ícones ou SVG simples (casa, cilindro, máquina da roupa, lâmpada), uma **barra de consumo** (tipo "medidor") com a linha do limite, cores claras (verde = dentro do limite, vermelho = passou). Animação simples (botão "Ligar a máquina da roupa" ou um controlo de tempo).
- Legível num projetor (texto grande, contraste WCAG AA) e num telemóvel.
- Identidade neutra (verde-petróleo já usado). **Sem logótipo, cores ou tipografia da Bosch.**
- Navegação por passos: **"1. O problema" → "2. Com DuoWatt" → "3. O que muda"**, com botões "Anterior"/"Seguinte" e indicador de passo.

### Ecrã 1: "O problema" (US1)
Título curto + uma frase ("Ao fim da tarde, o cilindro está a aquecer e a máquina da roupa liga…"). Casa ilustrada; ao carregar no botão, a barra sobe, passa o limite, e o ecrã mostra claramente **"A luz foi abaixo"** (ex.: zona escurecida, lâmpada apagada). Frase final: *"É por isto que muitas famílias continuam no gás."*

### Ecrã 2: "Com DuoWatt" (US1)
O mesmo cenário com DuoWatt: o cilindro aparece **"em pausa"**, a barra fica abaixo do limite, **"A luz mantém-se"**. Frase: *"O cilindro tem água quente guardada: ninguém nota a pausa."* **Número grande:** *"Evita ~64–78 €/ano: não precisa de aumentar a potência"* (estimativa). Um gráfico simples do serão, **com e sem DuoWatt**, com a linha do limite, mas limpo: 2 linhas, poucas marcas no eixo, legenda clara.

### Ecrã 3: "O que muda" (US2)
- **2 números grandes:** CO₂ evitado por casa/ano; cenário nacional (1 % de adoção).
- **Como funciona:** diagrama de 3 caixas: *Sensor no quadro → ligação local (sem internet) → módulo no cilindro*.
- **Imagem do produto:** mostra `assets/produto_3d.png` se existir, com a legenda *"Imagem concetual"*; se não existir, mostra um espaço reservado discreto (*"Imagem concetual a adicionar"*). O Tiago vai gerar e adicionar esta imagem.
- **Para a Bosch:** 3 frases (completa o Tronic; transforma trocas gás→gás em vendas de cilindro; garantia sem apagões) + `[números de negócio a preencher pela Contabilidade]`.
- **Concorrência:** tabela de 4 linhas × 2 colunas ("Concorrentes" vs. "DuoWatt"): quem paga, quando se vende, precisa de hub/app?, para quem.
- Expansor **"Para saber mais"**: pressupostos com fonte e classificação, regras de controlo (90/80/30 min, modo seguro), limite assumido, cenário adverso da rede.

### Rodapé discreto (todos os ecrãs)
*"Simulação ilustrativa. Valores por validar num piloto."* Uma linha, não um bloco.

---

## 4. Código: o que mudar

1. **Retirar** o assistente de 5 perguntas (`assistente.py`, `test_assistente.py`), o relatório HTML, e tudo o que fale de HAN, avisos, histórico ou "modo detalhado" antigo. Remove código, testes e referências.
2. **`duowatt.py`:** atualiza para o conceito novo, com a **menor alteração possível** (skill ponytail):
   - cilindro de **1 500 W** (Tronic 5501i);
   - cenário **"máquina da roupa"** (≈2 kW durante ≈20 min, pressuposto) e, opcionalmente, "indução";
   - regras de controlo: **desligar a 90 %, religar abaixo de 80 %, pausa máxima de 30 min, modo seguro** se o sensor falhar (simulável com um parâmetro);
   - continua a calcular a reserva de água quente e os minutos sem água quente.
3. **Testes novos** (os antigos que deixarem de fazer sentido são removidos; não deixes `xfail` de conceitos antigos):
   - sem DuoWatt, o cenário passa o limite; com DuoWatt, não passa;
   - 0 minutos sem água quente no cenário da demo;
   - a pausa nunca passa de 30 min seguidos;
   - religa só abaixo de 80 % (histerese);
   - modo seguro: sem sinal do sensor, o cilindro funciona normalmente;
   - formatação PT-PT dos números.
4. **Pronto para publicar no Streamlit Community Cloud:** `app.py` na raiz; `requirements.txt` com versões fixas; caminhos relativos (incluindo `assets/`); `.streamlit/config.toml` com o tema; nada que dependa de ficheiros locais fora do repositório. Testa que a app arranca do zero num ambiente limpo (`python -m venv /tmp/teste && pip install -r requirements.txt && streamlit run app.py` em modo headless).
5. **`DEPLOY.md`:** passos curtos para o Tiago publicar (entrar em share.streamlit.io com o GitHub, escolher `TiagoVieira59/duowatt`, ramo `main`, ficheiro `app.py`, "Deploy"); nota de que a app "adormece" sem uso e deve ser aberta uns minutos antes da apresentação.

---

## 5. Organização do repositório (tens permissão para apagar)

O Tiago autorizou apagar ficheiros que estejam a mais. Objetivo: **um repositório limpo, que qualquer pessoa da equipa ou do júri percebe em 1 minuto.** O histórico do git guarda tudo, por isso apagar é reversível.

### Estrutura final
```
README.md              ← o que é, como correr, como publicar, mapa da pasta
HANDOFF.md             ← porta de entrada para uma sessão nova do Claude (máx. ~40 linhas)
CLAUDE.md              ← regras para o Claude (aponta para HANDOFF.md)
PROGRESSO.md           ← curto: estado atual e próximos passos
PERGUNTAS.md
DECISOES.md            ← curto: só decisões que continuam válidas
requirements.txt
app.py  duowatt.py  impacto.py  formato.py
.streamlit/config.toml
assets/                ← imagem 3D concetual (o Tiago adiciona)
tests/                 ← todos os testes
ferramentas/           ← analisar_inquerito.py, criar_formulario.gs, capturar.py
dados/                 ← só dados reais (vazio até haver respostas)
docs/
  PRODUTO.md           ← PRD de 1 página (ver §7)
  ARQUITETURA.md       ← diagrama + máquina de estados + modo seguro
  CONCORRENCIA.md      ← tabela do §1 com fontes + diferenciação
  NEGOCIO.md           ← estrutura para a Contabilidade preencher
  IMPACTO.md           ← CO₂ por casa e cenário nacional, pressupostos e fontes
  DEMO_GUIAO.md        ← guião de 2–3 min seguindo os 3 ecrãs
  GUIA_EQUIPA.md + GUIA_EQUIPA.docx
  CRITERIOS_AVALIACAO.md
  PARAMETROS.md        ← valores com fonte e classificação (a partir de Parametros_Verificados.md)
  provas/              ← INQUERITO.md, ENTREVISTAS.md, PLANO_RECOLHA_PROVAS.md, FORMS_INSTRUCOES.md
  referencia/          ← PDFs do desafio e documentos escritos pela equipa
screenshots/           ← só os finais da versão nova
equipa/                ← só os relatórios dos agentes desta missão
```

### Regras para apagar e mover
- **Apagar** (conceito antigo ou obsoleto): `assistente.py`, `test_assistente.py`, código do relatório HTML, `PROMPT_Equipa_Autonoma_DuoWatt.md`, `PROMPT_Noite_2_DuoWatt.md`, `CONTEXTO_Projeto_DuoWatt.md` (substituído por `docs/PRODUTO.md`), `Parametros_Simulador.md`, `README_demo.md`, `ATUALIZACAO_PARA_CLAUDE_APP.md`, `BACKLOG.md`, `UX_PESQUISA.md`, `RELATORIO_FINAL.md` (antigo), `VIABILIDADE.md`, `DIFERENCIACAO.md` e `PESQUISA.md` antigos (depois de passares o que ainda vale para `docs/NEGOCIO.md`, `docs/CONCORRENCIA.md` e `docs/PARAMETROS.md`), `BloqueiosEAnguloInformatica.txt`, os relatórios antigos em `equipa/`, os screenshots antigos, `__pycache__/`, `.pytest_cache/`.
- **Mover para `docs/referencia/` (NÃO apagar, são documentos da equipa ou da organização):** os PDFs do desafio e da MAKE IT, os `.docx` da equipa (`DuoWatt_Proposta_...docx`, `Propostas_Inovacao_...docx`), `Descricao_Tecnica_Produto_Versao_A.md`, `Ficha_DuoWatt_Proposta_Equipa.md`. Não editar o conteúdo destes ficheiros.
- **Não tocar:** `.git/`, `.venv/`, `.claude/`, `.agents/` (se não souberes para que serve, deixa estar), `dados/` com dados reais.
- **O inquérito e o Forms:** o Tiago pode já ter criado o formulário. **Não alteres `ferramentas/criar_formulario.gs` nem as perguntas do `INQUERITO.md`.** Só move os ficheiros para os novos sítios e corrige caminhos. Se alguma pergunta já não fizer sentido com o conceito novo, regista em `PERGUNTAS.md`.
- Usa `git mv` e `git rm` para manter o histórico. No commit, lista o que foi apagado e o que foi movido.
- Depois de mover, corrige **todos** os caminhos: imports, comandos de teste, `ferramentas/`, `README.md`, `HANDOFF.md`, `CLAUDE.md`, ligações entre documentos. Verifica com uma pesquisa por nomes antigos que não ficou nenhuma referência partida.
- Atualiza o `.gitignore` (`.venv/`, `__pycache__/`, `.pytest_cache/`, `ferramentas/retomar.log`, CSV brutos na raiz).

---

## 6. A equipa de agentes

Guarda os papéis em `equipa/papeis/` (curtos). Lança cada agente com a ferramenta de subagentes, **modelo sempre explícito**, e prompt curto: *"Lê `equipa/papeis/<papel>.md` e a secção X deste prompt; faz Y; escreve em `equipa/<ficheiro>`; devolve um resumo de até 10 linhas."*

| Agente | Modelo | Missão | Edita código? |
|---|---|---|---|
| **Programador** | sonnet | Implementa §4 e §5 por lotes, com ponytail; corre os testes antes de devolver | Sim (um de cada vez) |
| **Auditor UX** | sonnet | Abre a demo com Playwright (screenshots em 390×844 e 1920×1080) e avalia: um júri não especialista percebe cada ecrã em menos de 30 s? Há números a mais? Contraste e tamanho de letra? | Não |
| **Modelador** | sonnet | Verifica `duowatt.py`/`impacto.py`: regras 90/80/30 min, modo seguro, cenário da máquina da roupa, coerência dos números entre app e documentos; escreve os testes do §4 | Só testes |
| **Redator** | sonnet | Escreve `docs/` (§7) a partir deste prompt, em PT-PT simples | Só `docs/` |
| **Júri** | sonnet | **Independente:** não vê código nem discussões. Recebe só o PDF do desafio (`docs/referencia/`), os critérios oficiais (`docs/CRITERIOS_AVALIACAO.md`), os screenshots finais e `docs/PRODUTO.md`. Pontua os critérios 1–5 (escala 1–5) e dá as 5 perguntas mais prováveis do júri, com resposta | Não |

Regras da equipa: no máximo **2 agentes em paralelo**; só um Programador de cada vez; só o Auditor UX e o Júri veem imagens; **nunca o modelo opus nos agentes**; o coordenador lê os resumos, não os ficheiros completos.

---

## 7. Documentos a escrever (`docs/`)

- **`PRODUTO.md` (PRD de 1 página):** problema; as 2 user stories com critérios de aceitação; a solução (o kit, 2 peças); como funciona (regras); o que NÃO faz; limite assumido; fator wow face aos Tronic; negócio (cliente Bosch, benefícios, `[preços a preencher pela Contabilidade]`); diferenciação; impacto; riscos e respostas (a tecnologia já existe; não resolve o espaço; precisa de técnico; a Bosch podia fazer sozinha; a casa passa o limite sem o cilindro); próximos passos (piloto com a Bosch para medir o tempo real de corte do contador; integração no Tronic 5501i; certificação CE).
- **`ARQUITETURA.md`:** diagrama em texto (quadro → sensor → ligação local → módulo → cilindro); máquina de estados `NORMAL` / `CILINDRO_PAUSADO` com as transições (90 %, 80 %, 30 min, sem sinal > 5 s → `NORMAL`); porque é local e sem internet; tempo de reação vs. EN 60898.
- **`CONCORRENCIA.md`:** a tabela do §1 com as fontes + a tabela "Concorrentes vs. DuoWatt" + a resposta à pergunta da programação do 5501i.
- **`NEGOCIO.md`:** só a **estrutura** para o colega de Contabilidade preencher (modelo B2B com a Bosch, custo das peças, preço à Bosch, opção incluída vs. opcional para a família, conta de equilíbrio para a Bosch: "o kit compensa se 1 em cada M/X kits se transformar numa venda de cilindro"), com todos os valores como `[a preencher]`, exceto os já estimados em `VIABILIDADE.md` (marcados como estimativa).
- **`IMPACTO.md`:** CO₂ por casa e cenário nacional com pressupostos, fontes e cenário adverso; frase honesta: *"o CO₂ desce porque a casa sai do gás; o DuoWatt tira a barreira que impedia essa troca"*.
- **`DEMO_GUIAO.md`:** 2–3 minutos, o que dizer e o que clicar em cada um dos 3 ecrãs; slogan no fim.
- **`GUIA_EQUIPA.md` + `.docx`** (para enviar pelo WhatsApp): o DuoWatt em 1 parágrafo, as 2 user stories, como é a demo, o que falta e quem faz (Contabilidade: negócio; Multimédia: deck; Tiago: demo, imagem 3D e publicação; todos: provas no fim), o que nunca dizer, as 5 perguntas prováveis do júri. Mantém os nomes dos perfis já usados no guia atual. Gera o `.docx` com `ferramentas/md_para_docx.py` (move-o para `ferramentas/` se não estiver lá).

---

## 8. Fases e verificação

1. **Fase A, organização (§5):** mover/apagar, corrigir caminhos, testes verdes. Commit + push.
2. **Fase B, simulação (§4.2–4.3):** Modelador + Programador. Commit + push.
3. **Fase C, demo (§3, §4.4–4.5):** Programador; Auditor UX revê; corrige o que for de impacto alto. Commit + push.
4. **Fase D, documentos (§7):** Redator (pode correr em paralelo com a Fase C). Commit + push.
5. **Fase E, Júri (§6):** uma avaliação no fim; se apontar algo de impacto alto e rápido, corrige; **não** faças segundo ciclo depois das 17:30.

**Verificação antes de cada push:** testes verdes; a app arranca sem erros nem avisos; percorrer os 3 ecrãs com Playwright (incluindo "Anterior"/"Seguinte"); nenhum texto em inglês na UI; nenhuma referência ao conceito antigo (pesquisa por "HAN", "assistente", "relatório", "aviso", "histórico"); os números da app batem certo com `docs/`.

---

## 9. Regras não negociáveis

- **Nunca inventar dados de utilizadores**, citações nem resultados de inquérito. `dados/` só com dados reais.
- **Nunca inventar preços ou números de negócio:** `[a preencher pela Contabilidade]`.
- Nunca *"somos os primeiros"*, *"sem eletricista"*, *"sem obras"*, nem que os Tronic se ligam a um gestor de energia. Nunca *"a Bosch não tem"* (usar *"pelo que vimos na gama Tronic"*).
- Todo o número novo leva fonte e classificação (confirmado / provável / derivado / pressuposto).
- **Nada de hardware.** Sem logótipo nem identidade visual da Bosch.
- Gestão de tokens (plano Pro): contexto do coordenador pequeno; resumos de até 10 linhas; imagens só para o Auditor UX e o Júri; skill ponytail no código; não releias ficheiros sem necessidade.

---

## 10. Fecho (começa às 17:45, ou antes se tudo estiver feito)

1. `HANDOFF.md` (máx. ~40 linhas): estado, decisões, o que falta, comandos, mapa da pasta. `CLAUDE.md` aponta para ele.
2. `PROGRESSO.md` curto e `README.md` atualizado.
3. Screenshots finais em `screenshots/` (390×844 e 1920×1080, os 3 ecrãs).
4. Testes verdes, app a arrancar, servidor do Streamlit desligado.
5. Commit, tag `entrega-21nov`, `git push origin main --tags`.
6. **Mensagem final no chat, 5 linhas:** o que ficou feito; nota do Júri; o que o Tiago tem de fazer agora (adicionar `assets/produto_3d.png`, publicar seguindo `DEPLOY.md`, enviar `docs/GUIA_EQUIPA.docx`); o que falta da equipa (negócio, deck, provas).

**Começa já pela Fase A.**

# Missão: equipa autónoma para levar o DuoWatt ao melhor produto possível

Hackathon@ShiftE 2026 · Desafio Bosch · Entrega: 21 nov 2026, 17:30 · Língua: português europeu (PT-PT) em tudo (UI, código, comentários, ficheiros, mensagens).

---

## 0. O teu papel

És o **coordenador** de uma pequena equipa de agentes. A tua função é **planear, decidir, integrar e verificar**. Não és tu quem faz todo o trabalho pesado: delegas nos agentes e manténs o teu contexto pequeno.

Não há hora marcada para parar. Trabalhas em **ciclos** enquanto houver melhorias com impacto real para o júri (ver o critério de paragem no §5). O Tiago está acordado, mas o trabalho não pode depender dele: tu encontras problemas, testas soluções, implementas, verificas e só depois integras.

**Princípio n.º 1:** o branch `main` está **sempre demonstrável**. Tudo o que entra no `main` passou nos testes e foi visto a funcionar no browser.

**Princípio n.º 2:** se uma abordagem falhar 2 vezes, muda de abordagem. Regista em `DECISOES.md`: "tentei X, falhou por Y, passei para Z".

---

## 1. Ler primeiro (uma vez, por esta ordem)

1. `CONTEXTO_Projeto_DuoWatt.md`: decisões tomadas, estado e regras. **É a fonte de verdade.**
2. `Parametros_Verificados.md` e `Ficha_DuoWatt_Proposta_Equipa.md`.
3. `duowatt.py`, `impacto.py`, `app.py`, `test_duowatt.py`, `test_impacto.py`.

Não leias o `.venv/`, os `.docx` nem o `Parametros_Simulador.md` (desatualizado). O PDF do desafio Bosch só é lido pelo agente **Júri** (§3).

---

## 2. O que é "o melhor produto possível" (rubrica)

O enunciado diz que o júri avalia **a solução mais viável na vida real** e o **impacto direto e mensurável na descarbonização**. A demo tem 2 a 3 minutos, num projetor. Tudo é avaliado com esta rubrica, de 0 a 5:

| # | Critério | O que significa um 5 |
|---|---|---|
| R1 | Impacto de CO₂ mensurável | Número por casa e nacional claro, com intervalo (cenário adverso) e fonte visível |
| R2 | Viabilidade real | Pressupostos explícitos; a app mostra também os casos em que o DuoWatt **não** chega |
| R3 | Clareza da demo | Em menos de 30 s cada, o júri percebe: problema → veredicto → como a gestão resolve → impacto |
| R4 | UI/UX e legibilidade | Hierarquia clara, contraste WCAG AA, texto legível a 5 m num projetor, bom em 1920×1080 e 1366×768 |
| R5 | Correção técnica | Modelo coerente, casos limite testados, os mesmos números na UI, no código e nos documentos |
| R6 | Honestidade | Nenhuma afirmação proibida (§7); limitações visíveis sem cansar |
| R7 | Robustez | Arranque limpo, sem erros nem avisos, com entradas extremas |

**Meta:** todos os critérios com 4 ou mais na avaliação do Júri, e **R6 sempre a 5**.

---

## 3. A equipa

Guarda a descrição de cada papel em `equipa/papeis/<papel>.md` (o texto abaixo, desenvolvido). Lança cada agente com a ferramenta de subagentes (tipo de uso geral) e o **modelo indicado**, com um prompt curto do tipo: "Lê `equipa/papeis/<papel>.md` e `PROGRESSO.md`, faz a tarefa X do ciclo N, escreve o resultado em `equipa/<ficheiro>` e devolve um resumo de até 10 linhas."

| Agente | Modelo | Missão | Pode editar código? | Escreve em |
|---|---|---|---|---|
| **Auditor UX** | sonnet | Abre a app com Playwright, vê os screenshots e avalia com as heurísticas de Nielsen, WCAG AA e a legibilidade em projetor. Lista os problemas por prioridade, com evidência (caminho do screenshot e zona do ecrã). | Não | `equipa/ux_cicloN.md` |
| **Modelador** | sonnet | Revê `duowatt.py` e `impacto.py`: correção física e elétrica, pressupostos, casos limite, coerência dos números. Escreve primeiro **testes que expõem** cada problema, e só depois propõe a correção. | Só testes novos | `equipa/modelo_cicloN.md` |
| **Programador** | sonnet | Implementa os itens do backlog que o coordenador lhe atribui, num branch próprio, com a skill **ponytail** (a menor alteração que resolve, sem funcionalidades a mais). Corre os testes antes de devolver. | Sim, só no branch do ciclo | código e `equipa/impl_cicloN.md` |
| **Investigador** | haiku | Pesquisa web dos itens por confirmar (CONTEXTO §6). Cada valor leva fonte, data e classificação (confirmado / provável / não encontrado). Máximo de ~5 pesquisas por item; se não encontrar, diz "não encontrado" e pára. | Não | `PESQUISA.md` |
| **Júri** | sonnet | **Olhos frescos:** não vê as discussões nem o código. Recebe só o PDF do desafio Bosch, os screenshots finais do ciclo e o `DEMO_GUIAO.md`. Faz de júri da Bosch: pontua a rubrica (§2) e lista as 5 objeções mais prováveis do júri. | Não | `equipa/juri_cicloN.md` |

Regras da equipa:
- No máximo **2 agentes em paralelo** (por exemplo, Auditor UX + Modelador na fase de diagnóstico; o Investigador pode correr em segundo plano).
- Só **um** Programador de cada vez, para não haver conflitos.
- Só o Auditor UX e o Júri veem imagens. Tu lês os relatórios deles, não os screenshots (exceto na verificação final do ciclo, se tiveres dúvidas).
- Nenhum agente usa o modelo opus.

---

## 4. Ciclo 0: preparação (antes de tudo)

1. **Git:** `git init`, `.gitignore` (`.venv/`, `__pycache__/`, `.pytest_cache/`), commit "estado inicial antes da equipa autónoma" no `main`.
2. **Papéis:** criar `equipa/papeis/` com os 5 papéis do §3.
3. **Playwright:** instalar no `.venv` (`.venv/bin/pip install playwright` e `.venv/bin/playwright install chromium`). Sem `sudo` e sem instalar nada global. Se faltarem bibliotecas do sistema, regista em `PERGUNTAS.md`, usa `streamlit.testing.v1.AppTest` como alternativa e continua.
4. **Ferramenta de captura reutilizável:** `ferramentas/capturar.py`. Arranca o Streamlit em modo headless numa porta livre (por exemplo, 8599), espera que a página renderize, define os cenários (abaixo), tira screenshots de página inteira em 1920×1080 e em 1366×768, guarda-os em `screenshots/cicloN/` e **mata sempre o servidor no fim** (mesmo em caso de erro). Também regista erros da consola e exceções do Streamlit.
5. **Cenários de teste fixos** (usar sempre os mesmos, para comparar ciclos):
   - A: casa típica, 3,45 kVA, 200 kWh/mês, 3 pessoas, indução moderada (história principal).
   - B: igual, mas com indução intensa (o caso em que o DuoWatt pode não chegar).
   - C: 6,9 kVA (aguenta sem gestão).
   - D: entradas extremas: 2,3 kVA, 1 pessoa, 0 garrafas; e 10,35 kVA, 8 pessoas, 50 garrafas.
6. **Linha de base:** testes, screenshots do ciclo 0 e primeira avaliação do Júri. Regista as notas da rubrica em `PROGRESSO.md`. É contra esta base que medes a melhoria.

Commit no fim do ciclo 0.

---

## 5. Ciclos de melhoria (repetir)

Cada ciclo N:

1. **Diagnosticar:** Auditor UX e Modelador em paralelo. O Investigador corre em segundo plano se ainda houver itens por confirmar.
2. **Triar:** junta os resultados em `BACKLOG.md`. Cada item tem: problema, evidência, critério da rubrica afetado, impacto (alto/médio/baixo), esforço (P/M/G) e decisão (fazer / adiar / rejeitar, com motivo). Escolhe **até 5 itens** com melhor relação impacto/esforço.
3. **Explorar quando há dúvida:** se não for óbvio qual de duas soluções é melhor (por exemplo, dois layouts, dois tipos de gráfico, duas formas de mostrar o veredicto), o Programador faz as duas em branches `exp-N-<nome>`, a ferramenta de captura gera os screenshots e o Auditor UX compara-as com a rubrica. Fica a melhor; regista a escolha em `DECISOES.md`.
4. **Implementar:** o Programador trabalha no branch `ciclo-N`.
5. **Verificar (obrigatório antes de integrar):**
   - Testes verdes: `python3 -I -m pytest -q test_impacto.py test_duowatt.py -p no:cacheprovider` (e os testes novos).
   - A app arranca sem erros nem avisos nos 4 cenários (ferramenta de captura).
   - Os números na UI batem certo com `impacto.py`/`duowatt.py` e com os documentos.
   - Se algo falhar: corrige ou reverte. Nunca integras com testes vermelhos.
6. **Integrar:** merge no `main`, tag `estavel-N`, commit, `PROGRESSO.md` atualizado, e uma mensagem de 3 linhas no chat ("ciclo N: feito / notas / próximo").
7. **Júri:** a cada 2 ciclos, ou quando achares que estás perto do fim, o Júri volta a avaliar (sempre sem ver as discussões).

**Critério de paragem** (não pares só porque um ciclo acabou). Paras quando se verificar uma destas:
- O Júri dá 4 ou mais em todos os critérios **e** o último ciclo só encontrou itens de impacto baixo; ou
- Dois ciclos seguidos sem subir nenhuma nota da rubrica; ou
- O limite do plano interrompe a sessão (nesse caso o estado já está guardado, ver §8).

Depois faz o fecho (§10).

**Salvaguarda do prazo:** a entrega é às 17:30 de 21 nov. A partir das **14:00** desse dia, só entram correções de erros no `main`, sem melhorias novas.

---

## 6. Âmbito: o que podes e não podes mudar

**Podes, livremente:** layout, textos, tema (`.streamlit/config.toml`, CSS), gráficos (podes usar Altair ou Plotly se justificares e os adicionares ao `requirements.txt`), estrutura do código, novos testes, novos ficheiros `.md`, um modo de apresentação ou cenários pré-definidos para a demo.

**Podes, com registo obrigatório em `DECISOES.md`** (antes, depois, motivo e fonte): valores por omissão, fórmulas, lógica do veredicto, perfil de consumo da casa, e métricas como "disparos".

**Não podes:** mudar de conceito (é o DuoWatt: diagnóstico + gestão de potência, só software), implementar o RetroFit Bridge/FitGauge (é da Mecânica), editar os PDFs ou os `.docx`, apagar ficheiros da equipa (marca-os como obsoletos), trabalhar fora desta pasta, instalar nada global, usar `sudo`, fazer push para remotos.

A stack é Python + Streamlit. Se o Streamlit limitar alguma coisa importante, regista em `ALTERNATIVAS.md` em vez de mudares de stack. Ideias de outro conceito também vão para `ALTERNATIVAS.md` e nunca para o código.

### Problemas já conhecidos (ponto de partida, valida-os, não os aceites às cegas)

- O `app.py` usa 0,21 €/kWh, mas o `Parametros_Verificados.md` recomenda 0,18. O comentário do `impacto.py` mistura IVA de 23 % com 0,171 €. Coerência a resolver.
- A base da casa é plana (consumo mensal ÷ 720 h). Isto subestima o pico do serão. Avaliar um perfil horário simples, com fonte ou claramente marcado como pressuposto.
- kVA é tratado como kW, e o disjuntor real tolera sobrecargas curtas: a métrica "disparos" pode exagerar. Avaliar se deve ser "minutos acima do limite" ou ter tolerância.
- Com indução intensa a 3,45 kVA o veredicto passa a "precisa de mais potência". A demo deve mostrar honestamente **um caso em que o DuoWatt resolve e um em que não chega**.
- O gráfico tem 1440 pontos para o dia inteiro: no projetor, a zona do serão (onde está a história) pode ficar ilegível. Avaliar um destaque ou zoom do serão.
- A barra lateral tem 9 entradas: talvez demasiado para uma demo de 2 minutos. Avaliar um cenário pré-definido "Casa típica" e entradas avançadas recolhidas.
- A app nunca foi vista num browser.
- A ficha fala em ~10 h de trabalho e um `.docx` em 30 h. Não é código: só regista em `PERGUNTAS.md`.

---

## 7. Regras de honestidade (não negociáveis, R6)

- Nunca afirmar "somos os primeiros", "sem eletricista", "sem obras", nem que os Tronic se ligam a um gestor de energia (não encontrado na documentação).
- A gestão de cargas já existe no mercado (Schneider Wiser, ABB). Não encontrámos uma ferramenta pública da Bosch que faça este diagnóstico, o que **não prova que não exista**.
- O CO₂ só desce se o gás for mesmo substituído. O DuoWatt tira o bloqueio da potência, não causa a troca sozinho.
- O benefício em € é pequeno (~33 €/ano). A mensagem é "descarboniza sem custar mais", não "poupa muito dinheiro".
- Cada valor novo leva fonte e classificação. Valores derivados ficam marcados como "derivado".

---

## 8. Gestão de tokens (plano Pro)

- Tu, coordenador, mantém o contexto pequeno: delega a leitura pesada, lê os resumos e não os ficheiros completos, não releias o que já leste.
- Os agentes devolvem resumos de até 10 linhas e põem os detalhes em ficheiros.
- Modelos: Investigador em haiku, os restantes em sonnet, nunca opus nos agentes.
- No máximo 2 agentes em paralelo.
- Imagens só para o Auditor UX e o Júri.
- Usa a skill **ponytail** em todas as alterações de código. Na UI, o objetivo é qualidade visual, não funcionalidades novas.
- O `PROGRESSO.md` tem de permitir que uma sessão nova retome só com "Lê `PROGRESSO.md` e continua". Atualiza-o no fim de cada ciclo com: estado do `main`, notas da rubrica, ciclo atual, próximo passo, decisões pendentes.
- Quando o contexto crescer muito, atualiza o `PROGRESSO.md` e compacta a conversa.

---

## 9. Comunicação com o Tiago

- **Não bloqueies.** Perguntas vão para `PERGUNTAS.md` e continuas com outra coisa. Só perguntas no chat se estiveres mesmo bloqueado e sem mais nada para fazer, em texto curto. Nunca perguntas de escolha múltipla.
- No fim de cada ciclo, 3 linhas no chat.
- Quando o Tiago disser que vai dormir: termina o item atual, confirma que o `main` está estável, atualiza o `PROGRESSO.md` e **continua sozinho**. A partir daí, nenhuma pergunta no chat: tudo para `PERGUNTAS.md`.
- O que só o Tiago decide: mudar o conceito, aceitar valores por omissão novos (fica registado e aplicado, mas ele valida), e tudo o que esteja em "não podes" no §6.

---

## 10. Fecho

Quando parares (critério do §5):

1. `RELATORIO_FINAL.md` com:
   - rubrica no ciclo 0 e no fim (tabela);
   - o que mudou e porquê (resumo de `DECISOES.md`);
   - **decisões que o Tiago tem de validar** (sobretudo valores por omissão alterados);
   - as 5 objeções prováveis do júri e uma resposta honesta a cada uma;
   - riscos e limitações conhecidos;
   - como correr a app e os testes.
2. `DEMO_GUIAO.md`: guião de 2 a 3 minutos, em PT-PT, com o que dizer e o que clicar em cada momento (cenário A e depois o B).
3. Screenshots finais em `screenshots/final/` (1920×1080 e 1366×768).
4. O `main` estável, com tag `final`, e o servidor do Streamlit desligado.

---

## Ficheiros de trabalho (resumo)

| Ficheiro | Para quê |
|---|---|
| `PROGRESSO.md` | Estado atual e como retomar |
| `BACKLOG.md` | Problemas encontrados e prioridades |
| `DECISOES.md` | Escolhas feitas, experiências, valores alterados |
| `PESQUISA.md` | Valores pesquisados com fonte e classificação |
| `PERGUNTAS.md` | Perguntas para o Tiago |
| `ALTERNATIVAS.md` | Ideias fora do âmbito |
| `equipa/` | Papéis e relatórios dos agentes |
| `ferramentas/capturar.py` | Screenshots automáticos dos cenários |
| `RELATORIO_FINAL.md`, `DEMO_GUIAO.md` | Entregáveis finais |

**Começa agora pelo ciclo 0.**

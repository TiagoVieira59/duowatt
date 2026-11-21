# Perguntas para o Tiago

1. **Prazo útil:** a ficha fala em ~10 h de trabalho e um .docx em 30 h. A entrega é às 17:30 de 21 nov. Qual é o prazo útil real da equipa?
2. **Base da casa de ~600 W ao serão:** sem fonte. Pedir valor à Mecânica.
3. **Identidade visual:** o colega de Multimédia tem paleta ou logo para a app seguir?
4. **Qual é o formato exato da entrega das 17:30 de sábado** (documento, link, vídeo, protótipo)? E o que se apresenta a 25 nov (critério 6, pitch)?
5. **Custo e instalação** (equipamento, instalador, relé): a Contabilidade e a Mecânica têm valores verificáveis? O Júri aponta esta lacuna (R2).
6. **Recolha de provas (critério 1, 20 %):** quem da equipa cria o Google Forms (`INQUERITO.md`) e faz as entrevistas (`ENTREVISTAS.md`)? Sem dados reais de utilizadores, a nota deste critério fica em 1 ou 2. Meta: 30 respostas e 3 entrevistas (1 por perfil). O script `ferramentas/analisar_inquerito.py` trata do CSV.

7. **Retoma automática (noite 2, Fase 2) NÃO criada:** o classificador de permissões do Claude Code bloqueou a criação de `ferramentas/retomar.sh` + cron (agente a relançar-se com ferramentas pré-autorizadas). Não contornei. Se a sessão parar no limite, retoma manualmente: "Lê PROGRESSO.md e continua". Para ativar, o Tiago tem de autorizar essa ação (regra de permissão Bash) e pedir de novo.

## Fase A (kit)
- `ferramentas/criar_formulario.gs` e `docs/provas/INQUERITO.md` não foram alterados (regra do prompt). O comentário do .gs aponta para caminhos antigos (`INQUERITO.md`, `FORMS_INSTRUCOES.md`, agora em `docs/provas/`). Algumas perguntas do inquérito (ex.: assistente, relatório) podem já não fazer sentido com o conceito novo: rever com a equipa. Escolha prudente: manter.

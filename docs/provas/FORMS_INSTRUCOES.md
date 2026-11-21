# Criar o inquérito no Google Forms (6 passos, ~5 minutos)

O script `ferramentas/criar_formulario.gs` cria sozinho o formulário (11 perguntas, anónimo, com texto de consentimento) e uma Google Sheet onde caem as respostas. Executa-o **uma só vez** (cada execução cria um formulário novo).

1. Abre https://script.google.com com a conta Google que vai ser dona do formulário e escolhe **Novo projeto**.
2. Apaga o código de exemplo e **cola** o conteúdo de `ferramentas/criar_formulario.gs` (no GitHub: abrir o ficheiro, botão **Raw**, selecionar tudo e copiar). Guarda com Ctrl+S.
3. No topo, escolhe a função **criarFormulario** e carrega em **Executar** (em inglês: *Run*).
4. **Autoriza** quando o Google pedir (*Rever autorizações* → a tua conta). Se aparecer "O Google não validou esta aplicação": **Avançadas** → **Aceder a … (não seguro)** → **Permitir**. O script é teu e só cria um formulário e uma folha.
5. Em baixo, no **Registo de execução** (*Execution log*), copia o **LINK DE RESPOSTA**. Aparecem também o link de edição (só para a equipa) e o da folha de respostas.
6. Partilha o link (texto abaixo). Meta: **30 respostas** (mínimo útil: 15).

Se o script der erro, cria o formulário à mão com `INQUERITO.md` (os títulos têm de começar por "P1.", "P2." … porque o analisador usa esse prefixo).

## Texto pronto para o WhatsApp
> Olá! Estou a fazer um trabalho na Universidade de Aveiro (um hackathon sobre como as casas portuguesas aquecem a água e cozinham). Podes ajudar-me a responder a 11 perguntas rápidas? Demora 2 minutos, é anónimo e é para quem tem **gás de garrafa ou esquentador** em casa. Obrigado! 🙏
> [LINK]

(Para grupos de condomínio, acrescentar: "Se partilharem com vizinhos, ajudam-me muito.")

## Depois, para analisar
1. Na Google Sheet das respostas: **Ficheiro → Transferir → Valores separados por vírgulas (.csv)** e guardar como `respostas.csv` na raiz do projeto (não é versionado).
2. `.venv/bin/python ferramentas/analisar_inquerito.py respostas.csv` escreve os números e os gráficos em `dados/`.
3. Reiniciar a app: o separador "Provas do utilizador" mostra n, os números principais e os gráficos.

## O que está e não está validado
- Validado: a sintaxe do script e a sua lógica numa simulação do Google Forms; as opções e os títulos coincidem com `analisar_inquerito.py` (testado com um CSV sintético, marcado como tal, fora do repositório).
- **Não validado:** a execução no Google (o Claude não tem acesso à tua conta). Se algum nome de método falhar, a mensagem de erro indica a linha.
- O formulário não pede nome, email nem morada.

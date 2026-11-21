/**
 * Cria o inquérito do DuoWatt no Google Forms (as mesmas perguntas de INQUERITO.md),
 * anónimo, e liga as respostas a uma Google Sheet nova.
 *
 * Como usar: ver FORMS_INSTRUCOES.md (6 passos). Executar UMA vez a função criarFormulario
 * (cada execução cria um formulário novo). No fim, o link de resposta, o link de edição e o
 * link da folha aparecem em "Registo de execução" / "Execution log".
 *
 * Os títulos das perguntas começam por "P1.", "P2." ... porque ferramentas/analisar_inquerito.py
 * identifica as colunas do CSV por esse prefixo. Não alterar os títulos.
 * Não pede nome, email nem morada.
 */
function criarFormulario() {
  var form = FormApp.create('Gás ou eletricidade em casa? (2 min, anónimo)');
  form.setDescription('Estamos a fazer um estudo para o Hackathon@ShiftE (Universidade de Aveiro) sobre como as casas portuguesas aquecem a água e cozinham. É para quem tem gás de garrafa ou esquentador. Demora cerca de 2 minutos.');
  form.setCollectEmail(false);
  form.setConfirmationMessage('Obrigado pela sua resposta!');
  form.setShowLinkToRespondAgain(false);
  try { form.setLimitOneResponsePerUser(false); } catch (e) {}
  try { form.setRequireLogin(false); } catch (e) {}

  form.addSectionHeaderItem()
    .setTitle('Antes de começar')
    .setHelpText('Este inquérito faz parte de um trabalho de estudantes da Universidade de Aveiro (Hackathon@ShiftE 2026). As respostas são anónimas: não pedimos nome, email nem morada. Os dados são usados apenas para este trabalho e apresentados de forma agregada. Responder é voluntário e pode parar quando quiser. Ao responder, aceita participar nestas condições.');

  form.addCheckboxItem()
    .setTitle('P1. Que equipamentos a gás de garrafa tem em casa?')
    .setChoiceValues(['Esquentador (água quente)', 'Fogão ou placa a gás', 'Forno a gás', 'Aquecedor a gás', 'Nenhum (só gás natural ou eletricidade)'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('P2. Em que tipo de habitação vive?')
    .setChoiceValues(['Apartamento', 'Moradia'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('P3. Quantas pessoas vivem na casa?')
    .setChoiceValues(['1', '2', '3', '4', '5 ou mais'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('P4. Que potência elétrica contratada tem?')
    .setHelpText('Está na fatura da luz, em "Potência contratada". Se não souber, escolha "Não sei".')
    .setChoiceValues(['2,3 kVA', '3,45 kVA', '4,6 kVA', '5,75 kVA', '6,9 kVA', '10,35 kVA ou mais', 'Não sei'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('P5. Já pensou em trocar o gás por equipamentos elétricos (esquentador → termoacumulador ou bomba de calor, fogão a gás → placa de indução)?')
    .setChoiceValues(['Nunca pensei', 'Já pensei, mas não avancei', 'Já pensei e vou avançar / já avancei'])
    .setRequired(true);

  var p6 = form.addCheckboxItem()
    .setTitle('P6. Se não trocou, qual é a razão principal? (escolha até 2)')
    .setChoiceValues([
      'Acho a eletricidade mais cara',
      'Não vejo vantagem',
      'Não tenho espaço para o equipamento',
      'Receio que o quadro dispare / a potência não chegue',
      'Custo da obra ou da instalação',
      'Não sei a quem pedir ajuda',
      'Só mudo quando avariar'
    ])
    .showOtherOption(true)
    .setRequired(false);
  p6.setValidation(FormApp.createCheckboxValidation()
    .setHelpText('Escolha no máximo 2 opções.')
    .requireSelectAtMost(2)
    .build());

  form.addMultipleChoiceItem()
    .setTitle('P7. Se o esquentador (ou o fogão) avariasse hoje, o que faria?')
    .setChoiceValues(['Compraria outro a gás, o mais depressa possível', 'Compraria um equipamento elétrico', 'Depende do preço e da rapidez da instalação', 'Não sei'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('P8. Alguma vez lhe disparou o quadro elétrico por ligar muitos aparelhos ao mesmo tempo?')
    .setChoiceValues(['Nunca', 'Raramente', 'Algumas vezes por ano', 'Muitas vezes'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('P9. Imagine um dispositivo no quadro que, quando liga o forno ou a placa, pausa durante uns minutos o aquecimento da água, para não ser preciso pagar mais potência. Teria interesse?')
    .setChoiceValues(['Sim', 'Talvez', 'Não', 'Não percebi'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('P10. Quanto estaria disposto a pagar, no máximo, por esse dispositivo instalado?')
    .setChoiceValues(['Nada (não pagaria)', 'Até 50 €', '50 a 150 €', '150 a 300 €', 'Mais de 300 €'])
    .setRequired(true);

  form.addTextItem()
    .setTitle('P11. Distrito onde vive (opcional)')
    .setRequired(false);

  // liga as respostas a uma Google Sheet (as colunas têm exatamente os títulos acima)
  var folha = SpreadsheetApp.create('Respostas - Gás ou eletricidade em casa (DuoWatt)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, folha.getId());

  Logger.log('LINK DE RESPOSTA (partilhar): ' + form.getPublishedUrl());
  Logger.log('LINK DE EDIÇÃO (só para a equipa): ' + form.getEditUrl());
  Logger.log('FOLHA DE RESPOSTAS: ' + folha.getUrl());
}

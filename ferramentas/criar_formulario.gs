/**
 * Cria o inquérito do DuoWatt no Google Forms (as mesmas perguntas de INQUERITO.md).
 *
 * Como usar (2 minutos, não testado: criado sem acesso à conta Google):
 *  1. Abre https://script.google.com e cria um "Novo projeto".
 *  2. Apaga o código que lá está e cola este ficheiro inteiro.
 *  3. Escolhe a função criarFormulario no menu e carrega em Executar (aceita as permissões).
 *  4. Abre Ver > Registos (ou o Registo de execução): aparecem o link para partilhar e o link para editar.
 *  5. Partilha o link de respostas. Depois, na folha de respostas: Ficheiro > Transferir > .csv
 *     e corre: .venv/bin/python ferramentas/analisar_inquerito.py respostas.csv
 *
 * Os títulos das perguntas começam por "P1.", "P2." ... porque o script de análise usa esse prefixo.
 * Não recolhe emails nem nomes.
 */
function criarFormulario() {
  var form = FormApp.create('Gás ou eletricidade em casa? (2 min, anónimo)');
  form.setDescription('Estamos a fazer um estudo para o Hackathon@ShiftE (Universidade de Aveiro) sobre como as casas portuguesas aquecem a água e cozinham. É anónimo e demora 2 minutos. Obrigado!');
  form.setCollectEmail(false);
  form.setConfirmationMessage('Obrigado pela sua resposta!');

  form.addCheckboxItem().setTitle('P1. Que equipamentos a gás de garrafa tem em casa?').setRequired(true)
    .setChoiceValues(['Esquentador (água quente)', 'Fogão ou placa a gás', 'Forno a gás', 'Aquecedor a gás', 'Nenhum (só gás natural ou eletricidade)']);

  form.addMultipleChoiceItem().setTitle('P2. Em que tipo de habitação vive?').setRequired(true)
    .setChoiceValues(['Apartamento', 'Moradia']);

  form.addMultipleChoiceItem().setTitle('P3. Quantas pessoas vivem na casa?').setRequired(true)
    .setChoiceValues(['1', '2', '3', '4', '5 ou mais']);

  form.addMultipleChoiceItem().setTitle('P4. Que potência elétrica contratada tem? (está na fatura da luz)').setRequired(true)
    .setChoiceValues(['2,3 kVA', '3,45 kVA', '4,6 kVA', '5,75 kVA', '6,9 kVA', '10,35 kVA ou mais', 'Não sei']);

  form.addMultipleChoiceItem().setTitle('P5. Já pensou em trocar o gás por equipamentos elétricos (esquentador → termoacumulador ou bomba de calor, fogão a gás → placa de indução)?').setRequired(true)
    .setChoiceValues(['Nunca pensei', 'Já pensei, mas não avancei', 'Já pensei e vou avançar / já avancei']);

  var p6 = form.addCheckboxItem().setTitle('P6. Se não trocou, qual é a razão principal? (até 2)').setRequired(false);
  p6.setChoices([
    p6.createChoice('Acho a eletricidade mais cara'),
    p6.createChoice('Não vejo vantagem'),
    p6.createChoice('Não tenho espaço para o equipamento'),
    p6.createChoice('Receio que o quadro dispare / a potência não chegue'),
    p6.createChoice('Custo da obra ou da instalação'),
    p6.createChoice('Não sei a quem pedir ajuda'),
    p6.createChoice('Só mudo quando avariar'),
    p6.createChoice('Outra', FormApp.PageNavigationType.CONTINUE)
  ]);
  p6.showOtherOption(true);

  form.addMultipleChoiceItem().setTitle('P7. Se o esquentador (ou o fogão) avariasse hoje, o que faria?').setRequired(true)
    .setChoiceValues(['Compraria outro a gás, o mais depressa possível', 'Compraria um equipamento elétrico', 'Depende do preço e da rapidez da instalação', 'Não sei']);

  form.addMultipleChoiceItem().setTitle('P8. Alguma vez lhe disparou o quadro elétrico por ligar muitos aparelhos ao mesmo tempo?').setRequired(true)
    .setChoiceValues(['Nunca', 'Raramente', 'Algumas vezes por ano', 'Muitas vezes']);

  form.addMultipleChoiceItem().setTitle('P9. Imagine um dispositivo no quadro que, quando liga o forno ou a placa, pausa durante uns minutos o aquecimento da água, para não ser preciso pagar mais potência. Teria interesse?').setRequired(true)
    .setChoiceValues(['Sim', 'Talvez', 'Não', 'Não percebi']);

  form.addMultipleChoiceItem().setTitle('P10. Quanto estaria disposto a pagar, no máximo, por esse dispositivo instalado?').setRequired(true)
    .setChoiceValues(['Nada (não pagaria)', 'Até 50 €', '50 a 150 €', '150 a 300 €', 'Mais de 300 €']);

  form.addTextItem().setTitle('P11. Distrito onde vive (opcional)').setRequired(false);

  Logger.log('Link para partilhar: ' + form.getPublishedUrl());
  Logger.log('Link para editar: ' + form.getEditUrl());
}

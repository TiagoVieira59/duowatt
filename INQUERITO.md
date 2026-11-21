# Inquérito (pronto a colar no Google Forms)

**Para quê:** critério 1 da avaliação (provas do utilizador, 20 %). Queremos dados reais de casas com gás de garrafa.
**Quem:** pessoas que vivem numa casa com **gás de garrafa** (esquentador e/ou fogão). Pede-se a familiares, vizinhos, colegas de residência, grupos de condomínio, redes sociais.
**Meta mínima:** 30 respostas até à hora da entrega (mais é melhor; 15 ainda dá percentagens com cuidado). **Nunca preencher respostas inventadas.**
**Tempo:** 2 minutos. **Anónimo:** sem nome, sem email (no Forms: não recolher endereços de email).

## Como criar o formulário
1. Google Forms → novo → título: **"Gás ou eletricidade em casa? (2 min, anónimo)"**.
2. Descrição (colar): *"Estamos a fazer um estudo para o Hackathon@ShiftE (Universidade de Aveiro) sobre como as casas portuguesas aquecem a água e cozinham. É anónimo e demora 2 minutos. Obrigado!"*
3. Criar as perguntas abaixo, **com o título exatamente igual** (os prefixos "P1.", "P2." são usados pelo script de análise).
4. Respostas → ligar a uma folha de cálculo → exportar como **CSV** quando tiver respostas (Ficheiro → Transferir → .csv).

## Perguntas
**P1. Que equipamentos a gás de garrafa tem em casa?** (caixas de verificação, obrigatória)
- Esquentador (água quente)
- Fogão ou placa a gás
- Forno a gás
- Aquecedor a gás
- Nenhum (só gás natural ou eletricidade)

**P2. Em que tipo de habitação vive?** (escolha única)
- Apartamento
- Moradia

**P3. Quantas pessoas vivem na casa?** (escolha única: 1 / 2 / 3 / 4 / 5 ou mais)

**P4. Que potência elétrica contratada tem?** (escolha única; está na fatura da luz)
- 2,3 kVA · 3,45 kVA · 4,6 kVA · 5,75 kVA · 6,9 kVA · 10,35 kVA ou mais · Não sei

**P5. Já pensou em trocar o gás por equipamentos elétricos (esquentador → termoacumulador ou bomba de calor, fogão a gás → placa de indução)?** (escolha única)
- Nunca pensei
- Já pensei, mas não avancei
- Já pensei e vou avançar / já avancei

**P6. Se não trocou, qual é a razão principal?** (caixas de verificação, até 2)
- Acho a eletricidade mais cara
- Não vejo vantagem
- Não tenho espaço para o equipamento
- Receio que o quadro dispare / a potência não chegue
- Custo da obra ou da instalação
- Não sei a quem pedir ajuda
- Só mudo quando avariar
- Outra (campo de texto)

**P7. Se o esquentador (ou o fogão) avariasse hoje, o que faria?** (escolha única)
- Compraria outro a gás, o mais depressa possível
- Compraria um equipamento elétrico
- Depende do preço e da rapidez da instalação
- Não sei

**P8. Alguma vez lhe disparou o quadro elétrico por ligar muitos aparelhos ao mesmo tempo?** (escolha única)
- Nunca · Raramente · Algumas vezes por ano · Muitas vezes

**P9. Imagine um dispositivo no quadro que, quando liga o forno ou a placa, pausa durante uns minutos o aquecimento da água, para não ser preciso pagar mais potência. Teria interesse?** (escolha única)
- Sim · Talvez · Não · Não percebi

**P10. Quanto estaria disposto a pagar, no máximo, por esse dispositivo instalado?** (escolha única)
- Nada (não pagaria) · Até 50 € · 50 a 150 € · 150 a 300 € · Mais de 300 €

(Opcional, resposta curta: **P11. Distrito onde vive.**)

## O que o script faz com isto
`ferramentas/analisar_inquerito.py` lê o CSV exportado e gera percentagens e gráficos por pergunta, para a entrega e para a app. Ver o ficheiro para o modo de uso.

## Nota ética
Anónimo, voluntário e sem dados pessoais. Não usar as respostas para outro fim.

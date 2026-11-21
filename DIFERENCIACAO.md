# Diferenciação do DuoWatt (critério 5: originalidade e diferenciação)

Estado: 21 nov 2026. Base: `PESQUISA.md`, secção "Concorrentes e alternativas existentes". **"Não encontrado" não prova que não exista**, e vários itens assentam em resultados de pesquisa, não em leitura direta da fonte (marcados "provável").

## 1. O que já existe (e portanto não é nosso)
| Tipo | Exemplos | O que fazem | Limite para o nosso caso |
|---|---|---|---|
| Gestão de carga antidisparo | Legrand Drivia with Netatmo (confirmado, ~147 € em França), Schneider Wiser "gestão anti-disparo" (provável) | Medem a potência da casa e cortam cargas para o quadro não disparar; o Wiser comuta resistências até 3 000 W (o manual cita um depósito de água) | Produto de controlo: não dizem se a casa deve trocar gás por elétrico |
| Medidores de energia e controladores programáveis | Shelly Pro EM / Pro 2PM, Sonoff POWR3 | Medem e comandam; a lógica de corte é feita pelo utilizador | Não vêm prontos como antidisparo |
| Gestores de energia com termoacumulador ou bomba de calor | SMA Sunny Home Manager 2.0, my-PV AC-THOR, Bosch Energy Manager | Controlam resistências ou bombas de calor, sobretudo com excedente solar | Pensados para quem tem solar; nenhuma ligação a Tronic encontrada |
| Simuladores de potência contratada | ERSE, EDP, Iberdrola (provável) | Sugerem o escalão de potência pelos equipamentos usados ao mesmo tempo | Só potência e tarifa; não tratam a troca de gás por elétrico |
| Dimensionamento de bomba de calor | Bosch Heatpump Advisor (descrições; página oficial não encontrada) | Escolhe e dimensiona a bomba de calor | Não indica pedir a potência contratada; não é para termoacumuladores |

## 2. O que o DuoWatt acrescenta (hipótese de diferenciação)
1. **Diagnóstico gás → elétrico** que responde "a minha casa aguenta?" com um de quatro veredictos (aguenta / aguenta com gestão / reserva de água insuficiente / precisa de mais potência), em vez de só sugerir um escalão de potência.
2. **O diagnóstico e a gestão no mesmo conceito:** o veredicto "aguenta com gestão" só existe porque há uma gestão que o torna verdadeiro. Os simuladores de potência não a têm; os gestores de carga não fazem o diagnóstico.
3. **O momento e o canal (a testar):** o diagnóstico feito **na hora da avaria**, por quem vende o aparelho (instalador ou loja), ligado à venda do termoacumulador Bosch. É a hipótese do bloqueio "só se muda na avaria" (85 % repetem gás). Nenhuma fonte encontrada tem esta ligação, mas **não verificámos o mercado de instaladores**, e as entrevistas do perfil B (`ENTREVISTAS.md`) servem para isto.
4. **Honestidade sobre os limites:** mostra os casos em que a gestão não chega e quanto custaria subir a potência.

## 3. O que NÃO podemos dizer
- "Somos os primeiros", "ninguém faz isto", "não existe": não está provado.
- Que inventámos a gestão de cargas ou o antidisparo: já existem (Legrand, Schneider, outros).
- Que os Tronic aceitam controlo externo: nada encontrado na documentação portuguesa.
- Que o diagnóstico é melhor do que o da ERSE ou o da Bosch: não comparámos com as ferramentas oficiais por dentro (a ERSE não abriu, o Heatpump Advisor só lido em descrições).

## 4. Como o dizer no pitch
> "A gestão de cargas já existe, e os simuladores de potência também. O que não encontrámos foi uma ferramenta que, no momento em que o esquentador avaria, diga à família se a casa aguenta passar a elétrico, e que, se for preciso, resolva o limite de potência sem subir o contrato. É isso que propomos testar com instaladores da Bosch."

## 5. Para a próxima verificação (antes de afirmar mais)
- Experimentar o Heatpump Advisor com uma casa fictícia de 3,45 kVA e ver se pergunta pela potência contratada.
- Ler o manual do Wiser (secção "Gestão Anti-disparo") e testar o simulador da ERSE diretamente.
- Entrevistar um instalador ou loja de esquentadores (perfil B): já existe um diagnóstico no momento da avaria?
- Análise de anterioridade e de patentes.

Leitura honesta para a nota do critério 5: o honesto é "adaptação interessante de soluções conhecidas" (nível 3). Subir para 4–5 exigiria confirmar que a combinação diagnóstico + gestão + canal Bosch é de facto nova.

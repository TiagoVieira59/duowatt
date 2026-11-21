# Júri, ciclo 1 (screenshots ciclo1c)

Visto: A, B2, C em 1366x768 "_tela" e 1920x1080 "_pagina"; D1 e D2 em 1920x1080 "_pagina"; erros.txt ("sem erros nem avisos"). Não vi B nem os "_tela" de D1/D2 nem os "_pagina" de 1366.

## Notas (0-5)

| Critério | Nota | Justificação |
|---|---|---|
| R1 CO₂ mensurável | 2 | Há números por casa (205 kg/ano a 107 g/kWh; 109 kg/ano no pior cenário) e total (4 516 t no cenário 1 %), mas o próprio ecrã diz que o CO₂ vem da eletrificação e "não é atribuído ao DuoWatt". O 1 % é arbitrário, os 205 kg não se ligam aos ">400 kg/casa" nem às 870 kt do enunciado, e o cálculo não reage às garrafas/pessoas (D2 com 50 garrafas e 8 pessoas mostra os mesmos 205 e 109 kg). |
| R2 Viabilidade real | 2 | O ecrã não mostra hardware (como se pausa o termoacumulador), custo, quem instala, nem como entra na compra de emergência (85 % repõem gás). Assume um termoacumulador, quando 60 % das casas não têm espaço para um. "Não inclui custo do equipamento" e o aviso de que a gestão de cargas já existe (Schneider, ABB) enfraquecem o argumento. |
| R3 Clareza da demo | 3 | Veredicto, gráfico com/sem gestão e comparação vêm por esta ordem e lê-se bem. Falta o problema no ecrã (só o título) e, a 1366x768, o impacto (CO₂, €) fica abaixo da dobra, por isso o último passo da história sai do ecrã. |
| R4 UI/UX e projetor | 3 | Veredicto em cores (verde/amarelo/vermelho), KPIs grandes, gráfico limpo com limite a negro. Contras: aspeto Streamlit padrão, legendas e avisos em cinzento pequeno ilegíveis num projetor, controlos da barra lateral pequenos, linhas tracejada e contínua sobrepostas em C. |
| R5 Correção técnica | 3 | Os picos fazem sentido (≈4 078 W = placa 1,8 kW + 2 kW + base; B2 dá 5 600 W com 3 kW). Há uma incoerência visível: em C o limite é 6 900 W e o pico 4 078 W, mas a "folga com a placa ligada" é 4 822 W (devia ser 2 822 W sem gestão). O mesmo desvio aparece em A (1 372 W) e D1 (222 W). A "folga" parece medida com o termoacumulador pausado, mas o texto diz o contrário. |
| R6 Honestidade | 4 | Muito bom: "n/d" em B2, "Sem gás" em D1, "não atribuído ao DuoWatt", C admite que a gestão é desnecessária, aviso "valores por validar". Perde ponto porque o KPI de topo "CO₂ evitado por casa 205 kg/ano" aparece ao lado do DuoWatt e só mais abaixo é desmentido. |
| R7 Robustez | 3 | Os extremos geram veredictos distintos e sem erros de consola: 2,3 kVA (D1), 10,35 kVA e 8 pessoas (D2), B2 (mesmo com gestão excede 40 min). Mas D2 mistura veredicto de água com veredicto de potência ("A gestão não é necessária" sobre "Reserva de água insuficiente"), mostra CO₂ inalterado com 50 garrafas, e o campo das garrafas exibe "Press Enter to apply", o que sugere que o valor pode não estar aplicado. Nenhuma sugestão acionável no B2. |

## 5 objeções mais prováveis (da mais perigosa)

1. "Onde está o impacto no CO₂ do vosso produto?" O ecrã diz que a troca de gás acontece sem o DuoWatt. O que o DuoWatt desbloqueia, e em que % das casas (só 3,45 kVA; C mostra que a 6,9 kVA não é preciso), não está quantificado.
2. "Como é que isto chega a 2,2 M de casas?" Sem custo, hardware, instalador, canal de venda ou ligação à compra de emergência (cold shower, 85 % gás), a viabilidade fica por demonstrar.
3. "A gestão de cargas já existe." O próprio aviso cita Schneider e ABB; falta dizer o que o DuoWatt tem de diferente.
4. "Assumem um termoacumulador; e o espaço?" O esquentador a gás sai, mas o ecrã não mostra a alternativa para quem não tem lugar para 100 L.
5. "Os números não batem." A folga (4 822 W a 6,9 kVA) não é 6 900 − 4 078; os 205 kg/ano não são os >400 kg do enunciado; o CO₂ não muda com as garrafas. Há ainda a "simulação ilustrativa, valores por validar".

## O que mais subiria a nota (por ordem)

1. Quantificar o impacto atribuível ao DuoWatt: % de casas a 3,45 kVA (ou "a precisar de gestão") × CO₂ por casa, ligado às 870 kt/400 kg do enunciado; ligar o CO₂ às garrafas/uso reais.
2. Mostrar o caminho real: o dispositivo (relé/contactor/ligação ao termoacumulador), custo e retorno, instalação sem eletricista especializado, e o argumento contra o "já existe".
3. Corrigir e explicar a "folga" (ou renomear), e separar o veredicto de potência do veredicto de água.
4. Pôr o impacto acima da dobra a 1366x768 (reordenar ou compactar) e aumentar o texto de apoio para projetor.
5. No B2, oferecer o passo seguinte (ex.: potência mínima a contratar ou limitar a placa a X kW) em vez de só "precisa de mais potência".

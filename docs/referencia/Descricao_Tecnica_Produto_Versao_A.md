# Bateria térmica plug-and-play, Versão A (Direct fit)
Descrição técnica para a Mecânica. **Rascunho para validação.** Todos os números marcados com (est.) são estimativas de ordem de grandeza e têm de ser verificados.

---

## 1. Objetivo do produto

Substituir um esquentador a gás (GPL) por um equipamento elétrico que:
- aproveita as ligações de água existentes;
- encaixa no espaço do esquentador antigo;
- **não ultrapassa os 3,45 kVA** de potência contratada (≈ 15 A a 230 V);
- permite uma instalação rápida, sem obras e sem reforço do quadro elétrico (hipótese a validar, ver secção 7).

Contexto: o cenário-alvo é a **troca urgente na avaria** ("banho frio"). 85% destas trocas repetem gás.

---

## 2. Princípio de funcionamento

Um esquentador a gás dá cerca de 15 a 25 kW (est.) de potência instantânea. Com 3,45 kVA isso é impossível em tempo real, pelo que o produto **armazena calor devagar e entrega-o depressa**.

1. **Carga lenta:** uma resistência elétrica aquece o acumulador térmico (a "bateria") com a potência que sobra à casa.
2. **Gestão de potência:** um sensor de corrente mede o consumo total da casa. O gestor reduz ou pausa a carga quando há outros consumos altos (forno, indução, máquina de lavar), para o disjuntor não disparar.
3. **Descarga rápida:** ao abrir a torneira, a água fria atravessa o acumulador e sai quente, sem depender da potência elétrica nesse momento.

Esquema de blocos:

```
Água fria -> [Interface hidráulica] -> [Core Unit: bateria térmica + resistência] -> Água quente
                                                  ^
                                   [Smart Power Interface]
                              sensor de corrente + controlo da resistência
```

---

## 3. Arquitetura modular

| Módulo | Conteúdo |
|---|---|
| **Core Unit** | Acumulador térmico, resistência, isolamento, eletrónica de controlo e segurança |
| **Connection Interface** | Ligações hidráulicas e suportes mecânicos (na Versão A, fixas para um modelo de referência) |
| **Smart Power Interface** | Medição do consumo da casa, limitação de potência, lógica de carga |

Decisão de projeto: a parte elétrica/inteligente é **independente** da parte hidráulica. Isto permite, mais tarde, a Versão B (kit universal) sem redesenhar o núcleo.

**Âmbito atual: só a Versão A.** A Versão B é o caminho de escala e não será desenvolvida no protótipo.

---

## 4. Dimensionamento (estimativa para validar)

**Energia de um duche (est.):**
- 8 min × 8 L/min = 64 L a 38 °C, com água fria a 15 °C.
- Q = 64 × 4,18 × (38 − 15) ≈ 6150 kJ ≈ **1,7 kWh**.

**Água armazenada a 65 °C (est.):**
- Fração de água quente na mistura = (38 − 15) / (65 − 15) ≈ 0,46, ou seja, ~**30 L** de água a 65 °C por duche.
- Com perdas, estratificação imperfeita e margem: **40 a 50 L** de capacidade útil.

**Carga (est.):** aquecer 50 L de 15 a 65 °C ≈ 2,9 kWh.
| Potência disponível para a resistência | Tempo de carga |
|---|---|
| 3,0 kW | ~1 h |
| 2,5 kW | ~1,2 h |
| 1,5 kW | ~2 h |

A potência real disponível depende do consumo restante da casa. É por isso que o gestor existe.

**Geometria (est.):** 50 L ≈ cilindro de 30 cm de diâmetro interno e ~70 cm de altura. Com isolamento (~4 cm), fica à volta de **38 cm de diâmetro × 80 cm de altura**.

---

## 5. Pontos críticos para a Mecânica (decisões a tomar)

1. **Dimensões do espaço.** O documento fala em "40 × 60 cm" sem dizer se é largura × altura ou largura × profundidade. **Precisamos de medidas reais de um esquentador de referência** (largura, altura, profundidade, posição das ligações). Muitos esquentadores têm cerca de 55 a 65 cm de altura (est.).
2. **Altura.** O cilindro de 50 L estimado (~80 cm) pode ser mais alto do que o esquentador. Opções a avaliar: volume menor, formato mais achatado, ou material de mudança de fase (PCM, mais compacto mas mais caro).
3. **Isolamento.** Espessura e material vs. perdas térmicas em standby. Quanto calor se perde por dia?
4. **Fixação.** Reaproveitar os pontos de fixação do esquentador antigo? Peso do equipamento cheio (50 L de água ≈ 50 kg + estrutura) e se a parede aguenta.
5. **Ligações hidráulicas.** Posição e diâmetro da entrada de água fria e da saída de água quente, face ao modelo de referência.
6. **Componentes de segurança:** válvula de segurança (pressão), dreno, termóstato com corte térmico, válvula misturadora termostática (anti-queimadura), e a questão da legionela (temperatura de armazenamento). As normas aplicáveis têm de ser consultadas.
7. **Ventilação e exaustão.** O esquentador a gás tinha chaminé ou tubo de exaustão. O novo equipamento não precisa dela, mas a abertura tem de ser selada de forma segura.

---

## 6. Instalação (cenário-alvo)

Meta de instalação: **menos de 1 hora, como objetivo a validar, e não como promessa.**

1. Um profissional certificado **fecha e sela a ligação de gás** e trata da exaustão do esquentador antigo.
2. Retira-se o esquentador antigo.
3. Fixa-se a Core Unit nos pontos de fixação existentes (ou em suportes dedicados).
4. Ligam-se a entrada de água fria e a saída de água quente às tubagens existentes, com válvula de segurança e dreno.
5. Liga-se à alimentação elétrica (tomada ou ligação dedicada) e instala-se o sensor de corrente.
6. Ensaio de estanquidade, ensaio elétrico e verificação de segurança.

---

## 7. Hipóteses por validar

- **"Sem reforço do quadro."** Pode ser necessário um circuito dedicado e proteção própria. A validar com um eletricista.
- **Sensor de corrente.** A forma mais fiável de medir o consumo total é uma pinça no quadro, o que implica trabalho de eletricista. Alternativas: ligação à porta HAN do contador E-REDES (opcional) ou medição só no circuito do equipamento (menos fiável).
- **Gás e exaustão** exigem sempre profissional certificado.
- Tempos de carga, dimensões e perdas são estimativas, não resultados de cálculo.

---

## 8. O que pedimos à Mecânica

1. Escolher e medir **um esquentador de referência** comum no mercado português.
2. Confirmar se o volume de ~40 a 50 L cabe no espaço, e propor alternativas se não couber.
3. Fazer o **modelo 3D em SolidWorks** da Core Unit, com cotas, ligações e fixações.
4. Gerar uma **vista explodida** dos 3 módulos e **renders** para o pitch.
5. Dizer-nos que valores da secção 4 devem mudar, para atualizarmos a simulação de potência (Informática) e o modelo de CO₂.

**Ponto de contacto Mecânica ↔ Informática:** o volume da bateria (litros) e a potência de carga (kW) definem a simulação do gestor de potência. Convém acordar estes dois números cedo.

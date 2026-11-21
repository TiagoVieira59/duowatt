O# Parâmetros do simulador (valores de partida, a validar)

Estado: valores de pesquisa web de 20 nov 2026. "Derivado" = conta minha, não vem da fonte. Tudo isto tem de ser confirmado pela equipa antes do pitch.

## Potências (para o simulador de picos)
| Item | Valor | Estado | Fonte |
|---|---|---|---|
| Limite da casa | 3,45 kVA ≈ 3 450 W (assumindo fator de potência ~1) | enunciado | PDF do desafio |
| Termoacumulador Tronic 4000 T, 80 L | 2 000 W (o de 50 L tem 1 500 W) | ficha técnica Bosch | [ficha Tronic 4000 T](https://www.bosch-homecomfort.com/pt/media/country_pool/bosch_monof_termo_tronic_4000_7m_pweb_002_002.pdf) |
| Placa de indução | ~1,8 kW (valor do documento DuoWatt) | por confirmar (Mecânica) | doc. da equipa |
| Consumo base da casa | ~0,6 kW (valor do documento DuoWatt) | por confirmar | doc. da equipa |

Conta de teste: 0,6 + 1,8 + 2,0 = **4,4 kW > 3,45** → dispara sem gestão. Com o termoacumulador pausado: 2,4 kW → aguenta.

## Água quente
- ~40 L de água quente por pessoa e por dia ([Repsol](https://www.repsol.pt/particulares/assessoramento/termoacumulador-escolher-ideal/), [Bosch](https://www.bosch-homecomfort.com/pt/pt/conhecimentos/agua-quente-sanitaria/cilindro-agua-quente/)); a ADENE usa 50 L ([manual](https://ligar.adene.pt/wp-content/uploads/2019/03/Manual-Ligar-4.-Aquecimento-Água.pdf)).
- Derivado: aquecer 40 L em ΔT = 45 °C ≈ 2,1 kWh por pessoa/dia, sem perdas. Família de 4 ≈ 8,4 kWh/dia.
- Derivado: o termoacumulador de 2 kW precisa de ~4 h ligado para isso, por isso pausá-lo 10–20 min é viável. Validar com a Mecânica.

## CO₂
| Item | Valor | Estado | Fonte |
|---|---|---|---|
| GPL (propano/butano) | 63 tCO₂/TJ, PCI 46 MJ/kg → ~2,9 kg CO₂/kg | de fichas de comercializadores que citam a DGEG | [ficha Cepsa](https://pt.cepsa.com/stfls/cepsa-pt/Ficheros/ISP-Dever_Informacao_Tabela_CEPSA_a_01022024.pdf) |
| GPL por kWh | ~0,227 kg CO₂/kWh | derivado (63 / 1000 / 3,6 × 1000) | idem |
| Eletricidade | 40 a 120 g CO₂/kWh conforme o método (APREN ~40 g; Electricity Maps ~119 g em 2024) | **sem valor oficial confirmado** | [APA](https://apambiente.pt/sites/default/files/_Clima/Inventarios/20250715/fe_gee_eletricidade_2025_final.pdf), [Electricity Maps](https://www.electricitymaps.com/grid-in-review-2025/portugal) |
| Referência do desafio | >400 kg CO₂/casa/ano (~870 kton) | enunciado | PDF do desafio |

Sanidade (derivado): 400 kg ÷ 2,9 ≈ 138 kg de GPL ≈ 10–11 garrafas de 13 kg por ano.

## Custos (para o Bloco da Contabilidade e para o pitch)
| Item | Valor | Estado | Fonte |
|---|---|---|---|
| Garrafa de butano 13 kg | ~42–44 € (ERSE, nov 2026). Notícias de julho falam de um teto de 29,47 €; conflito por resolver | por confirmar | [ERSE nov 2026](https://www.erse.pt/media/k2lk12yi/relat%C3%B3rio-mensal-nov2026.pdf) |
| Eletricidade, preço médio | ~0,198 €/kWh (BTN, 2026) | fonte de comercializador | [Repsol](https://www.repsol.pt/particulares/assessoramento/tarifa-regulada-eletricidade/) |

## Pontos de atenção
- O fator de CO₂ da eletricidade muda muito o resultado líquido: no simulador, que seja um **parâmetro ajustável** e mostra-se o intervalo.
- Entradas do diagnóstico: potência contratada, tarifa e consumo mensal (lidos da fatura de eletricidade), sem sensores. O DuoWatt é só simulado.

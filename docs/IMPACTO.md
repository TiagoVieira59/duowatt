# Impacto: CO₂ por casa e cenário nacional (critério 2)

Estado: 21 nov 2026. Valores gerados com `impacto.py` (`impacto_casa(12)` e `extrapolar`); a app usa os mesmos. Classificações: confirmado / provável / derivado / pressuposto.

**Frase honesta:** o CO₂ desce porque a casa sai do gás; o DuoWatt tira a barreira que impedia essa troca.

## Por casa e ano (12 garrafas)
12 garrafas de 13 kg ≈ 1 993 kWh de gás ≈ 452 kg de CO₂; o cilindro elétrico faz o mesmo com ≈ 1 923 kWh ≈ 206 kg.

| Cenário da rede | Fator | CO₂ evitado por casa/ano |
|---|---|---|
| Por omissão (APA 2023) | 107 g/kWh | **~246 kg** |
| Adverso (média 5 anos, APA) | 167 g/kWh | **~131 kg** |

## Cenário nacional: 1 % das casas a gás troca
`casas = 2,2 M × 1 % = 22 000`; `t CO₂ = kg por casa × casas ÷ 1000`; `% = t ÷ 870 000`.

| Cenário da rede | t CO₂/ano | % das 870 kton do enunciado |
|---|---|---|
| Por omissão (107 g/kWh) | **~5 419** | 0,6 % |
| Adverso (167 g/kWh) | **~2 881** | 0,3 % |

Não é previsão: não há dado de adoção.

## Pressupostos
| Pressuposto | Valor | Fonte | Classificação |
|---|---|---|---|
| Casas a GPL em garrafa | 2,2 M | Enunciado Bosch | confirmado |
| Emissões do GPL | 870 kton/ano | Enunciado Bosch | confirmado |
| Fator da rede | 107 g/kWh (adverso 167) | APA 2023 | confirmado |
| Eficiências | gás 0,82; elétrico 0,85 | Fichas Bosch / Energy Star | provável |
| Garrafas | 12/ano | Valor de trabalho (INE 2020 dá ~11) | pressuposto |
| Adoção 1 % | 22 000 casas | Cenário ilustrativo | pressuposto |
| Todas as trocas atribuídas ao DuoWatt | sim | Simplificação | pressuposto |

## Limites
- O cenário supõe que as casas que trocam o fazem por causa do kit; é um teto de atribuição, não uma medição.
- O fator da rede é média anual, não marginal.
- Não inclui o custo do aparelho novo nem o consumo do kit.
- O enunciado refere >400 kg por casa (o que o gás emite); a eletricidade também emite, por isso o evitado é cerca de metade.

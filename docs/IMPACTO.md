# Impacto do DuoWatt: métrica principal e sensibilidade (critério 2)

Estado: 21 nov 2026. Gerado com as funções de `impacto.py` (`impacto_casa`, `metrica_principal`); os números da app são os mesmos. Classificações: confirmado / provável / derivado / hipótese.

## 1. A métrica principal
**Casas em que o bloqueio da potência é removido**, o **CO₂ atribuível** (t/ano e % das 870 kton do enunciado) e a **oportunidade para a Bosch** (parte proporcional dos 60 M€/ano do enunciado).

`casas = 2,2 M × 44 % × adoção`; `t CO₂ = kg evitados por casa × casas ÷ 1000`; `% = t CO₂ ÷ 870 000`; `M€ = 60 × casas ÷ 2,2 M`.

| Pressuposto | Valor | Fonte | Classificação |
|---|---|---|---|
| Casas a GPL | 2,2 M | Enunciado Bosch | confirmado |
| Emissões do GPL | 870 kton/ano (>400 kg/casa) | Enunciado Bosch | confirmado |
| Mercado | 60 M€/ano | Enunciado Bosch | confirmado |
| Casas onde a potência é o bloqueio | ≤44 % (teto) | E-REDES 2023: contratos <3,45 kVA em 44,1 % dos BTN; inclui não domésticos | provável (proxy) |
| Adoção | 1 / 5 / 10 % | Cenários ilustrativos, sem dado | hipótese |
| Mercado por casa | proporcional (≈27 €/casa) | 60 M€ ÷ 2,2 M | hipótese |
| Fator da rede | 107 g/kWh (adverso 167) | APA 2023 | confirmado |
| Eficiências | gás 0,82; elétrico 0,85 | Esquentador / Energy Star | provável |
| Garrafas | 12/ano (uma por mês) | Valor típico de trabalho | hipótese |

## 2. Resultado com os valores por omissão (12 garrafas, 107 g/kWh)

| Adoção | Casas desbloqueadas | t CO₂/ano | % das 870 kton | M€/ano do mercado |
|---|---|---|---|---|
| 1 % | 9 680 | 2 384 | 0,3 % | 0,3 |
| 5 % | 48 400 | 11 922 | 1,4 % | 1,3 |
| 10 % | 96 800 | 23 845 | 2,7 % | 2,6 |

**Leitura honesta:** mesmo com 10 % de adoção, o DuoWatt só atribui ~2,7 % das 870 kton: o grande potencial está na eletrificação em si, e o DuoWatt tira apenas o bloqueio da potência. O CO₂ vem de trocar gás por elétrico, não do equipamento. Não é previsão: não há dado de adoção.

## 3. Sensibilidade (t CO₂/ano atribuíveis; adoção × fator da rede × garrafas)

| Garrafas/ano | Fator (g/kWh) | kg/casa | 1 % | 5 % | 10 % |
|---|---|---|---|---|---|
| 6 | 107 | 123 | 1 192 | 5 961 | 11 922 |
| 6 | 167 | 65 | 634 | 3 169 | 6 338 |
| 12 | 107 | 246 | 2 384 | 11 922 | 23 845 |
| 12 | 167 | 131 | 1 268 | 6 338 | 12 676 |
| 18 | 107 | 369 | 3 577 | 17 883 | 35 767 |
| 18 | 167 | 196 | 1 901 | 9 507 | 19 014 |

## 4. Limites
- A quota de 44 % é um teto: inclui contratos não domésticos e casas sem gás; só uma parte tem a potência como bloqueio e só algumas passam a «aguenta com gestão».
- O fator da rede é média anual, não marginal.
- Não inclui o custo do aparelho novo nem o consumo do controlador.
- Vendas de Tronic: não há dado de quantas casas comprariam; a oportunidade é só a parte proporcional dos 60 M€ (hipótese).

# Viabilidade do DuoWatt (critério 4: técnica, económica e de implementação)

Estado: 21 nov 2026. Os preços vêm de pesquisa web (ver `PESQUISA.md`, secção "Custos para a viabilidade do DuoWatt"). Cada valor leva a classificação **confirmado / provável / derivado / hipótese**. Nada aqui é uma cotação oficial nem um resultado de ensaio.

## 1. O que é tecnicamente
Um medidor de corrente no quadro lê a potência total da casa; um controlador decide; um relé ou contactor corta e retoma o circuito do termoacumulador (2 kW) quando a placa de indução faz a casa aproximar-se do limite (3,45 kVA). A lógica já está simulada em `duowatt.py`. Tecnologia usada: componentes que existem no mercado (medidor Wi-Fi com pinça, relé, contactor modular).

**Plausibilidade:** 2 kW a 230 V são ~8,7 A (derivado), dentro dos 16 A do relé de um controlador comercial (Shelly Pro 2PM). A instalação no quadro deve ser feita por um eletricista habilitado.

## 2. Custo do DuoWatt (protótipo, com componentes de retalho)
| Item | Preço | Classificação | Fonte |
|---|---|---|---|
| Medidor com pinça (Shelly Pro EM 50) | 101,88 € | confirmado (IVA incluído) | Domadoo PT |
| Controlador Wi-Fi com relé 16 A (Shelly Pro 2PM) | 69,99 € | confirmado (IVA incluído) | Powerplanet PT |
| Contactor modular 25 A bipolar (Hager ESC225) | 49,78 € | provável (IVA não confirmado) | catálogo Hager |
| **Material, sem contactor** | **171,87 €** | derivado | |
| **Material, com contactor** | **221,65 €** | derivado | |
| Mão de obra do eletricista | ~30 €/h | provável (plataformas, não tarifa oficial) | Habitissimo, Zaask |
| Instalação (hipótese: 1 a 2 horas) | 30 a 60 € | hipótese | |
| **Total instalado, quadro já adequado** | **~200 a 280 €** | derivado | |
| Se for preciso quadro novo | +150 a 400 € | provável | Zaask, expert-zoom |
| **Total instalado, com quadro novo** | **~370 a 620 €** | derivado | |

Fica de fora o termoacumulador (Tronic 4000 T de 80 L: 245 a 255 €, provável, lojas PT) porque é igual com ou sem DuoWatt.
Um produto industrial da Bosch, em escala, custaria menos do que montar peças de retalho, mas **não temos dado para estimar** quanto.

## 3. A alternativa: aumentar a potência (3,45 → 6,9 kVA)
| Item | Valor | Classificação |
|---|---|---|
| Termo de potência a 3,45 kVA | 0,1917 €/dia | confirmado (ERSE, Diretiva 4/2026) |
| Termo de potência a 6,9 kVA | 0,3659 €/dia | confirmado (idem; a coluna exata do PDF convém rever) |
| Diferença | **~63,6 €/ano sem IVA** (~78 €/ano com IVA de 23 %) | derivado (o IVA aplicável não foi verificado) |
| Custo único | **não encontrado**: se a instalação já suporta 6,9 kVA, em geral sem custos; se precisar de reforço, orçamento da E-REDES (um relato isolado fala em ~1 000 €, anedótico) | provável / não encontrado |

## 4. Comparação a 10 anos (preços constantes, sem desconto)
| | Subir a potência | DuoWatt |
|---|---|---|
| Custo único | ~0 € (se a instalação já suportar) | ~200 a 280 € (quadro adequado) ou ~370 a 620 € (quadro novo) |
| Custo anual | +64 a 78 €/ano | ~0 € (consumo do controlador não estimado) |
| Total em 10 anos | **~640 a 780 €** | **~200 a 280 €** ou **~370 a 620 €** |
| Equilíbrio | | o DuoWatt compensa ao fim de **~2,6 a 4,4 anos** (quadro adequado) ou **~4,8 a 9,8 anos** (quadro novo) (derivado) |

**Efeito na fatura da família** (valores por omissão da app, derivados): a troca de gás por elétrico poupa ~33 €/ano de combustível (sensível ao preço da garrafa: ~99 € com a garrafa a 43,55 €). Se subir a potência, isso passa a **−31 €/ano** (custo extra). Com o DuoWatt, amortizado em 10 anos (~25 €/ano), fica **~+8 €/ano**. A mensagem honesta é **"descarboniza sem custar mais"**, e não "poupa dinheiro". Os custos do aparelho novo não estão incluídos em nenhum dos caminhos.

## 5. Benefícios
**Para a família:** evita pagar mais potência (64 a 78 €/ano) ou obras; mantém a água quente (0 min sem água no cenário típico); menos risco de disparo (25 → 0 min acima do limite no cenário típico). Só em casas em que a gestão chega: com indução intensa e base alta (cenário B2) a casa continua a precisar de mais potência.
**Para a Bosch (hipóteses, por validar com a Bosch):** vender termoacumuladores Tronic a casas que hoje ficam no gás por receio da potência; ligar o diagnóstico ao momento da compra (instalador, loja); abrir um acessório ou serviço novo. Não está confirmado que os Tronic aceitem controlo externo (nada encontrado na documentação portuguesa); o corte seria por contactor no circuito.
**Para o clima:** até ~205 kg de CO₂ por casa e ano evitados pela eletrificação (107 g/kWh; 109 kg com 167 g/kWh), dos quais só a parte das casas bloqueadas pela potência depende do DuoWatt: limite superior ~44 % das casas (proxy, ver app).

## 6. Riscos e limites
- Segurança elétrica: instalação por eletricista habilitado; normas, proteções, anti-legionela e temperatura sanitária a validar.
- O disjuntor real tolera sobrecargas curtas: "disparos" é risco, não certeza.
- A maioria das casas a gás tem **esquentador (67 %)**, não termoacumulador (17 %): teriam de comprar o aparelho novo (custo não incluído) e ter espaço. É a objeção do espaço, que o DuoWatt não resolve.
- A gestão de cargas já existe no mercado (Schneider, ABB e outros); a diferença está no diagnóstico e na ligação à venda (ver `DIFERENCIACAO.md`).
- Valores por confirmar: taxa da E-REDES, TAR, IVA do contactor, certificação do eletricista, preço de um produto industrial.

## 7. Próximos passos concretos para a Bosch
1. **Validar a segurança** com um eletricista habilitado (guião do perfil C em `ENTREVISTAS.md`) e com a equipa de produto: contactor/relé, proteções, normas.
2. **Perguntar à Bosch** se algum Tronic ou a app HomeCom Easy aceita controlo externo; se sim, o hardware pode reduzir-se ao medidor.
3. **Ensaio em bancada** (tensão baixa ou com carga fictícia) para medir minutos acima do limite, comutações e água quente.
4. **Piloto** com 20 a 30 casas de instaladores parceiros (por exemplo, na região de Aveiro) com o diagnóstico no momento da avaria: medir adesão, trocas feitas e minutos acima do limite.
5. **Obter dados em falta:** percentagem de casas a GPL por potência contratada (E-REDES/ERSE), taxa de alteração de potência.
6. **Análise de anterioridade** e de patentes antes de qualquer afirmação de novidade.

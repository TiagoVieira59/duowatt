# BACKLOG (ciclo 1)

Fontes: `equipa/juri_ciclo0.md`, `equipa/ux_ciclo1.md`, `equipa/modelo_ciclo1.md`. Impacto/esforço: A/M/B e P/M/G.

## Escolhidos para o ciclo 1 (5 itens, em 2 lotes pelo mesmo Programador)

**Lote 1 (UI)**
| # | Item | Evidência | Rubrica | Imp. | Esf. | Decisão |
|---|---|---|---|---|---|---|
| I1 | Acima da dobra em 1366×768: título curto, sidebar recolhida ou entradas avançadas recolhidas (kVA, consumo e indução à vista), 3 números-chave (veredicto, pico sem/com gestão, CO₂); métricas 2 por coluna sem "episódios"; frase de uma linha por cenário ("gestão não necessária" / "mesmo com gestão excede"); margem em W | UX: 1366 só mostra título+veredicto+gráfico; Júri R3 | R3, R4 | A | M | fazer |
| I2 | Gráfico só 17:00–23:00 com Altair (domínio explícito, horas formatadas), limite grosso e rotulado, serão sombreado, "Sem gestão" tracejado atrás de "Com DuoWatt" | UX: serão pequeno, "24.0" cortado, curvas coincidem em C/B2; 28+ avisos "Infinite extent" | R3, R4, R7 | A | M | fazer |
| I3 | Legibilidade em projetor: CSS (legendas ≥16 px, contraste, eixos ≥14 px), esconder "Deploy" (`toolbarMode="minimal"`), avisos honestos compactos (2 linhas + expander, sempre visíveis) | UX/Júri: letra pequena e cinzenta, Deploy visível, avisos minúsculos | R4, R6 | A | P | fazer |

**Lote 2 (honestidade e modelo)**
| # | Item | Evidência | Rubrica | Imp. | Esf. | Decisão |
|---|---|---|---|---|---|---|
| I4 | Atribuição do impacto: dizer que o CO₂ vem da eletrificação e que o DuoWatt desbloqueia a troca (qualitativo: "sem gestão esta casa teria de aumentar a potência"); extrapolação como "potencial da eletrificação"; "disparos" → "pode disparar"; extremos coerentes (0 garrafas = sem gás para substituir; slider de garrafas até 20; aviso quando há minutos sem água quente) | Júri objeção 1 e 5; D1/D2 incoerentes; Modelador §4 | R1, R5, R6, R7 | A | M | fazer |
| I5 | Higiene do modelo: corrigir o comentário de `impacto.py` (0,171 € é sem IVA), validar `efic_eletrica`>0, resolver os `xfail` do `test_modelo_ciclo1.py` que sejam correções simples | Modelador §1, §6 | R5 | M | P | fazer |

## Adiados (e porquê)
- **Custo, instalação e integração com hardware Bosch (R2, objeção 2):** não há dados verificados; precisa da Contabilidade e da Mecânica → `PERGUNTAS.md`.
- **Objeção 4 (espaço, compra urgente, esquentador em vez de termoacumulador):** é conteúdo do pitch, não da app → `DEMO_GUIAO.md` no fecho.
- **Entrada "base ao serão" (~600 W):** sem fonte; mostra-se a margem em W (I1) e pergunta-se à Mecânica.
- **Modo de apresentação com cenários pré-definidos:** reavaliar no ciclo 2 se o Júri ainda baixar R3.

## Rejeitados
- Mudar o preço para 0,18 €/kWh: o Modelador mostra que exagera a poupança 2,4× (0,21 €/kWh é o marginal certo acima de 200 kWh/mês). Mantém-se 0,21.

## Ciclo 1, lote 3 (polimento da UI, depois do lote 2; fonte: `equipa/ux_ciclo1_revisao.md` + verificação minha do screenshot A 1366×768)
| # | Item | Evidência | Rubrica | Imp. | Esf. |
|---|---|---|---|---|---|
| I6 | **Bug do eixo X:** as camadas `serao` e `rotulo` do gráfico usam `x` sem o domínio 17–23, e a escala partilhada volta a começar em 0 h; os dados ficam numa fatia de ~25 % do gráfico. Usar a mesma `alt.Scale(domain=[17,23], zero=False, nice=False)` em todas as camadas | `screenshots/ciclo1/A_tipica_1366x768_tela.png` (eixo a começar muito antes das 17:00) | R3, R4 | A | P |
| I7 | Etiqueta "Limite 3,45 kW" colide com o pico tracejado: pô-la à direita; "Sem gestão" tracejado desenhado mais grosso por trás para ficar visível em C (curvas coincidem) | UX revisão, problemas novos 1 e 4 | R3, R4 | A | P |
| I8 | Frases sem jargão: "Margem ao serão (limite menos base menos indução)" → "Folga com a placa ligada: X W" / "Faltam X W"; rótulos de CO₂ que reconciliam 205 kg (107 g/kWh) com 109 kg ("no pior cenário, 167 g/kWh"); peso menor para as toneladas nacionais | UX revisão, 3 e 4 | R3, R6 | M | P |
| I9 | Legenda e eixos mais escuros (≥ #222) e maiores (≥16 px); texto dos campos da sidebar ≥16 px | UX revisão, parciais 1, 2, 5, 6, 12 | R4 | M | P |

# DuoWatt — ficha de uma página (proposta para a equipa)

Hackathon@ShiftE 2026 · Desafio Bosch · Entrega: 21 nov, 17:30 · Rascunho do Tiago (Eng. Informática)

## O problema (em simples)
~2,2 M de casas portuguesas usam gás para o banho e a cozinha. Muitas têm potência contratada baixa (3,45 kVA). Se ligarem a placa de indução e o termoacumulador ao mesmo tempo, o quadro dispara. A família conclui "eletrificar = pagar mais potência ou fazer obras" e fica com o gás.

## A ideia: DuoWatt, em duas partes
1. **Diagnóstico (antes da troca):** a casa tem potência para passar de gás a elétrico? Resposta: "aguenta" / "aguenta com gestão" / "precisa de mais potência".
2. **Gestão (depois da troca):** um controlador pausa o termoacumulador uns minutos quando se usa a indução, e retoma depois. Em casos de uso normal, a casa não dispara e não é preciso aumentar a potência (a validar; com indução forte ou base alta pode não chegar).

Posicionamento: **complemento dos termoacumuladores Tronic da Bosch**, não produto concorrente. Nota: não encontrámos controlo externo documentado nos Tronic; a gestão seria um relé no circuito do termoacumulador (a confirmar com a Mecânica). O modelo de 2 kW confirmado é o Tronic 4001 T de 80 L ou mais.

## Que bloqueios resolve
| Bloqueio | Resolve? | Como |
|---|---|---|
| Potência contratada | **Sim** | Gestão de cargas dentro do limite |
| Não veem vantagem | Em parte | Diagnóstico claro, custo e CO₂ visíveis |
| Venda complexa | Em parte | Menos intervenções (sem aumentar potência / reforçar quadro) |
| Troca só na avaria | Em parte (hipótese) | Diagnóstico em ~2 min no momento da avaria |
| Falta de espaço | Não | Fica para Mecânica / Bridge |
| Falta de instaladores | Não | Ainda precisa de eletricista |

## O que vamos construir em ~10 h (software, sem hardware)
- **Simulador** de 24 h de uma casa de 3,45 kVA, com e sem gestão (picos, cortes, água quente disponível).
- **Modelo de CO₂:** poupança por casa e extrapolação para as 2,2 M de casas.
- **Veredicto** do diagnóstico (3 respostas acima).
- Se sobrar tempo: fluxo clicável "troca num só passo".

## Divisão sugerida (a confirmar com a equipa)
- Informática: simulador, modelo de CO₂, veredicto.
- Mecânica: potências reais dos aparelhos, reserva de água quente.
- Contabilidade: custo a 10 anos gás vs. elétrico.
- Multimédia: interface e pitch.
- Ciência Política: contexto PNEC/RNC, incentivos, pesquisa.

## Plano até às 17:30
Reunião de 30 min a fechar a decisão → ~5 h simulador + CO₂ → ~2 h demo e gráficos → ~1 h pitch → **1 h de margem**.

## Como dizer ao júri (honestidade)
- Pesquisa feita: não encontrámos uma ferramenta pública da Bosch que diga se a casa aguenta a eletrificação. O Energy Manager serve casas com solar + bomba de calor; o Heatpump Advisor dimensiona bombas de calor. **Isto não prova que não exista.**
- A gestão de cargas já existe (Schneider Wiser, ABB). Não dizer "somos os primeiros".
- Não prometer "sem eletricista" nem proteção total.
- O CO₂ só desce quando o gás é mesmo substituído.

## Por verificar antes do pitch
- [ ] Experimentar o Heatpump Advisor com uma casa fictícia de 3,45 kVA: pergunta pela potência contratada? Cobre termoacumuladores?
- [ ] Confirmar se algum Tronic permite controlo/corte externo.
- [ ] Valores de consumo, preço de eletricidade/GPL e fator de emissão do GPL (fontes oficiais, ex.: DGEG).
- [ ] Confirmar com a equipa: prazo (10 h úteis) e escolha DuoWatt vs. Bridge.

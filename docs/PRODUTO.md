# DuoWatt: produto numa página

*Garantia sem apagões.* Estado: 21 nov 2026. Só software e simulação; nenhum hardware construído. Classificação dos números: confirmado / provável / derivado / pressuposto.

**Numa frase:** o DuoWatt é um kit que completa os cilindros elétricos Bosch: pausa o cilindro sozinho antes de a luz ir abaixo, para que as casas com esquentador a gás passem para elétrico sem medo e sem aumentar a potência.

## Problema
Quem tem esquentador a gás não muda para cilindro elétrico com medo de que a luz vá abaixo, e por achar que teria de subir a potência contratada, pagar mais e tratar de burocracias. Segundo o enunciado, 85 % das trocas urgentes de esquentador são "gás por gás".

## User stories
**US1, a família.** *Como família com esquentador a gás e 3,45 kVA, quero passar para um cilindro elétrico sem que a luz vá abaixo, para deixar o gás sem pagar mais pela potência.*
Aceitação na demo: ao fim da tarde o cilindro (Tronic 5501i, 1,5 kW) aquece e a máquina da roupa liga (~2 kW, ~20 min); base da casa ~0,6 kW (todos pressupostos). Total sem DuoWatt ≈ 4,1 kW, acima dos 3,45 kVA. Sem DuoWatt a luz vai abaixo; com DuoWatt o cilindro pausa, a luz mantém-se e há 0 minutos sem água quente. Número: evita ~64–78 €/ano (não sobe a potência; estimativa).

**US2, a Bosch e o instalador.** *Como instalador da Bosch, numa troca urgente de esquentador, quero oferecer um cilindro com garantia sem apagões, para vender um cilindro em vez de outro esquentador a gás.*
Aceitação na demo: CO₂ evitado por casa e ano (12 garrafas) e cenário nacional de 1 % (ver `IMPACTO.md`), com o cenário adverso da rede; texto curto "para a Bosch"; diagrama e concorrência.

## A solução: o kit (2 peças, emparelhadas de fábrica)
1. **Sensor no quadro elétrico:** mede o consumo total da casa em tempo real.
2. **Módulo de controlo do cilindro:** tomada de potência ou relé, conforme a instalação. Evolução com a Bosch: integrado no Tronic 5501i (tem Wi-Fi) e o kit passa a ser só o sensor.

## Como funciona
Ligação **local e direta** entre as peças, sem internet. Consumo acima de ~90 % do limite: cilindro desligado de imediato. Volta a ligar abaixo de ~80 %. Pausa máxima de 30 min seguidos (prioridade à água quente). Se o sensor deixar de comunicar, o cilindro volta ao funcionamento normal. Regras 90/80/30 min e pressupostos em `PARAMETROS.md`; máquina de estados em `ARQUITETURA.md`.

## O que não faz
Sem app para a família, avisos, histórico, porta HAN, sensor de temperatura, assistente nem relatório. **Limite assumido:** se a casa passar o limite mesmo sem o cilindro, o DuoWatt não resolve. Promessa exata: *"o cilindro nunca é a causa do apagão"*.

## Fator wow face aos Tronic
Pelo que vimos na gama Tronic, o cilindro sabe quando a família precisa de água quente (Wi-Fi, HomeCom Easy, modos Smart/Eco/programado), mas não o que se passa no resto da casa. O DuoWatt acrescenta isso. "O 5501i já tem programação; não chega?" A programação usa horas fixas; a máquina da roupa pode ligar a qualquer hora. O DuoWatt reage ao que está a acontecer.

## Negócio, diferenciação, impacto
- **Cliente: a Bosch (B2B).** Compra os kits e inclui-os no Tronic ou vende-os como opção na troca do esquentador. Transforma trocas gás por gás em vendas de cilindro e diferencia os Tronic. Família: não sobe a potência (3,45 para 6,9 kVA custa ~64–78 €/ano, estimativa em `NEGOCIO.md`). Preços e custos do kit: `[a preencher pela Contabilidade]` (ver `NEGOCIO.md`).
- **Diferenciação:** quem paga (a Bosch), quando se vende (na avaria, pelo mesmo instalador), simplicidade (2 peças, sem hub, app nem internet), mercado (Portugal e Espanha) e integração com os Tronic. Ver `CONCORRENCIA.md`.
- **Impacto:** ~246 kg de CO₂ por casa e ano (131 kg no cenário adverso); 1 % das casas a gás: ~5 419 t/ano. O CO₂ desce porque a casa sai do gás; o DuoWatt tira a barreira que impedia essa troca.

## Riscos e respostas
| Risco | Resposta |
|---|---|
| "A tecnologia já existe" | Existe em quadros e hubs (Schneider, Legrand, Delta Dore, Shelly); a diferença é o par emparelhado para o cilindro, pago pela Bosch e vendido na avaria. Sem "somos os primeiros". |
| Não resolve o espaço | Verdade: 67 % das casas têm esquentador e 17 % termoacumulador (INE 2020). O DuoWatt resolve a potência, não o espaço. |
| Precisa de técnico | Sim, instalação por eletricista habilitado; segurança por validar. |
| A Bosch podia fazer sozinha | Sim, e é a evolução prevista (integrar no 5501i). O kit é o caminho rápido e valida a regra num piloto. |
| A casa passa o limite sem o cilindro | Limite assumido; o cilindro nunca é a causa. |

## Próximos passos
Piloto com a Bosch para medir o tempo real de corte do contador (pressuposto); integração no Tronic 5501i; certificação CE.

# Arquitetura

Estado: 21 nov 2026. Só simulação em software (`duowatt.py`); nada de hardware construído.

## Diagrama
```
Quadro elétrico --> [Sensor] --(ligação local, sem internet)--> [Módulo] --> Cilindro (Tronic 5501i, 1,5 kW)
  consumo total        mede a casa      emparelhados de fábrica   tomada de potência ou relé
```

## Máquina de estados
| Estado | Transição | Novo estado |
|---|---|---|
| `NORMAL` | consumo da casa ≥ ~90 % do limite | `CILINDRO_PAUSADO` |
| `CILINDRO_PAUSADO` | consumo < ~80 % do limite (histerese) | `NORMAL` |
| `CILINDRO_PAUSADO` | pausa chegou a 30 min seguidos | `NORMAL` (prioridade à água quente) |
| qualquer | sem sinal do sensor > 5 s | `NORMAL` (modo seguro: como sem DuoWatt) |

Regras 90/80/30 min e 5 s: pressupostos (`PARAMETROS.md`).

## Porque é local e sem internet
Corte rápido e independente do Wi-Fi do cliente ou de servidores; menos pontos de falha e sem dados a sair de casa. Falha segura: sem sinal, tudo volta ao normal.

## Tempo de reação vs. EN 60898
A norma dos disjuntores domésticos dá segundos a minutos de tolerância: 1,13× não dispara em 1 h; 1,45× dispara em menos de 1 h; 2,55× dispara entre 1 e 60 s. Cortar o cilindro de imediato aos 90 % fica dentro dessa margem. O tempo real do contador inteligente é **pressuposto a validar num piloto com a Bosch**.

## Evolução
Integrar o módulo no Tronic 5501i (já tem Wi-Fi): o kit passa a ser só o sensor.

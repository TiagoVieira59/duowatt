"""DuoWatt: simulação por minuto de um serão (18:00-21:00) numa casa de 3,45 kVA.

Conceito em docs/referencia/PROMPT_Kit_DuoWatt_Final.md. Valores marcados "pressuposto" por validar.
"""

P_CILINDRO_W = 1500           # Tronic 5501i (ficha Bosch)
BASE_W = 600                  # pressuposto: base da casa
LIMITE_W = 3450               # 3,45 kVA tratado como kW (shortcut: fator de potência 1)
INICIO, FIM = 18 * 60, 21 * 60
# cenário -> (potência W, início min, fim min); máquina: ~2 kW durante 20 min (pressuposto)
CENARIOS = {"maquina": (2000, 18 * 60 + 40, 19 * 60), "inducao": (1800, 19 * 60 + 30, 20 * 60 + 10)}
DUCHE_MIN, DUCHE_INICIO = 15, 19 * 60 + 45
KWH_LITRO = 50 * 1.163 / 1000                     # reserva: 15 -> 65 °C
KWH_AQS_PESSOA = 40 * 45 * 1.163 / 1000           # ~2,1 kWh por pessoa e dia
PAUSA_MAX_MIN = 30


def simular(cenario="maquina", duowatt=True, limite_w=LIMITE_W, sensor_ok=True, litros=100,
            pessoas=3, base_w=BASE_W, reserva_inicial=0.5):
    """Devolve a potência de cada minuto e as métricas do serão.

    Regras (§1): desliga se a casa com o cilindro passa 90 % do limite; religa quando o consumo
    medido sem o cilindro desce abaixo de 80 %. Acrescento: só religa se com o cilindro não
    ultrapassa o limite (senão ligava e desligava a cada minuto); após 30 min de pausa religa à
    força (prioridade à água quente) e fica ligado até a casa, sem o cilindro, descer de 80 %.
    sensor_ok=False: modo seguro, cilindro como sem DuoWatt.
    """
    p_maq, ini, fim = CENARIOS[cenario]
    capacidade = litros * KWH_LITRO
    guardado = capacidade * reserva_inicial        # ao fim da tarde o cilindro está a aquecer
    pedido = pessoas * KWH_AQS_PESSOA * 0.6 / DUCHE_MIN
    ligado = forcado = False
    pausa = max_pausa = 0
    total, cil, sem_agua = [], [], 0

    for t in range(INICIO, FIM):
        casa = base_w + (p_maq if ini <= t < fim else 0)
        if DUCHE_INICIO <= t < DUCHE_INICIO + DUCHE_MIN:
            sem_agua += pedido > guardado + 1e-9
            guardado = max(0.0, guardado - pedido)
        quer = guardado < capacidade
        if not (duowatt and sensor_ok):
            ligado = quer
        elif not quer:
            ligado = forcado = False
        elif ligado and casa + P_CILINDRO_W > 0.9 * limite_w and not forcado:
            ligado = False
        elif not ligado and (pausa >= PAUSA_MAX_MIN or
                             (casa < 0.8 * limite_w and casa + P_CILINDRO_W <= limite_w)):
            ligado, forcado = True, pausa >= PAUSA_MAX_MIN
        if forcado and casa < 0.8 * limite_w:
            forcado = False
        pausa = 0 if ligado or not quer else pausa + 1
        max_pausa = max(max_pausa, pausa)
        if ligado:
            guardado = min(capacidade, guardado + P_CILINDRO_W / 60 / 1000)
        cil.append(P_CILINDRO_W if ligado else 0)
        total.append(casa + cil[-1])

    acima = [w > limite_w for w in total]
    return {
        "total_w": total,
        "cilindro_w": cil,
        "minutos_acima": sum(acima),
        "disparos": sum(1 for i, a in enumerate(acima) if a and (i == 0 or not acima[i - 1])),
        "minutos_sem_agua": int(sem_agua),
        "max_pausa_min": max_pausa,
        "pico_w": max(total),
    }


if __name__ == "__main__":
    sem, com = simular(duowatt=False), simular()
    assert sem["pico_w"] == 4100 and sem["disparos"] == 1 and com["minutos_acima"] == 0
    for nome, r in (("sem DuoWatt", sem), ("com DuoWatt", com)):
        print(f"{nome}: pico {r['pico_w']} W | minutos acima {r['minutos_acima']} | disparos "
              f"{r['disparos']} | sem água quente {r['minutos_sem_agua']} | pausa máx {r['max_pausa_min']} min")

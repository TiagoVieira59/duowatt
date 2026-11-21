"""DuoWatt: simulador de potência de uma casa durante 24 h (um passo por minuto).

Modelo simples e didático. Valores de partida em Parametros_Simulador.md (a validar).
"""

MIN_DIA = 24 * 60
P_INDUCAO_W = 1800            # placa de indução (valor do documento da equipa)
P_TERMO_W = 2000              # Tronic 4001 T de 80 L ou mais (ficha Bosch); o 5501i T é de 1 500 W
INDUCAO = range(19 * 60 + 30, 20 * 60 + 10)       # 19:30-20:10
DUCHES = {7 * 60 + 30: 0.4, 19 * 60 + 45: 0.6}    # início (min) -> fração da água quente do dia
DUCHE_MIN = 15
KWH_LITRO = 50 * 1.163 / 1000                     # reserva: 15 -> 65 °C
KWH_AQS_PESSOA = 40 * 45 * 1.163 / 1000           # ~2,1 kWh por pessoa e dia


def simular(limite_w, consumo_mensal_kwh, pessoas=3, litros=100, gestao=True, pausa_min=5,
            inducao_w=P_INDUCAO_W):
    """Devolve a potência de cada minuto e as métricas do dia.

    shortcut: kVA tratado como kW (fator de potência 1) e base da casa plana
    (consumo mensal / 720 h); melhorar se houver dados reais ou protótipo.
    """
    base_w = consumo_mensal_kwh / 720 * 1000
    capacidade = litros * KWH_LITRO
    dia = pessoas * KWH_AQS_PESSOA
    guardado, ligado, desde = capacidade, False, -pausa_min
    total, sem_agua = [], 0

    for t in range(MIN_DIA):
        inducao = inducao_w if t in INDUCAO else 0

        for inicio, fracao in DUCHES.items():
            if inicio <= t < inicio + DUCHE_MIN:
                pedido = dia * fracao / DUCHE_MIN
                sem_agua += pedido > guardado + 1e-9
                guardado = max(0.0, guardado - pedido)

        quer = guardado < capacidade
        if not gestao:
            ligado = quer
        else:
            cabe = base_w + inducao + P_TERMO_W <= limite_w
            if ligado and not (quer and cabe):          # desligar é sempre imediato
                ligado, desde = False, t
            elif not ligado and quer and cabe and t - desde >= pausa_min:
                ligado, desde = True, t                 # retomar só após o tempo mínimo

        if ligado:
            guardado = min(capacidade, guardado + P_TERMO_W / 60 / 1000)
        total.append(base_w + inducao + (P_TERMO_W if ligado else 0))

    acima = [w > limite_w for w in total]
    return {
        "total_w": total,
        "minutos_acima": sum(acima),
        "disparos": sum(1 for i, a in enumerate(acima) if a and (i == 0 or not acima[i - 1])),
        "minutos_sem_agua": int(sem_agua),
        "pico_w": max(total),
    }


def veredicto(limite_w, consumo_mensal_kwh, pessoas=3, litros=100, inducao_w=P_INDUCAO_W):
    """'aguenta', 'aguenta com gestão', 'reserva de água insuficiente' ou 'precisa de mais potência'."""
    sem = simular(limite_w, consumo_mensal_kwh, pessoas, litros, gestao=False, inducao_w=inducao_w)
    if sem["minutos_acima"] == 0:
        return "aguenta" if sem["minutos_sem_agua"] == 0 else "reserva de água insuficiente"
    com = simular(limite_w, consumo_mensal_kwh, pessoas, litros, gestao=True, inducao_w=inducao_w)
    if com["minutos_acima"] > 0:
        return "precisa de mais potência"
    return "aguenta com gestão" if com["minutos_sem_agua"] == 0 else "reserva de água insuficiente"


if __name__ == "__main__":
    # autoverificação: casa de 200 kWh/mês, 3 pessoas
    assert veredicto(3450, 200) == "aguenta com gestão"
    assert veredicto(6900, 200) == "aguenta"
    assert veredicto(1500, 200) == "precisa de mais potência"
    sem = simular(3450, 200, gestao=False)
    com = simular(3450, 200, gestao=True)
    assert sem["disparos"] >= 1 and com["disparos"] == 0 and com["minutos_sem_agua"] == 0
    for nome, r in (("sem gestão", sem), ("com DuoWatt", com)):
        print(f"{nome}: pico {r['pico_w']:.0f} W | minutos acima do limite {r['minutos_acima']} "
              f"| disparos {r['disparos']} | minutos sem água quente {r['minutos_sem_agua']}")
    print("Veredicto 3,45 kVA:", veredicto(3450, 200))

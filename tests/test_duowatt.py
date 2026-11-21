from duowatt import simular, veredicto


def test_tres_veredictos_basicos():
    assert veredicto(6900, 200) == "aguenta"
    assert veredicto(3450, 200) == "aguenta com gestão"
    assert veredicto(1500, 200) == "precisa de mais potência"


def test_sem_gestao_dispara_e_com_gestao_nao():
    sem = simular(3450, 200, gestao=False)
    com = simular(3450, 200, gestao=True)
    assert sem["disparos"] >= 1 and sem["pico_w"] > 3450
    assert com["minutos_acima"] == 0 and com["minutos_sem_agua"] == 0


def test_aguenta_exige_agua_quente():
    # família grande com depósito pequeno: a potência chega, a água não
    assert simular(6900, 200, pessoas=8, litros=100, gestao=False)["minutos_sem_agua"] > 0
    assert veredicto(6900, 200, pessoas=8) == "reserva de água insuficiente"


def test_inducao_forte_e_base_alta_mudam_o_veredicto():
    # 432 kWh/mês = base de 600 W; 600 + 3000 W já passa os 3 450 W sem o termoacumulador
    assert veredicto(3450, 200, inducao_w=3000) == "aguenta com gestão"
    assert veredicto(3450, 432, inducao_w=3000) == "precisa de mais potência"

from duowatt import simular, LIMITE_W


def test_sem_duowatt_passa_o_limite_e_com_duowatt_nao():
    sem, com = simular(duowatt=False), simular()
    assert sem["pico_w"] == 4100 > LIMITE_W and sem["disparos"] >= 1
    assert com["minutos_acima"] == 0 and com["disparos"] == 0


def test_demo_sem_minutos_sem_agua_quente():
    assert simular()["minutos_sem_agua"] == 0


def test_pausa_nunca_passa_de_30_min():
    for c in ("maquina", "inducao"):
        assert simular(c)["max_pausa_min"] <= 30


def test_historese_religa_so_abaixo_de_80_por_cento():
    r = simular()
    for t in range(1, len(r["total_w"])):
        if r["cilindro_w"][t] and not r["cilindro_w"][t - 1]:
            assert r["total_w"][t] - r["cilindro_w"][t] < 0.8 * LIMITE_W


def test_modo_seguro_cilindro_normal():
    assert simular(sensor_ok=False) == simular(duowatt=False)


def test_inducao_forca_religar_ao_fim_de_30_min():
    r = simular("inducao")
    assert r["max_pausa_min"] == 30 and r["minutos_sem_agua"] == 0

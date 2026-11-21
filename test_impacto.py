from impacto import impacto_casa, extrapolar


def test_enunciado_400kg_corresponde_a_cerca_de_10_garrafas():
    r = impacto_casa(10.6)
    assert 390 < r["co2_gas_kg"] < 410


def test_sem_gas_tudo_zero():
    r = impacto_casa(0)
    assert r["co2_evitado_kg"] == 0 and r["poupanca_eur"] == 0


def test_eletricidade_limpa_evita_todo_o_co2_do_gas():
    r = impacto_casa(10, fator_elet_g_kwh=0)
    assert r["co2_evitado_kg"] == r["co2_gas_kg"]


def test_extrapolacao_1_por_cento():
    assert round(extrapolar(400)) == 8800   # 22 000 casas x 400 kg

import pytest
from impacto import impacto_casa, extrapolar, custo_subir_potencia, custo_duowatt, anos_equilibrio


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


def test_subir_3_45_para_6_9():
    assert custo_subir_potencia(3.45, 6.9) == pytest.approx(63.6, abs=0.1)
    with pytest.raises(ValueError):
        custo_subir_potencia(3.45, 10.35)


def test_custo_duowatt_instalado():
    assert custo_duowatt() == pytest.approx((201.87, 281.65))
    assert custo_duowatt(quadro_novo=True) == pytest.approx((351.87, 681.65))


def test_ano_de_equilibrio():
    extra = custo_subir_potencia(3.45, 6.9)
    assert anos_equilibrio(200, extra * 1.23) == pytest.approx(2.56, abs=0.01)
    assert anos_equilibrio(*custo_duowatt()[1:], extra) == pytest.approx(4.43, abs=0.01)
    with pytest.raises(ValueError):
        anos_equilibrio(200, 0)


def test_metrica_principal():
    from impacto import metrica_principal
    m = metrica_principal(200, 0.01)
    assert round(m["casas"]) == 9680                       # 2,2 M x 44 % x 1 %
    assert round(m["t_co2"]) == 1936                       # 200 kg x 9 680 casas
    assert abs(m["pct_enunciado"] - 1936 / 870_000 * 100) < 1e-9
    assert abs(m["mercado_meur"] - 0.264) < 1e-9           # 60 M€ x 0,44 % das casas
    assert metrica_principal(200, 0.10)["casas"] == 10 * m["casas"]

"""Testes do Modelador, ciclo 1. XFAIL(strict) = problema real exposto (passa a falhar o dia em que for corrigido)."""
import pathlib
import pytest
from duowatt import simular, veredicto, KWH_AQS_PESSOA, P_TERMO_W, INDUCAO
from impacto import impacto_casa, extrapolar

AQUI = pathlib.Path(__file__).parent
PRECO_SEM_IVA = 0.1711          # Parametros_Verificados.md, ERSE out 2026


def termo_kwh(r, consumo, inducao_w=1800):
    """Energia que o termoacumulador consumiu (deduzida da potência total)."""
    base = consumo / 720 * 1000
    return sum(round((w - base - (inducao_w if t in INDUCAO else 0)) / P_TERMO_W)
               for t, w in enumerate(r["total_w"])) * P_TERMO_W / 60 / 1000


# ---------- (1) preço da eletricidade e poupança ----------
def test_contas_do_preco_com_iva():
    assert PRECO_SEM_IVA * 1.06 == pytest.approx(0.1814, abs=1e-4)   # primeiros 200 kWh/mês
    assert PRECO_SEM_IVA * 1.23 == pytest.approx(0.2105, abs=1e-4)   # acima de 200 kWh/mês


def test_poupanca_33_euros_vale_para_casa_acima_de_200_kwh_mes():
    # 0,21 €/kWh é o marginal de uma casa que já gasta >200 kWh/mês (IVA 23 %)
    assert impacto_casa(10)["poupanca_eur"] == pytest.approx(33.5, abs=0.1)


def test_preco_marginal_misto_por_escaloes():
    """IVA 6 % só até 200 kWh/mês: custo médio do kWh adicional depende do consumo atual."""
    kwh_mes = impacto_casa(10)["kwh_eletrico"] / 12

    def marginal(base):
        extra_caro = min(kwh_mes, max(0, base + kwh_mes - 200) - max(0, base - 200))
        return PRECO_SEM_IVA * (1.06 * (kwh_mes - extra_caro) + 1.23 * extra_caro) / kwh_mes
    assert marginal(280) == pytest.approx(0.2105, abs=2e-3)   # casa média INE: 0,21 está certo
    assert marginal(158) == pytest.approx(0.2013, abs=2e-3)   # casa ERSE: 0,21 é ligeiramente prudente
    assert impacto_casa(10, preco_kwh=marginal(158))["poupanca_eur"] == pytest.approx(47.4, abs=0.5)


def test_recomendacao_018_exagera_a_poupanca():
    # Parametros_Verificados.md recomenda 0,18: serviria só a quem gasta ~0 kWh/mês de base
    assert impacto_casa(10, preco_kwh=0.18)["poupanca_eur"] == pytest.approx(81.6, abs=0.1)


def test_comentario_impacto_nao_mistura_iva():
    assert "0,171 € com IVA" not in (AQUI / "impacto.py").read_text(encoding="utf-8")


def test_poupanca_muito_sensivel_ao_preco_da_garrafa():
    # 36,87 € -> 33 €/ano; 43,55 € (ERSE com margens máximas) -> ~99 €/ano
    assert impacto_casa(10, preco_garrafa=43.55)["poupanca_eur"] == pytest.approx(98.98, abs=0.5)
    assert impacto_casa(10, preco_garrafa=30)["poupanca_eur"] < 0


def test_iec_omitido_custa_cerca_de_2_euros():
    kwh = impacto_casa(10)["kwh_eletrico"]
    assert kwh * 0.001 * 1.23 == pytest.approx(1.97, abs=0.05)


# ---------- CO2 ----------
def test_co2_cenario_adverso_e_extrapolacao():
    r167 = impacto_casa(10, fator_elet_g_kwh=167)
    assert r167["co2_evitado_kg"] == pytest.approx(109, abs=1)
    assert extrapolar(r167["co2_evitado_kg"]) == pytest.approx(2400, rel=0.02)
    assert extrapolar(impacto_casa(10)["co2_evitado_kg"]) == pytest.approx(4516, rel=0.01)


def test_entradas_invalidas_nao_sao_rejeitadas():
    assert impacto_casa(-5)["poupanca_eur"] < 0          # garrafas negativas aceites
    with pytest.raises(ValueError):
        impacto_casa(10, efic_eletrica=0)
    with pytest.raises(ValueError):
        impacto_casa(10, efic_gas=0)


@pytest.mark.xfail(strict=True, reason="DEPENDE DE DECISÃO (ligar pessoas a garrafas muda a UI/valores): 3 pessoas (simulador) precisam de mais energia útil de água quente (2,3 MWh/ano) do que 10 garrafas dão a TODA a casa (1,6 MWh/ano elétricos); pessoas e garrafas são entradas independentes")
def test_pessoas_e_garrafas_sao_coerentes():
    aqs_ano = 3 * KWH_AQS_PESSOA * 365
    assert aqs_ano <= impacto_casa(10)["kwh_eletrico"]


# ---------- (2)(4) base plana e veredicto ----------
def test_limiar_do_veredicto_e_450w_nao_600w():
    # com indução de 3 kW a 3,45 kVA o veredicto muda aos ~324 kWh/mês (base 450 W), não aos 432
    assert veredicto(3450, 324, inducao_w=3000) == "aguenta com gestão"
    assert veredicto(3450, 325, inducao_w=3000) == "precisa de mais potência"


def test_margem_da_casa_media_sem_termo_e_minuscula():
    base = 280 / 720 * 1000                       # casa média INE
    assert 3450 - (base + 3000) == pytest.approx(61, abs=1)
    assert veredicto(3450, 280, inducao_w=3000) == "aguenta com gestão"


@pytest.mark.xfail(strict=True, reason="DEPENDE DE DECISÃO (valor sem fonte: base ao serão ~600 W): base plana (389 W para 280 kWh/mês) subestima o serão (~600 W, pressuposto); com 600 W a casa média + indução 3 kW devia dar 'precisa de mais potência'")
def test_casa_media_com_inducao_forte_ao_serao():
    assert veredicto(3450, 280, inducao_w=3000) == "precisa de mais potência"


def test_inducao_normal_aguenta_com_gestao_mesmo_com_base_alta():
    assert veredicto(3450, 1000, inducao_w=1800) == "aguenta com gestão"   # base 1 389 W + 1 800 W < 3 450 W


# ---------- (3) kVA como kW e disparos ----------
def test_fator_de_potencia_desloca_o_limiar():
    # com FP 0,9 o limite útil de 3,45 kVA seria 3 105 W: 280 kWh + 3 kW deixa de caber
    assert veredicto(3450 * 0.9, 280, inducao_w=3000) == "precisa de mais potência"
    assert veredicto(3450, 280, inducao_w=3000) == "aguenta com gestão"


def test_demo_sem_gestao_sobrecarga_de_18_por_cento_durante_25_min():
    r = simular(3450, 200, gestao=False)
    assert r["disparos"] == 1 and r["minutos_acima"] == 25
    assert r["pico_w"] / 3450 == pytest.approx(1.18, abs=0.01)   # 1,13-1,45 x In: pode disparar em <1 h, não é certo


def test_sobrecarga_toleravel_conta_como_acima():
    # indução 1,5 kW: pico 1,095 x limite (<1,13 x In: o disjuntor aguentaria) mas o modelo conta "disparo"
    r = simular(3450, 200, gestao=False, inducao_w=1500)
    assert r["pico_w"] / 3450 < 1.13 and r["disparos"] == 1
    assert veredicto(3450, 200, inducao_w=1500) == "aguenta com gestão"   # conservador


# ---------- (5) balanço e casos limite ----------
@pytest.mark.parametrize("pessoas,litros", [(3, 100), (5, 200)])
def test_balanco_do_deposito_fecha(pessoas, litros):
    r = simular(6900, 200, pessoas, litros, gestao=False)
    assert r["minutos_sem_agua"] == 0
    assert termo_kwh(r, 200) == pytest.approx(pessoas * KWH_AQS_PESSOA, abs=0.1)


@pytest.mark.xfail(strict=True, reason="DEPENDE DE DECISÃO (muda a lógica do simulador, fora do âmbito): 8 pessoas/200 L acabam o dia 1,5 kWh abaixo do cheio (o aquecimento do serão acaba depois da meia-noite) mas o dia seguinte começaria cheio: o simulador esconde o défice")
def test_dia_fecha_em_regime_estacionario_8_pessoas():
    r = simular(6900, 200, 8, 200, gestao=False)
    assert termo_kwh(r, 200) == pytest.approx(8 * KWH_AQS_PESSOA, abs=0.1)


@pytest.mark.xfail(strict=True, reason="DEPENDE DE DECISÃO (valor de perdas muda o simulador): sem perdas térmicas em repouso (Parametros_Verificados.md: ~1,5 kWh/24 h para 80 L); impacto.py usa 85 % mas o simulador usa 100 %")
def test_perdas_em_repouso_modeladas():
    r = simular(6900, 200, 3, 100, gestao=False)
    assert termo_kwh(r, 200) >= 3 * KWH_AQS_PESSOA + 1.0


def test_zero_pessoas_nao_precisa_de_agua():
    assert simular(3450, 200, pessoas=0)["minutos_sem_agua"] == 0
    assert veredicto(3450, 200, pessoas=0) in ("aguenta", "aguenta com gestão")   # sem água a pedir, o termo nunca liga: "aguenta"
    assert veredicto(3450, 200, pessoas=0) == "aguenta"


def test_deposito_zero_litros_nao_rebenta():
    r = simular(3450, 200, pessoas=3, litros=0)
    assert r["minutos_sem_agua"] == 30                     # os dois duches de 15 min
    assert veredicto(3450, 200, litros=0) == "reserva de água insuficiente"


def test_deposito_minimo_para_3_pessoas_e_70_litros_com_gestao():
    assert veredicto(3450, 200, 3, 70) == "aguenta com gestão"
    assert veredicto(3450, 200, 3, 60) == "reserva de água insuficiente"
    assert veredicto(6900, 200, 3, 60) == "aguenta"          # aqui é a gestão que custa 2 min de água


def test_8_pessoas_precisam_de_deposito_grande():
    assert simular(6900, 200, pessoas=8, litros=100, gestao=False)["minutos_sem_agua"] == 8
    assert veredicto(6900, 200, pessoas=8, litros=200) == "aguenta"


def test_limite_zero_ou_muito_baixo():
    assert veredicto(0, 200) == "precisa de mais potência"
    assert veredicto(1500, 200) == "precisa de mais potência"   # nem termo + base cabem


def test_10_35_kva_aguenta_sempre_mas_assume_monofasico():
    # 10,35 kVA trifásico = 3 x 3,45 kVA por fase; o modelo soma tudo num só limite
    assert veredicto(10350, 432, inducao_w=3000) == "aguenta"
    assert veredicto(3450, 432, inducao_w=3000) == "precisa de mais potência"  # se tudo estiver numa fase


def test_pausa_minima_de_5_min_respeitada():
    r = simular(3450, 200)
    base = 200 / 720 * 1000
    lig = [(w - base - (1800 if t in INDUCAO else 0)) > 1 for t, w in enumerate(r["total_w"])]
    desl = None
    for t, x in enumerate(lig):
        if not x and desl is None:
            desl = t
        if x and desl is not None:
            assert t - desl >= 5 or desl == 0
            desl = None

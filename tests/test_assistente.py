from assistente import PASSOS, calcular, relatorio_html, valores
from duowatt import veredicto
from impacto import impacto_casa


def test_omissoes_e_mesmos_numeros_que_o_modo_detalhado():
    v, assumido = valores({p["id"]: len(p["opcoes"]) - 1 for p in PASSOS if p["opcoes"][-1][1] is None})
    assert len(assumido) == 4  # kva, consumo, placa, garrafas
    r = calcular(v["kva"], v["consumo"], v["pessoas"], v["placa"], v["garrafas"])
    assert r["veredicto"] == veredicto(3450, 200, 3, 100, inducao_w=1800) == "aguenta com gestão"
    assert r["ev"] == impacto_casa(12)
    assert r["extra"] is not None


def test_relatorio_e_casos_limite():
    r = calcular(10.35, 100, 1, 1800, 0)
    assert r["veredicto"] == "aguenta" and r["ev"] is None
    h = relatorio_html(r, [("<b>x</b>", "n")])
    assert "&lt;b&gt;" in h and "Veredicto: Aguenta" in h
    assert calcular(2.3, 500, 6, 3000, 18)["veredicto"] == "precisa de mais potência"

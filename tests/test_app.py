from pathlib import Path

import pytest

pytest.importorskip("streamlit")
from streamlit.testing.v1 import AppTest  # noqa: E402

APP = str(Path(__file__).parent.parent / "app.py")


def test_percorre_os_3_passos():
    at = AppTest.from_file(APP, default_timeout=30).run()
    assert not at.exception
    next(b for b in at.button if b.label == "Ligar a máquina da roupa").click().run()
    assert not at.exception and any("A luz foi abaixo" in e.value for e in at.error)
    for _ in range(2):
        next(b for b in at.button if b.label == "Seguinte").click().run()
        assert not at.exception
    assert any(e.label == "Para saber mais" for e in at.expander)
    for _ in range(2):
        next(b for b in at.button if b.label == "Anterior").click().run()
        assert not at.exception


def test_bloco_negocio_so_com_valores():
    f = Path(APP).parent / "negocio.json"
    orig = f.read_text(encoding="utf-8")

    def ecra3():
        at = AppTest.from_file(APP, default_timeout=30).run()
        for _ in range(2):
            next(b for b in at.button if b.label == "Seguinte").click().run()
        return at

    try:
        assert not any("Custo do kit" in t.value.to_string() for t in ecra3().table)
        f.write_text('{"custo_kit": 1234.5, "preco_a_bosch": null, "opcao_familia": null, "ponto_equilibrio_1_em_M": null}',
                     encoding="utf-8")
        assert any("Custo do kit" in t.value.to_string() for t in ecra3().table)
    finally:
        f.write_text(orig, encoding="utf-8")

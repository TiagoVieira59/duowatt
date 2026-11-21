from pathlib import Path

from streamlit.testing.v1 import AppTest

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

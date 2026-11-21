from formato import pt


def test_pt():
    assert pt(3450) == "3450"
    assert pt(2200000) == "2\u00a0200\u00a0000"
    assert pt(3.45, 2) == "3,45"
    assert pt(12345.6, 1) == "12\u00a0345,6"



def test_agrupar_milhares():
    assert pt(5419, agrupar=True) == "5\u00a0419"

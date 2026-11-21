def pt(x, casas=0, agrupar=False):
    """Número em PT-PT: espaço fino nos milhares (>=10 000, como a norma; agrupar=True desde 1 000), vírgula nos decimais."""
    s = f"{x:,.{casas}f}"
    if abs(x) < 10000 and not agrupar:
        s = s.replace(",", "")
    return s.replace(",", "\u00a0").replace(".", ",")

def pt(x, casas=0):
    """Número em PT-PT: espaço fino nos milhares (>=10 000, como a norma), vírgula nos decimais."""
    s = f"{x:,.{casas}f}"
    if abs(x) < 10000:
        s = s.replace(",", "")
    return s.replace(",", "\u00a0").replace(".", ",")

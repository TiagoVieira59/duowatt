"""DuoWatt: CO2 e custo anuais de uma casa, gás (GPL) contra elétrico.

Valores marcados 'a validar' estão em Parametros_Simulador.md / Parametros_Verificados.md.
"""

KG_GARRAFA = 13                    # butano T3
KWH_POR_KG_GPL = 46 / 3.6          # PCI 46 MJ/kg -> ~12,8 kWh/kg
KG_CO2_POR_KWH_GPL = 0.063 * 3.6   # 63 tCO2/TJ -> ~0,227 kg/kWh
CASAS_GPL = 2_200_000              # enunciado Bosch
# Termo de potência (€/dia, sem IVA): ERSE, Diretiva 4/2026, em vigor desde 1 out 2026,
# comercializador de último recurso (PESQUISA.md, secção 4).
TERMO_POTENCIA_EUR_DIA = {3.45: 0.1917, 6.9: 0.3659}
# PROXY: <3,45 kVA = 44,1 % dos contratos BTN (E-REDES, perfis 2025, dados 2023);
# inclui não domésticos e não é específico das casas a GPL.
QUOTA_ATE_3_45_KVA = 0.44
# Valores por omissão de impacto_casa (Parametros_Verificados.md), expostos para a app os citar.
PRECO_GARRAFA_EUR = 37.0                # confirmado: último preço anunciado (ERSE, out 2026)
PRECO_GARRAFA_ALTO_EUR = (42.0, 43.55)  # confirmado: cenário alto
PRECO_KWH_EUR = 0.21                    # derivado: marginal com IVA 23 % (tarifa regulada ERSE 2026)
FATOR_ELET_G_KWH = 107                  # confirmado: APA 2023, média anual
FATOR_ELET_ADVERSO_G_KWH = 167          # confirmado: APA, média de 5 anos (cenário adverso)
EFIC_GAS = 0.82                         # provável: esquentador
EFIC_ELETRICA = 0.85                    # provável: termoacumulador/indução (Energy Star)
# Custo do DuoWatt (VIABILIDADE.md §2; preços de retalho PT, não cotações oficiais).
CUSTO_MATERIAL_DUOWATT_EUR = (171.87, 221.65)  # derivado: sem / com contactor (Shelly Pro EM 50 + Pro 2PM [+ Hager ESC225]); IVA do contactor por confirmar
MAO_DE_OBRA_EUR = (30, 60)                     # hipótese: 1 a 2 h a ~30 €/h (plataformas, não tarifa oficial)
CUSTO_QUADRO_NOVO_EUR = (150, 400)             # provável: Zaask, expert-zoom
IVA_POTENCIA = 0.23                            # hipótese: IVA do termo de potência por verificar
ANOS_COMPARACAO = 10                           # horizonte da comparação, preços constantes


def impacto_casa(garrafas_ano, preco_garrafa=PRECO_GARRAFA_EUR, preco_kwh=PRECO_KWH_EUR,
                 fator_elet_g_kwh=FATOR_ELET_G_KWH, efic_gas=EFIC_GAS, efic_eletrica=EFIC_ELETRICA):
    """CO2 (kg/ano) e custo (€/ano) de uma casa, antes (GPL) e depois (elétrico).

    A mesma energia útil (água quente + cozinha) é entregue por eletricidade.
    Valores de Parametros_Verificados.md: preco_garrafa 37 € (último preço
    anunciado, out 2026; cenário alto 42-43,5 €), preco_kwh 0,21 €/kWh (preço
    marginal: tarifa regulada 0,171 € SEM IVA; com IVA de 23 % acima dos 200 kWh/mês
    dá ~0,21 €; abaixo desse escalão (IVA 6 %) é ~0,18 €), fator_elet_g_kwh 107 (APA 2023, média anual de
    produção, não marginal; intervalo 40-167), efic_gas 0,82 (esquentador; o
    fogão a gás, ~0,4, tornaria a poupança maior, por isso 0,82 é prudente) e
    efic_eletrica 0,85 (termoacumulador com perdas e indução). Não inclui o custo
    do equipamento nem o termo de potência da fatura.
    """
    if efic_gas <= 0 or efic_eletrica <= 0:
        raise ValueError("efic_gas e efic_eletrica têm de ser > 0")
    kwh_gas = garrafas_ano * KG_GARRAFA * KWH_POR_KG_GPL
    kwh_elet = kwh_gas * efic_gas / efic_eletrica
    co2_gas = kwh_gas * KG_CO2_POR_KWH_GPL
    co2_elet = kwh_elet * fator_elet_g_kwh / 1000
    custo_gas = garrafas_ano * preco_garrafa
    custo_elet = kwh_elet * preco_kwh
    return {
        "kwh_gas": kwh_gas, "kwh_eletrico": kwh_elet,
        "co2_gas_kg": co2_gas, "co2_eletrico_kg": co2_elet,
        "co2_evitado_kg": co2_gas - co2_elet,
        "custo_gas_eur": custo_gas, "custo_eletrico_eur": custo_elet,
        "poupanca_eur": custo_gas - custo_elet,
    }


def extrapolar(co2_evitado_kg_casa, adocao=0.01, casas=CASAS_GPL):
    """Toneladas de CO2/ano evitadas se 'adocao' (0-1) das casas a GPL trocar."""
    return co2_evitado_kg_casa * casas * adocao / 1000


def custo_subir_potencia(de_kva, para_kva):
    """Custo extra (€/ano, sem IVA) do termo de potência ao subir de 'de_kva' para 'para_kva'."""
    try:
        return (TERMO_POTENCIA_EUR_DIA[para_kva] - TERMO_POTENCIA_EUR_DIA[de_kva]) * 365
    except KeyError as e:
        raise ValueError(f"sem termo de potência para {e.args[0]} kVA (há {sorted(TERMO_POTENCIA_EUR_DIA)})") from None


def custo_duowatt(quadro_novo=False):
    """(mínimo, máximo) do custo único do DuoWatt instalado, em €: material sem/com contactor + mão de obra (+ quadro novo)."""
    extra = CUSTO_QUADRO_NOVO_EUR if quadro_novo else (0, 0)
    return tuple(CUSTO_MATERIAL_DUOWATT_EUR[i] + MAO_DE_OBRA_EUR[i] + extra[i] for i in (0, 1))


def anos_equilibrio(custo_unico_eur, extra_anual_eur):
    """Anos até o custo único igualar o extra anual de subir a potência (a partir daí o DuoWatt compensa)."""
    if extra_anual_eur <= 0:
        raise ValueError("extra_anual_eur tem de ser > 0")
    return custo_unico_eur / extra_anual_eur

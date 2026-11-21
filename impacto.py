"""DuoWatt: CO2 e custo anuais de uma casa, gás (GPL) contra elétrico.

Valores marcados 'a validar' estão em Parametros_Simulador.md / Parametros_Verificados.md.
"""

KG_GARRAFA = 13                    # butano T3
KWH_POR_KG_GPL = 46 / 3.6          # PCI 46 MJ/kg -> ~12,8 kWh/kg
KG_CO2_POR_KWH_GPL = 0.063 * 3.6   # 63 tCO2/TJ -> ~0,227 kg/kWh
CASAS_GPL = 2_200_000              # enunciado Bosch


def impacto_casa(garrafas_ano, preco_garrafa=37.0, preco_kwh=0.21,
                 fator_elet_g_kwh=107, efic_gas=0.82, efic_eletrica=0.85):
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

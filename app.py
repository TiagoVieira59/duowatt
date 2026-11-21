import pandas as pd
import streamlit as st

from duowatt import simular, veredicto
from impacto import extrapolar, impacto_casa

st.set_page_config(page_title="DuoWatt", layout="wide")
st.title("DuoWatt: do gás para a eletricidade, sem disparar o quadro")

with st.sidebar:
    st.header("A sua casa")
    kva = st.selectbox("Potência contratada (kVA)", [2.3, 3.45, 6.9, 10.35], index=1)
    consumo = st.number_input("Consumo mensal (kWh)", 50, 1500, 200, step=10)
    pessoas = st.number_input("Número de pessoas", 1, 8, 3)
    litros = st.number_input("Depósito do termoacumulador (L)", 50, 200, 100, step=10)
    inducao = st.radio("Uso da placa de indução", ["Moderado (1,8 kW)", "Intenso (3 kW)"])
    garrafas = st.number_input("Garrafas de gás por ano", 0, 50, 10)
    preco_kwh = st.number_input("Preço marginal da eletricidade (€/kWh)", 0.05, 0.60, 0.21, step=0.005, format="%.3f")
    fator = st.slider("Fator de CO2 da eletricidade (g/kWh)", 40, 167, 107)
    adocao = st.slider("Casas a GPL que trocam, em % (cenário)", 1, 20, 1)

limite = int(kva * 1000)
ind_w = 1800 if inducao.startswith("Moderado") else 3000
sem = simular(limite, consumo, pessoas, litros, gestao=False, inducao_w=ind_w)
com = simular(limite, consumo, pessoas, litros, gestao=True, inducao_w=ind_w)

v = veredicto(limite, consumo, pessoas, litros, inducao_w=ind_w)
cor = {
    "aguenta": st.success,
    "aguenta com gestão": st.warning,
    "reserva de água insuficiente": st.warning,
    "precisa de mais potência": st.error,
}[v]
cor(f"## Veredicto: {v.capitalize()}")

horas = [m / 60 for m in range(1440)]
st.subheader("Potência ao longo do dia (W)")
st.line_chart(
    pd.DataFrame(
        {"Sem gestão": sem["total_w"], "Com DuoWatt": com["total_w"], "Limite": limite},
        index=pd.Index(horas, name="Hora do dia"),
    )
)

st.subheader("Sem gestão vs. com DuoWatt")
for col, (nome, r) in zip(st.columns(2), [("Sem gestão", sem), ("Com DuoWatt", com)]):
    with col:
        st.markdown(f"**{nome}**")
        a, b, c = st.columns(3)
        a.metric("Episódios acima da potência contratada", r["disparos"])
        b.metric("Minutos acima do limite", r["minutos_acima"])
        c.metric("Minutos sem água quente", r["minutos_sem_agua"])
st.caption("Acima do limite = risco de disparo; o disjuntor real tolera pequenas sobrecargas por pouco tempo.")

st.subheader("Impacto se a casa trocar o gás pela eletricidade")
if v == "precisa de mais potência":
    st.info("Esta casa teria primeiro de aumentar a potência contratada: o impacto abaixo só se realiza depois disso.")
else:
    ev = impacto_casa(garrafas, preco_kwh=preco_kwh, fator_elet_g_kwh=fator)
    adverso = impacto_casa(garrafas, preco_kwh=preco_kwh, fator_elet_g_kwh=167)
    a, b, c = st.columns(3)
    a.metric(f"CO2 evitado por casa ({fator} g/kWh)", f"{ev['co2_evitado_kg']:.0f} kg/ano")
    b.metric("Cenário adverso (167 g/kWh)", f"{adverso['co2_evitado_kg']:.0f} kg/ano")
    c.metric("Variação de custo", f"{ev['poupanca_eur']:.0f} €/ano")
    nacional = extrapolar(ev["co2_evitado_kg"], adocao=adocao / 100)
    st.metric(
        f"Cenário ilustrativo: {adocao} % das 2,2 M de casas a GPL trocam",
        f"{nacional:,.0f} t CO2/ano".replace(",", " "),
    )
    st.caption(
        "O CO2 só desce se o gás for mesmo substituído, e a troca pode acontecer sem o DuoWatt: "
        "o que o DuoWatt faz é tirar o bloqueio da potência. O fator é uma média anual, não marginal."
    )

st.info(
    "**Avisos honestos:** simulação ilustrativa, valores por validar. "
    "O cenário (indução 19:30-20:10, duche às 19:45) é um caso de demonstração, "
    "com a base da casa estimada pelo consumo mensal. "
    "Não inclui custo do equipamento nem termo de potência. "
    "Gestão de cargas já existe no mercado (Schneider, ABB); não encontrámos controlo externo documentado nos Tronic."
)

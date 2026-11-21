import altair as alt
import pandas as pd
import streamlit as st

from duowatt import INDUCAO, simular, veredicto
from impacto import extrapolar, impacto_casa

st.set_page_config(page_title="DuoWatt", layout="wide")
# legibilidade em projetor: texto >= 16 px, cinzento só escuro, menos espaço no topo
st.markdown(
    """<style>
.block-container {padding-top: 2.5rem; padding-bottom: 1rem;}
h1 {font-size: 2rem !important; padding: 0 0 .25rem 0;}
[data-testid="stMetricLabel"] p, [data-testid="stCaptionContainer"] p, [data-testid="stSidebar"] label p,
[data-testid="stSidebar"] label, [data-testid="stExpander"] p {font-size: 16px !important; color: #222 !important;}
[data-testid="stCaptionContainer"] p {color: #333 !important;}
[data-testid="stMetricValue"] {font-size: 2rem;}
[data-testid="stAlert"] p {font-size: 16px;}
h4 {margin: 0; padding: 0;}
</style>""",
    unsafe_allow_html=True,
)
st.title("DuoWatt: gás para elétrico, sem disparar")

with st.sidebar:
    st.header("A sua casa")
    kva = st.selectbox("Potência contratada (kVA)", [2.3, 3.45, 6.9, 10.35], index=1)
    consumo = st.number_input("Consumo mensal (kWh)", 50, 1500, 200, step=10)
    inducao = st.radio("Uso da placa de indução", ["Moderado (1,8 kW)", "Intenso (3 kW)"])
    with st.expander("Avançado"):
        pessoas = st.number_input("Número de pessoas", 1, 8, 3)
        litros = st.number_input("Depósito do termoacumulador (L)", 50, 200, 100, step=10)
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
cor(f"#### Veredicto: {v.capitalize()}")

base_w = consumo / 720 * 1000
margem = limite - base_w - ind_w
if sem["minutos_acima"] == 0:
    frase = "A gestão não é necessária: a casa aguenta sem ela."
elif com["minutos_acima"] == 0:
    frase = f"Com gestão deixa de exceder o limite (sem ela passa {sem['minutos_acima']} min acima)."
else:
    frase = f"Mesmo com gestão excede o limite durante {com['minutos_acima']} min."
st.markdown(f"**{frase}** Margem ao serão (limite menos base menos indução): {margem:,.0f} W.".replace(",", " "))

if v == "precisa de mais potência":
    co2 = "n/d"
    co2_ajuda = "Precisa primeiro de aumentar a potência contratada."
else:
    ev = impacto_casa(garrafas, preco_kwh=preco_kwh, fator_elet_g_kwh=fator)
    co2, co2_ajuda = f"{ev['co2_evitado_kg']:.0f} kg/ano", f"Fator {fator} g/kWh"
a, b, c = st.columns(3)
a.metric("Pico sem gestão", f"{sem['pico_w']:,.0f} W".replace(",", " "))
b.metric("Pico com DuoWatt", f"{com['pico_w']:,.0f} W".replace(",", " "))
c.metric("CO2 evitado por casa", co2, help=co2_ajuda)

# gráfico só do serão (17:00-23:00); domínios explícitos evitam avisos "Infinite extent"
ini, fim = 17 * 60, 23 * 60
dados = pd.DataFrame(
    [{"Hora": m / 60, "Série": nome, "W": w}
     for nome, r in (("Sem gestão", sem), ("Com DuoWatt", com))
     for m, w in enumerate(r["total_w"]) if ini <= m <= fim]
)
topo = max(limite, sem["pico_w"], com["pico_w"]) * 1.15
x = alt.X("Hora:Q", scale=alt.Scale(domain=[17, 23]), title=None,
          axis=alt.Axis(values=list(range(17, 24)), labelExpr="datum.value + ':00'"))
y = alt.Y("W:Q", scale=alt.Scale(domain=[0, topo]), title="Potência (W)")
serie = alt.Color("Série:N", scale=alt.Scale(domain=["Sem gestão", "Com DuoWatt"], range=["#b3261e", "#0b57a4"]), legend=alt.Legend(title=None, orient="top"))
traco = alt.StrokeDash("Série:N", scale=alt.Scale(domain=["Sem gestão", "Com DuoWatt"], range=[[8, 5], [1, 0]]), legend=None)
linha = lambda nome, larg: (alt.Chart(dados).transform_filter(alt.datum["Série"] == nome)
                            .mark_line(strokeWidth=larg, interpolate="step-after").encode(x=x, y=y, color=serie, strokeDash=traco))
serao = alt.Chart(pd.DataFrame({"a": [INDUCAO[0] / 60], "b": [(INDUCAO[-1] + 1) / 60]})).mark_rect(color="#f5c542", opacity=0.3).encode(x="a:Q", x2="b:Q")
lim = alt.Chart(pd.DataFrame({"W": [limite]})).mark_rule(color="#111", strokeWidth=4).encode(y="W:Q")
rotulo = alt.Chart(pd.DataFrame({"Hora": [17.05], "W": [limite], "t": [f"Limite {kva:g} kW".replace(".", ",")]})).mark_text(
    align="left", baseline="bottom", dy=-6, fontSize=16, fontWeight="bold", color="#111").encode(x="Hora:Q", y="W:Q", text="t:N")
st.altair_chart(
    (serao + linha("Sem gestão", 3) + linha("Com DuoWatt", 5) + lim + rotulo)
    .properties(height=300)
    .configure_axis(labelFontSize=14, titleFontSize=16, labelColor="#222", titleColor="#222")
    .configure_legend(labelFontSize=16, symbolStrokeWidth=4, symbolSize=300),
    width="stretch",
)

st.subheader("Sem gestão vs. com DuoWatt")
for col, (nome, r) in zip(st.columns(2), [("Sem gestão", sem), ("Com DuoWatt", com)]):
    with col:
        st.markdown(f"**{nome}**")
        a, b = st.columns(2)
        a.metric("Min. acima do limite", r["minutos_acima"])
        b.metric("Min. sem água quente", r["minutos_sem_agua"])
st.caption("Acima do limite = risco de disparo; o disjuntor real tolera pequenas sobrecargas por pouco tempo.")

st.subheader("Impacto se a casa trocar o gás pela eletricidade")
if v == "precisa de mais potência":
    st.error("Esta casa teria primeiro de aumentar a potência contratada: o impacto abaixo só se realiza depois disso.")
else:
    adverso = impacto_casa(garrafas, preco_kwh=preco_kwh, fator_elet_g_kwh=167)
    a, b = st.columns(2)
    a.metric("Cenário adverso (167 g/kWh)", f"{adverso['co2_evitado_kg']:.0f} kg/ano")
    b.metric("Poupança de custo" if ev["poupanca_eur"] >= 0 else "Custo extra", f"{abs(ev['poupanca_eur']):.0f} €/ano")
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
    "**Avisos honestos:** simulação ilustrativa, valores por validar; o cenário é um caso de demonstração. "
    "Não inclui custo do equipamento; gestão de cargas já existe no mercado (Schneider, ABB)."
)
with st.expander("Pressupostos e limites"):
    st.markdown(
        "- Cenário: indução 19:30-20:10 e duche às 19:45, com a base da casa estimada pelo consumo mensal.\n"
        "- Não inclui o termo de potência da fatura.\n"
        "- Não encontrámos controlo externo documentado nos Tronic."
    )

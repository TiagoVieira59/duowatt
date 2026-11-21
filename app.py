import json
import os
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

from duowatt import INDUCAO, P_TERMO_W, simular, veredicto
from impacto import CASAS_GPL, QUOTA_ATE_3_45_KVA, custo_subir_potencia, extrapolar, impacto_casa

DADOS = Path(os.environ.get("DUOWATT_DADOS", Path(__file__).parent / "dados"))  # a variável só serve para testar
KVA = [2.3, 3.45, 6.9, 10.35]
st.set_page_config(page_title="DuoWatt", layout="wide")
# legibilidade em projetor: texto >= 16 px, cinzento só escuro, menos espaço no topo
st.markdown(
    """<style>
.block-container {padding-top: 2.5rem; padding-bottom: 1rem;}
h1 {font-size: 2rem !important; padding: 0 0 .25rem 0;}
[data-testid="stMetricLabel"] p, [data-testid="stCaptionContainer"] p, [data-testid="stSidebar"] label p,
[data-testid="stSidebar"] label, [data-testid="stExpander"] p {font-size: 16px !important; color: #222 !important;}
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p {font-size: 16px !important; color: #222 !important; opacity: 1 !important;}
[data-testid="stMetricValue"] {font-size: 1.6rem;}
[data-testid="stAlert"] p {font-size: 16px;}
[data-testid="stSidebar"] input, [data-testid="stSidebar"] [data-baseweb="select"] div,
[data-testid="stSidebar"] [role="radiogroup"] p {font-size: 16px !important; color: #222 !important;}
h4 {margin: 0; padding: 0;}
</style>""",
    unsafe_allow_html=True,
)
st.title("DuoWatt: gás para elétrico, sem disparar")

with st.sidebar:
    st.header("A sua casa")
    kva = st.selectbox("Potência contratada (kVA)", KVA, index=1)
    consumo = st.number_input("Consumo mensal (kWh)", 50, 1500, 200, step=10)
    inducao = st.radio("Uso da placa de indução", ["Moderado (1,8 kW)", "Intenso (3 kW)"])
    with st.expander("Avançado"):
        pessoas = st.number_input("Número de pessoas", 1, 8, 3)
        litros = st.number_input("Depósito do termoacumulador (L)", 50, 200, 100, step=10)
        garrafas = st.number_input("Garrafas de gás por ano", 0, 20, 10)
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
tab_diag, tab_provas = st.tabs(["Diagnóstico", "Provas do utilizador"])
with tab_diag:
    cor(f"#### Veredicto: {v.capitalize()}")

    base_w = consumo / 720 * 1000
    pedido_w = base_w + ind_w + P_TERMO_W
    ev = None
    if v == "reserva de água insuficiente":
        frase = "A potência chega, mas o depósito não dá para a água quente deste agregado: aumentar o depósito."
    elif sem["minutos_acima"] == 0:
        frase = "A gestão não é necessária: a casa aguenta sem ela."
    elif com["minutos_acima"] == 0:
        frase = f"Com gestão deixa de exceder o limite (sem ela passa {sem['minutos_acima']} min acima)."
    else:
        frase = f"Mesmo com gestão excede o limite durante {com['minutos_acima']} min."
    folga = f"Placa + termoacumulador juntos pedem {pedido_w:,.0f} W; o limite é {limite:,.0f} W.".replace(",", " ")
    if v == "precisa de mais potência":
        cabe = next((f"{k:g}".replace(".", ",") for k in KVA if k * 1000 >= com["pico_w"]), None)
        folga += f" Para caber, precisaria de pelo menos {cabe} kVA: contratar {cabe} kVA." if cabe else " Nem a maior potência da lista chega."
    st.markdown(f"**{frase}** {folga}")

    if v == "precisa de mais potência":
        co2 = "n/d"
        co2_ajuda = "Precisa primeiro de aumentar a potência contratada."
    elif garrafas == 0:
        co2, co2_ajuda = "Sem gás", "Sem gás a substituir: sem impacto de CO2"
    else:
        ev = impacto_casa(garrafas, preco_kwh=preco_kwh, fator_elet_g_kwh=fator)
        co2, co2_ajuda = f"{ev['co2_evitado_kg']:.0f} kg/ano", f"Fator {fator} g/kWh"
    a, b, c, d, e, f = st.columns(6)
    a.metric("Pico sem gestão", f"{sem['pico_w']:,.0f} W".replace(",", " "))
    b.metric("Pico com DuoWatt", f"{com['pico_w']:,.0f} W".replace(",", " "))
    c.metric("CO2 evitado", co2, help=co2_ajuda)
    if ev:
        d.metric("Poupança" if ev["poupanca_eur"] >= 0 else "Custo extra", f"{abs(ev['poupanca_eur']):.0f} €/ano")
    else:
        d.metric("Poupança", "n/d")
    e.metric("Min. acima", f"{sem['minutos_acima']} → {com['minutos_acima']}", help="Minutos acima do limite, sem → com DuoWatt")
    f.metric("Min. sem água", f"{sem['minutos_sem_agua']} → {com['minutos_sem_agua']}", help="Minutos sem água quente, sem → com DuoWatt")

    # gráfico só do serão (17:00-23:00); domínios explícitos evitam avisos "Infinite extent"
    ini, fim = 17 * 60, 23 * 60
    dados = pd.DataFrame(
        [{"Hora": m / 60, "Série": nome, "W": w}
         for nome, r in (("Sem gestão", sem), ("Com DuoWatt", com))
         for m, w in enumerate(r["total_w"]) if ini <= m <= fim]
    )
    topo = max(limite, sem["pico_w"], com["pico_w"]) * 1.15
    xs = alt.Scale(domain=[17, 23], zero=False, nice=False)  # mesma escala em todas as camadas (senão volta a incluir 0)
    x = alt.X("Hora:Q", scale=xs, title=None,
              axis=alt.Axis(values=list(range(17, 24)), labelExpr="datum.value + ':00'"))
    y = alt.Y("W:Q", scale=alt.Scale(domain=[0, topo]), title="Potência (W)")
    serie = alt.Color("Série:N", scale=alt.Scale(domain=["Sem gestão", "Com DuoWatt"], range=["#b3261e", "#0b57a4"]), legend=alt.Legend(title=None, orient="top"))
    traco = alt.StrokeDash("Série:N", scale=alt.Scale(domain=["Sem gestão", "Com DuoWatt"], range=[[8, 5], [1, 0]]), legend=alt.Legend(title=None, orient="top"))
    linha = lambda nome, larg: (alt.Chart(dados).transform_filter(alt.datum["Série"] == nome)
                                .mark_line(strokeWidth=larg, interpolate="step-after").encode(x=x, y=y, color=serie, strokeDash=traco))
    serao = alt.Chart(pd.DataFrame({"a": [INDUCAO[0] / 60], "b": [(INDUCAO[-1] + 1) / 60]})).mark_rect(color="#f5c542", opacity=0.3).encode(x=alt.X("a:Q", scale=xs), x2="b:Q")
    lim = alt.Chart(pd.DataFrame({"W": [limite]})).mark_rule(color="#111", strokeWidth=4).encode(y="W:Q")
    rotulo = alt.Chart(pd.DataFrame({"Hora": [22.95], "W": [limite], "t": [f"Limite {kva:g} kW".replace(".", ",")]})).mark_text(
        align="right", baseline="bottom", dy=-6, fontSize=16, fontWeight="bold", color="#111").encode(x=alt.X("Hora:Q", scale=xs), y="W:Q", text="t:N")
    st.altair_chart(
        (serao + linha("Sem gestão", 8) + linha("Com DuoWatt", 4) + lim + rotulo)
        .properties(height=240)
        .configure_axis(labelFontSize=14, titleFontSize=16, labelColor="#222", titleColor="#222")
        .configure_legend(labelFontSize=16, labelColor="#222", symbolStrokeWidth=4, symbolSize=300),
        width="stretch",
    )

    st.caption("Acima do limite = risco de disparo; o disjuntor real tolera pequenas sobrecargas por pouco tempo.")

    st.subheader("Impacto se a casa trocar o gás pela eletricidade")
    st.caption("O CO2 evitado vem da eletrificação (trocar o gás pela eletricidade), não só do DuoWatt; o DuoWatt desbloqueia a troca.")
    if v == "aguenta com gestão":
        st.info("Sem gestão esta casa teria de aumentar a potência; com o DuoWatt a troca é possível.")
        if kva == 3.45:
            extra = custo_subir_potencia(3.45, 6.9)
            comp = f", mais do que a poupança do gás ({ev['poupanca_eur']:.0f} €/ano)" if ev and extra > ev["poupanca_eur"] else (f", menos do que a poupança do gás ({ev['poupanca_eur']:.0f} €/ano)" if ev else "")
            st.caption(f"Sem gestão, a casa teria de subir para 6,9 kVA: +{extra:.0f} €/ano só no termo de potência (sem IVA, ERSE 2026){comp}.")
    elif v == "aguenta":
        st.info("Esta casa já aguenta sem gestão: aqui o DuoWatt não é necessário.")
    elif v == "reserva de água insuficiente":
        st.warning("Com este depósito falta água quente: aumentar o depósito.")
    if v == "precisa de mais potência":
        st.error("Esta casa teria primeiro de aumentar a potência contratada: o impacto abaixo só se realiza depois disso.")
    elif garrafas == 0:
        st.info("Sem gás a substituir: sem impacto de CO2.")
    else:
        adverso = impacto_casa(garrafas, preco_kwh=preco_kwh, fator_elet_g_kwh=167)
        st.markdown(f"**CO2:** gás {ev['co2_gas_kg']:.0f} kg/ano → elétrico {ev['co2_eletrico_kg']:.0f} kg/ano → evitado {ev['co2_evitado_kg']:.0f} kg/ano. "
                    f"No pior cenário (167 g/kWh): {adverso['co2_evitado_kg']:.0f} kg/ano evitados.")
        nacional = extrapolar(ev["co2_evitado_kg"], adocao=adocao / 100)
        st.caption(
            f"Potencial da eletrificação (não atribuído ao DuoWatt), cenário ilustrativo: {adocao} % das 2,2 M de casas a GPL trocam: "
            f"{nacional:,.0f} t CO2/ano.".replace(",", " ")
        )
        teto = extrapolar(ev["co2_evitado_kg"], adocao=adocao / 100, casas=int(CASAS_GPL * QUOTA_ATE_3_45_KVA))
        st.caption(
            f"Limite superior do que depende de desbloquear a potência: casas com ≤3,45 kVA (~44 % dos contratos BTN, proxy): "
            f"{teto:,.0f} t CO2/ano com {adocao} % de adoção.".replace(",", " ")
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
            "- No INE (2020), 67 % das casas têm esquentador a gás e só 17 % têm termoacumulador: a maioria teria de comprar um aparelho novo (custo não incluído).\n"
            "- Não encontrámos controlo externo documentado nos Tronic."
        )


def pc(x):
    return "n/d" if x is None else f"{x:.0f} %".replace(".", ",")


with tab_provas:
    st.subheader("Dados da Bosch (enunciado do desafio): dados secundários, não são provas recolhidas por nós")
    cols = st.columns(5)
    for col, (rot, val) in zip(cols, [
        ("dos consumidores nunca ponderou trocar o aquecimento de água para elétrico", "68 %"),
        ("nunca ponderou trocar a cozinha", "57 %"),
        ("da procura de equipamento é por avaria urgente", "60 %"),
        ("das substituições urgentes de gás compram outro aparelho a gás", "85 %"),
        ("das casas têm restrições de espaço", "60 %"),
    ]):
        with col.container(border=True):
            st.markdown(f"### {val}")
            st.markdown(rot)
    st.caption("Fonte: Bosch, enunciado Hackathon@ShiftE 2026.")

    st.subheader("Provas da nossa equipa")
    resumo = DADOS / "inquerito_resumo.json"
    try:
        r = json.loads(resumo.read_text(encoding="utf-8")) if resumo.is_file() else None
    except (OSError, ValueError):
        r = None
    if r is None:
        st.info("Ainda sem dados: inquérito e entrevistas em recolha (ver INQUERITO.md e ENTREVISTAS.md)")
    else:
        ind = r.get("indicadores", {})
        st.markdown(f"**Inquérito: n = {r['n_respostas']} respostas.**" + (" Amostra pequena: percentagens indicativas." if r["n_respostas"] < 30 else ""))
        m = st.columns(3)
        m[0].metric("Nunca pensou em trocar (P5)", pc(ind.get("nunca_pensou_pct")))
        m[1].metric("Já lhes disparou o quadro (P8)", pc(ind.get("ja_disparou_quadro_pct")))
        m[2].metric("Comprariam gás se avariasse (P7)", pc(ind.get("compraria_gas_na_avaria_pct")))
        graficos = sorted((DADOS / "graficos").glob("P*.png"), key=lambda p: int(p.stem[1:]))
        for par in range(0, len(graficos), 2):
            for col, img in zip(st.columns(2), graficos[par:par + 2]):
                col.image(str(img))

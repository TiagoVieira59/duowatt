"""DuoWatt: demo de 3 ecrãs (Hackathon@ShiftE). Conceito em docs/referencia/PROMPT_Kit_DuoWatt_Final.md."""
import base64
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

import impacto
from duowatt import LIMITE_W, simular
from formato import pt

st.set_page_config(page_title="DuoWatt", layout="centered")
PASSOS = ["1. O problema", "2. Com DuoWatt", "3. O que muda"]
VERDE, VERMELHO, TEAL = "#1b7f3b", "#b3261e", "#0b5c6b"
IMG = Path(__file__).parent / "assets" / "produto_3d.png"

SEM, COM = simular("maquina", False), simular("maquina", True)
CASA = impacto.impacto_casa(12)
CO2_CASA = CASA["co2_evitado_kg"]
CO2_PAIS_T = impacto.extrapolar(CO2_CASA, 0.01)
EUR = impacto.custo_subir_potencia(3.45, 6.9)
EUR_TXT = f"~{pt(EUR)}–{pt(EUR * (1 + impacto.IVA_POTENCIA))} €/ano"  # sem IVA – com IVA

st.session_state.setdefault("passo", 0)
st.session_state.setdefault("ligada", False)


def ir(d):
    st.session_state.passo = min(2, max(0, st.session_state.passo + d))


def grande(valor, texto):
    st.html(f'<div style="border-left:6px solid {TEAL};padding:4px 16px;margin:8px 0">'
            f'<div style="font-size:40px;font-weight:700;color:{TEAL};line-height:1.2">{valor}</div>'
            f'<div style="font-size:18px;color:#1f2933">{texto}</div></div>')


def cena(luz, pausa, maquina):
    """Casa, cilindro, máquina da roupa e lâmpada em SVG inline."""
    fundo = "#fff6d6" if luz else "#2b2f36"
    lamp = "#f5b800" if luz else "#6b7280"
    cil = "#9bb8bd" if pausa else "#d9822b"
    nota = "em pausa" if pausa else "a aquecer"
    maq = "#0b5c6b" if maquina else "#9aa5ab"
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 218" width="360" height="218">
      <polygon points="10,80 180,10 350,80" fill="{TEAL}"/>
      <rect x="30" y="80" width="300" height="110" fill="{fundo}" stroke="{TEAL}" stroke-width="3"/>
      <line x1="180" y1="80" x2="180" y2="105" stroke="#555" stroke-width="3"/>
      <circle cx="180" cy="115" r="14" fill="{lamp}"/>
      <rect x="55" y="105" width="60" height="75" rx="14" fill="{cil}"/>
      <text x="85" y="212" font-size="20" text-anchor="middle" fill="#1f2933">{nota}</text>
      <rect x="245" y="115" width="65" height="65" rx="6" fill="{maq}"/>
      <circle cx="277" cy="150" r="20" fill="#fff" opacity=".85"/></svg>'''
    # o st.html remove <svg> inline; vai como imagem data-URI
    st.html('<img style="width:100%%" alt="Casa com cilindro %s, máquina da roupa e lâmpada %s" src="data:image/svg+xml;base64,%s">'
            % (nota, 'acesa' if luz else 'apagada', base64.b64encode(svg.encode()).decode()))


def medidor(pct, limite=100):
    """Barra de consumo com a linha do limite: verde dentro, vermelho se passou."""
    cor = VERDE if pct <= limite else VERMELHO
    esc = 130  # a barra vai até 130 % do limite
    st.html(f'''<div style="font-size:18px;margin-top:8px">Consumo da casa: <b>{pct:.0f} % do limite</b></div>
      <div role="img" aria-label="Consumo a {pct:.0f} % do limite" style="position:relative;height:36px;background:#e5e9eb;border-radius:8px;overflow:hidden">
      <div style="width:{min(pct, esc) / esc * 100:.1f}%;height:100%;background:{cor};animation:cresce 1.2s ease-out"></div>
      <div style="position:absolute;left:{limite / esc * 100:.1f}%;top:0;bottom:0;border-left:4px solid #1f2933"></div></div>
      <div style="font-size:18px;margin-left:{limite / esc * 100 - 12:.1f}%">limite</div>
      <style>@keyframes cresce{{from{{width:0}}}}</style>''')


def grafico():
    h = [m / 60 for m in range(18 * 60, 21 * 60)]
    df = pd.DataFrame({"hora": h * 2, "% do limite": [w / LIMITE_W * 100 for w in SEM["total_w"] + COM["total_w"]],
                       "Cenário": ["Sem DuoWatt"] * len(h) + ["Com DuoWatt"] * len(h)})
    eixo = alt.Axis(values=[18, 19, 20, 21], labelExpr="datum.value + ':00'", title="Hora do serão",
                    labelFontSize=16, titleFontSize=16)
    linhas = alt.Chart(df).mark_line(strokeWidth=3).encode(
        x=alt.X("hora:Q", axis=eixo, scale=alt.Scale(domain=[18, 21])),
        y=alt.Y("% do limite:Q", scale=alt.Scale(domain=[0, 130]),
                axis=alt.Axis(values=[0, 50, 100], title="Consumo (% do limite)", labelFontSize=16, titleFontSize=16)),
        color=alt.Color("Cenário:N", scale=alt.Scale(domain=["Sem DuoWatt", "Com DuoWatt"], range=[VERMELHO, VERDE]),
                        legend=alt.Legend(orient="bottom", labelFontSize=16, title=None)))
    lim = alt.Chart(pd.DataFrame({"y": [100]})).mark_rule(color="#1f2933", strokeDash=[6, 4], strokeWidth=2).encode(y="y:Q")
    st.altair_chart(linhas + lim, alt=("Consumo da casa ao serão, com e sem DuoWatt, e linha do limite. "
                                       "Sem DuoWatt passa o limite por volta das 18:40; com DuoWatt fica abaixo."))
    st.caption("Linha tracejada: o limite da casa.")


def ecra1():
    st.header("O problema")
    st.write("Ao fim da tarde, o cilindro está a aquecer e a máquina da roupa liga.")
    ligada = st.session_state.ligada
    cena(not ligada, False, ligada)
    medidor(SEM["pico_w"] / LIMITE_W * 100 if ligada else COM["total_w"][0] / LIMITE_W * 100)
    if ligada:
        st.error("A luz foi abaixo.")
        st.write("É por isto que muitas famílias continuam no gás.")
        st.button("Repor", on_click=lambda: st.session_state.update(ligada=False))
    else:
        st.button("Ligar a máquina da roupa", type="primary", on_click=lambda: st.session_state.update(ligada=True))


def ecra2():
    st.header("Com DuoWatt")
    st.write("O mesmo serão, agora com o DuoWatt a vigiar a casa.")
    cena(True, True, True)
    medidor(COM["pico_w"] / LIMITE_W * 100)
    st.success("O cilindro está em pausa. A luz mantém-se.")
    st.write("O cilindro tem água quente guardada: ninguém nota a pausa.")
    grande(EUR_TXT, "evita: não precisa de aumentar a potência (estimativa)")
    grafico()


def ecra3():
    st.header("O que muda")
    c1, c2 = st.columns(2)
    with c1:
        grande(f"~{pt(CO2_CASA)} kg", "de CO₂ evitados por casa, por ano (12 garrafas de gás)")
    with c2:
        grande(f"~{pt(CO2_PAIS_T)} t", "de CO₂ por ano se 1 % das casas a gás trocarem")
    st.subheader("Como funciona")
    st.html(f'''<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:18px;color:#1f2933">
      <div style="flex:1 1 110px;border:2px solid {TEAL};border-radius:8px;padding:8px;text-align:center">Sensor no quadro</div>
      <div style="flex:1 1 110px;text-align:center">&rarr; ligação local, sem internet &rarr;</div>
      <div style="flex:1 1 110px;border:2px solid {TEAL};border-radius:8px;padding:8px;text-align:center">Módulo no cilindro</div></div>''')
    if IMG.exists():
        st.image(str(IMG), caption="Imagem concetual", alt="Imagem concetual do kit DuoWatt")
    else:
        st.caption("Imagem concetual a adicionar")
    st.subheader("Para a Bosch")
    st.write("O DuoWatt completa o cilindro Tronic, que não sabe o que se passa no resto da casa. "
             "Transforma trocas de gás por gás em vendas de cilindro. Garantia sem apagões.")
    st.write("[números de negócio a preencher pela Contabilidade]")
    st.table(pd.DataFrame({
        "": ["Quem paga", "Quando se vende", "Precisa de hub ou app?", "Para quem"],
        "Concorrentes": ["A família", "Em qualquer altura, em loja ou online", "Em geral sim", "Entusiastas ou mercados fora de Portugal"],
        "DuoWatt": ["A Bosch", "Na avaria do esquentador, pelo mesmo instalador", "Não: duas peças emparelhadas, sem internet", "Casas em Portugal com o limite de 3,45 kVA e gás em garrafa"],
    }).set_index(""))
    with st.expander("Para saber mais"):
        st.markdown(f"""
- **Regras de controlo (pelo conceito):** o cilindro desliga quando a casa chega a 90 % do limite, volta a ligar abaixo de 80 %, e a pausa nunca passa de 30 min seguidos. Se o sensor deixar de comunicar, o cilindro funciona como sem DuoWatt (modo seguro).
- **Limite assumido:** o cilindro nunca é a causa do apagão. Se a casa passar o limite mesmo sem o cilindro, o DuoWatt não resolve.
- **Pressupostos:** máquina da roupa ~2 kW durante ~20 min (hipótese); resto da casa ~0,6 kW (hipótese); cilindro Tronic 5501i de 1,5 kW (confirmado, ficha Bosch); 12 garrafas de gás por ano (hipótese); fator da rede 107 g/kWh (confirmado, APA 2023); potência 3,45 para 6,9 kVA: {pt(EUR)} €/ano sem IVA (derivado, tarifa regulada ERSE 2026), IVA de 23 % por verificar (hipótese).
- **Cenário adverso da rede:** com 167 g/kWh (confirmado, APA, média de 5 anos), o CO₂ evitado por casa desce para ~{pt(impacto.impacto_casa(12, fator_elet_g_kwh=impacto.FATOR_ELET_ADVERSO_G_KWH)["co2_evitado_kg"])} kg por ano.
- **Comparação com a gama Tronic:** pelo que vimos, a programação usa horas fixas; o DuoWatt reage ao que acontece na casa.""")


st.html(f'<div style="font-size:18px;color:{TEAL};font-weight:700">Passo {st.session_state.passo + 1} de 3: '
        f'{PASSOS[st.session_state.passo]}</div>')
st.progress((st.session_state.passo + 1) / 3)
(ecra1, ecra2, ecra3)[st.session_state.passo]()
a, b = st.columns(2)
a.button("Anterior", on_click=ir, args=(-1,), disabled=st.session_state.passo == 0, width="stretch")
b.button("Seguinte", on_click=ir, args=(1,), disabled=st.session_state.passo == 2, width="stretch", type="primary")
st.caption("Simulação ilustrativa. Valores por validar num piloto.")

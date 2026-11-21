"""Assistente passo a passo para a família: mesmas funções de duowatt.py e impacto.py que o modo detalhado."""
import datetime
import html

from duowatt import P_TERMO_W, simular, veredicto
from formato import pt
from impacto import (FATOR_ELET_ADVERSO_G_KWH, FATOR_ELET_G_KWH, IVA_POTENCIA, PRECO_GARRAFA_EUR, PRECO_KWH_EUR,
                     anos_equilibrio, custo_duowatt, custo_subir_potencia, impacto_casa)

LITROS = 100  # depósito por omissão (igual ao modo detalhado)
N_PASSOS = 5

# (rótulo, valor); valor None = "Não sei" (usa-se `omissao`). `pre` = índice pré-selecionado.
PASSOS = [
    dict(id="kva", titulo="Que potência tem contratada?", pre=1, omissao=3.45,
         ajuda="Na sua fatura de eletricidade, procure «Potência contratada». "
               "Os kVA medem quanto a casa pode usar ao mesmo tempo antes de o quadro disparar.",
         nao_sei="Assumimos 3,45 kVA, um valor frequente em casas pequenas (hipótese de trabalho).",
         opcoes=[("2,3 kVA", 2.3), ("3,45 kVA", 3.45), ("6,9 kVA", 6.9), ("10,35 kVA", 10.35), ("Não sei", None)]),
    dict(id="consumo", titulo="Quanta eletricidade gasta por mês?", pre=1, omissao=200,
         ajuda="Na fatura de eletricidade, procure «Consumo» em kWh no mês.",
         nao_sei="Assumimos 200 kWh por mês (valor típico de trabalho, hipótese).",
         opcoes=[("Até 150 kWh", 100), ("De 150 a 250 kWh", 200), ("De 250 a 400 kWh", 325), ("Mais de 400 kWh", 500), ("Não sei", None)]),
    dict(id="pessoas", titulo="Quantas pessoas vivem na casa?", pre=2, omissao=3,
         ajuda="Conte as pessoas que tomam duche em casa todos os dias.",
         nao_sei="Assumimos 3 pessoas.",
         opcoes=[("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6 ou mais", 6)]),
    dict(id="placa", titulo="Se passar a elétrico, como vai cozinhar?", pre=0, omissao=1800,
         ajuda="Placa de indução: com duas zonas ligadas é uso normal; com três ou mais zonas e o forno ao mesmo tempo é uso intenso.",
         nao_sei="Assumimos uso normal da placa (1,8 kW; hipótese da equipa, por confirmar).",
         opcoes=[("Uso normal (cerca de 1,8 kW)", 1800), ("Uso intenso (cerca de 3 kW)", 3000), ("Não sei", None)]),
    dict(id="garrafas", titulo="Quantas garrafas de gás gasta por ano?", pre=3, omissao=12,
         ajuda="Uma garrafa por mês são 12 por ano. Se não usa gás de garrafa, escolha «Nenhuma».",
         nao_sei="Assumimos 12 garrafas por ano (uma por mês).",
         opcoes=[("Nenhuma", 0), ("Poucas (4 por ano)", 4), ("Algumas (8 por ano)", 8), ("Uma por mês (12 por ano)", 12), ("Muitas (18 por ano)", 18), ("Não sei", None)]),
]

FRASES = {
    "aguenta": "A sua casa consegue passar para elétrico sem aumentar a potência.",
    "aguenta com gestão": "A sua casa consegue passar para elétrico sem aumentar a potência, se o termoacumulador for gerido.",
    "reserva de água insuficiente": "A potência chega, mas o depósito de água quente fica curto para a sua casa: peça ao instalador um depósito maior.",
    "precisa de mais potência": "Para passar para elétrico, esta casa precisa primeiro de aumentar a potência contratada.",
}
COR = {"aguenta": "#1b6e3c", "aguenta com gestão": "#8a5a00", "reserva de água insuficiente": "#8a5a00", "precisa de mais potência": "#a3201a"}
PROXIMOS = {
    "aguenta": ["Leve o relatório ao instalador e peça-lhe um termoacumulador e uma placa de indução.",
                "Confirme com ele que o quadro elétrico está em bom estado."],
    "aguenta com gestão": ["Leve o relatório ao instalador: peça um termoacumulador e um gestor de potência que o pause quando a casa está no limite.",
                           "O DuoWatt é um conceito em teste: pergunte ao instalador se consegue instalar um sistema deste tipo, com um eletricista habilitado."],
    "reserva de água insuficiente": ["Leve o relatório ao instalador e peça um depósito maior (ver o litros e o número de pessoas)."],
    "precisa de mais potência": ["Leve o relatório ao instalador e à comercializadora: o contrato teria de subir de potência antes de trocar o gás."],
}


def valores(resp):
    """Respostas (índice por passo) -> valores usados nos cálculos e lista do que foi assumido ('Não sei')."""
    v, assumido = {}, []
    for p in PASSOS:
        rot, val = p["opcoes"][resp.get(p["id"], p["pre"])]
        if val is None:
            val = p["omissao"]
            assumido.append((p["titulo"], p["nao_sei"]))
        v[p["id"]] = val
    return v, assumido


def calcular(kva, consumo, pessoas, placa_w, garrafas, litros=LITROS):
    """Tudo o que o resultado e o relatório mostram. Só chama funções de duowatt.py e impacto.py."""
    limite = int(kva * 1000)
    sem = simular(limite, consumo, pessoas, litros, gestao=False, inducao_w=placa_w)
    com = simular(limite, consumo, pessoas, litros, gestao=True, inducao_w=placa_w)
    r = dict(kva=kva, consumo=consumo, pessoas=pessoas, placa_w=placa_w, garrafas=garrafas, litros=litros,
             limite=limite, sem=sem, com=com,
             veredicto=veredicto(limite, consumo, pessoas, litros, inducao_w=placa_w),
             ev=None, ev_adverso=None, extra=None, extra_iva=None, duowatt=custo_duowatt())
    if r["veredicto"] != "precisa de mais potência" and garrafas > 0:
        r["ev"] = impacto_casa(garrafas)
        r["ev_adverso"] = impacto_casa(garrafas, fator_elet_g_kwh=FATOR_ELET_ADVERSO_G_KWH)
    if kva == 3.45:
        r["extra"] = custo_subir_potencia(3.45, 6.9)
        r["extra_iva"] = r["extra"] * (1 + IVA_POTENCIA)
    return r


def _custo_texto(r):
    """(número grande, legenda) do custo de potência."""
    v = r["veredicto"]
    if v == "aguenta":
        return "0 €", "A potência atual chega: não paga mais pela potência contratada."
    if r["extra"] is None:
        return "n/d", "Não temos tarifa para esta potência contratada."
    num = f"{pt(r['extra'])}–{pt(r['extra_iva'])} €/ano"
    if r["sem"]["minutos_acima"] > 0 and r["com"]["minutos_acima"] == 0:
        lo, hi = r["duowatt"]
        eq = f"{pt(anos_equilibrio(lo, r['extra_iva']), 1)}–{pt(anos_equilibrio(hi, r['extra']), 1)}"
        return num, (f"É o que custaria a mais subir de 3,45 para 6,9 kVA. Com a gestão do DuoWatt evita-se esse custo; "
                     f"o equipamento custa uma vez {pt(lo)}–{pt(hi)} € e compensa ao fim de {eq} anos (estimativa, sem validação).")
    return num, "É o que custaria a mais subir de 3,45 para 6,9 kVA (sem IVA e com IVA de 23 %)."


def numeros(r):
    """Os 3 números grandes: [(valor, legenda, ajuda)]."""
    ev = r["ev"]
    if ev:
        co2 = (f"{pt(ev['co2_evitado_kg'])} kg/ano",
               f"CO₂ evitado por trocar gás por elétrico. No pior cenário da rede elétrica: {pt(r['ev_adverso']['co2_evitado_kg'])} kg/ano.")
    elif r["garrafas"] == 0:
        co2 = ("Sem gás", "Sem gás de garrafa a substituir, não há CO₂ a evitar.")
    else:
        co2 = ("n/d", "Só há CO₂ evitado depois de aumentar a potência.")
    custo, custo_leg = _custo_texto(r)
    sem, com = r["sem"], r["com"]
    agua = (f"{com['minutos_sem_agua']} min", f"Minutos sem água quente ao serão (sem gestão: {sem['minutos_sem_agua']} min).")
    return [(co2[0], "CO₂ evitado por ano", co2[1]), (custo, "Custo a mais na potência", custo_leg), (agua[0], "Sem água quente", agua[1])]


def pressupostos(r):
    """[(item, valor, fonte e classificação)] para o relatório e para o resultado."""
    return [
        ("Termoacumulador", f"{pt(P_TERMO_W)} W, depósito de {r['litros']} L", "Ficha Bosch (Tronic 4001 T), confirmado"),
        ("Serão simulado", "placa 19:30–20:10 e duche às 19:45", "Pressuposto da equipa, hipótese"),
        ("Consumo da casa", "consumo mensal ÷ 720 h, plano", "Pressuposto, hipótese"),
        ("CO₂ da eletricidade", f"{FATOR_ELET_G_KWH} g/kWh (pior cenário {FATOR_ELET_ADVERSO_G_KWH})", "APA 2023, confirmado"),
        ("Garrafa de gás", f"{pt(PRECO_GARRAFA_EUR)} €, 13 kg", "ERSE, out 2026, confirmado"),
        ("Eletricidade", f"{pt(PRECO_KWH_EUR, 2)} €/kWh", "ERSE 2026 com IVA de 23 %, derivado"),
        ("Termo de potência", "3,45 → 6,9 kVA", "ERSE, Diretiva 4/2026, derivado; IVA por verificar"),
        ("Custo do DuoWatt", f"{pt(r['duowatt'][0])}–{pt(r['duowatt'][1])} € instalado", "Preços de retalho em PT, derivado; mão de obra é hipótese"),
    ]


def relatorio_html(r, assumido):
    """Página única, para guardar ou imprimir e levar ao instalador."""
    e = html.escape
    linhas = lambda itens: "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in itens)
    entradas = [("Potência contratada", f"{pt(r['kva'], 2).rstrip('0').rstrip(',')} kVA", ""), ("Consumo mensal", f"{pt(r['consumo'])} kWh", ""),
                ("Pessoas", str(r["pessoas"]), ""), ("Placa de indução", f"{pt(r['placa_w'])} W", ""), ("Garrafas de gás por ano", str(r["garrafas"]), "")]
    ass = "".join(f"<li>{e(t)} {e(n)}</li>" for t, n in assumido) or "<li>Nenhuma resposta «Não sei».</li>"
    sem, com = r["sem"], r["com"]
    nums = "".join(f"<tr><td>{e(rot)}</td><td><b>{e(val)}</b></td><td>{e(leg)}</td></tr>" for val, rot, leg in numeros(r))
    return f"""<!doctype html><html lang="pt-PT"><head><meta charset="utf-8"><title>Relatório DuoWatt</title>
<style>body{{font:14px/1.45 sans-serif;color:#222;max-width:760px;margin:20px auto;padding:0 12px}}
h1{{font-size:20px;margin:0}}h2{{font-size:15px;margin:14px 0 4px}}table{{border-collapse:collapse;width:100%}}
td{{border:1px solid #bbb;padding:3px 6px;vertical-align:top}}.v{{border:2px solid {COR[r['veredicto']]};padding:8px;font-size:16px;margin:8px 0}}
@media print{{body{{font-size:11px;margin:0}}}}</style></head><body>
<h1>Relatório DuoWatt para o instalador</h1><div>Gerado em {datetime.date.today().strftime('%d/%m/%Y')}. Simulação ilustrativa, não substitui a avaliação de um eletricista habilitado.</div>
<div class="v"><b>Veredicto: {e(r['veredicto'].capitalize())}.</b> {e(FRASES[r['veredicto']])}</div>
<h2>Respostas da família</h2><table>{linhas(entradas)}</table><ul>{ass}</ul>
<h2>O que a simulação mostra (serão típico)</h2><table>
<tr><td>Pico de potência</td><td>sem gestão {pt(sem['pico_w'])} W; com gestão {pt(com['pico_w'])} W; limite {pt(r['limite'])} W</td><td></td></tr>
<tr><td>Minutos acima do limite</td><td>{sem['minutos_acima']} → {com['minutos_acima']}</td><td>sem → com gestão</td></tr></table>
<h2>Números principais</h2><table>{nums}</table>
<h2>Pressupostos e fontes</h2><table>{linhas(pressupostos(r))}</table>
<h2>O que pedir ao instalador</h2><ul>{''.join(f'<li>{e(t)}</li>' for t in PROXIMOS[r['veredicto']])}</ul>
<div>O CO₂ evitado vem de trocar gás por elétrico, não do DuoWatt: o DuoWatt só retira o bloqueio da potência. Segurança elétrica, proteções e anti-legionela por validar com um eletricista habilitado.</div>
</body></html>"""


CSS = """<style>
.block-container{max-width:720px;padding-top:1.5rem}
.stButton button,.stDownloadButton button{min-height:48px;font-size:18px;font-weight:600}
[data-testid="stRadio"] label p{font-size:18px}
[data-testid="stRadio"] label{padding:6px 0}
h1{font-size:1.7rem !important}
.vd{border-left:10px solid var(--c);background:#f4f4f4;padding:16px;font-size:22px;line-height:1.35;font-weight:700;color:#111;margin:8px 0 16px}
.num{border:1px solid #bbb;border-radius:8px;padding:12px 14px;margin:8px 0;background:#fff}
.num b{display:block;font-size:34px;line-height:1.15;color:#111}.num span{font-size:16px;color:#222}.num small{display:block;font-size:15px;color:#333;margin-top:4px}
</style>"""


def _ir(passo):
    import streamlit as st  # só aqui: a lógica acima testa-se sem Streamlit
    st.session_state.passo = passo


def _guardar_e_ir(passo, pid=None):
    import streamlit as st  # só aqui: a lógica acima testa-se sem Streamlit
    if pid:
        p = next(x for x in PASSOS if x["id"] == pid)
        rotulos = [o[0] for o in p["opcoes"]]
        st.session_state.resp[pid] = rotulos.index(st.session_state[f"w_{pid}"])
    st.session_state.passo = passo


def _recomecar():
    import streamlit as st  # só aqui: a lógica acima testa-se sem Streamlit
    st.session_state.resp, st.session_state.passo = {}, 0


def _detalhado():
    import streamlit as st  # só aqui: a lógica acima testa-se sem Streamlit
    st.session_state.modo = "detalhado"


def render():
    import streamlit as st  # só aqui: a lógica acima testa-se sem Streamlit
    st.markdown(CSS, unsafe_allow_html=True)
    ss = st.session_state
    ss.setdefault("resp", {})
    ss.setdefault("passo", 0)
    st.title("DuoWatt: passar de gás a elétrico")
    if ss.passo < N_PASSOS:
        p = PASSOS[ss.passo]
        st.progress((ss.passo + 1) / N_PASSOS, text=f"Passo {ss.passo + 1} de {N_PASSOS}")
        if ss.passo == 0:
            st.write("Responda a 5 perguntas curtas e veja se a sua casa aguenta trocar o gás por elétrico. Não guardamos nada.")
        rotulos = [o[0] for o in p["opcoes"]]
        st.radio(p["titulo"], rotulos, index=ss.resp.get(p["id"], p["pre"]), key=f"w_{p['id']}")
        st.info(p["ajuda"])
        if rotulos.index(ss[f"w_{p['id']}"]) == len(rotulos) - 1 and p["opcoes"][-1][1] is None:
            st.caption(p["nao_sei"])
        voltar, seguir = st.columns(2)
        voltar.button("Voltar", disabled=ss.passo == 0, on_click=_guardar_e_ir, args=(ss.passo - 1, p["id"]), use_container_width=True)
        seguir.button("Continuar" if ss.passo < N_PASSOS - 1 else "Ver o resultado", type="primary",
                      on_click=_guardar_e_ir, args=(ss.passo + 1, p["id"]), use_container_width=True)
        return

    v, assumido = valores(ss.resp)
    r = calcular(v["kva"], v["consumo"], v["pessoas"], v["placa"], v["garrafas"])
    ss.resultado = r
    st.markdown(f'<div class="vd" style="--c:{COR[r["veredicto"]]}">{html.escape(FRASES[r["veredicto"]])}</div>', unsafe_allow_html=True)
    if r["veredicto"] == "precisa de mais potência":
        cabe = next((k for k in (2.3, 3.45, 6.9, 10.35) if k * 1000 >= r["com"]["pico_w"]), None)
        st.write(f"Precisaria de pelo menos {pt(cabe, 2).rstrip('0').rstrip(',')} kVA." if cabe else "Nem a maior potência da lista chega.")
    for val, rot, leg in numeros(r):
        st.markdown(f'<div class="num"><span>{html.escape(rot)}</span><b>{html.escape(val)}</b><small>{html.escape(leg)}</small></div>', unsafe_allow_html=True)
    st.subheader("O que fazer a seguir")
    for t in PROXIMOS[r["veredicto"]]:
        st.markdown(f"- {t}")
    st.download_button("Descarregar o relatório para o instalador", relatorio_html(r, assumido).encode("utf-8"),
                       file_name="relatorio_duowatt.html", mime="text/html", use_container_width=True, type="primary")
    st.caption("Abra o ficheiro e imprima-o ou guarde-o em PDF.")
    if assumido:
        with st.expander("O que assumimos por si («Não sei»)"):
            for t, n in assumido:
                st.markdown(f"- **{t}** {n}")
    with st.expander("Pressupostos e cenário adverso"):
        st.table({"Item": [a for a, _, _ in pressupostos(r)], "Valor": [b for _, b, _ in pressupostos(r)], "Fonte e classificação": [c for _, _, c in pressupostos(r)]})
    st.caption("Simulação ilustrativa, com valores por validar. O CO₂ evitado vem de trocar gás por elétrico, não do DuoWatt, que só retira o bloqueio da potência.")
    voltar, rec = st.columns(2)
    voltar.button("Voltar à última pergunta", on_click=_ir, args=(N_PASSOS - 1,), use_container_width=True)
    rec.button("Recomeçar", on_click=_recomecar, use_container_width=True)
    st.button("Modo detalhado (gráficos e números técnicos)", on_click=_detalhado, use_container_width=True)

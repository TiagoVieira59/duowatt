"""Analisa o CSV exportado do Google Forms (ver docs/provas/INQUERITO.md).

Uso: .venv/bin/python ferramentas/analisar_inquerito.py <respostas.csv> [--saida dados/]
Gera inquerito_resumo.json, inquerito_resumo.md e graficos/P<n>.png na pasta de saída.
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
AMOSTRA_MIN = 30
CHECKBOX = {"P1", "P6"}
TEXTO_LIVRE = "P11"
# opções de docs/provas/INQUERITO.md (ordem de apresentação); o que não constar agrupa-se em "Outra" nas caixas de verificação
OPCOES = {
    "P1": ["Esquentador (água quente)", "Fogão ou placa a gás", "Forno a gás", "Aquecedor a gás",
           "Nenhum (só gás natural ou eletricidade)"],
    "P2": ["Apartamento", "Moradia"],
    "P3": ["1", "2", "3", "4", "5 ou mais"],
    "P4": ["2,3 kVA", "3,45 kVA", "4,6 kVA", "5,75 kVA", "6,9 kVA", "10,35 kVA ou mais", "Não sei"],
    "P5": ["Nunca pensei", "Já pensei, mas não avancei", "Já pensei e vou avançar / já avancei"],
    "P6": ["Acho a eletricidade mais cara", "Não vejo vantagem", "Não tenho espaço para o equipamento",
           "Receio que o quadro dispare / a potência não chegue", "Custo da obra ou da instalação",
           "Não sei a quem pedir ajuda", "Só mudo quando avariar"],
    "P7": ["Compraria outro a gás, o mais depressa possível", "Compraria um equipamento elétrico",
           "Depende do preço e da rapidez da instalação", "Não sei"],
    "P8": ["Nunca", "Raramente", "Algumas vezes por ano", "Muitas vezes"],
    "P9": ["Sim", "Talvez", "Não", "Não percebi"],
    "P10": ["Nada (não pagaria)", "Até 50 €", "50 a 150 €", "150 a 300 €", "Mais de 300 €"],
}
AVISO = "amostra pequena: percentagens indicativas"


def erro(msg):
    print(f"Erro: {msg}", file=sys.stderr)
    sys.exit(1)


def ler(caminho):
    p = Path(caminho)
    if not p.is_file():
        erro(f"o ficheiro '{caminho}' não existe.")
    if p.stat().st_size == 0:
        erro(f"o ficheiro '{caminho}' está vazio.")
    with open(p, newline="", encoding="utf-8-sig") as f:
        linhas = list(csv.reader(f))
    cab, corpo = linhas[0], linhas[1:]
    colunas = {}  # número da pergunta -> índice da coluna
    for i, titulo in enumerate(cab):
        m = re.match(r"^\s*P(\d+)\.", titulo)
        if m and int(m.group(1)) not in colunas:
            colunas[int(m.group(1))] = i
    if not colunas:
        erro("não encontrei colunas de perguntas (títulos a começar por 'P1.', 'P2.', ...). É o CSV do Forms?")
    corpo = [r for r in corpo if any(c.strip() for c in r)]
    if not corpo:
        erro("o ficheiro só tem o cabeçalho, sem respostas.")
    return colunas, cab, corpo


def contar(chave, valores):
    """valores: lista de respostas (str) não vazias. Devolve (n_que_respondeu, {opção: contagem})."""
    c = Counter()
    for v in valores:
        if chave in CHECKBOX:
            partes = [x.strip() for x in v.split(", ") if x.strip()]
            escolhidas = {x if x in OPCOES[chave] else "Outra" for x in partes}  # "Outra" conta uma vez por pessoa
        else:
            escolhidas = {v.strip()}
        c.update(escolhidas)
    ordem = OPCOES.get(chave, [])
    extras = sorted(k for k in c if k not in ordem)
    return len(valores), {k: c[k] for k in ordem + extras if c[k] or k in ordem}


def analisar(colunas, cab, corpo):
    res = {"n_respostas": len(corpo), "perguntas": {}, "avisos": []}
    for num in range(1, 12):
        chave = f"P{num}"
        if num not in colunas:
            res["avisos"].append(f"coluna {chave} em falta no CSV")
            continue
        valores = [r[colunas[num]].strip() for r in corpo if colunas[num] < len(r) and r[colunas[num]].strip()]
        titulo = cab[colunas[num]].strip()
        if chave == TEXTO_LIVRE:
            top = Counter(v.casefold() for v in valores)
            nomes = {v.casefold(): v for v in valores}
            res["perguntas"][chave] = {"pergunta": titulo, "n": len(valores),
                                       "distritos_mais_frequentes": [{"distrito": nomes[k], "contagem": n} for k, n in top.most_common(5)]}
            continue
        n, cont = contar(chave, valores)
        res["perguntas"][chave] = {"pergunta": titulo, "n": n, "opcoes": {
            k: {"contagem": v, "percentagem": round(100 * v / n, 1) if n else 0.0} for k, v in cont.items()}}
    return res


def pct(res, chave, opcao):
    q = res["perguntas"].get(chave)
    return q["opcoes"].get(opcao, {"percentagem": 0.0})["percentagem"] if q and q["n"] else None


def indicadores(res):
    p8 = res["perguntas"].get("P8")
    return {
        "nunca_pensou_pct": pct(res, "P5", "Nunca pensei"),
        "ja_disparou_quadro_pct": round(100 - pct(res, "P8", "Nunca"), 1) if p8 and p8["n"] else None,
        "compraria_gas_na_avaria_pct": pct(res, "P7", OPCOES["P7"][0]),
        "disposicao_a_pagar_P10_pct": {k: v["percentagem"] for k, v in res["perguntas"]["P10"]["opcoes"].items()}
        if "P10" in res["perguntas"] else None,
    }


def grafico(chave, q, destino):
    nomes = list(q["opcoes"])[::-1]
    vals = [q["opcoes"][k]["percentagem"] for k in nomes]
    fig, ax = plt.subplots(figsize=(10, 0.6 * len(nomes) + 1.6), dpi=100)
    ax.barh(nomes, vals, color="#4a6b8a")
    for i, v in enumerate(vals):
        ax.text(v + 1, i, f"{v:.0f} %", va="center", fontsize=14, color="#222")
    ax.set_xlim(0, 110)
    ax.set_xlabel("% de quem respondeu", fontsize=14)
    ax.tick_params(labelsize=14)
    ax.set_title(f"{chave} (n = {q['n']})", fontsize=14, loc="left")
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    fig.tight_layout()
    fig.savefig(destino)
    plt.close(fig)


def escrever(res, saida):
    saida.mkdir(parents=True, exist_ok=True)
    (saida / "graficos").mkdir(exist_ok=True)
    res["indicadores"] = indicadores(res)
    (saida / "inquerito_resumo.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    n = res["n_respostas"]
    md = ["# Resumo do inquérito", "", f"**n = {n} respostas.**"]
    if n < AMOSTRA_MIN:
        md.append(f"**Aviso: {AVISO} (n < {AMOSTRA_MIN}).**")
    md += [f"Aviso: {a}." for a in res["avisos"]]
    for chave, q in res["perguntas"].items():
        md += ["", f"## {q['pergunta']}", "", f"Respostas a esta pergunta: {q['n']}.", ""]
        if "opcoes" in q:
            md += ["| Opção | Contagem | % |", "|---|---|---|"]
            md += [f"| {k} | {v['contagem']} | {v['percentagem']:.1f} % |".replace(".", ",") for k, v in q["opcoes"].items()]
            if q["n"]:
                grafico(chave, q, saida / "graficos" / f"{chave}.png")
        else:
            md += [f"- {d['distrito']}: {d['contagem']}" for d in q["distritos_mais_frequentes"]] or ["Sem respostas."]
    (saida / "inquerito_resumo.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv", help="CSV exportado do Google Forms")
    ap.add_argument("--saida", default=str(RAIZ / "dados"), help="pasta de saída (por omissão dados/)")
    a = ap.parse_args(argv)
    colunas, cab, corpo = ler(a.csv)
    res = analisar(colunas, cab, corpo)
    escrever(res, Path(a.saida))
    print(f"{res['n_respostas']} respostas analisadas; resultados em {a.saida}")


if __name__ == "__main__":
    main()

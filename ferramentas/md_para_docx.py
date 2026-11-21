"""Converte o subconjunto de Markdown do GUIA_EQUIPA.md (#, ##, -, tabelas, **negrito**) para .docx. Uso: md_para_docx.py in.md out.docx"""
import re
import sys

from docx import Document


def runs(par, texto):
    for i, parte in enumerate(re.split(r"\*\*(.+?)\*\*", texto)):
        par.add_run(parte).bold = i % 2 == 1


def main(entrada, saida):
    d, tabela = Document(), []
    linhas = open(entrada, encoding="utf-8").read().splitlines() + [""]
    for l in linhas:
        if l.startswith("|"):
            if not re.fullmatch(r"\|[-| ]+\|", l):
                tabela.append([c.strip() for c in l.strip("|").split("|")])
            continue
        if tabela:
            t = d.add_table(rows=len(tabela), cols=len(tabela[0]), style="Table Grid")
            for i, linha in enumerate(tabela):
                for j, c in enumerate(linha):
                    runs(t.cell(i, j).paragraphs[0], c)
                    if i == 0:
                        for r in t.cell(i, j).paragraphs[0].runs:
                            r.bold = True
            tabela = []
        if l.startswith("# "):
            d.add_heading(l[2:], 0)
        elif l.startswith("## "):
            d.add_heading(l[3:], 1)
        elif re.match(r"(- |\d+\. )", l):
            runs(d.add_paragraph(style="List Bullet" if l.startswith("-") else "List Number"), re.sub(r"^(- |\d+\. )", "", l))
        elif l.strip():
            runs(d.add_paragraph(), l.lstrip("> "))
    d.save(saida)


if __name__ == "__main__":
    main(*sys.argv[1:3])

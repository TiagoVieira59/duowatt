"""Testes do analisador do inquérito. Usam só o CSV SINTÉTICO (inventado) e escrevem sempre em tmp_path, nunca em dados/."""
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SCRIPT = AQUI.parent / "analisar_inquerito.py"
# o matplotlib só está instalado no .venv
PY = AQUI.parent.parent / ".venv/bin/python"
CSV = AQUI / "respostas_SINTETICAS_so_para_testar.csv"


def correr(csv, saida):
    return subprocess.run([str(PY) if PY.exists() else sys.executable, "-I", str(SCRIPT), str(csv), "--saida", str(saida)], capture_output=True, text=True)


def test_contagens_e_percentagens(tmp_path):
    r = correr(CSV, tmp_path)
    assert r.returncode == 0, r.stderr
    d = json.loads((tmp_path / "inquerito_resumo.json").read_text(encoding="utf-8"))
    assert d["n_respostas"] == 8
    assert d["perguntas"]["P5"]["opcoes"]["Nunca pensei"] == {"contagem": 3, "percentagem": 37.5}
    assert d["perguntas"]["P1"]["opcoes"]["Esquentador (água quente)"]["contagem"] == 6
    assert d["perguntas"]["P6"]["opcoes"]["Outra"]["contagem"] == 1  # texto livre com vírgula conta uma vez
    assert d["perguntas"]["P6"]["n"] == 7  # uma resposta em branco
    assert d["indicadores"]["ja_disparou_quadro_pct"] == 62.5
    assert d["indicadores"]["compraria_gas_na_avaria_pct"] == 25.0
    assert d["indicadores"]["disposicao_a_pagar_P10_pct"]["50 a 150 €"] == 37.5
    assert d["perguntas"]["P11"]["distritos_mais_frequentes"][0] == {"distrito": "Aveiro", "contagem": 4}
    assert "amostra pequena: percentagens indicativas" in (tmp_path / "inquerito_resumo.md").read_text(encoding="utf-8")
    assert (tmp_path / "graficos" / "P5.png").stat().st_size > 0


def test_ficheiro_vazio(tmp_path):
    vazio = tmp_path / "vazio.csv"
    vazio.write_text("")
    r = correr(vazio, tmp_path / "saida")
    assert r.returncode == 1 and "vazio" in r.stderr and "Traceback" not in r.stderr
    assert not (tmp_path / "saida").exists()


def test_sem_colunas_de_perguntas(tmp_path):
    f = tmp_path / "x.csv"
    f.write_text("a,b\n1,2\n")
    r = correr(f, tmp_path / "saida")
    assert r.returncode == 1 and "P1." in r.stderr

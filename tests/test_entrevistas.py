"""Testes do bloco de entrevistas. Dados SINTÉTICOS (inventados), só em tmp_path; nunca em dados/."""
import json
import os
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent.parent
PY = AQUI / ".venv/bin/python"
CODIGO = """
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("app.py", default_timeout=60)
at.session_state["modo"] = "detalhado"  # as provas estão no modo detalhado
at.run()
print("EXC", len(at.exception))
print("SUB", [s.value for s in at.subheader])
print("WARN", [w.value for w in at.warning])
print("MD", " ".join(m.value for m in at.markdown))
"""


def correr(tmp_path, conteudo=None):
    if conteudo is not None:
        (tmp_path / "entrevistas.json").write_text(conteudo, encoding="utf-8")
    env = {**os.environ, "DUOWATT_DADOS": str(tmp_path)}
    r = subprocess.run([str(PY) if PY.exists() else sys.executable, "-c", CODIGO], cwd=AQUI, env=env, capture_output=True, text=True)
    assert "EXC 0" in r.stdout, r.stdout + r.stderr
    return r.stdout


def test_valido_e_ignora_modelo(tmp_path):
    d = [{"perfil": "A", "data": "SINTETICO", "citacao": "citacao sintetica um", "facto": "facto sintetico um"},
         {"perfil": "C", "citacao": "citacao sintetica dois"},
         {"perfil": "B", "citacao": "[preencher]", "facto": "[preencher]"}, {}]
    o = correr(tmp_path, json.dumps(d))
    assert "Entrevistas da equipa (2)" in o and "«citacao sintetica um»" in o and "eletricista" in o
    assert "[preencher]" not in o


def test_json_invalido(tmp_path):
    o = correr(tmp_path, "{isto nao e json")
    assert "Ficheiro de entrevistas inválido: ver ferramentas/modelo_entrevistas.json" in o


def test_ficheiro_inexistente(tmp_path):
    o = correr(tmp_path)
    assert "Entrevistas da equipa" not in o and "inválido" not in o


def test_modelo_nao_mostra_nada(tmp_path):
    o = correr(tmp_path, (AQUI / "ferramentas/modelo_entrevistas.json").read_text(encoding="utf-8"))
    assert "Entrevistas da equipa" not in o


def test_citacao_com_asteriscos_e_sublinhados_fica_literal(tmp_path):
    # SINTÉTICO: * e _ não podem virar formatação markdown numa citação literal
    o = correr(tmp_path, json.dumps([{"perfil": "A", "citacao": "sintetico *caro* e a_b"}]))
    assert r"«sintetico \*caro\* e a\_b»" in o

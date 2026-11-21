"""Screenshots automáticos da app DuoWatt nos cenários fixos.

Uso: .venv/bin/python ferramentas/capturar.py <nome_do_ciclo>   (ex.: ciclo0)
Saída: screenshots/<nome_do_ciclo>/<cenario>_<LxA>_<tela|pagina>.png e erros.txt
Os widgets são encontrados pelo rótulo; se a UI mudar os rótulos, atualizar CENARIOS/ROTULOS.
"""
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
TAMANHOS = [(1920, 1080), (1366, 768)]
ALTURA_PAGINA = 2600
ROTULOS = {
    "kva": "Potência contratada (kVA)",
    "consumo": "Consumo mensal (kWh)",
    "pessoas": "Número de pessoas",
    "garrafas": "Garrafas de gás por ano",
}
CENARIOS = {
    "A_tipica": {},
    "B_inducao_intensa": {"inducao": "Intenso (3 kW)"},
    "B2_precisa_mais_potencia": {"inducao": "Intenso (3 kW)", "consumo": 432},  # base de 600 W: o DuoWatt não chega
    "C_6_9kva": {"kva": "6.9"},
    "D1_minimo": {"kva": "2.3", "pessoas": 1, "garrafas": 0},
    "D2_maximo": {"kva": "10.35", "pessoas": 8, "garrafas": 20},
}


def porta_livre(preferida=8599):
    for p in (preferida, 0):
        with socket.socket() as s:
            try:
                s.bind(("127.0.0.1", p))
                return s.getsockname()[1]
            except OSError:
                continue


def esperar_servidor(url, tentativas=60):
    for _ in range(tentativas):
        try:
            urllib.request.urlopen(url + "/_stcore/health", timeout=1)
            return
        except Exception:
            time.sleep(0.5)
    raise RuntimeError("O Streamlit não arrancou a tempo")


def aplicar(page, cenario):
    for chave, valor in cenario.items():
        if chave == "kva":
            page.get_by_label(ROTULOS["kva"]).click()
            page.get_by_role("option", name=valor, exact=True).click()
        elif chave == "inducao":
            page.get_by_text(valor, exact=True).click()
        else:
            if chave in ("pessoas", "garrafas") and not page.get_by_label(ROTULOS[chave]).is_visible():
                page.get_by_text("Avançado", exact=True).click()  # campos no expander
            campo = page.get_by_label(ROTULOS[chave])
            campo.fill(str(valor))
            campo.press("Enter")
            campo.press("Tab")  # sai do campo: sem "Press Enter to apply" no screenshot
        page.wait_for_timeout(1200)


def main(ciclo):
    saida = RAIZ / "screenshots" / ciclo
    saida.mkdir(parents=True, exist_ok=True)
    porta = porta_livre()
    url = f"http://127.0.0.1:{porta}"
    servidor = subprocess.Popen(
        [str(RAIZ / ".venv/bin/streamlit"), "run", "app.py", "--server.headless", "true",
         "--server.port", str(porta), "--browser.gatherUsageStats", "false"],
        cwd=RAIZ, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    erros = []
    try:
        esperar_servidor(url)
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            for largura, altura in TAMANHOS:
                for nome, cenario in CENARIOS.items():
                    ctx = navegador.new_context(viewport={"width": largura, "height": altura}, locale="pt-PT")
                    page = ctx.new_page()
                    page.on("console", lambda m, n=nome: erros.append(f"[{n}] consola {m.type}: {m.text}")
                            if m.type in ("error", "warning") else None)
                    page.goto(url)
                    page.get_by_text("Veredicto").first.wait_for(timeout=30000)
                    aplicar(page, cenario)
                    page.wait_for_timeout(800)
                    for exc in page.locator('[data-testid="stException"]').all():
                        erros.append(f"[{nome}] exceção Streamlit: {exc.inner_text()[:200]}")
                    base = f"{nome}_{largura}x{altura}"
                    page.screenshot(path=saida / f"{base}_tela.png")
                    page.set_viewport_size({"width": largura, "height": ALTURA_PAGINA})
                    page.wait_for_timeout(600)
                    page.screenshot(path=saida / f"{base}_pagina.png")
                    ctx.close()
            navegador.close()
    finally:
        servidor.terminate()
        try:
            servidor.wait(timeout=10)
        except subprocess.TimeoutExpired:
            servidor.kill()
    (saida / "erros.txt").write_text("\n".join(erros) if erros else "sem erros nem avisos\n", encoding="utf-8")
    print(f"{len(list(saida.glob('*.png')))} imagens em {saida}; erros: {len(erros)}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "ciclo0")

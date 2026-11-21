# Decisões da equipa autónoma

Formato: data/ciclo · decisão · antes → depois · motivo · fonte.

- Ciclo 0 · Playwright instalado só no `.venv` (sem sudo, nada global) para ver a app num browser.
- Ciclo 0 · Acrescentado o cenário B2 (indução intensa + 432 kWh/mês) à captura: com B (200 kWh/mês) o veredicto continua 'aguenta com gestão', e o caso em que o DuoWatt não chega só aparece com base de ~600 W.
- Ciclo 1 · Mantido 0,21 €/kWh (não 0,18): o Modelador mostra que 0,18 exagera a poupança 2,4× (33 € vs 82 €/ano) porque o IVA de 6 % só cobre os primeiros 200 kWh/mês. Fonte: Parametros_Verificados.md + conta em equipa/modelo_ciclo1.md.
- Ciclo 1 · Custo/instalação e objeção 4 adiados (sem dados verificados; vão para PERGUNTAS.md e DEMO_GUIAO.md).
- Ciclo 2 · (para o Tiago validar) 64 €/ano para subir de 3,45 para 6,9 kVA · antes: sem número → depois: `custo_subir_potencia` = (0,3659 − 0,1917) × 365 ≈ 63,6 €/ano, sem IVA · motivo: comparar com a poupança do gás (33 €/ano) · fonte: ERSE, Diretiva 4/2026 (1 out 2026), comercializador de último recurso; PESQUISA.md §4. Não é o termo de acesso (TAR), que não foi encontrado.
- Ciclo 2 · (para o Tiago validar) 44 % proxy · antes: sem teto → depois: legenda 'limite superior' com 44 % das 2,2 M de casas · motivo: majorar o que depende de desbloquear a potência · fonte: E-REDES, perfis 2025 (dados 2023): <3,45 kVA = 44,1 % dos contratos BTN. Proxy: inclui não domésticos e não é específico das casas a GPL.
- Ciclo 2 · (para o Tiago validar) 67 % / 17 % · antes: sem aviso → depois: nota em 'Pressupostos e limites' · motivo: a maioria das casas teria de comprar termoacumulador (custo não incluído) · fonte: ICESD 2020 (INE/DGEG/ADENE), secção 2.4.3; PESQUISA.md.

# Decisões da equipa autónoma

Formato: data/ciclo · decisão · antes → depois · motivo · fonte.

- Ciclo 0 · Playwright instalado só no `.venv` (sem sudo, nada global) para ver a app num browser.
- Ciclo 0 · Acrescentado o cenário B2 (indução intensa + 432 kWh/mês) à captura: com B (200 kWh/mês) o veredicto continua 'aguenta com gestão', e o caso em que o DuoWatt não chega só aparece com base de ~600 W.
- Ciclo 1 · Mantido 0,21 €/kWh (não 0,18): o Modelador mostra que 0,18 exagera a poupança 2,4× (33 € vs 82 €/ano) porque o IVA de 6 % só cobre os primeiros 200 kWh/mês. Fonte: Parametros_Verificados.md + conta em equipa/modelo_ciclo1.md.
- Ciclo 1 · Custo/instalação e objeção 4 adiados (sem dados verificados; vão para PERGUNTAS.md e DEMO_GUIAO.md).
- Ciclo 2 · (para o Tiago validar) 64 €/ano para subir de 3,45 para 6,9 kVA · antes: sem número → depois: `custo_subir_potencia` = (0,3659 − 0,1917) × 365 ≈ 63,6 €/ano, sem IVA · motivo: comparar com a poupança do gás (33 €/ano) · fonte: ERSE, Diretiva 4/2026 (1 out 2026), comercializador de último recurso; PESQUISA.md §4. Não é o termo de acesso (TAR), que não foi encontrado.
- Ciclo 2 · (para o Tiago validar) 44 % proxy · antes: sem teto → depois: legenda 'limite superior' com 44 % das 2,2 M de casas · motivo: majorar o que depende de desbloquear a potência · fonte: E-REDES, perfis 2025 (dados 2023): <3,45 kVA = 44,1 % dos contratos BTN. Proxy: inclui não domésticos e não é específico das casas a GPL.
- Ciclo 2 · (para o Tiago validar) 67 % / 17 % · antes: sem aviso → depois: nota em 'Pressupostos e limites' · motivo: a maioria das casas teria de comprar termoacumulador (custo não incluído) · fonte: ICESD 2020 (INE/DGEG/ADENE), secção 2.4.3; PESQUISA.md.
- Noite 2 · Formato PT-PT numa função (`formato.py`): espaço sem quebra nos milhares a partir de 10 000, vírgula nos decimais; eixos dos gráficos iguais.
- Noite 2 · (por validar) Assistente: valores pré-selecionados/«Não sei» · 3,45 kVA, 200 kWh/mês, 3 pessoas, placa normal 1,8 kW, 12 garrafas/ano (uma por mês) · motivo: valores típicos de trabalho, todos hipótese; o resultado e o relatório listam o que foi assumido. O modo detalhado usa 10 garrafas por omissão só se não houver respostas do assistente.
- Noite 2 · Identidade visual: tema neutro (cartões, cinzento escuro, verde/âmbar/vermelho só para o veredicto), sem logo nem vermelho Bosch.
- Noite 2b · 12 garrafas/ano por omissão em TODA a app e documentos (antes 10 no modo detalhado e 12 no assistente) · motivo: uma só omissão (uma por mês), hipótese; CO₂ 246 kg/casa, 40 €/ano. Atualizados CONTEXTO, VIABILIDADE, DEMO_GUIAO, RELATORIO_FINAL.
- Noite 2b · Métrica principal de impacto (`impacto.metrica_principal`) · casas desbloqueadas = 2,2 M × 44 % × adoção (1/5/10 %); % dos 870 kton; mercado de 60 M€ repartido por casa (hipótese de proporcionalidade) · fontes: enunciado Bosch (confirmado), E-REDES (proxy). Sem unidades de Tronic: não há dado. Detalhe em IMPACTO.md.
- Noite 2b · Cor principal dos botões: verde-petróleo #0b5c6b (contraste ~7,6:1 com branco, WCAG AA), em `.streamlit/config.toml`; sem vermelho (Bosch).
- Kit · `simular`: reserva inicial de 50 % às 18:00 (pressuposto, para o cilindro estar a aquecer às 18:40); só religa se o total com o cilindro não passa o limite (evita ligar/desligar a cada minuto); após 30 min de pausa religa à força.

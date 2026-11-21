# Modelo, ciclo 1 (Modelador)

Testes: `test_modelo_ciclo1.py` (31 testes no total com os antigos: 31 passam, 5 `xfail(strict)` = problemas reais; ficam verdes e passam a falhar no dia em que forem corrigidos, para forçar a retirar a marca).
Comando: `python3 -I -m pytest -q test_modelo_ciclo1.py -p no:cacheprovider`. Nada em duowatt.py, impacto.py ou app.py foi alterado.

## Gravidade ALTA

### A1. O veredicto a 3,45 kVA com indução de 3 kW é frágil e a base plana esconde isso (pontos 2 e 4)
- Base plana = consumo/720 h. Casa média INE (280 kWh/mês) dá 389 W; ao serão o pressuposto é ~600 W.
- O veredicto muda para "precisa de mais potência" a **324 kWh/mês (base 450 W)**, não a 432 (o teste antigo usa 432 só por estar bem acima). Provado por `test_limiar_do_veredicto_e_450w_nao_600w` (324 passa, 325 falha).
- A casa média (280 kWh) com indução 3 kW tem margem de **61 W** sem o termoacumulador (`test_margem_da_casa_media_sem_termo_e_minuscula`): "aguenta com gestão" é apenas por acaso da base plana. Com 600 W reais seria "precisa de mais potência" (`test_casa_media_com_inducao_forte_ao_serao`, xfail).
- Resposta ao ponto 4: é coerente que o veredicto vire à volta de 450 W de base, mas a conclusão depende quase só de um número sem fonte. Mostrar honestamente: (a) pedir à UI a "base ao serão (W)" como entrada separada, com a média INE (389 W) e o pressuposto 600 W como dois cenários; (b) mostrar a margem em W (limite − base − indução) e um intervalo ("a 389 W aguenta com 61 W de folga; a 600 W não aguenta"), em vez de um veredicto único.
- Correção sugerida: parâmetro `base_serao_w` (por omissão max(base plana, valor pressuposto) rotulado "pressuposto") e devolver `margem_w` em `veredicto`.
- Impacto: para a casa média + indução 3 kW o veredicto passa de "aguenta com gestão" para "precisa de mais potência" (muda a conclusão do pitch). Com indução 1,8 kW nada muda (aguenta com gestão até base ~1 650 W; `test_inducao_normal_aguenta_com_gestao_mesmo_com_base_alta`).

### A2. A poupança de ~33 €/ano é muito sensível e a recomendação de 0,18 €/kWh exagera (ponto 1)
- Conta coerente: energia 0,1711 € sem IVA; x1,06 = 0,1814 (até 200 kWh/mês) ; x1,23 = 0,2105 (acima). O comentário de `impacto.py` diz "0,171 € com IVA de 23 %": errado, 0,171 é sem IVA (`test_comentario_impacto_nao_mistura_iva`, xfail).
- O IVA de 6 % só cobre os primeiros 200 kWh/mês da casa; o kWh **adicional** (o das garrafas, ~134 kWh/mês) paga 23 % se a casa já gasta >200 kWh/mês. Logo **0,21 é o preço marginal certo para a casa média (280 kWh) e para o exemplo de 200 kWh**; 0,18 só seria certo para uma casa com ~0 kWh/mês de base (`test_preco_marginal_misto_por_escaloes`).
- Números (10 garrafas, 37 €): 0,21 -> 33,5 €/ano; 0,18 -> 81,6 €/ano (exagera 2,4x); casa ERSE de 158 kWh/mês (preço misto 0,201) -> 47,4 €/ano. Com IEC (0,001 €/kWh +IVA) -2,0 €. Com garrafa a 43,55 € -> ~99 €/ano; garrafa a 30 € -> poupança negativa.
- Veredicto: ~33 € é correto como valor central para casas >200 kWh/mês; a gama honesta é **~30-50 € (preço 37 €)** e **~90-100 € (preço 43,5 €)**. A poupança é dominada pelo preço da garrafa (+-1 € = +-10 €/ano) e não pela tarifa.
- Correção sugerida: manter 0,21 por omissão, corrigir o comentário e o `Parametros_Verificados.md` (0,18 só vale ≤200 kWh/mês totais); usar o consumo mensal da UI para calcular o preço misto; mostrar a gama em vez de 33 €.

## Gravidade MÉDIA

### M1. Pessoas e garrafas incoerentes entre os dois módulos
- 3 pessoas pedem 2,29 MWh/ano de água quente útil (40 L x 45 K); 10 garrafas dão 1,60 MWh/ano elétricos para a casa toda, cozinha incluída. Teste: `test_pessoas_e_garrafas_sao_coerentes` (xfail).
- Correção: na UI avisar quando garrafas < água quente das pessoas (~12-17 garrafas para 3 pessoas só em água quente), ou derivar um valor do outro.
- Impacto: não altera cada módulo isoladamente, mas o júri pode apanhar o desencontro (10 garrafas vs. 3 pessoas).

### M2. kVA tratado como kW e "disparos" sem tolerância (ponto 3)
- O modelo é conservador num sentido e otimista no outro: FP<1 aumenta a carga em kVA (com FP 0,9 o limite útil é 3 105 W e a casa média + 3 kW deixa de caber, `test_fator_de_potencia_desloca_o_limiar`); mas o disjuntor tolera sobrecarga. Valores IEC 60898 de memória (não verificados nas fontes do projeto): sem disparo até 1,13 x In durante 1 h; disparo em <1 h entre 1,13 e 1,45 x In.
- Caso demo (3 450 W, 200 kWh, indução 1,8 kW, sem gestão): pico 4 078 W = **1,18 x limite durante 25 min**, "1 disparo". Está na zona 1,13-1,45, por isso "pode disparar", não "dispara" (`test_demo_sem_gestao_sobrecarga_de_18_por_cento_durante_25_min`). Com indução 1,5 kW o pico é 1,095 x e o modelo conta "disparo" quando o disjuntor aguentava (`test_sobrecarga_toleravel_conta_como_acima`; o veredicto é conservador, não errado).
- Correção: apresentar "risco de disparo" com o rácio pico/limite e a duração; chamar-lhe "minutos acima do limite", e só falar em "disparo provável" se rácio > 1,13 (pressuposto com fonte a verificar).

### M3. Dia que não fecha: o estado inicial "cheio" esconde défices
- 8 pessoas / 200 L: o termoacumulador acaba o dia 1,5 kWh abaixo do cheio (reaquecimento do serão passa a meia-noite) mas o dia seguinte começava cheio (`test_dia_fecha_em_regime_estacionario_8_pessoas`, xfail). Para 3 e 5 pessoas o balanço fecha (`test_balanco_do_deposito_fecha`).
- Correção: simular 2 dias e devolver o segundo (ou reiniciar com o nível final).
- Impacto: só com famílias grandes (>=6 pessoas); o resultado "minutos sem água" fica subestimado nesses casos.

### M4. Sem perdas térmicas em repouso
- Parâmetros: ~1,5 kWh/24 h (80 L, Tronic). O simulador consome exatamente a energia útil (6,3 kWh/dia para 3 pessoas, +0 de perdas), enquanto `impacto.py` usa 85 % (`test_perdas_em_repouso_modeladas`, xfail).
- Correção: subtrair `perda_w = 1500/24` W ao depósito (0,0104 kWh/min).
- Impacto: +24 % de tempo ligado (~+45 min/dia), pequeno efeito nos veredictos (a sobreposição com indução é gerida), mas o consumo diário fica ~1,5 kWh abaixo da realidade.

## Gravidade BAIXA

- **10,35 kVA**: o modelo soma tudo num só limite e devolve sempre "aguenta" (`test_10_35_kva_aguenta_sempre_mas_assume_monofasico`). Se for trifásico e a indução e o termoacumulador estiverem na mesma fase, o limite relevante é 3,45 kVA por fase. Assinalar o pressuposto "monofásico".
- **Controlador ideal**: decide no mesmo minuto em que a indução liga (sem latência) e sabe que a indução está ligada (o contexto diz sem sensores). Pressuposto a declarar no pitch.
- **"Precisa de mais potência"** ignora a alternativa de limitar a potência da placa (muitas têm gestão de potência).
- **Histerese do termostato** inexistente (reaquece logo que sai 0,03 kWh do máximo); só afeta a contagem de ciclos, não os veredictos. A pausa mínima de 5 min funciona (`test_pausa_minima_de_5_min_respeitada`).
- **Entradas inválidas**: garrafas negativas aceites; `efic_eletrica=0` dá ZeroDivisionError (`test_entradas_invalidas_nao_sao_rejeitadas`). A UI deve limitar.
- **Temperaturas**: o depósito guarda 50 K (15->65 °C) mas a procura é 45 K (15->60 °C); levemente a favor da casa.
- **0 garrafas, 0 pessoas, depósito 0 L, limite 0**: sem erros e com resultados sensatos (`test_sem_gas_tudo_zero` já existente; `test_zero_pessoas_nao_precisa_de_agua`, `test_deposito_zero_litros_nao_rebenta`, `test_limite_zero_ou_muito_baixo`).
- **Depósito mínimo** para 3 pessoas: 70 L com gestão; a 60 L a gestão custa 2 min sem água, sem gestão a 6 900 VA não falta (`test_deposito_minimo_para_3_pessoas_e_70_litros_com_gestao`). 8 pessoas com 100 L: 8 min sem água; 200 L resolve (`test_8_pessoas_precisam_de_deposito_grande`).

## CO2 e extrapolação (sem problemas)
GPL 0,227 kg/kWh e 10 garrafas = 377 kg batem com o enunciado (>400 kg a 11 garrafas). Cenário 167 g/kWh: 109 kg/casa e ~2 400 t com 1 % de adoção; cenário 107 g: 205 kg e ~4 516 t (`test_co2_cenario_adverso_e_extrapolacao`). O cálculo de `efic_gas=0,82` é prudente (fogão a gás ~40 % aumentaria a poupança).

## Resumo dos testes xfail (a retirar quando corrigidos)
1. `test_comentario_impacto_nao_mistura_iva`
2. `test_pessoas_e_garrafas_sao_coerentes`
3. `test_casa_media_com_inducao_forte_ao_serao`
4. `test_dia_fecha_em_regime_estacionario_8_pessoas`
5. `test_perdas_em_repouso_modeladas`

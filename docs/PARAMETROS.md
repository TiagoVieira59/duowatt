# Parâmetros verificados (pesquisa de 20 nov 2026)

Legenda: CONFIRMADO = li o valor na fonte primária; PROVÁVEL = fonte indireta ou valor derivado de dados oficiais; NÃO ENCONTRADO = não achei fonte. "Derivado" = conta minha, assinalada como tal.

## 1. Fator de emissão da eletricidade em Portugal

| Item | Valor | Fonte | Classificação | Nota |
|---|---|---|---|---|
| APA, último valor anual publicado (2023), Portugal | 0,107 tCO2eq/MWh = **107 g/kWh** (Continente 92 g) | [APA, Fator de Emissão da Eletricidade 2025](https://apambiente.pt/sites/default/files/_Clima/Inventarios/20250808/fe_gee_eletricidade_2025_final_apc.pdf) | CONFIRMADO | Série 2005-2023. Em 2022 foi 158 g, em 2021 153 g, em 2020 184 g. |
| APA, média móvel 5 anos (2019-2023), Portugal | 0,167 tCO2eq/MWh = **167 g/kWh** (Continente 156 g) | idem | CONFIRMADO | Média dos 5 anos terminados no ano X. |
| Método da APA | Emissões de CO2, CH4 e N2O da combustão nas centrais (bottom-up, inventário nacional) a dividir pela eletricidade produzida (dados REN, EEM, EDA). Só emissões diretas; sem extração/transporte de combustível. | idem (secções 3, 6 e Anexo I) | CONFIRMADO | Mede produção nacional, não o consumo (não corrige importações). |
| Electricity Maps 2024, ~119 g/kWh | Não reverifiquei | [Electricity Maps](https://www.electricitymaps.com/grid-in-review-2025/portugal) | PROVÁVEL | Inclui ciclo de vida e fluxos de interligação, por isso é naturalmente mais alto. Fica próximo dos 107 g da APA. |
| APREN, ~40 g/kWh | Não encontrei este valor. Os boletins mensais da APREN dão **58,8 g (out 2025)** e **59,4 g (fev 2026)**. | [APREN, boletim fev 2026](https://www.apren.pt/wp-content/uploads/2026/03/Fev2026_Boletim.pdf) | NÃO ENCONTRADO (40 g) | Se os 40 g vieram de um mês ou ano específico, a equipa deve guardar a origem. |

Edição mais recente: só encontrei a edição de 2025 (dados até 2023). Não encontrei uma edição de 2026 (dados de 2024). O link da APA que está no `Parametros_Simulador.md` (pasta `20250715`) dá 404. O que funciona é o da pasta `20250808`, acima.

**Recomendação por omissão:** usar **107 g/kWh** (APA, valor anual oficial e citável). É coerente com os 119 g da Electricity Maps. Num parâmetro ajustável, mostrar o intervalo de 40 a 167 g. O fator mais alto (167 g, média de 5 anos) é o mais prudente para a poupança de CO2, porque encarece a eletricidade. Mostrar o resultado também com 167 g responde a uma acusação de exagero. Os 40 g não devem ser o valor por omissão, porque não os consegui sustentar.

## 2. Preço da garrafa de butano 13 kg (nov 2026)

| Item | Valor | Fonte | Classificação | Nota |
|---|---|---|---|---|
| Preço eficiente ERSE, nov 2026 | **41,98 €** (3,23 €/kg) | [ERSE, relatório mensal nov 2026](https://www.erse.pt/media/k2lk12yi/relat%C3%B3rio-mensal-nov2026.pdf) | CONFIRMADO | Referência de custos e margens médias (Regulamento 1184/2022). Não é preço de venda. |
| Preço eficiente com margens, nov 2026 | **43,55 €** (3,35 €/kg), +15,1% face a outubro | idem | CONFIRMADO | Aplica os limites máximos legais das **margens** (Diretiva 11/2023). É um indicador de supervisão, não um teto de preço de venda. |
| Preço anunciado (venda real), out 2026 | **36,87 €** (2,84 €/kg). Jul 36,34, ago 35,96, set 35,82. | idem, pág. 17 | CONFIRMADO | Média dos preços reportados no Balcão Único da Energia. É o último preço de venda medido. O de novembro só sairá no relatório de dezembro. |
| Teto de 29,47 € | Origem: Governo, **agosto de 2022**, máximo de 2,267 €/kg com impostos para a T3 13 kg | [DN, 2022](https://www.dn.pt/arquivo/diario-de-noticias/governo-volta-a-fixar-precos-maximos-da-botija-de-gas-15088934.html), [RR, 2022](https://rr.pt/noticia/pais/2022/08/16/precos-maximos-da-botija-de-gas-entram-hoje-em-vigor/296021/) | CONFIRMADO (existiu em 2022) | Não encontrei nenhum teto em vigor em 2026. O relatório da ERSE de nov 2026 não o menciona. As "notícias de julho" que a equipa viu não as encontrei: só achei as de 2022. |

Divergência e escolha: o teto de 29,47 € é de 2022 e não aparece como vigente na fonte oficial de 2026. Prefiro a ERSE, porque é o regulador, tem data e mede os preços reais. Em 2026 há apenas o programa de apoio "Botija de Gás Solidária" (Despacho 1016/2026), que não fixa preço máximo.

**Preço a usar:** **37 € por omissão** (último preço anunciado, 36,87 €). Como a ERSE diz que o preço anunciado está a subir para se aproximar do eficiente, mostrar também o cenário **42 a 43,5 €**. Para o pitch, 37 € é o valor que ninguém contesta. Em €/kWh de GPL (derivado, PCI 46 MJ/kg = 12,8 kWh/kg, 13 kg = 166 kWh): 37 € dá **0,22 €/kWh**, 43,55 € dá 0,26 €/kWh.

## 3. Preço da eletricidade, 3,45 kVA, tarifa simples, 2026

| Item | Valor | Fonte | Classificação | Nota |
|---|---|---|---|---|
| Energia, tarifa simples, mercado regulado, desde 1 out 2026 | **0,1711 €/kWh** (sem IVA e sem taxas) | [ERSE, Diretiva 4/2026](https://www.erse.pt/media/hjab13zj/diretiva-erse-4-2026-ajuste-tenergia-se-4t2026.pdf) | CONFIRMADO | Já inclui o ajuste de +0,005 €/kWh de outubro. |
| Termo fixo de potência, 3,45 kVA | **0,1917 €/dia** (sem IVA) | idem | CONFIRMADO | Cerca de 5,75 €/mês sem IVA. |
| Com IVA | Energia: 0,1711 x 1,06 = **0,181 €/kWh** (primeiros 200 kWh/mês, IVA 6%); acima disso x 1,23 = 0,210. Potência: 0,1917 x 1,06 = **0,203 €/dia**. | [ERSE, tarifa social out 2026](https://www.erse.pt/media/vhajllzh/tarifa-social-eletricidade-out2026.pdf): IVA de 6% nos primeiros 200 kWh e na potência até 3,45 kVA | CONFIRMADO (IVA), derivado (contas) | Acresce o IEC (0,001 €/kWh) e a contribuição audiovisual (1,85 €/mês). |
| Fatura de referência ERSE, 3,45 kVA, 1 900 kWh/ano | 36,82 € (jan 2026), **38,15 €/mês (out 2026)** | [ERSE, comunicado 2026](https://www.erse.pt/media/5dypdjby/comunicado-tarifas-ele_2026.pdf), tarifa social out 2026 | CONFIRMADO | Dá 0,24 €/kWh "tudo incluído" (derivado), porque o termo fixo pesa muito com pouco consumo. |
| Os ~0,198 €/kWh da Repsol | A Repsol cita 0,1979 €/kWh como **preço médio agregado BTN** (jan 2026), não é específico de 3,45 kVA | [Repsol](https://www.repsol.pt/particulares/assessoramento/tarifa-regulada-eletricidade/) | CONFIRMADO (como média BTN) | Conceito diferente do preço marginal. Anterior à subida de outubro. |
| Mercado liberalizado (comercializadores) | Não consegui ler as tabelas (Galp/Endesa) | | NÃO ENCONTRADO | |

**Preço a usar:** **0,18 €/kWh** como preço marginal (regulado, com IVA 6%). Termo de potência 0,20 €/dia. Para o pitch dizer "0,18 €/kWh de energia, mais ~6 €/mês de potência fixa". Os 0,198 € ficam como cenário alto.

## 4. Eficiência de utilização

| Equipamento | Valor | Fonte | Classificação | Nota |
|---|---|---|---|---|
| Esquentador a gás | **80-88%** (valor de ficha). Usar **82%** em uso real. | [Bosch Therm 4600 F: 86%](https://www.bosch-homecomfort.com/ocsmedia/optimized/full/o489079v272_JU_BO_Monofolha_Therm_4600F_2021_4F_pWEB.pdf), [Bosch Therm 4300: 88%](https://www.bosch-homecomfort.com/pt/media/country_pool/documentos/agua-quente/ju_bo_monofolha_therm_4300_2021_4f_pweb.pdf) | PROVÁVEL | Rendimento nominal de fabricante, aparelhos de classe A. Esquentadores antigos são piores (a ADENE avisa, sem valor). Não encontrei o valor oficial da ADENE. |
| Fogão a gás | **~40%** (LBNL 1998). Energy Star indica ~32%. | [ACEEE (cita LBNL/DOE)](https://www.aceee.org/files/proceedings/2014/data/papers/9-702.pdf), [Energy Star](https://www.energystar.gov/about/2021_residential_induction_cooking_tops) | PROVÁVEL | Fontes dos EUA. Intervalo 30-40%. Prefiro 40% para não exagerar a vantagem da indução. |
| Placa de indução | **~85%** (Energy Star). A DOE/EPRI cita 72% noutro teste. | [Energy Star](https://www.energystar.gov/about/2021_residential_induction_cooking_tops), [EEC NZ: 80-90%](https://www.eeca.govt.nz/for-homes/energy-saving-technology/induction-cooktops/) | PROVÁVEL | Usar 80-85%. Resistência elétrica clássica 74-80%. |
| Termoacumulador elétrico (com perdas) | Resistência ~100% para a água, **perdas térmicas de 1,16 a 1,73 kWh/24 h** (Tronic 5501i, 50 a 120 L; 80 L = 1,5 kWh/24 h). Eficiência global **~85%** para 8,4 kWh/dia úteis (derivado: 8,4 / (8,4 + 1,5)). | [Ficha Bosch Tronic 5501i](https://www.bosch-homecomfort.com/ocsmedia/optimized/full/o629179v272_FT_Tronic_5501T_03M_pWEB.pdf) | PROVÁVEL (perdas CONFIRMADAS, % derivada) | Com pouca água quente as perdas pesam mais e a eficiência cai. |

Nota (derivado): com o esquentador a 82%, cada kWh útil emite ~277 g (0,227 / 0,82). O termoacumulador a 85% com a rede a 107 g emite ~126 g por kWh útil. O ponto de equilíbrio da rede fica perto de 235 g/kWh, acima de todos os valores da APA.

## 5. Potências e consumos da casa

| Item | Valor | Fonte | Classificação | Nota |
|---|---|---|---|---|
| Placa de indução, 2-4 zonas, potência nominal | Modelos de 4 zonas: **~7,2 kW** somados (por exemplo Hotpoint HB 4860B NE). Faixa 6 a 7,4 kW. | [Casa dos Eletrodomésticos](https://www.casadoseletrodomesticos.com.br/cooktop-de-inducao-4-bocas-consome-muita-energia-usando-todas-as-zonas-ao-mesmo-tempo) (site brasileiro) | PROVÁVEL | Pico teórico só com todas as zonas no máximo, raro. Muitas placas têm gestão de potência. Não encontrei o limite por defeito para casas de 3,45 kVA. |
| Placa de indução, uso normal | Não encontrei medição publicada. **1,8 kW** (1 zona, ou 2 em baixa) é plausível. | doc. DuoWatt da equipa | NÃO ENCONTRADO (fonte) | Pico realista com 2 zonas altas: ~3 kW (suposição minha). Marcar como pressuposto no pitch. |
| Consumo médio de eletricidade por alojamento | **0,289 tep/alojamento = 3 361 kWh/ano = ~280 kWh/mês** (2020). Potência média: 0,39 kW (derivado). | [INE/DGEG/ADENE, ICESD 2020](https://www.ine.pt/ngt_server/attachfileu.jsp?look_parentBoui=527966984&att_display=n&att_download=y), figura 18; conversão 1 tep = 11 630 kWh minha | CONFIRMADO (tep), derivado (kWh) | O Polígrafo chegou ao mesmo valor. Dados de 2020. Casas com 3,45 kVA consomem menos: o exemplo da ERSE é 1 900 kWh/ano = 158 kWh/mês. |
| Consumo base da casa (~0,6 kW) | Não encontrei valor publicado de consumo base de uma casa portuguesa | | NÃO ENCONTRADO | 0,6 kW é razoável como carga simultânea ao fim da tarde (frigorífico, iluminação, TV, router), acima da média de 0,39 kW. Manter como pressuposto. |

## 6. Garrafas de 13 kg por ano

| Item | Valor | Fonte | Classificação | Nota |
|---|---|---|---|---|
| GPL garrafa por alojamento (2020) | **0,158 tep/alojamento** e 264 €/alojamento (Portugal). 355 260 tep no total. | [INE ICESD 2020](https://www.ine.pt/ngt_server/attachfileu.jsp?look_parentBoui=527966984&att_display=n&att_download=y), figuras 17-18 | CONFIRMADO | Média por alojamento que usa GPL garrafa, para todos os usos (cozinha e água quente). |
| Conversão para garrafas | 0,158 tep = 1 838 kWh = ~144 kg de GPL = **~11 garrafas de 13 kg/ano** | derivado (PCI 46 MJ/kg) | PROVÁVEL | Assume só garrafas de 13 kg. Com 2,9 kg CO2/kg dá ~417 kg CO2/ano, o que bate com o ">400 kg" do enunciado. |
| Cenário DECO | 1 garrafa por mês = 12/ano = 293 € | [Notícias ao Minuto/DECO](https://www.noticiasaominuto.com/economia/2023787/preco-da-botija-de-gas-deco-aponta-4-solucoes-que-podem-ser-adotadas) | PROVÁVEL | Cenário ilustrativo, não média medida. |

Validação: o "cerca de 10-11 garrafas" fica **validado** por uma via independente (INE). Dizer "~11 garrafas/ano (INE 2020)". Dado de 2020.

## 7. Produtos Bosch com controlo externo / ligação a gestor de energia

| Produto | O que a documentação oficial diz | Fonte | Classificação | Nota |
|---|---|---|---|---|
| Tronic 5501i T (50 a 120 L) | Wi-Fi integrado, app HomeCom Easy (smartphone), 4 modos (Smart, Eco, manual, programado). "Smart" aprende hábitos de consumo. **Potência 1 500 W em todos os tamanhos**, 6,5 A, 230 V. | [Página Bosch PT](https://www.bosch-homecomfort.com/pt/pt/ocs/tronic-5501i-t-21962100-p/), [ficha técnica 04.2026](https://www.bosch-homecomfort.com/ocsmedia/optimized/full/o629179v272_FT_Tronic_5501T_03M_pWEB.pdf) | CONFIRMADO (Wi-Fi/app/modos) | **Não aparece** entrada de controlo externo, limitação de potência, gestor de energia, fotovoltaico ou SG Ready. Controlo só pela app da Bosch. |
| Controlo externo / gestor de energia no Tronic 5501i | Não encontrado | | NÃO ENCONTRADO | |
| Tronic 4001 T | 1 500 W (50 e 70 L) e **2 000 W (80, 100 e 120 L)**, 8,7 A. Função Smart. | [Ficha Tronic 4001 T](https://www.bosch-homecomfort.com/pt/media/country_pool/documentos/agua-quente/ft_aqs_tronic_4001_t_pweb_0926.pdf) | CONFIRMADO | Sem controlo externo na ficha. O Tronic 4000 T de 80 L a 2 000 W (do doc. atual) não o consegui reabrir. |
| Bosch Energy Manager | Existe, mas é para **bombas de calor** com fotovoltaico Fronius, ajusta a potência ao excedente solar. Página suíça/italiana, não portuguesa. | [Bosch CH](https://www.bosch-homecomfort.com/ch/it/residenziale/assistenza-e-manutenzione/apps/energy-manager/) | PROVÁVEL | Não cobre termoacumuladores elétricos. |
| Compress 5000/5001 DW (bomba de calor de AQS) | Páginas de outros países falam de ligação a fotovoltaico (inversor, sinal 230 V ou 5 V). Não confirmei na versão portuguesa. | [Bosch SI](https://www.bosch-homecomfort.com/si/sl/ocs/stanovanjski/compress-5000-dw-19617098-p/), [Bosch ES](https://www.bosch-homecomfort.com/es/es/ocs/compress-5001-dw-w-22039028-p/) | PROVÁVEL | Produto diferente de um termoacumulador. |

**Para o pitch:** não afirmar que o Tronic "se liga ao gestor". Dizer que o DuoWatt **pausa a alimentação do circuito** (por exemplo, com um relé) e que a Bosch tem Wi-Fi e app própria, mas sem interface documentada de gestão de energia (para o Tronic). A ligação à Bosch fica como trabalho futuro com a Bosch Home Comfort Portugal.

## 8. Bosch Heatpump Advisor

| Item | Valor | Fonte | Classificação | Nota |
|---|---|---|---|---|
| O que é | Simulador em 3 passos que recomenda a bomba de calor Bosch mais adequada, com dados de consumo, custos de funcionamento e nível sonoro. Gera relatório PDF e permite guardar projetos. | [Bosch PT, Heatpump advisor (páginas de bombas de calor)](https://www.bosch-homecomfort.com/pt/pt/conhecimentos/aerotermia/bomba-de-calor-casa/), [Bosch ES, comunicado](https://www.bosch-homecomfort.com/es/es/sobre-junkers-bosch/prensa/novedades-de-comunicacion/asesor-de-bombas-de-calor/) | CONFIRMADO | Descrição do comunicado em espanhol e das páginas portuguesas. A ferramenta em si é interativa e não a pude usar. |
| Entradas | Código postal (clima automático) e necessidades de aquecimento e de água quente (a partir do consumo do ano anterior e valores-padrão). **Não menciona potência contratada nem capacidade elétrica da casa.** | comunicado ES | PROVÁVEL | Falta confirmar abrindo a ferramenta. |
| Cobre termoacumuladores? | A descrição fala de bombas de calor como sistema de climatização. Não menciona termoacumuladores elétricos. | idem | NÃO ENCONTRADO (confirmação) | Conclusão provável: **não cobre** termoacumuladores. |

Consequência para o desafio: o DuoWatt cobre uma lacuna que o Advisor não aborda (limite elétrico da casa, 3,45 kVA). Isto é interpretação minha, a confirmar abrindo a ferramenta.

---

## Valores recomendados para o simulador

- Potência contratada: 3,45 kVA (= 3 450 W com fator de potência 1, pressuposto).
- Termoacumulador: **2 000 W** (Tronic 4001 T de 80 L ou mais). Atenção: o Tronic 5501i T é de **1 500 W** em todos os tamanhos. Escolher o modelo e manter o número coerente.
- Placa de indução: 1,8 kW em uso normal (pressuposto), pico realista 3 kW com duas zonas altas (pressuposto). Nominal da placa de 4 zonas: ~7,2 kW.
- Consumo base: 0,6 kW (pressuposto, sem fonte). Média real de uma casa: ~0,39 kW (INE 2020, 280 kWh/mês).
- Consumo médio mensal: 280 kWh/mês (INE 2020). Exemplo regulado da ERSE para 3,45 kVA: 158 kWh/mês.
- Fator de CO2 da eletricidade: **107 g/kWh** (APA, 2023). Intervalo 40 a 167 g. Mostrar sempre o cenário de 167 g.
- Fator de CO2 do GPL: 2,9 kg CO2/kg = 0,227 kg CO2/kWh (63 tCO2/TJ, valor de comercializadores a citar a DGEG, não reverificado).
- Garrafa 13 kg: **37 €** (último preço anunciado, ERSE out 2026: 36,87 €). Cenário alto 42 a 43,55 €. Sem teto legal em vigor (o de 29,47 € foi de 2022).
- Garrafas por ano: ~11 (INE 2020, derivado).
- Eletricidade: **0,18 €/kWh** (0,1711 sem IVA, IVA 6%). Termo de potência 0,20 €/dia com IVA (0,1917 sem IVA).
- Eficiências: esquentador 82%, fogão a gás 40%, indução 85%, termoacumulador ~85% (perdas de 1,5 kWh/24 h para 80 L).
- Água quente: 40 L/pessoa/dia (Repsol e Bosch, do doc. atual; a ADENE usa 50 L, não reverificado).

## O que não consegui confirmar

1. O valor de ~40 g/kWh da APREN: os boletins dão ~59 g. Não confirmei o de 119 g da Electricity Maps (não reabri a página).
2. Edição da APA com dados de 2024 (não encontrei, só a de 2025 com dados até 2023).
3. Teto de preço da garrafa em 2026: não encontrei nenhum. O preço de novembro de 2026 só aparece no relatório da ERSE de dezembro.
4. Preços de comercializadores do mercado liberalizado (tabelas ilegíveis).
5. Consumo base da casa (0,6 kW) e potência de uso normal da placa de indução: sem medições publicadas.
6. Controlo externo ou limitação de potência no Tronic 5501i T (e outros Tronic): não consta na documentação oficial portuguesa que li. Perguntar à Bosch Home Comfort Portugal.
7. Se o Heatpump Advisor pergunta a potência contratada e se cobre termoacumuladores: só li descrições, não usei a ferramenta.
8. Potência de 2 000 W do Tronic 4000 T de 80 L (não reabri a ficha). Está confirmada para o Tronic 4001 T.
9. Rendimento oficial (ADENE) do esquentador: o site da ADENE não respondeu. Usei valores de fichas da Bosch.
10. Dados de 2020 (INE) para consumo de eletricidade e GPL: podem estar desatualizados em 2026.

---

## 9. Pressupostos do kit (conceito atual, 21 nov 2026)

Todos classificados como **PRESSUPOSTO** (sem fonte de medição; a validar num piloto com a Bosch), exceto o que é dito.

| Item | Valor | Classificação | Nota |
|---|---|---|---|
| Consumo base da casa | 0,6 kW | PRESSUPOSTO | Média real ~0,39 kW (INE 2020); 0,6 kW é ao fim da tarde, sem medições publicadas |
| Máquina da roupa | 2 kW durante ~20 min (fase de aquecimento) | PRESSUPOSTO | Sem fonte de medição |
| Cilindro Tronic 5501i | 1,5 kW | CONFIRMADO (ficha Bosch PT, ver §5) | Total do cenário ≈ 4,1 kW > 3,45 kVA |
| Desligar o cilindro | consumo ≥ ~90 % do limite | PRESSUPOSTO | Regra de controlo escolhida |
| Religar o cilindro | consumo < ~80 % do limite | PRESSUPOSTO | Histerese |
| Pausa máxima | 30 min seguidos | PRESSUPOSTO | Prioridade à água quente |
| Perda de sinal do sensor | > 5 s: volta a `NORMAL` | PRESSUPOSTO | Modo seguro |
| Tempo de reação do contador inteligente | não conhecido | PRESSUPOSTO | A medir no piloto; EN 60898 dá segundos a minutos de tolerância |

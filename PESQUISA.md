# PESQUISA: itens por confirmar (CONTEXTO_Projeto_DuoWatt.md §6)

Data: 21 nov 2026. Responsável: Investigador (haiku). Só pesquisa; nenhum código foi alterado.

Legenda de classificação: **confirmado** (lido no documento oficial), **provável** (proxy ou dado parcial), **derivado** (conta feita sobre valores de uma fonte), **não encontrado**.

---

## 1. Distribuição dos clientes domésticos por potência contratada (Portugal)

**Lacuna principal:** nenhuma fonte isola os clientes **domésticos** por escalão de potência. Os valores abaixo são para o total de clientes BTN (inclui não domésticos) e servem de proxy.

### 1a. E-REDES, Perfis de consumo 2025 (população BTN 2023, Portugal Continental)
- Fonte: https://e-redes.pt/sites/eredes/files/2024-12/Documento%20Justificativo%20dos%20Perfis%20de%20Consumo%20e%20Inje%C3%A7%C3%A3o%202025.pdf (Relatório final, dez. 2024; Tabela 1, p. 6)
- Ano da fonte: 2024 (publicação); população de 2023.
- Domésticos = 88,5% dos locais BTN (5 568 033 de 6 294 032). Classes de potência do total BTN:
  - <3,45 kVA: **44,1%**
  - ≥3,45 a ≤6,95 kVA: **41,9%** (inclui 4,6, 5,75 e 6,9 sem separação)
  - =10,35 kVA: **6,6%**
  - =13,80 kVA: **2,6%**
  - ≥17,25 kVA: **4,7%**
- Classificação: **confirmado** para o total BTN; **provável** como proxy do doméstico (não separado).

### 1b. ERSE, Caracterização da procura de energia elétrica em 2026 (Quadros 7-4 e 9-7)
- Fonte: https://www.erse.pt/media/5zclblrg/caracteriza%C3%A7%C3%A3o-procura-se-2026.pdf (dez. 2025)
- Ano da fonte: publicação dez. 2025; ano de referência dos dados não confirmado.
- Contagens de clientes (n.º) por potência, somando tarifas simples, bi-horária e tri-horária. Percentagens **derivado** destas contagens.
- Mercado regulado, BTN ≤20,7 kVA (Quadro 7-4 + ≤2,3 kVA; total ≈766 639 clientes):
  - ≤3,45 kVA: **48,5%** (1,15/2,30 kVA: 12,4%; 3,45 kVA: 36,2%)
  - 4,6 kVA: **9,0%**
  - 5,75 kVA: **4,8%**
  - 6,9 kVA: **25,7%**
  - 10,35 kVA e acima: **11,9%** (10,35: 5,9%; 13,8: 2,4%; 17,25: 0,8%; 20,7: 2,8%)
- Mercado liberalizado, BTN ≤20,7 kVA (Quadro 9-7; total ≈5,40 M clientes):
  - ≤3,45 kVA: **41,1%**
  - 4,6 kVA: **10,1%**
  - 5,75 kVA: **5,4%**
  - 6,9 kVA: **29,7%**
  - 10,35 kVA e acima: **13,8%**
- Classificação: **derivado** (contas sobre contagens confirmadas). Inclui não domésticos; **provável** como proxy.

### Conclusão 1
A percentagem de contratos domésticos com ≤3,45 kVA não foi encontrada de forma isolada. O proxy mais próximo é ~41–49% (BTN total), com 6,9 kVA a ~26–30%. Para o número exato do doméstico seria preciso pedir os dados à ERSE ou à E-REDES.

---

## 2. Potência contratada das casas com GPL em garrafa

- **Não encontrado.** Nenhuma fonte cruza GPL em garrafa com potência contratada de eletricidade.
- Contexto (confirmado): ICESD 2020 indica que **52,5%** dos alojamentos usam GPL em garrafa (Continente 51,2%; RAA 90,0%; RAM 71,7%).
  - Fonte: https://www.ine.pt/ngt_server/attachfileu.jsp?look_parentBoui=527966984&att_display=n&att_download=y (ICESD 2020, PDF; página de publicação: https://www.ine.pt/xurl/pub/48433981)
  - Ano da fonte: 2020 (inquérito); publicado 2021.
- Os quadros Excel do ICESD 2020 ainda não foram verificados; podem ter cruzamentos adicionais.

---

## 3. Termoacumulador elétrico vs. esquentador a gás (água quente)

- Fonte: ICESD 2020 (INE/DGEG/ADENE), secção 2.4.3 "Aquecimento de Águas" e Figura 40 / tabela de equipamentos. Link: https://www.ine.pt/ngt_server/attachfileu.jsp?look_parentBoui=527966984&att_display=n&att_download=y
- Ano da fonte: 2020 (publicado 2021).
- Percentagem de alojamentos que usam cada equipamento (Portugal, base: 4 270 311 alojamentos; um alojamento pode ter mais de um equipamento):
  - **Esquentador: 67,3%** (Continente 67,0%; RAA 88,3%; RAM 60,2%)
  - **Termoacumulador: 16,7%** (Continente 16,5%; RAA 8,3%; RAM 33,0%)
  - Caldeira: 16,7%
  - Sistema solar térmico: 8,0%
  - Bomba de calor: 0,8%
  - Outro: 0,9%
- Em 2010 (ICESD 2010): esquentador 78,6%, termoacumulador 11,2%.
- Classificação: **confirmado**.

---

## 4. Custo do termo de potência: 3,45 kVA vs. 6,9 kVA (tarifas reguladas ERSE 2026)

- Fonte: ERSE, Diretiva n.º 4/2026 (primeira alteração à Diretiva 1/2026; a vigorar a partir de 1 de outubro de 2026). Link: https://www.erse.pt/media/hjab13zj/diretiva-erse-4-2026-ajuste-tenergia-se-4t2026.pdf
- Ano da fonte: 2026.
- Tarifa transitória de Venda a Clientes Finais (CUR), **Continente**, BTN ≤20,7 kVA e >2,3 kVA, tarifa simples, bi-horária e tri-horária:
  - 3,45 kVA: **0,1917 €/dia**
  - 6,9 kVA: **0,3659 €/dia**
  - Classificação: **confirmado** (valor no documento).
- Diferença (3,45 → 6,9 kVA): 0,1742 €/dia, ou seja **~63,6 €/ano sem IVA** (derivado: 0,1742 × 365).
- Outras regiões (mesma diretiva): RAA 0,1929 / 0,3665 €/dia; RAM 0,1919 / 0,3648 €/dia.
- Notas:
  - Este é o preço de venda (CUR) da parte de potência. O termo de potência de **acesso às redes** (TAR, ERSE) não foi encontrado.
  - Os valores das faturas-tipo e das notícias (ex.: 37,77 €/mês para 3,45 kVA) são faturas completas, não o termo. Não foram usados.
  - Os valores de out. 2026 (tarifa de 0,1083 €/dia para 3,45 kVA) são tarifa social com desconto. Não se usam.
  - O comunicado ERSE de tarifas 2026 não foi lido (PDF ilegível pela ferramenta); a diretiva é a fonte usada.

---

## Lacunas e pontos a verificar
1. Percentagem exata de **clientes domésticos** por potência (incl. 4,6, 5,75 e 10,35 separados): não encontrada. Pedir à ERSE ou E-REDES.
2. Estatística GPL × potência contratada: não encontrada.
3. Termo de potência de **acesso** (TAR) para 3,45 e 6,9 kVA: não encontrado; só o CUR.
4. Quadros Excel do ICESD 2020 não consultados.
5. O relatório de perfis E-REDES usa população 2023; a data de referência do relatório ERSE 2026 não está explícita.


## Custos para a viabilidade do DuoWatt

Data da pesquisa: 21 nov 2026. Preços em € com IVA quando a fonte o indica. Nenhuma página indica a sua data de publicação; a "data" de cada valor é a data de consulta (21 nov 2026). Os valores vêm de resultados de pesquisa; o WebFetch à Leroy Merlin devolveu 403, por isso as páginas não foram lidas na íntegra.

### 1. Contactor bipolar 25 A para o termoacumulador
- **Hager ESC225** (25 A, 2 NA, 230 V, 1 módulo): **49,78 €**. Fonte: https://hager.com/pt/catalogo/produto/esc225-contactor-25a-2na-230v-1m . Classificação: **provável** (preço de catálogo do fabricante; a pesquisa não confirma se inclui IVA).
- Leroy Merlin PT e Worten: **não encontrado** (a Leroy Merlin só mostrou fichas sem preço nos resultados; a Worten não devolveu resultados).
- Referência fora de Portugal, não usar como preço PT: Legrand 2F 25 A a 78,90 € na Castorama FR (https://www.castorama.fr/contacteur-de-puissance-bipolaire-2f-25a-230v-legrand/3245060927028_CAFR.prd).

### 2. Medidor de energia com pinça (CT) para o quadro
- **Shelly Pro EM 50** (monofásico, calha DIN, Wi-Fi, 2 canais de 50 A): **101,88 €** com IVA, Domadoo (versão PT). Fonte: https://www.domadoo.fr/pt/domotica-energia/6804-contador-de-energia-monofasico-em-calha-din-shelly-pro-em-50a-wi-fi-shelly-3800235268148.html . Classificação: **confirmado** (preço com IVA indicado na página).
- PcComponentes PT: **104,43 €**. Fonte: https://www.pccomponentes.pt/rele-wi-fi-shelly-pro-em-50a-monitorizacao-de-energia-controle-din . Classificação: **provável** (IVA não explícito).
- Smartify.pt (101,00 com símbolo de dólar): não usado, moeda não confirmada.
- Shelly EM, Eastron e outras marcas: não pesquisados.

### 3. Controlador com Wi-Fi (Shelly Pro 2PM)
- **Shelly Pro 2PM** (2 canais, relé 16 A, medição de energia, calha DIN, Wi-Fi): **69,99 €** com IVA, Powerplanet PT (PVP recomendado indicado: 89,99 €). Fonte: https://www.powerplanetonline.com/pt/shelly-pro-2pm-preto . Classificação: **confirmado** (a página indica IVA incluído).
- PcComponentes PT: **82,99 €**. Fonte: https://www.pccomponentes.pt/rele-wi-fi-shelly-pro-2pm-controle-de-persianas-e-iluminacao-monitorizacao-de-energia-embutido-din . Classificação: **provável** (IVA não explícito).
- Nota (derivado): 2 kW a 230 V dá cerca de 8,7 A, dentro dos 16 A do relé do Shelly.
- ESP32: não pesquisado.

### 4. Eletricista certificado (2026)
- Hora de mão de obra: **~30 €/h** (Habitissimo; a Zaask indica 10 a 40 €/h). Fontes: https://www.habitissimo.pt/orcamentos/instalar-quadro-eletrico e https://www.zaask.pt/quanto-custa/electricistas . Classificação: **provável** (estimativas de plataformas de orçamentos, não tarifas oficiais).
- Substituição ou instalação de quadro: **150 a 400 €** (Zaask, https://www.zaask.pt/quanto-custa/substituir-um-quadro-electrico); **250 a 600 €** (expert-zoom, https://expert-zoom.com/pt/revista/servicos-para-casa/eletricista-residencial ); média de 250 € (Habitissimo). Classificação: **provável**.
- Materiais não incluídos no preço do serviço (Worten, https://www.worten.pt/servicos-worten-resolve/servicos-para-casa/eletricidade/instalacao-eletrica ).
- Certificação do eletricista (registo DGEG): não pesquisado.

### 5. Aumento de potência 3,45 para 6,9 kVA
- Diferença do termo de potência (CUR, tarifa de venda, Continente): 0,1917 para 0,3659 €/dia (valores já registados acima, **confirmado**). Diferença de 0,1742 €/dia = **63,58 €/ano sem IVA** (**derivado**). Com IVA de 23%: **~78,2 €/ano** (**derivado**; a taxa de IVA aplicável ao termo de potência não foi verificada).
- Termo de acesso (TAR, ERSE): **não encontrado** (lacuna já registada).
- Taxa da E-REDES pelo pedido de alteração: **não encontrado**. Não há tabela oficial nos resultados.
- Se a instalação já suportar 6,9 kVA, a alteração pedida ao comercializador costuma ser sem custos (fonte de terceiros, https://lojaluz.com/gestoes/alterar-potencia/mudar-potencia-contratada ). Classificação: **provável**.
- Se for preciso reforço do ramal: o custo depende do orçamento da E-REDES, **não encontrado**. Há um relato isolado de cerca de 1 000 € (https://portaldaqueixa.com/brands/e-redes/complaints/e-redes-pedido-de-aumento-de-potencia-sem-resolucao-e-com-despesas-acumuladas-162586126 ). Anedótico; não usar como média.
- ERSE: um resumo de pesquisa (PDF não lido) indica poupança de 20 a 30 €/ano por escalão de potência descido, em documento de jan. 2025 (https://www.erse.pt/media/o5admnus/custo-pot%C3%AAncia-contratada_jan2025.pdf ). Classificação: **provável** (2025, não verificado no PDF). Simulador de preços: https://simulador.precos.erse.pt/ .

### 6. Termoacumulador Bosch Tronic 4000 T 80 L
- Existência: o modelo de 80 L existe em PT (50, 80 e 100 L). Fonte: catálogo Bosch abr. 2026, https://www.bosch-homecomfort.com/pt/media/country_pool/documentos/catalogo_cons_termoacumuladores_abr2026_web.pdf . Classificação: **confirmado**.
- **Leroy Merlin PT: 245 €**. Fonte: https://www.leroymerlin.pt/produtos/termoacumulador-bosch-tronic-tr-4000t-80l-84801328.html . Classificação: **provável** (a ficha indica 75 L no campo capacidade e 80 L no título; IVA não indicado).
- PcComponentes PT: **255,07 €** (80 L, 2000 W, vertical; desconto de 17% sobre 307,73 €). Fonte: https://www.pccomponentes.pt/termoacumulador-eletrico-bosch-80-l-2000-w-vertical . Classificação: **provável** (modelo exato 4000 T não confirmado).
- Worten: **não encontrado** (a categoria de 80 L não devolveu resultados).

### Resumo derivado (com IVA, valores das lojas)
- Material do controlo: contactor 49,78 + Shelly Pro 2PM 69,99 + Shelly Pro EM 50 101,88 = **221,65 €** (**derivado**).
- Com instalação de pequeno quadro (150 a 400 €, Zaask): **~372 a 622 €** (**derivado**), sem termoacumulador.
- Custo anual evitado do aumento de potência: **~78 €/ano** (**derivado**), sem TAR nem taxa E-REDES.

### Lacunas
1. Preço do contactor na Leroy Merlin PT e na Worten: não encontrado.
2. IVA não confirmado nos preços da Hager e da PcComponentes.
3. Taxa da E-REDES para alteração de potência e orçamento de reforço: não encontrado.
4. Termo de acesso (TAR) para 3,45 e 6,9 kVA: não encontrado (lacuna já registada).
5. Não pesquisados: ESP32, Shelly EM, Eastron e certificação do eletricista (DGEG).
6. Nenhuma fonte de preço indica a data de publicação.

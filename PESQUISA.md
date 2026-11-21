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

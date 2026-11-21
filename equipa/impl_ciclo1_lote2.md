# Implementação ciclo 1, lote 2 (I4, I5)

I5 (impacto.py, testes): comentário corrigido (0,171 € sem IVA; 0,21 € com IVA 23 %); ValueError se efic_gas ou efic_eletrica <= 0; `test_comentario_impacto_nao_mistura_iva` passou a normal; teste de entradas inválidas agora espera ValueError. Os 4 xfail restantes ficam com motivo "depende de decisão" (pessoas vs garrafas, base ao serão 600 W, 8 pessoas em regime estacionário, perdas em repouso). Nenhum valor ou fórmula alterado; sem propostas novas.

I4 (app.py): garrafas máx. 20; 0 garrafas mostra "Sem gás a substituir: sem impacto de CO2" (métrica e secção); frase de atribuição por veredicto (aguenta / aguenta com gestão) e nota de que o CO2 vem da eletrificação; aviso "Com este depósito falta água quente: aumentar o depósito" para "reserva de água insuficiente"; extrapolação renomeada "Potencial da eletrificação (não atribuído ao DuoWatt), cenário ilustrativo". Avisos honestos intactos.

Verificação: pytest 32 passed, 4 xfailed; capturar.py ciclo1b: "sem erros nem avisos".

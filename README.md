# DuoWatt · app de demonstração (Simulação)

Web app do **modo ligado** do DuoWatt e demonstração ao vivo do pitch (Hackathon@ShiftE 2026). Tudo o que mostra é uma **simulação**; os dados do histórico e do consumo são **dados de exemplo**.

O DuoWatt é um kit de duas peças (sensor no quadro + ficha inteligente no cilindro) que pausa o cilindro antes de a luz ir abaixo. A promessa é só esta: **o cilindro nunca é a causa do apagão.** Se a casa passa o limite sem o cilindro, o DuoWatt não resolve.

## Como correr
```
npm i
npm run dev       # desenvolvimento
npm run build && npm run preview   # versão final, funciona sem internet
npm test          # testes da lógica
```

## Atalhos (ecrã ≥ 1024 px) e parâmetros de URL
`Espaço` reproduzir/pausar · `R` recomeçar · `D` com/sem DuoWatt · `1`–`4` separadores · `?` ajuda.
`?modo=com|sem` · `?autoplay=1` · `?tab=agora|historico|poupanca|definicoes`

## Como usar no pitch
1. Abrir a app num ecrã largo (1280×720 ou mais) e carregar em `Espaço`.
2. Deixar correr o serão (30–40 s); cada legenda fica visível pelo menos 2,5 s.
3. Às 19:05 mostrar o pico e a pausa; às 19:25 a retoma.
4. Carregar em `D` para ver o mesmo serão sem DuoWatt (apagão às 19:12).
5. O júri abre o QR no telemóvel: aparece o modo telemóvel, com botão «Ver o serão (simulação)». Vídeo de reserva em `entregaveis/`.

## Honestidade
«Simulação» sempre visível; o sensor mede a casa toda e não sabe que aparelho ligou; a app não mostra temperatura da água; estimativas com «≈»; dados de exemplo identificados; sem marca nem identidade visual da Bosch. Detalhe em `PRODUCT.md`.

## Factos usados (`src/data/facts.ts`)
| Facto | Valor | Tipo | Fonte |
|---|---|---|---|
| Potência contratada | 3,45 kVA (≈ 15 A) | Derivado | 3 450 VA ÷ 230 V |
| Pausa | 90 % do limite | Regra do produto | Equipa DuoWatt |
| Retoma | corrente + cilindro < 80 % | Regra do produto | Equipa DuoWatt |
| Pausa mínima / máxima | 1 min / 30 min | Proposta / Regra | Equipa DuoWatt |
| Reação | < 1 s | Meta | Equipa DuoWatt |
| Cilindro (exemplo) | ≈ 1,55 kW (6,75 A) | Exemplo | Cenário do pitch |
| Garrafas de gás evitadas | ≈ 1/mês | Estimativa | Pressuposto da equipa |
| CO₂ evitado | ≈ 20 kg/mês (prudente ≈ 11) | Estimativa | Cálculo da equipa |
| Potência que não foi preciso subir | ≈ 5 €/mês | Estimativa | Tarifas ERSE 2026 |
| Horas baratas | até ≈ 4 €/mês | Limite superior | 557 kWh × 0,0902 € (Costa et al., 2026) |

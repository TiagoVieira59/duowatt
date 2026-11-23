export type Tipo = 'Derivado' | 'Regra do produto' | 'Proposta' | 'Meta' | 'Exemplo' | 'Estimativa' | 'Limite superior'
export interface Fact { valor: number; texto: string; tipo: Tipo; fonte: string }

const f = (valor: number, texto: string, tipo: Tipo, fonte: string): Fact => ({ valor, texto, tipo, fonte })

export const FACTS = {
  potencia: f(3.45, '3,45 kVA (≈ 15 A a 230 V)', 'Derivado', '3 450 VA ÷ 230 V'),
  limiteA: f(15, '15 A', 'Derivado', '3 450 VA ÷ 230 V'),
  pausaPct: f(90, '90 % do limite (13,5 A)', 'Regra do produto', 'Equipa DuoWatt'),
  retomaPct: f(80, 'corrente + cilindro < 80 % (12 A)', 'Regra do produto', 'Equipa DuoWatt'),
  pausaMinMin: f(1, '1 min', 'Proposta', 'Equipa DuoWatt'),
  pausaMaxMin: f(30, '30 min', 'Regra do produto', 'Equipa DuoWatt'),
  reacaoS: f(1, '< 1 s', 'Meta', 'Equipa DuoWatt'),
  cilindroA: f(6.75, '≈ 1,55 kW (6,75 A)', 'Exemplo', 'Cenário do pitch'),
  reacaoSimS: f(0.4, '0,4 s (simulado)', 'Exemplo', 'Valor simulado do cenário'),
  garrafas: f(1, '≈ 1 por mês (12 por ano)', 'Estimativa', 'Pressuposto da equipa'),
  co2: f(20, '≈ 20 kg/mês (prudente ≈ 11 kg/mês)', 'Estimativa', '246 kg/ano e 131 kg/ano, cálculo da equipa'),
  co2Prudente: f(11, '≈ 11 kg/mês', 'Estimativa', '131 kg/ano, cálculo da equipa'),
  potenciaPoupanca: f(5, '≈ 5 €/mês (≈ 64 €/ano, sem IVA)', 'Estimativa', 'Tarifas ERSE 2026, cenário tarifário'),
  horasBaratas: f(4, 'até ≈ 4 €/mês (≈ 50 €/ano)', 'Limite superior', '557 kWh × 0,0902 € (Costa et al., 2026); só com tarifa bi-horária'),
} as const

export const LIMITE_A = FACTS.limiteA.valor
export const CILINDRO_A = FACTS.cilindroA.valor
export const PAUSA_A = LIMITE_A * FACTS.pausaPct.valor / 100 // 13.5
export const RETOMA_A = LIMITE_A * FACTS.retomaPct.valor / 100 // 12
export const PAUSA_MIN = FACTS.pausaMinMin.valor
export const PAUSA_MAX = FACTS.pausaMaxMin.valor
export const SILENCIO_RADIO_S = 5

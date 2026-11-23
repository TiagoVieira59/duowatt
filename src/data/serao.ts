import { CILINDRO_A } from './facts'

export const hm = (h: number, m: number) => h * 60 + m
export const INICIO = hm(18, 30)
export const FIM = hm(21, 0)
export const BASE_A = 3.0
export const CILINDRO_INICIO = hm(18, 40)
export const CILINDRO_FIM = hm(20, 15) // thermostat
export const APARELHO_INICIO = hm(19, 5)
export const APARELHO_PESADO_FIM = hm(19, 25) // last heavy sample is 19:24
export const APARELHO_FIM = hm(19, 50)
export const APARELHO_PESADO_A = 8.1
export const APARELHO_LEVE_A = 0.5
export const APAGAO_APOS_MIN = 7 // illustrative: 19:05 → 19:12

export { CILINDRO_A }

export function aparelhoA(t: number): number {
  if (t < APARELHO_INICIO || t >= APARELHO_FIM) return 0
  return t < APARELHO_PESADO_FIM ? APARELHO_PESADO_A : APARELHO_LEVE_A
}
export const aquecer = (t: number) => t >= CILINDRO_INICIO && t < CILINDRO_FIM

export const fmtHora = (t: number) => {
  const m = Math.floor(t)
  return `${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`
}

import { CILINDRO_A, LIMITE_A } from '../data/facts'
import { APAGAO_APOS_MIN, BASE_A, FIM, INICIO, aparelhoA, aquecer, APARELHO_INICIO, CILINDRO_INICIO, CILINDRO_FIM } from '../data/serao'
import { ControllerState, decide, initialState } from './controller'

export type Modo = 'com' | 'sem'
export type Cilindro = 'aquecer' | 'pausa' | 'parado'
export interface Ponto { t: number; amps: number; pct: number; cilindro: Cilindro; apagao: boolean }
export type EventoTipo = 'inicio' | 'cilindro' | 'pico' | 'pausa' | 'retoma' | 'fim-aquecer' | 'apagao' | 'fim'
export interface Evento { t: number; tipo: EventoTipo; texto: string }
export interface Resultado { serie: Ponto[]; eventos: Evento[]; fimT: number }

export function simular(modo: Modo): Resultado {
  const serie: Ponto[] = []
  const eventos: Evento[] = [{ t: INICIO, tipo: 'inicio', texto: 'Início do serão' }]
  let st: ControllerState = initialState
  let permitido = true // controller allows the cylinder
  let acima = 0
  let fimT = FIM

  for (let t = INICIO; t <= FIM; t++) {
    const quer = aquecer(t)
    const cil = quer && permitido ? CILINDRO_A : 0
    const amps = BASE_A + aparelhoA(t) + cil
    const pct = (amps / LIMITE_A) * 100
    let cilindro: Cilindro = !quer ? 'parado' : permitido ? 'aquecer' : 'pausa'
    if (t === CILINDRO_INICIO) eventos.push({ t, tipo: 'cilindro', texto: 'O cilindro começou a aquecer' })
    if (t === APARELHO_INICIO) eventos.push({ t, tipo: 'pico', texto: 'Um aparelho grande ligou' })

    if (modo === 'com') {
      if (quer) {
        const d = decide(st, amps, t)
        st = d.state
        if (d.cylinderOn !== permitido) {
          permitido = d.cylinderOn
          eventos.push(permitido
            ? { t, tipo: 'retoma', texto: 'O cilindro voltou a ligar' }
            : { t, tipo: 'pausa', texto: 'Pausa: um aparelho grande ligou' })
        }
      }
    } else {
      acima = pct > 100 ? acima + 1 : 0
      if (acima > APAGAO_APOS_MIN) {
        serie.push({ t, amps, pct, cilindro, apagao: true })
        eventos.push({ t, tipo: 'apagao', texto: 'A luz foi abaixo' })
        fimT = t
        return { serie, eventos, fimT }
      }
    }
    if (t === CILINDRO_FIM && quer === false) eventos.push({ t, tipo: 'fim-aquecer', texto: 'O cilindro terminou de aquecer' })
    if (cilindro === 'pausa' && !quer) cilindro = 'parado'
    serie.push({ t, amps, pct, cilindro, apagao: false })
  }
  eventos.push({ t: FIM, tipo: 'fim', texto: 'Fim do serão' })
  return { serie, eventos, fimT }
}


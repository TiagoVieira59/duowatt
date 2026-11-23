import { PAUSA_A, PAUSA_MAX, PAUSA_MIN, RETOMA_A, CILINDRO_A, SILENCIO_RADIO_S } from '../data/facts'

export interface ControllerState { pausedSince: number | null }
export type Reason = 'normal' | 'pausa-limite' | 'pausa-mantida' | 'retoma-margem' | 'retoma-maximo' | 'modo-seguro'
export interface Decision { cylinderOn: boolean; reason: Reason; state: ControllerState }

export const initialState: ControllerState = { pausedSince: null }

/** readingAmps: whole-house current as measured now; nowMin: minutes; radioSilenceS: seconds without radio signal. */
export function decide(state: ControllerState, readingAmps: number, nowMin: number, radioSilenceS = 0): Decision {
  if (radioSilenceS >= SILENCIO_RADIO_S) return { cylinderOn: true, reason: 'modo-seguro', state: initialState }
  if (state.pausedSince === null) {
    if (readingAmps > PAUSA_A) return { cylinderOn: false, reason: 'pausa-limite', state: { pausedSince: nowMin } }
    return { cylinderOn: true, reason: 'normal', state }
  }
  const dur = nowMin - state.pausedSince
  if (dur >= PAUSA_MAX) return { cylinderOn: true, reason: 'retoma-maximo', state: initialState }
  // while paused the reading excludes the cylinder, so add it back to know if there is margin
  if (dur >= PAUSA_MIN && readingAmps + CILINDRO_A < RETOMA_A)
    return { cylinderOn: true, reason: 'retoma-margem', state: initialState }
  return { cylinderOn: false, reason: 'pausa-mantida', state }
}

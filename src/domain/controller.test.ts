import { describe, expect, it } from 'vitest'
import { decide, initialState } from './controller'

describe('controller', () => {
  it('pausa acima de 90 %', () => {
    expect(decide(initialState, 13.4, 0).cylinderOn).toBe(true)
    const d = decide(initialState, 13.6, 0)
    expect(d.cylinderOn).toBe(false)
    expect(d.reason).toBe('pausa-limite')
  })
  it('não retoma enquanto corrente + cilindro ≥ 80 %', () => {
    const p = decide(initialState, 17.85, 0).state
    expect(decide(p, 5.25, 10).cylinderOn).toBe(false) // 5,25 + 6,75 = 12 → não < 12
    expect(decide(p, 5.2, 10).cylinderOn).toBe(true)
  })
  it('respeita a pausa mínima', () => {
    const p = decide(initialState, 17.85, 0).state
    expect(decide(p, 1, 0.5).cylinderOn).toBe(false)
    expect(decide(p, 1, 1).cylinderOn).toBe(true)
  })
  it('retoma aos 30 min e volta a pausar se a casa continuar acima', () => {
    const p = decide(initialState, 17.85, 0).state
    const r = decide(p, 11.1, 30)
    expect(r.cylinderOn).toBe(true)
    expect(r.reason).toBe('retoma-maximo')
    expect(decide(r.state, 17.85, 31).cylinderOn).toBe(false)
  })
  it('modo seguro: liga o cilindro ao fim de 5 s sem sinal', () => {
    const p = decide(initialState, 17.85, 0).state
    expect(decide(p, 17.85, 1, 4.9).cylinderOn).toBe(false)
    const d = decide(p, 17.85, 1, 5)
    expect(d.cylinderOn).toBe(true)
    expect(d.reason).toBe('modo-seguro')
  })
})

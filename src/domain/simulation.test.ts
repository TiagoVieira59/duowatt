import { describe, expect, it } from 'vitest'
import { hm } from '../data/serao'
import { simular } from './simulation'

const at = (r: ReturnType<typeof simular>, h: number, m: number) => r.serie.find((p) => p.t === hm(h, m))!
const round = (n: number) => Math.round(n)

describe('simulação', () => {
  const com = simular('com')
  const sem = simular('sem')

  it('65 % às 18:40 e pico de 119 % às 19:05', () => {
    expect(round(at(com, 18, 40).pct)).toBe(65)
    expect(round(at(com, 19, 5).pct)).toBe(119)
  })
  it('com DuoWatt: 74 % depois da pausa e retoma às 19:25', () => {
    expect(round(at(com, 19, 6).pct)).toBe(74)
    expect(at(com, 19, 24).cilindro).toBe('pausa')
    expect(com.eventos.find((e) => e.tipo === 'retoma')!.t).toBe(hm(19, 25))
    expect(at(com, 19, 26).cilindro).toBe('aquecer')
  })
  it('com DuoWatt: nunca acima de 100 % depois da pausa e sem oscilação', () => {
    expect(com.serie.filter((p) => p.t > hm(19, 5)).every((p) => p.pct <= 100)).toBe(true)
    expect(com.eventos.filter((e) => e.tipo === 'pausa' || e.tipo === 'retoma')).toHaveLength(2)
  })
  it('sem DuoWatt: apagão às 19:12', () => {
    expect(sem.eventos.find((e) => e.tipo === 'apagao')!.t).toBe(hm(19, 12))
    expect(sem.fimT).toBe(hm(19, 12))
  })
})

describe('carga potencial durante a pausa', () => {
  it('fica acima da retoma (80 %) até às 19:24 e abaixo às 19:25', () => {
    const com = simular('com')
    const p = (h: number, m: number) => com.serie.find((q) => q.t === hm(h, m))!
    expect(p(19, 24).potencial).toBeGreaterThan(80)
    expect(p(19, 25).potencial).toBeLessThan(80)
  })
})

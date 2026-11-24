import { INICIO, fmtHora } from '../data/serao'
import type { Clock } from './useDemoClock'
import type { Modo, Ponto, Resultado } from '../domain/simulation'

export type Estado = 'folgada' | 'perto' | 'acima'
export const estadoDe = (pct: number): Estado => (pct > 90 ? 'acima' : pct >= 80 ? 'perto' : 'folgada')

const LEGENDAS: Record<string, (m: Modo) => string> = {
  inicio: () => 'Serão normal. A casa está tranquila.',
  cilindro: () => 'O cilindro começa a aquecer água.',
  pico: () => 'Liga um aparelho grande. A casa passa o limite: 119 %.',
  pausa: () => 'O DuoWatt pausa o cilindro em menos de 1 s. A casa desce para 74 %.',
  acima: () => 'Sem DuoWatt, a casa fica acima do limite.',
  retoma: () => 'Há margem: o cilindro volta a ligar. Ninguém ficou sem água quente.',
  'fim-aquecer': () => 'O cilindro terminou de aquecer.',
  apagao: () => 'A luz foi abaixo.',
  fim: (m) => (m === 'com' ? 'Resultado: a luz nunca foi abaixo por causa do cilindro.' : ''),
}

export interface View {
  ponto: Ponto; idx: number; hora: string; legenda: string; apagao: boolean
  reacao: boolean; pausaMin: number | null; eventos: { t: number; hora: string; texto: string }[]
}

export function derivar(r: Resultado, c: Clock, modo: Modo): View {
  const last = r.serie.length - 1
  let idx = Math.min(last, Math.max(0, Math.floor(c.t) - INICIO))
  const ev = c.evento
  if ((ev?.tipo === 'pausa' || ev?.tipo === 'retoma') && Math.floor(c.t) === ev.t) idx = Math.min(last, idx + 1) // show the post-pause reading
  const ponto = r.serie[idx]!
  const quando = (tipo: string) => r.eventos.find((e) => e.tipo === tipo)
  const p = quando('pausa'), rt = quando('retoma')
  let pausaMin: number | null = null
  if (p && c.beat >= r.eventos.indexOf(p) && (!rt || c.beat < r.eventos.indexOf(rt))) pausaMin = Math.max(0, Math.floor(c.t) - p.t)
  const lista = r.eventos.slice(0, c.beat + 1).filter((e) => e.tipo !== 'inicio' && !(modo === 'com' && e.tipo === 'pico') && e.tipo !== 'fim')
  return {
    ponto, idx, hora: fmtHora(Math.min(c.t, r.fimT)),
    legenda: ev ? (LEGENDAS[ev.tipo]?.(modo) ?? '') : '',
    apagao: ponto.apagao && c.beat >= r.eventos.length - 1,
    reacao: ev?.tipo === 'pausa' && c.msDesdeEvento < 3500,
    pausaMin, eventos: lista.map((e) => ({ t: e.t, hora: fmtHora(e.t), texto: e.texto })).reverse(),
  }
}

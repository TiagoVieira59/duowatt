import { useCallback, useEffect, useRef, useState } from 'react'
import { INICIO } from '../data/serao'
import type { Evento, Resultado } from '../domain/simulation'

const SPEED = 9 // simulated minutes per real second
export const HOLD_MS = 2600 // every caption stays visible ≥ 2.5 s (clock freezes on each event)

export function buildTimeline(r: Resultado) {
  const arr: number[] = []
  let ms = 0, t = INICIO
  for (const e of r.eventos) {
    ms += ((e.t - t) / SPEED) * 1000; t = e.t
    arr.push(ms); ms += HOLD_MS
  }
  return { arr, total: ms }
}

export interface Clock {
  t: number; beat: number; evento: Evento | null; msDesdeEvento: number
  playing: boolean; done: boolean
  toggle(): void; restart(): void; play(): void
}

export function useDemoClock(r: Resultado, autoplay: boolean): Clock {
  const { arr, total } = buildTimeline(r)
  const [ms, setMs] = useState(0)
  const [playing, setPlaying] = useState(autoplay)
  const last = useRef(0)

  useEffect(() => { setMs(0); setPlaying(autoplay) }, [r, autoplay])
  useEffect(() => {
    if (!playing) return
    let raf = 0
    last.current = performance.now()
    const tick = (now: number) => { const dt = now - last.current; last.current = now; setMs((m) => Math.min(total, m + dt)); raf = requestAnimationFrame(tick) }
    raf = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(raf)
  }, [playing, total])

  const done = ms >= total
  useEffect(() => { if (done) setPlaying(false) }, [done])

  let beat = -1
  arr.forEach((a, i) => { if (ms >= a) beat = i })
  const cur = beat >= 0 ? r.eventos[beat]! : null
  let t = INICIO
  if (cur) {
    const dep = arr[beat]! + HOLD_MS
    const next = r.eventos[beat + 1]
    t = ms < dep || !next ? cur.t : cur.t + ((ms - dep) / (arr[beat + 1]! - dep)) * (next.t - cur.t)
  }
  return {
    t, beat, evento: cur, msDesdeEvento: cur ? ms - arr[beat]! : 0, playing, done,
    toggle: useCallback(() => setPlaying((p) => !p), []),
    restart: useCallback(() => { setMs(0); setPlaying(true) }, []),
    play: useCallback(() => setPlaying(true), []),
  }
}

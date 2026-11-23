import { useEffect, useRef } from 'react'
import { AnimatePresence, animate, motion, useMotionValue, useReducedMotion } from 'motion/react'
import { Flame, PauseCircle, Power, Radio, Wifi } from 'lucide-react'
import { FACTS, LIMITE_A } from '../../data/facts'
import { estadoDe } from '../../demo/view'
import { kw, num, pct } from '../../format'
import { SeraoChart } from '../../presenter/SeraoChart'
import type { ShellProps } from '../AppShell'
import s from '../app.module.css'

const ROTULO = { folgada: 'Folgada', perto: 'Perto do limite', acima: 'Acima do limite' } as const

function Meter({ value, delay }: { value: number; delay: number }) {
  const mv = useMotionValue(value)
  const el = useRef<HTMLSpanElement>(null)
  const reduce = useReducedMotion()
  useEffect(() => {
    const c = animate(mv, value, reduce ? { duration: 0 } : { type: 'spring', stiffness: 120, damping: 20, delay })
    return () => c.stop()
  }, [value, delay, reduce, mv])
  useEffect(() => mv.on('change', (v) => { if (el.current) el.current.textContent = pct(v) }), [mv])
  return <span ref={el} className={s.big}>{pct(value)}</span>
}

export function Agora({ view, clock, res, ghost, compact }: ShellProps) {
  const v = view.ponto
  const est = estadoDe(v.pct)
  const reduce = useReducedMotion()
  const pausa = v.cilindro === 'pausa'
  const dur = reduce ? 0 : 0.2
  return (
    <>
      <section className={`${s.meter} ${s[est]} ${v.pct > 100 ? s.over100 : ''}`}>
        <div className={s.meterTop}><span>Casa agora</span><span aria-live="polite">{ROTULO[est]}{v.pct > 100 ? ' · acima de 100 %' : ''}</span></div>
        <Meter value={v.pct} delay={pausa ? 0.35 : 0} />
        <div>≈ {kw(v.amps)} kW de {num(FACTS.potencia.valor, 2)} kVA</div>
      </section>

      <AnimatePresence>
        {view.reacao && (
          <motion.div className={s.react} initial={{ opacity: 0, y: -6 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }} transition={{ duration: dur }}>
            Pausado em {num(FACTS.reacaoSimS.valor, 1)} s (simulado) · meta &lt; {FACTS.reacaoS.valor} s
          </motion.div>
        )}
      </AnimatePresence>

      <section className={s.card} aria-label="Cilindro">
        <div className={s.row}>
          {v.cilindro === 'aquecer' ? <Flame aria-hidden /> : pausa ? <PauseCircle aria-hidden /> : <Power aria-hidden />}
          <div style={{ flex: 1 }}>
            <h2>Cilindro</h2>
            <motion.div key={v.cilindro} initial={reduce ? false : { opacity: 0, y: 4 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: dur, delay: pausa && !reduce ? 0.15 : 0 }}>
              <strong>{v.cilindro === 'aquecer' ? 'A aquecer' : pausa ? `Em pausa há ${view.pausaMin ?? 0} min` : 'Parado'}</strong>
            </motion.div>
          </div>
        </div>
        {pausa && <p className={s.muted} style={{ marginTop: 8 }}>Pausámos o cilindro para a luz não ir abaixo. Volta a ligar quando houver margem. Tens água quente guardada.</p>}
      </section>

      {compact && (
        <section className={s.card}>
          <h2>Serão (simulação)</h2>
          <div className={s.chartBox}><SeraoChart serie={res.serie} upto={view.idx} ghost={ghost} eventos={res.eventos} beat={clock.beat} compact /></div>
          <p className={s.muted}>{view.hora} · {view.legenda}</p>
          <button className={`${s.btn} ${s.primary}`} style={{ marginTop: 10 }} onClick={clock.done || !clock.playing ? clock.restart : clock.toggle}>
            {clock.playing ? 'Pausar' : clock.done || clock.beat > 0 ? 'Recomeçar' : 'Ver o serão (simulação)'}
          </button>
        </section>
      )}

      <section className={s.card}>
        <h2>Eventos de hoje</h2>
        <ul className={s.ev}>
          {view.eventos.length === 0 && <li className={s.muted}>Ainda sem eventos.</li>}
          {view.eventos.map((e) => <li key={e.t + e.texto}><b>{e.hora}</b>· {e.texto}</li>)}
        </ul>
      </section>

      <section className={s.card}>
        <h2>Ligação</h2>
        <div className={s.row}><Radio size={18} aria-hidden /> Rádio local · ligado</div>
        <div className={s.row} style={{ marginTop: 6 }}><Wifi size={18} aria-hidden /> Wi-Fi · ligado (opcional)</div>
        <p className={s.muted} style={{ marginTop: 8 }}>Limite da casa: {LIMITE_A} A</p>
      </section>
    </>
  )
}

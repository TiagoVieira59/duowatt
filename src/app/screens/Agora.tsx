import { useEffect, useRef } from 'react'
import { AnimatePresence, animate, motion, useMotionValue, useReducedMotion } from 'motion/react'
import { BellDot, GitBranch, House, Power, Radio, Wifi } from 'lucide-react'
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
  const pillEst = est === 'folgada' ? '' : est === 'perto' ? s.warn : s.bad
  return (
    <>
      <section className={`${s.meter} ${s[est]} ${v.pct > 100 ? s.over100 : ''}`}>
        <div className={s.hrow}>
          <div><House size={26} aria-hidden /><h2>Casa agora</h2></div>
          <span className={`${s.pill} ${pillEst}`} aria-live="polite">{ROTULO[est]}</span>
        </div>
        <Meter value={v.pct} delay={pausa ? 0.35 : 0} />
        <div className={s.kw}>≈ {kw(v.amps)} kW de {num(FACTS.potencia.valor, 2)} kVA</div>
      </section>

      <AnimatePresence>
        {view.reacao && (
          <motion.div className={s.react} initial={{ opacity: 0, y: -6 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }} transition={{ duration: dur }}>
            Pausado em {num(FACTS.reacaoSimS.valor, 1)} s (simulado) · meta &lt; {FACTS.reacaoS.valor} s
          </motion.div>
        )}
      </AnimatePresence>

      <section className={s.card} aria-label="Cilindro">
        <div className={s.hrow}>
          <div><Power size={26} aria-hidden /><h2>Cilindro</h2></div>
          <motion.span key={v.cilindro} className={`${s.pill} ${v.cilindro === 'aquecer' ? '' : pausa ? s.warn : s.neutral}`}
            initial={reduce ? false : { opacity: 0, y: 4 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: dur, delay: pausa && !reduce ? 0.15 : 0 }}>
            {v.cilindro === 'aquecer' ? 'A aquecer' : pausa ? `Em pausa há ${view.pausaMin ?? 0} min` : 'Não está a aquecer'}
          </motion.span>
        </div>
        {pausa && <p className={s.muted} style={{ marginTop: 12 }}>Pausámos o cilindro para a luz não ir abaixo. Volta a ligar quando houver margem. A água que já aqueceu fica guardada no cilindro.</p>}
      </section>

      {compact && (
        <section className={s.card}>
          <h2>Serão (simulação)</h2>
          <div className={s.chartBox}><SeraoChart serie={res.serie} upto={view.idx} ghost={ghost} eventos={res.eventos} beat={clock.beat} compact /></div>
          <p className={s.muted}>{view.hora} · {view.legenda}</p>
          <button className={`${s.btn} ${s.primary}`} style={{ marginTop: 12 }} onClick={clock.done || !clock.playing ? clock.restart : clock.toggle}>
            {clock.playing ? 'Pausar' : clock.done || clock.beat > 0 ? 'Recomeçar' : 'Ver o serão (simulação)'}
          </button>
        </section>
      )}

      <section className={s.card}>
        <div className={s.hrow}>
          <div><BellDot size={26} aria-hidden /><h2>Eventos de hoje</h2></div>
          <span className={`${s.pill} ${s.neutral}`}>{view.eventos.length === 0 ? 'Nenhum' : view.eventos.length}</span>
        </div>
        {view.eventos.length > 0 && (
          <ul className={s.ev}>{view.eventos.map((e) => <li key={e.t + e.texto}><b>{e.hora}</b>· {e.texto}</li>)}</ul>
        )}
      </section>

      <section className={s.card}>
        <div className={s.hrow}><div><GitBranch size={26} aria-hidden /><h2>Ligação</h2></div></div>
        <div className={s.lrow}><Radio size={24} aria-hidden /> Rádio local <em>Ligado</em></div>
        <div className={s.lrow}><Wifi size={24} aria-hidden /> Wi-Fi <em>Ligado</em><span className={s.right}>Opcional</span></div>
        <p className={s.muted} style={{ marginTop: 18 }}>Limite da casa: {LIMITE_A} A</p>
      </section>
    </>
  )
}

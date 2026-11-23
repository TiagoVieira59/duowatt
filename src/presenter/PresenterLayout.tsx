import type { ReactNode } from 'react'
import { motion, useReducedMotion } from 'motion/react'
import { Pause, Play, RotateCcw } from 'lucide-react'
import { PhoneFrame } from '../app/PhoneFrame'
import type { View } from '../demo/view'
import { estadoDe } from '../demo/view'
import type { Clock } from '../demo/useDemoClock'
import type { Modo, Resultado } from '../domain/simulation'
import { pct } from '../format'
import { SeraoChart } from './SeraoChart'
import s from './presenter.module.css'

interface Props { res: Resultado; ghost?: Resultado['serie']; view: View; clock: Clock; modo: Modo; onModo: (m: Modo) => void; help: boolean; phone: ReactNode }
const ROTULO = { folgada: 'Folgada', perto: 'Perto do limite', acima: 'Acima do limite' } as const

export function PresenterLayout({ res, ghost, view, clock, modo, onModo, help, phone }: Props) {
  const reduce = useReducedMotion()
  const est = estadoDe(view.ponto.pct)
  const sem = ghost && modo === 'com' && clock.done
  return (
    <div className={s.wrap}>
      <PhoneFrame>{phone}</PhoneFrame>
      <section className={s.panel} aria-label="Painel do serão">
        <div className={s.top}>
          <span className={s.clock}>{view.hora}</span>
          <span className={s.state}>{pct(view.ponto.pct)} · {ROTULO[est]}</span>
          <span className={s.tag}>Simulação</span>
        </div>
        <div className={s.chart}><SeraoChart serie={res.serie} upto={view.idx} ghost={sem ? ghost : undefined} eventos={res.eventos} beat={clock.beat} /></div>
        <motion.div key={view.legenda} className={s.cap} aria-live="polite" initial={reduce ? false : { opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.25 }}>
          {view.legenda}{sem ? ' Sem DuoWatt teria ficado acima do limite.' : ''}
        </motion.div>
        <div className={s.ctrl}>
          <button onClick={clock.toggle} aria-label={clock.playing ? 'Pausar' : 'Reproduzir'}>{clock.playing ? <Pause size={22} /> : <Play size={22} />}</button>
          <button onClick={clock.restart}><RotateCcw size={22} /> Recomeçar</button>
          <div className={s.toggle} role="group" aria-label="Modo">
            <button className={modo === 'com' ? s.on : ''} aria-pressed={modo === 'com'} onClick={() => onModo('com')}>Com DuoWatt</button>
            <button className={modo === 'sem' ? s.on : ''} aria-pressed={modo === 'sem'} onClick={() => onModo('sem')}>Sem DuoWatt</button>
          </div>
          <span className={s.keys}>Espaço · R · D · 1–4 · ?</span>
        </div>
        {view.apagao && <motion.div className={s.dark} initial={{ opacity: 0 }} animate={{ opacity: 0.93 }} transition={{ duration: reduce ? 0 : 0.6 }} />}
        {help && (
          <div className={s.help} role="dialog" aria-label="Atalhos">
            <div><kbd>Espaço</kbd>reproduzir / pausar</div><div><kbd>R</kbd>recomeçar</div>
            <div><kbd>D</kbd>com / sem DuoWatt</div><div><kbd>1–4</kbd>mudar de separador</div><div><kbd>?</kbd>esconder esta ajuda</div>
          </div>
        )}
      </section>
    </div>
  )
}

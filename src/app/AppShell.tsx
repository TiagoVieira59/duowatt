import { AnimatePresence, motion, useReducedMotion } from 'motion/react'
import { FACTS } from '../data/facts'
import { num } from '../format'
import type { View } from '../demo/view'
import type { Resultado } from '../domain/simulation'
import type { Clock } from '../demo/useDemoClock'
import { Agora } from './screens/Agora'
import { Historico } from './screens/Historico'
import { Poupanca } from './screens/Poupanca'
import { Definicoes } from './screens/Definicoes'
import { TabBar, type TabId } from './TabBar'
import s from './app.module.css'

export interface ShellProps { tab: TabId; onTab: (t: TabId) => void; view: View; clock: Clock; res: Resultado; ghost?: Resultado['serie']; compact: boolean }

export function AppShell(p: ShellProps) {
  const reduce = useReducedMotion()
  return (
    <div className={s.shell}>
      <header className={s.head}>
        <span className={s.brand}>DuoWatt</span>
        <span className={s.tag}>Simulação</span>
      </header>
      <div className={s.sub}>Casa · {num(FACTS.potencia.valor, 2)} kVA</div>
      <main className={s.main}>
        {p.tab === 'agora' && <Agora {...p} />}
        {p.tab === 'historico' && <Historico />}
        {p.tab === 'poupanca' && <Poupanca />}
        {p.tab === 'definicoes' && <Definicoes />}
      </main>
      <TabBar tab={p.tab} onTab={p.onTab} />
      <AnimatePresence>
        {p.view.apagao && (
          <motion.div className={s.blackout} role="alert" initial={{ opacity: 0 }} animate={{ opacity: 0.98 }} transition={{ duration: reduce ? 0 : 0.6 }}>
            <h2>A luz foi abaixo.</h2>
            <p>Ilustrativo: o tempo até ao corte depende do contador E-REDES e do disjuntor (EN 60898).</p>
            <button className={s.btn} style={{ width: 'auto', background: 'transparent', color: 'inherit', borderColor: 'currentColor' }} onClick={p.clock.restart}>Recomeçar</button>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

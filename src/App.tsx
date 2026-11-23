import { useEffect, useMemo, useState } from 'react'
import { MotionConfig } from 'motion/react'
import { AppShell } from './app/AppShell'
import { TABS, type TabId } from './app/TabBar'
import { useDemoClock } from './demo/useDemoClock'
import { derivar } from './demo/view'
import { simular, type Modo } from './domain/simulation'
import { PresenterLayout } from './presenter/PresenterLayout'

const q = new URLSearchParams(location.search)
const tab0 = TABS.find((t) => t.id === q.get('tab'))?.id ?? 'agora'

function useWide() {
  const m = window.matchMedia('(min-width: 1024px)')
  const [w, setW] = useState(m.matches)
  useEffect(() => { const f = () => setW(m.matches); m.addEventListener('change', f); return () => m.removeEventListener('change', f) }, [m])
  return w
}

export default function App() {
  const wide = useWide()
  const [modo, setModo] = useState<Modo>(q.get('modo') === 'sem' ? 'sem' : 'com')
  const [tab, setTab] = useState<TabId>(tab0)
  const [auto, setAuto] = useState(q.get('autoplay') === '1')
  const [help, setHelp] = useState(false)
  const res = useMemo(() => simular(modo), [modo])
  const ghost = useMemo(() => (modo === 'com' ? simular('sem').serie : undefined), [modo])
  const clock = useDemoClock(res, auto)
  const view = derivar(res, clock, modo)

  useEffect(() => {
    if (!wide) return
    const down = (e: KeyboardEvent) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return
      const k = e.key.toLowerCase()
      if (k === ' ') { e.preventDefault(); clock.toggle() }
      else if (k === 'r') clock.restart()
      else if (k === 'd') { setModo((m) => (m === 'com' ? 'sem' : 'com')); setAuto(true) }
      else if (k === '?') setHelp((h) => !h)
      else if ('1234'.includes(k) && k.length === 1) setTab(TABS[Number(k) - 1]!.id)
    }
    const up = (e: KeyboardEvent) => { if (e.key === ' ') e.preventDefault() }
    window.addEventListener('keydown', down); window.addEventListener('keyup', up)
    return () => { window.removeEventListener('keydown', down); window.removeEventListener('keyup', up) }
  }, [wide, clock])

  const shell = <AppShell tab={tab} onTab={setTab} view={view} clock={clock} res={res} ghost={clock.done ? ghost : undefined} compact={!wide} />
  return (
    <MotionConfig reducedMotion="user">
      {wide
        ? <PresenterLayout res={res} ghost={ghost} view={view} clock={clock} modo={modo} help={help} onModo={(m) => { setModo(m); setAuto(true) }} phone={shell} />
        : <div style={{ height: '100dvh' }}>{shell}</div>}
    </MotionConfig>
  )
}

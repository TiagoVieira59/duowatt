import { Clock, Euro, Minimize2, Settings } from 'lucide-react'
import s from './app.module.css'

export const TABS = [
  { id: 'agora', label: 'Agora', Icon: Minimize2 },
  { id: 'historico', label: 'Histórico', Icon: Clock },
  { id: 'poupanca', label: 'Poupança', Icon: Euro },
  { id: 'definicoes', label: 'Definições', Icon: Settings },
] as const
export type TabId = (typeof TABS)[number]['id']

export function TabBar({ tab, onTab }: { tab: TabId; onTab: (t: TabId) => void }) {
  return (
    <nav className={s.tabs} aria-label="Separadores">
      {TABS.map(({ id, label, Icon }) => (
        <button key={id} className={s.tab} aria-current={tab === id ? 'page' : undefined} onClick={() => onTab(id)}>
          <span><Icon size={22} aria-hidden /></span> {label}
        </button>
      ))}
    </nav>
  )
}

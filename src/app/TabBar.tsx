import { Activity, BarChart3, PiggyBank, Settings } from 'lucide-react'
import s from './app.module.css'

export const TABS = [
  { id: 'agora', label: 'Agora', Icon: Activity },
  { id: 'historico', label: 'Histórico', Icon: BarChart3 },
  { id: 'poupanca', label: 'Poupança', Icon: PiggyBank },
  { id: 'definicoes', label: 'Definições', Icon: Settings },
] as const
export type TabId = (typeof TABS)[number]['id']

export function TabBar({ tab, onTab }: { tab: TabId; onTab: (t: TabId) => void }) {
  return (
    <nav className={s.tabs} aria-label="Separadores">
      {TABS.map(({ id, label, Icon }) => (
        <button key={id} className={s.tab} aria-current={tab === id ? 'page' : undefined} onClick={() => onTab(id)}>
          <Icon size={22} aria-hidden /> {label}
        </button>
      ))}
    </nav>
  )
}

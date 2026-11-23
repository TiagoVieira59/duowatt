import { INICIO, FIM, fmtHora } from '../data/serao'
import type { Ponto, Evento } from '../domain/simulation'

const W = 800, H = 340, R = 16, T = 16, B = 34, YMAX = 130
let L = 56
const x = (t: number) => L + ((t - INICIO) / (FIM - INICIO)) * (W - L - R)
const y = (p: number) => T + (1 - p / YMAX) * (H - T - B)
const path = (s: Ponto[], k: 'pct' | 'potencial' = 'pct') => s.map((p, i) => `${i ? 'L' : 'M'}${x(p.t).toFixed(1)},${y(p[k]).toFixed(1)}`).join('')

interface Props { serie: Ponto[]; upto: number; ghost?: Ponto[]; eventos: Evento[]; beat: number; compact?: boolean }

export function SeraoChart({ serie, upto, ghost, eventos, beat, compact }: Props) {
  L = compact ? 84 : 56
  const ticks: number[] = []
  for (let t = INICIO; t <= FIM; t += 30) ticks.push(t)
  const fs = compact ? 26 : 15
  const shown = serie.slice(0, upto + 1)
  const espera = shown.filter((p, i) => p.cilindro === 'pausa' || serie[i + 1]?.cilindro === 'pausa')
  const marks = eventos.slice(0, beat + 1).filter((e) => e.tipo === 'pausa' || e.tipo === 'retoma' || e.tipo === 'apagao')
  const ref = (v: number, label: string, dash?: string, strong?: boolean) => (
    <g key={v}>
      <line x1={L} x2={W - R} y1={y(v)} y2={y(v)} stroke={strong ? 'var(--ink)' : 'var(--ink-soft)'} strokeWidth={strong ? 2 : 1.5} strokeDasharray={dash} />
      <text x={W - R - 4} y={y(v) - 5} textAnchor="end" fontSize={fs} fill="var(--ink)" fontWeight={600}>{label}</text>
    </g>
  )
  return (
    <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label="Gráfico do consumo da casa em percentagem do limite, das 18:30 às 21:00" style={{ width: '100%', height: '100%', display: 'block' }}>
      {[0, 50, 100].map((v) => <text key={v} x={L - 8} y={y(v) + 5} textAnchor="end" fontSize={fs} fill="var(--ink-soft)">{v} %</text>)}
      {ticks.map((t) => (
        <g key={t}>
          <line x1={x(t)} x2={x(t)} y1={T} y2={H - B} stroke="var(--line)" />
          {(!compact || (t - INICIO) % 60 === 0) && <text x={x(t)} y={H - 10} textAnchor="middle" fontSize={fs} fill="var(--ink-soft)">{fmtHora(t)}</text>}
        </g>
      ))}
      {ref(100, 'Limite contratado', undefined, true)}
      {ref(90, 'Pausa', '7 5')}
      {ref(80, 'Retoma', '3 5')}
      {ghost && <path d={path(ghost)} fill="none" stroke="var(--over-bg)" strokeWidth={2.5} strokeDasharray="2 5" opacity={0.7} />}
      {espera.length > 1 && (
        <g>
          <path d={path(espera, 'potencial')} fill="none" stroke="var(--ink-soft)" strokeWidth={2.5} strokeDasharray="6 5" />
          <text x={x(espera[0]!.t) + 10} y={y(espera[0]!.potencial) + 4} fontSize={fs} fill="var(--ink)">Se o cilindro ligasse</text>
        </g>
      )}
      <path d={path(shown)} fill="none" stroke="var(--brand)" strokeWidth={compact ? 4 : 4} strokeLinejoin="round" strokeLinecap="round" />
      {marks.map((e) => {
        const p = serie.find((q) => q.t === e.t); if (!p) return null
        const yy = e.tipo === 'pausa' ? serie[serie.indexOf(p)]!.pct : p.pct
        return <circle key={e.tipo + e.t} cx={x(e.t)} cy={y(yy)} r={7} fill="var(--surface)" stroke="var(--ink)" strokeWidth={3} />
      })}
    </svg>
  )
}

import { PAUSAS_SEMANA } from '../../data/exemplo'
import s from '../app.module.css'

export function Historico() {
  const total = PAUSAS_SEMANA.reduce((a, d) => a + d.min, 0)
  const max = Math.max(...PAUSAS_SEMANA.map((d) => d.min))
  return (
    <>
      <section className={s.card}>
        <span className={s.badge}>Dados de exemplo</span>
        <h2>Pausas por dia, esta semana</h2>
        <div className={s.bars} role="img" aria-label="Minutos de pausa por dia">
          {PAUSAS_SEMANA.map((d) => (
            <div key={d.dia} className={s.bar}><span>{d.min}</span><i style={{ height: `${(d.min / max) * 80}%` }} /><span>{d.dia}</span></div>
          ))}
        </div>
        <p className={s.muted}>Total: {total} min em pausa. Os picos da tua casa são entre as 19h e as 21h.</p>
      </section>
      <section className={s.card} style={{ background: 'var(--ok-bg)', color: 'var(--ok-ink)' }}>
        <span className={s.badge}>Dados de exemplo</span>
        <h2>Esta semana, o cilindro nunca fez ir a luz abaixo.</h2>
      </section>
      <section className={s.card}>
        <span className={s.badge}>Dados de exemplo</span>
        <h2>Avisos recentes</h2>
        <p style={{ margin: '4px 0' }}><b>Ontem, 20:40</b> · A casa passou o limite sem o cilindro. Aqui o DuoWatt não resolve: desliga um aparelho ou pondera subir a potência.</p>
        <p className={s.muted}>O DuoWatt mede a casa toda; não sabe que aparelho ligou.</p>
      </section>
    </>
  )
}

import { FACTS } from '../../data/facts'
import { CONSUMO_MES } from '../../data/exemplo'
import { eur, num } from '../../format'
import s from '../app.module.css'

export function Poupanca() {
  const F = FACTS
  return (
    <>
      <p className={s.muted} style={{ padding: '0 4px' }}>Este mês, estimativas.</p>
      <div className={s.grid2}>
        <section className={s.card}><h2>Garrafas de gás evitadas</h2><div className={s.val}>≈ {num(F.garrafas.valor)}</div><p className={s.muted}>{F.garrafas.fonte}</p></section>
        <section className={s.card}><h2>CO₂ evitado</h2><div className={s.val}>≈ {num(F.co2.valor)} kg</div><p className={s.muted}>cenário prudente ≈ {num(F.co2Prudente.valor)} kg. {F.co2.fonte}</p></section>
      </div>
      <section className={s.card}><h2>Potência que não foi preciso subir</h2><div className={s.val}>≈ {eur(F.potenciaPoupanca.valor)}</div><p className={s.muted}>Cenário tarifário, sem IVA. {F.potenciaPoupanca.fonte}</p></section>
      <section className={s.card}><h2>Aquecer nas horas baratas</h2><div className={s.val}>até ≈ {eur(F.horasBaratas.valor)}</div><p className={s.muted}>Só com tarifa bi-horária. {F.horasBaratas.fonte}</p></section>
      <section className={s.card}>
        <span className={s.badge}>Dados de exemplo</span>
        <h2>Consumo deste mês</h2>
        <p style={{ margin: 0 }}>Casa: {num(CONSUMO_MES.casaKwh)} kWh · Água quente: {num(CONSUMO_MES.aguaQuenteKwh)} kWh</p>
      </section>
      <p className={s.muted} style={{ padding: '0 4px' }}>Estimativas da equipa DuoWatt. A fatura oficial é a da tua comercializadora.</p>
    </>
  )
}

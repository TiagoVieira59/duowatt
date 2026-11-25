import { useState } from 'react'
import s from '../app.module.css'

const MODOS = ['Automático', 'Horas de vazio (ex.: 22h–8h)']

export function Definicoes() {
  const [modo, setModo] = useState(0)
  const [ferias, setFerias] = useState(false)
  const [ligado, setLigado] = useState(true)
  return (
    <>
      <section className={s.card}>
        <h2>Quando aquecer a água</h2>
        <div className={s.seg} role="radiogroup" aria-label="Quando aquecer a água">
          {MODOS.map((m, i) => <button key={m} role="radio" aria-checked={modo === i} onClick={() => setModo(i)}>{m}</button>)}
        </div>
        <p className={s.muted}>A segurança da casa e a água quente mínima vêm sempre primeiro.</p>
      </section>
      <section className={s.card}>
        <div className={s.switch}><h2 style={{ margin: 0 }}>Modo férias</h2><button role="switch" aria-checked={ferias} aria-label="Modo férias" onClick={() => setFerias(!ferias)} /></div>
        <p className={s.muted} style={{ marginTop: 6 }}>Não aquece enquanto estás fora. Volta a ligar o cilindro antes de chegares, para teres água quente.</p>
      </section>
      <section className={s.card}>
        <div className={s.switch}><h2 style={{ margin: 0 }}>Ajudar a rede (em breve) <span className={s.badge} style={{ marginLeft: 6, marginBottom: 0 }}>Futuro</span></h2><button role="switch" aria-checked={false} disabled aria-label="Ajudar a rede" /></div>
        <p className={s.muted} style={{ marginTop: 6 }}>Com a tua autorização, o cilindro pode adiar o aquecimento nos picos da rede. A tua água quente e a segurança da casa vêm sempre primeiro.</p>
      </section>
      <section className={s.card}>
        <h2>Wi-Fi e dados</h2>
        <p className={s.muted} style={{ marginBottom: 10 }}>{ligado ? 'Autorizaste o modo ligado. Podes desligá-lo a qualquer momento: a proteção continua por rádio, sem internet.' : 'Modo ligado desligado. A proteção continua por rádio, sem internet.'}</p>
        <button className={s.btn} onClick={() => setLigado(!ligado)}>{ligado ? 'Desligar o modo ligado' : 'Ligar o modo ligado'}</button>
      </section>
      <section className={s.card}><h2>Sobre</h2><p className={s.muted}>Simulação criada para o Hackathon@ShiftE 2026 (Universidade de Aveiro). Valores ilustrativos.</p></section>
    </>
  )
}

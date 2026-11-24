import { useEffect, useState, type ReactNode } from 'react'

const W = 390, H = 844
export function PhoneFrame({ children }: { children: ReactNode }) {
  const [k, setK] = useState(1)
  useEffect(() => {
    const f = () => setK(Math.min(1, (window.innerHeight - 56) / (H + 24)))
    f(); window.addEventListener('resize', f); return () => window.removeEventListener('resize', f)
  }, [])
  return (
    <div style={{ width: (W + 24) * k, height: (H + 24) * k, flex: 'none' }}>
      <div style={{ width: W + 24, height: H + 24, transform: `scale(${k})`, transformOrigin: 'top left', background: '#111', borderRadius: 54, padding: 12, boxShadow: '0 24px 60px rgba(40,30,10,.28)' }}>
        <div style={{ width: W, height: H, borderRadius: 42, overflow: 'hidden', position: 'relative', background: 'var(--bg)' }}>{children}</div>
      </div>
    </div>
  )
}

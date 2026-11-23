const nf = (d: number) => new Intl.NumberFormat('pt-PT', { minimumFractionDigits: d, maximumFractionDigits: d })
export const pct = (n: number) => `${nf(0).format(Math.round(n))} %`
export const num = (n: number, d = 0) => nf(d).format(n)
export const eur = (n: number) => `${nf(0).format(n)} €`
export const kw = (amps: number) => nf(2).format((amps * 230) / 1000)

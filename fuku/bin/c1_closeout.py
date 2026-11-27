#!/usr/bin/env python3
"""M-001 criterion 1 close-out (12/05 judge, window 11/28-12/04).

Feed the locked days of the judged window; prints leads still needed,
a Poisson chance of a miss at the current BC lead rate, and the pre-written
readout line. All outputs are *(calc)*.

  python3 fuku/bin/c1_closeout.py --locked SPEND LEADS DAYS [--rate SPEND_PER_DAY] [--cpl BASE_CPL]
  --locked 0 0 0  = nothing locked yet (pre-window forecast)
"""
import argparse, math

TARGET = 95_000
WINDOW_DAYS = 7

def poisson_cdf(k, mu):
    if k < 0:
        return 0.0
    return sum(math.exp(-mu) * mu**i / math.factorial(i) for i in range(k + 1))

p = argparse.ArgumentParser()
p.add_argument("--locked", nargs=3, type=float, metavar=("SPEND", "LEADS", "DAYS"), required=True)
p.add_argument("--rate", type=float, default=135_045, help="spend/day for unlocked days (default 7d 11/20-11/26 = 945,317/7)")
p.add_argument("--cpl", type=float, default=72_717, help="expected CPL for unlocked days (default 7d 72.7k)")
a = p.parse_args()

s_lock, l_lock, d_lock = a.locked
l_lock, d_lock = int(l_lock), int(d_lock)
d_left = WINDOW_DAYS - d_lock
s_total = s_lock + a.rate * d_left
need_total = math.ceil(s_total / TARGET - 1e-9)
need_left = max(0, need_total - l_lock)
mu = a.rate * d_left / a.cpl
p_miss = poisson_cdf(need_left - 1, mu) if need_left > 0 else 0.0
proj = s_total / (l_lock + mu) if (l_lock + mu) else float("inf")

print(f"Window 11/28-12/04: locked {d_lock}d Rp {s_lock:,.0f} / {l_lock}; {d_left}d left at Rp {a.rate:,.0f}/day")
print(f"Projected 7d spend Rp {s_total:,.0f} -> needs >= {need_total} leads in the window (95k line) *(calc)*")
print(f"Leads still needed: {need_left} in {d_left}d; expected {mu:.1f} at {a.cpl/1000:.1f}k CPL *(calc)*")
print(f"Projected 7d CPL {proj/1000:.1f}k; P(miss) = {p_miss*100:.0f}% (Poisson, INFERRED) *(calc)*")
if d_left == 0:
    cpl = s_lock / l_lock if l_lock else float("inf")
    ok = cpl <= TARGET
    print(f"VERDICT LINE: M-001 criterion 1 {'MET ✅' if ok else 'MISSED ❌'} on 12/05: 7d 11/28-12/04 Rp {s_lock:,.0f} / {l_lock} = {cpl/1000:.1f}k *(calc)* vs 95k.")
elif need_left == 0:
    print("STATUS LINE: criterion 1 already safe unless spend jumps (more spend with 0 leads can still lift it; re-run if spend/day > 1.3x rate).")
else:
    print(f"STATUS LINE: criterion 1 needs {need_left} more leads in {d_left}d (expected {mu:.1f}); P(miss) {p_miss*100:.0f}% *(calc)*.")

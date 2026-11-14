# 11/20 gate scenario model (Fuku, 2026-11-14; CLI added 2026-11-14 21:01).
# Window 11/13-11/19 (7 days). Gate = 7d Fab CPL <= Rp 95,000.
# Each 07:00 readout: lock every finished PEIKIRA day in the window with --lock (in date order, 11/13 first),
# and pass the fresh 7d bases. No flags = the 11/14 07:02 base with 11/13 locked (original output).
#   python3 fuku/bin/gate_model_1120.py --lock 293851 0 --lock <S_11/14> <L_11/14> \
#       --peik <7d S> <7d L> --bc <7d S> <7d L> --p2 <7d S> <7d L>
# --lock = PEIKIRA campaign spend/leads for that day (BC is modelled flat at its 7d rate on all 7 days).
# --peik = PEIKIRA 7d base for the open days (daily spend = S/7, CPL = S/L). --p2 = PEIKIRA2 7d (the "Ad015 paused" CPL).
import argparse, datetime as dt

ap = argparse.ArgumentParser()
ap.add_argument("--lock", nargs=2, type=float, action="append", metavar=("SPEND", "LEADS"))
ap.add_argument("--peik", nargs=2, type=float, default=[2016453, 14], metavar=("SPEND", "LEADS"))
ap.add_argument("--bc", nargs=2, type=float, default=[313500, 6], metavar=("SPEND", "LEADS"))
ap.add_argument("--p2", nargs=2, type=float, default=[924806, 8], metavar=("SPEND", "LEADS"))
a = ap.parse_args()

START = dt.date(2026, 11, 13)
LOCKED = a.lock or [[293851, 0]]
N_OPEN = 7 - len(LOCKED)  # PEIKIRA days still to come
assert N_OPEN >= 1, "window already closed: read the 11/20 actual instead"
P_DAY = a.peik[0] / 7; P_CPL = a.peik[0] / a.peik[1]
BC_S, BC_L = a.bc
P2_CPL = a.p2[0] / a.p2[1]

def run(days_changed, peik_cpl_after, site=1.0, a3_share=0, a3_cpl=None):
    # the last `days_changed` days of the window run with the change live
    s = sum(x[0] for x in LOCKED); l = sum(x[1] for x in LOCKED)
    for d in range(N_OPEN):
        if d < N_OPEN - days_changed:
            s += P_DAY; l += P_DAY / P_CPL
        else:
            base = peik_cpl_after
            if a3_share:
                leads = P_DAY * (1 - a3_share) / base + P_DAY * a3_share / a3_cpl
            else:
                leads = P_DAY / base
            s += P_DAY; l += leads * site
    # BC: site multiplier only on changed days
    bc_day_s = BC_S / 7; bc_day_l = BC_L / 7
    for d in range(7):
        ch = d >= 7 - days_changed
        s += bc_day_s; l += bc_day_l * (site if ch else 1)
    return s / l, l

def k(x): return f"{x/1000:.1f}k"
locked_to = START + dt.timedelta(days=len(LOCKED) - 1)
print(f"Locked PEIKIRA days: 11/13 -> {locked_to:%m/%d} ({len(LOCKED)}), open days: {N_OPEN}. "
      f"Base PEIKIRA {k(P_CPL)}, P2 {k(P2_CPL)}, BC {k(BC_S/BC_L)}")
print("A nothing:", [round(x, 1) for x in run(0, P_CPL)])
for days in [x for x in (N_OPEN - 1, N_OPEN - 2, N_OPEN - 3) if x >= 1]:
    live = START + dt.timedelta(days=7 - days - 1)
    lbl = ("live " if days == N_OPEN - 1 else "") + f"{live:%m/%d} eve"
    print(lbl)
    print(f"  Ad015 paused, freed->P2 {k(P2_CPL)}:", round(run(days, P2_CPL)[0]))
    print("  Ad015 paused, freed at 130k:", round(run(days, 130000)[0]))
    print("  Site +0.5pt:", round(run(days, P_CPL, site=4.4/3.9)[0]), " +1pt:", round(run(days, P_CPL, site=4.9/3.9)[0]))
    print(f"  Ad015+site0.5 ({k(P2_CPL)}):", round(run(days, P2_CPL, site=4.4/3.9)[0]), " +1pt:", round(run(days, P2_CPL, site=4.9/3.9)[0]))
    for sh in (1/3, 0.6):
        print(f"  A3 share {sh:.2f} @70/95/130 (rest {k(P_CPL)}):", [round(run(days, P_CPL, a3_share=sh, a3_cpl=c)[0]) for c in (70000, 95000, 130000)])
        print(f"  Ad015 paused + A3 {sh:.2f} @70/95/130 (rest {k(P2_CPL)}):", [round(run(days, P2_CPL, a3_share=sh, a3_cpl=c)[0]) for c in (70000, 95000, 130000)])
        print(f"  ALL (Ad015+site .5+A3 {sh:.2f}) @70/95/130:", [round(run(days, P2_CPL, site=4.4/3.9, a3_share=sh, a3_cpl=c)[0]) for c in (70000, 95000, 130000)])

D = N_OPEN - 1  # earliest realistic live: tonight
def be(share, rest, site=1.0, days=D):
    if days < 1: return None
    lo, hi = 10000, 300000
    for _ in range(60):
        m = (lo + hi) / 2
        if run(days, rest, site=site, a3_share=share, a3_cpl=m)[0] <= 95000: lo = m
        else: hi = m
    return round(lo) if lo > 10000 else "NONE"
print(f"BE A3 ({D}d):", {f"{sh:.2f}/{n}": be(sh, r) for sh in (1/3, 0.6, 0.8) for n, r in ((k(P_CPL), P_CPL), ("Ad015off", P2_CPL))})
print("BE A3 + site .5:", {f"{sh:.2f}": be(sh, P2_CPL, site=4.4/3.9) for sh in (1/3, 0.6)})
if D >= 1:
    print(f"Ad015off+site+1pt {D}d:", round(run(D, P2_CPL, site=4.9/3.9)[0]))

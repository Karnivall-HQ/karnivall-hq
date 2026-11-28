#!/usr/bin/env python3
"""Incess R2 placement read for the 11/30 weekly (call 6a rows -> table rows + R2 line).

Rule (fab_advertising/reports/weekly/2026-11-30.md, R2; source
fab_advertising/reports/2026-11-23_incess_lp_and_placement_check.md):
  - close  : IG reels CPL <= 25k  OR  campaign 7d CPL <= 35k
  - propose: campaign 7d CPL > 35k AND (FB reels + FB feed) CPL > 1.4x IG feed CPL
             (2nd week: prior week was 1.55x) -> placement-exclusion proposal
  - else   : watch one more week
Read-only maths; every output is *(calc)*. Propose-only: Alvian applies.

  python3 fuku/bin/incess_r2.py --campaign SPEND LEADS \
      --row "IG feed" SPEND CLICKS LPV LEADS --row "IG reels" ... --row "FB reels" ... \
      --row "FB feed" ... [--row "IG stories" ...] [--row Threads ...]
Exit 0 = close, 2 = proposal printed, 3 = watch, 1 = input error.
"""
import argparse, sys

PRIOR = {  # 11/16-11/22: spend, LPV/click %, lead/LPV %, CPL
    "IG feed": (2_793_667, 91.8, 7.83, 34_100), "IG reels": (1_487_395, 83.8, 3.33, 36_300),
    "IG stories": (1_640_951, 97.3, 5.06, 42_100), "FB reels": (527_335, 70.3, 2.87, 52_700),
    "FB feed": (318_311, 72.0, 4.03, 53_100), "Threads": (299_362, 69.6, 3.64, 27_200),
}
REQUIRED = ("IG feed", "IG reels", "FB reels", "FB feed")
PRIOR_RATIO = 1.55
CAMPAIGN = "OMO ADVLeads 120233576079370222"

p = argparse.ArgumentParser()
p.add_argument("--campaign", nargs=2, type=float, metavar=("SPEND", "LEADS"), required=True)
p.add_argument("--row", nargs=5, action="append", metavar=("PLACEMENT", "SPEND", "CLICKS", "LPV", "LEADS"), required=True)
a = p.parse_args()

rows = {}
for name, *vals in a.row:
    if name not in PRIOR:
        sys.exit(f"unknown placement {name!r}; expected one of {list(PRIOR)}")
    rows[name] = tuple(float(v) for v in vals)
missing = [n for n in REQUIRED if n not in rows]
if missing:
    print(f"ERROR: missing rows {missing} (R2 needs IG feed, IG reels, FB reels, FB feed)", file=sys.stderr)
    sys.exit(1)

cpl = lambda s, l: s / l if l else float("inf")
k = lambda x: "∞ (0 leads)" if x == float("inf") else f"{x/1000:.1f}k"
pct = lambda a_, b, d=1: f"{a_/b*100:.{d}f}%" if b else "—"

print("| Placement | Spend (prior) | LPV÷click (prior) | Lead÷LPV (prior) | CPL (prior) |")
print("|---|---|---|---|---|")
for n in PRIOR:
    if n not in rows:
        continue
    s, c, lpv, l = rows[n]
    ps, pc, pl, pcpl = PRIOR[n]
    print(f"| {n} | {s:,.0f} ({ps:,}) | {pct(lpv, c)} ({pc}%) | {pct(l, lpv, 2)} ({pl}%) | {k(cpl(s, l))} ({pcpl/1000:.1f}k) |")

cs, cl = a.campaign
camp = cpl(cs, cl)
fbs = rows["FB reels"][0] + rows["FB feed"][0]
fbl = rows["FB reels"][3] + rows["FB feed"][3]
fb = cpl(fbs, fbl)
igf = cpl(rows["IG feed"][0], rows["IG feed"][3])
igr = cpl(rows["IG reels"][0], rows["IG reels"][3])
ratio = fb / igf if igf not in (0, float("inf")) else float("inf")
print(f"\nR2 test: FB reels+feed Rp {fbs:,.0f} / {fbl:.0f} = {k(fb)} ÷ IG feed {k(igf)} = {ratio:.2f} "
      f"(prior {PRIOR_RATIO}); campaign 7d Rp {cs:,.0f} / {cl:.0f} = {k(camp)}; IG reels {k(igr)} *(calc)*")
small = " small counts," if fbl < 20 else ""

if igr <= 25_000 or camp <= 35_000:
    why = f"7d {k(camp)} ≤ 35k" if camp <= 35_000 else f"IG reels {k(igr)} ≤ 25k"
    print(f"→ CLOSE. Incess placement watch closed: {why};{small} FB still {ratio:.2f}× IG feed; re-open only if 7d > 35k.")
    sys.exit(0)

if ratio > 1.4:
    exp = cpl(cs, cl - fbl + fbs / igf) if igf != float("inf") else float("nan")
    print(f"""→ PROPOSAL (7d {k(camp)} > 35k and FB {ratio:.2f}× IG feed for a 2nd week).
Proposed changes for Alvian to apply (Incess, {CAMPAIGN}):
1. In each live ad set's Placements, untick Facebook Feed + Facebook Reels (keep Instagram, Threads, the rest).
   Why: 7d 11/23–11/29 FB reels+feed Rp {fbs:,.0f} / {fbl:.0f} = {k(fb)} vs IG feed {k(igf)} ({ratio:.2f}×; prior week 1.55×);{small} campaign 7d {k(camp)} > 35k *(calc)*.
   Where the spend goes: budget unchanged; Meta re-routes Rp {fbs:,.0f}/wk to the remaining placements.
   Expected: campaign 7d → {k(exp)} *(calc)*, if the moved spend converts at the IG feed CPL (best case; IG reels/stories run higher).
   Undo: re-tick FB feed + reels if campaign 3-day CPL > 7d-before CPL after the change.
   (INFERRED: placements are set per ad set; list the live ad sets from call 5 before sending.)""")
    sys.exit(2)

print(f"→ WATCH one more week: 7d {k(camp)} > 35k but FB only {ratio:.2f}× IG feed (≤ 1.4).")
sys.exit(3)

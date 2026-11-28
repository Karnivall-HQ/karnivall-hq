#!/usr/bin/env python3
"""Incess R7 (4 picks) read for the 11/30 weekly + the cut-list line if it fires.

Rules come from fab_advertising/reports/weekly/2026-11-30.md (R7) and the cut-list
skeleton in fab_advertising/reports/2026-11-27_incess_placement_prepull.md:
  - 4-pick 7d CPL > 35k  -> cut list for ONE pick; <= 35k -> "R7 closed".
  - Pick rule: highest 7d CPL among picks with spend >= 2x ITS bid cap
    (026 cap is 45,000, the rest 46,000); if that pick has < 3 leads, cut only
    if spend >= 3x cap, else next-highest eligible. Never 2 picks.
  - 047 line: 7d CPL > 35.6k (2nd week) and CTR not down > 30% vs prior
    -> "post-click drop, not fatigue", watch in Top 3, no cut while 1 of 4.
  - 030 line: watch vs its 46.1k flag line (small counts).
Read-only maths; every output is *(calc)*. Propose-only: Alvian applies.

  python3 fuku/bin/incess_r7.py --pick 042 S L --pick 047 S L --pick 030 S L --pick 026 S L \
      [--ctr 047=2.40] [--ctr-prior 047=3.02]
Exit 0 = R7 closed, 2 = cut list written, 1 = input error.
"""
import argparse, sys

PICKS = {  # name: (ad set id, bid cap, flag line, live ads, carrying ad id)
    "042": ("120239651281900222", 46_000, 46_900, 1, "ImageAd042 120239651281890222"),
    "047": ("120239723303450222", 46_000, 35_600, 1, "ImageAd047 120239723303440222"),
    "030": ("120239636846070222", 46_000, 46_100, 1, "ImageAd030 120239636846080222"),
    "026": ("120244551313580222", 45_000, 32_600, 6, "026D Copy 3 120244561032460222"),
}
NAMES = {"042": "042", "047": "047 – Copy", "030": "030 Kotak", "026": "026 Manny5"}
LINE = 35_000
PRIOR = (4_474_301, 119)  # 11/16-11/22, 37.6k

def kv(items):
    out = {}
    for it in items or []:
        k, v = it.split("=")
        out[k] = float(v)
    return out

# Stale-base guard (11/28 sweep): PRIOR = 11/16-11/22 and the rule wording are for the 11/30 weekly only.
import datetime as _dt
if _dt.datetime.now(_dt.timezone(_dt.timedelta(hours=7))).date() > _dt.date(2026, 11, 30) and "--allow-stale-prior" not in sys.argv:
    sys.exit("ERROR: PRIOR is the 11/16-11/22 base (valid for the 11/30 weekly only). Update PRIOR + rules first, or pass --allow-stale-prior for a historical re-run.")
sys.argv = [x for x in sys.argv if x != "--allow-stale-prior"]

p = argparse.ArgumentParser()
p.add_argument("--pick", nargs=3, action="append", metavar=("NAME", "SPEND", "LEADS"), required=True)
p.add_argument("--ctr", action="append", help="NAME=pct, this week (047 line)")
p.add_argument("--ctr-prior", action="append", help="NAME=pct, prior week (default 047=3.02)")
a = p.parse_args()

data = {}
for n, s, l in a.pick:
    if n not in PICKS:
        sys.exit(f"unknown pick {n}; expected {sorted(PICKS)}")
    data[n] = (float(s), int(float(l)))
missing = set(PICKS) - set(data)
if missing:
    print(f"ERROR: missing picks {sorted(missing)} (R7 is the 4-pick total)", file=sys.stderr)
    sys.exit(1)
ctr, ctr_prior = kv(a.ctr), {"047": 3.02, **kv(a.ctr_prior)}

cpl = lambda s, l: s / l if l else float("inf")
fmt = lambda x: "∞ (0 leads)" if x == float("inf") else f"{x/1000:.1f}k"
S = sum(s for s, _ in data.values()); L = sum(l for _, l in data.values())
total = cpl(S, L)
wow = (total / (PRIOR[0] / PRIOR[1]) - 1) * 100 if L else float("nan")
print(f"4 picks 7d: Rp {S:,.0f} / {L} = {fmt(total)} (prior 37.6k, WoW {wow:+.1f}%) *(calc)*")
for n in PICKS:
    s, l = data[n]
    cap, flag = PICKS[n][1], PICKS[n][2]
    print(f"  {n}: Rp {s:,.0f} / {l} = {fmt(cpl(s, l))} | {s/cap:.1f}x cap | flag {flag/1000:.1f}k {'OVER' if cpl(s, l) > flag else 'ok'}")

watch = []
s47, l47 = data["047"]
if cpl(s47, l47) > 35_600:
    if "047" in ctr:
        drop = (1 - ctr["047"] / ctr_prior["047"]) * 100
        label = "post-click drop, not fatigue" if drop <= 30 else f"CTR down {drop:.0f}% > 30%: fatigue possible"
        watch.append(f"047 {fmt(cpl(s47, l47))} > 35.6k (2nd week); CTR {ctr['047']:.2f}% vs {ctr_prior['047']:.2f}% → {label}")
    else:
        watch.append(f"047 {fmt(cpl(s47, l47))} > 35.6k (2nd week); pass --ctr 047=<pct> to label it")
s30, l30 = data["030"]
watch.append(f"030 Rp {s30:,.0f} / {l30} = {fmt(cpl(s30, l30))} vs flag 46.1k ({'over' if cpl(s30, l30) > 46_100 else 'under'}; small counts)")

if total <= LINE:
    print(f"\nR7 closed: 4-pick 7d {fmt(total)} ≤ 35k *(calc)*. Watch lines only:")
    for w in watch:
        print(f"  - {w}")
    sys.exit(0)

def eligible(n):
    s, l = data[n]; cap = PICKS[n][1]
    return s >= (3 if l < 3 else 2) * cap
ranked = sorted(PICKS, key=lambda n: cpl(*data[n]), reverse=True)
cut = next((n for n in ranked if eligible(n)), None)
print(f"\nR7 FIRES: 4-pick 7d {fmt(total)} > 35k *(calc)*")
if cut is None:
    print("  no pick passes the spend-multiple rule → no cut this week; watch lines only")
    for w in watch:
        print(f"  - {w}")
    sys.exit(0)
skipped = [n for n in ranked[: ranked.index(cut)]]
for n in skipped:
    s, l = data[n]
    print(f"  skipped {n} ({fmt(cpl(s, l))}): spend {s/PICKS[n][1]:.1f}x cap < {'3' if l < 3 else '2'}x with {l} leads")
sid, cap, flag, live, ad = PICKS[cut]
s, l = data[cut]
rest = [n for n in PICKS if n != cut]
cheap = min(rest, key=lambda n: cpl(*data[n]))
exp = cpl(S - s, L - l)
what = f"its only live ad {ad}" if live == 1 else f"{live} live ads; carrying ad {ad} — pausing the ad set pauses all {live}"
print(f"""
Proposed changes for Alvian to apply (Incess, OMO ADVLeads 120233576079370222):
1. Pause ad set {NAMES[cut]} {sid} ({what}). 7d 11/23–11/29: Rp {s:,.0f} / {l} = {fmt(cpl(s, l))} (flag line {flag/1000:.1f}k); 4-pick 7d {fmt(total)} > 35k *(calc)*.
   Where the spend goes: campaign budget unchanged; Meta re-routes to the other picks (cheapest 7d: {cheap} {fmt(cpl(*data[cheap]))}). (INFERRED: campaign-level budget; confirm daily_budget at campaign level in call 5 before sending.)
   Expected: 4-pick CPL → {fmt(exp)} *(calc)*, if the moved spend converts at the remaining picks' average.
   Undo: re-activate if the other 3 picks' 3-day CPL > 35k after the pause.""")
others = [w for w in watch if not w.startswith(cut)]
if others:
    print("Watch lines:")
    for w in others:
        print(f"  - {w}")
sys.exit(2)

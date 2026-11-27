#!/usr/bin/env python3
"""W1/W2 site-fix lift read (rule pre-written 11/27 in fab_advertising/reports/w1w2_lift_template.md).

Usage:
  w1w2_read.py dates <day0 YYYY-MM-DD>          # print the read calendar
  w1w2_read.py read --vc N --lead N --days 7|14 # verdict on a LOCKED post-fix window

Rule: baseline VC->Lead 3.55% (11/16-11/25, caps regime). "Lift confirmed" when
leads >= VC*p + 1.28*sqrt(VC*p). Day 7 is directional; day 14 is the main read.
Counts are browser+server events (noise ~sqrt2 larger) -> confidence is an upper bound.
"""
import argparse, datetime as dt, math, sys

P = 0.0355

def dates(day0):
    d0 = dt.date.fromisoformat(day0)
    f = lambda n: (d0 + dt.timedelta(days=n)).isoformat()
    print(f"Day 0 (first full PT day after the edit): {f(0)}")
    print(f"Day-7 window  PT {f(0)} .. {f(6)}  -> lock/read on or after {f(9)} (>=3 d after end)")
    print(f"Day-14 window PT {f(0)} .. {f(13)} -> lock/read on or after {f(16)}")
    print(f"W3 earliest (after d14 locked, guardrail Form/VC >= 4.2%): {f(16)}")

def read(vc, lead, days):
    exp = vc * P
    line = exp + 1.28 * math.sqrt(exp)
    rate = lead / vc * 100 if vc else 0
    if lead >= line:
        v = "LIFT CONFIRMED" + (" (directional; day 14 decides)" if days == 7 else "")
    elif lead >= exp:
        v = "UNPROVEN" + (" -> extend to day 14" if days == 7 else " -> site fix kept (no-regret), no lift claim")
    else:
        v = "NO LIFT -> site wasn't the leak; look upstream (cost per LPV)"
    print(f"Day {days}: VC {vc:,} / Lead {lead} = {rate:.2f}% vs base {P*100:.2f}% (calc)")
    print(f"Expected {exp:.1f}, lift line {line:.1f} -> {v}")
    print("Cross-check: Meta 7d CPL + Meta leads/LPV same window; log confounders (activity log, Wave 1, budget).")

ap = argparse.ArgumentParser()
sp = ap.add_subparsers(dest="cmd", required=True)
a = sp.add_parser("dates"); a.add_argument("day0")
b = sp.add_parser("read"); b.add_argument("--vc", type=int, required=True)
b.add_argument("--lead", type=int, required=True); b.add_argument("--days", type=int, choices=[7, 14], required=True)
x = ap.parse_args()
dates(x.day0) if x.cmd == "dates" else read(x.vc, x.lead, x.days)

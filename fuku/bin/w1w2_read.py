#!/usr/bin/env python3
"""W1/W2 site-fix lift read (rule pre-written 11/27 in fab_advertising/reports/w1w2_lift_template.md).

Usage:
  w1w2_read.py day0 "<edit time WIB, YYYY-MM-DD HH:MM>"   # edit time -> day 0 + read calendar
  w1w2_read.py dates <day0 YYYY-MM-DD>                      # read calendar only
  w1w2_read.py read --rows FILE --day0 D --days 7|14 [--today-pt D]
        # FILE: one line per PT day copied from ONE ads_get_dataset_stats call
        #       (aggregation=event, granularity=day): "YYYY-MM-DD,VC,Lead" (# comments ok).
        # Must hold baseline 11/16-11/25 AND the post-fix window (same call, lessons 11/27).
  w1w2_read.py read --vc N --lead N --days 7|14           # legacy: hand-summed window

Rule: baseline VC->Lead 3.55% (11/16-11/25, caps regime). "Lift confirmed" when
leads >= VC*p + 1.28*sqrt(VC*p). Day 7 is directional; day 14 is the main read.
With --rows, p = max(3.55%, same-call re-pulled baseline): counts get revised up
after the day, so a fresher baseline can only make the bar harder, never easier.
Counts are browser+server events (noise ~sqrt2 larger) -> confidence is an upper bound.
Exit: 0 lift confirmed, 2 unproven, 3 no lift, 1 input error / window not lockable.
"""
import argparse, datetime as dt, math, sys
from zoneinfo import ZoneInfo

P = 0.0355
BASE = ("2026-11-16", "2026-11-25")
WIB, PT = ZoneInfo("Asia/Jakarta"), ZoneInfo("America/Los_Angeles")
D = dt.date.fromisoformat

def die(m):
    print("ERROR: " + m); sys.exit(1)

def dates(day0):
    d0 = D(day0)
    f = lambda n: (d0 + dt.timedelta(days=n)).isoformat()
    print(f"Day 0 (first full PT day after the edit): {f(0)}")
    print(f"Day-7 window  PT {f(0)} .. {f(6)}  -> lock/read on or after {f(9)} (>=3 d after end)")
    print(f"Day-14 window PT {f(0)} .. {f(13)} -> lock/read on or after {f(16)}")
    print(f"W3 earliest (after d14 locked, guardrail Form/VC >= 4.2%): {f(16)}")

def day0(ts):
    try:
        t = dt.datetime.strptime(ts, "%Y-%m-%d %H:%M").replace(tzinfo=WIB)
    except ValueError:
        die('edit time must be "YYYY-MM-DD HH:MM" (WIB)')
    p = t.astimezone(PT)
    d = p.date() + dt.timedelta(days=1)  # first FULL PT day after the edit
    print(f"Edit {ts} WIB = {p:%Y-%m-%d %H:%M} PT ({p.tzname()})")
    dates(d.isoformat())
    print(f"Next: `w1w2_read.py read --rows <file> --day0 {d} --days 7` on/after {d + dt.timedelta(days=9)}")

def verdict(vc, lead, days, p):
    exp = vc * p
    line = exp + 1.28 * math.sqrt(exp)
    rate = lead / vc * 100 if vc else 0
    if lead >= line:
        v, code = "LIFT CONFIRMED" + (" (directional; day 14 decides)" if days == 7 else ""), 0
    elif lead >= exp:
        v, code = "UNPROVEN" + (" -> extend to day 14" if days == 7 else " -> site fix kept (no-regret), no lift claim"), 2
    else:
        v, code = "NO LIFT -> site wasn't the leak; look upstream (cost per LPV)", 3
    print(f"Day {days}: VC {vc:,} / Lead {lead} = {rate:.2f}% vs base {p*100:.2f}% (calc)")
    print(f"Expected {exp:.1f}, lift line {line:.1f} -> {v}")
    print("Cross-check: Meta 7d CPL + Meta leads/LPV same window; log confounders (activity log, Wave 1, budget).")
    return code

def load(path):
    rows = {}
    for n, ln in enumerate(open(path), 1):
        ln = ln.split("#")[0].strip()
        if not ln:
            continue
        try:
            d, vc, ld = [x.strip() for x in ln.split(",")]
            d = D(d); vc = int(vc.replace("_", "")); ld = int(ld.replace("_", ""))
        except ValueError:
            die(f"line {n}: want YYYY-MM-DD,VC,Lead -> {ln!r}")
        if d in rows:
            die(f"line {n}: duplicate day {d}")
        rows[d] = (vc, ld)
    return rows

def span(rows, a, b, label):
    days = [a + dt.timedelta(days=i) for i in range((b - a).days + 1)]
    miss = [x.isoformat() for x in days if x not in rows]
    if miss:
        die(f"{label} missing PT day(s): {', '.join(miss)}")
    return sum(rows[x][0] for x in days), sum(rows[x][1] for x in days)

def read_rows(a):
    rows = load(a.rows)
    d0 = D(a.day0); end = d0 + dt.timedelta(days=a.days - 1)
    today = D(a.today_pt) if a.today_pt else dt.datetime.now(PT).date()
    if today < end + dt.timedelta(days=3):
        die(f"window ends {end}; lockable on/after {end + dt.timedelta(days=3)} (today PT {today}). Provisional only.")
    bvc, bld = span(rows, D(BASE[0]), D(BASE[1]), "baseline")
    tvc, tld = span(rows, d0, end, "post-fix window")
    bp = bld / bvc if bvc else 0
    p = max(P, bp)
    print(f"Baseline PT {BASE[0]}..{BASE[1]} (same call): VC {bvc:,} / Lead {bld} = {bp*100:.2f}% (calc); rule base 3.55%")
    if bp > P:
        print(f"  -> re-pulled baseline is higher: bar uses {bp*100:.2f}% (revisions only make it harder)")
    print(f"Post-fix PT {d0}..{end}: summed {a.days} rows")
    return verdict(tvc, tld, a.days, p)

ap = argparse.ArgumentParser()
sp = ap.add_subparsers(dest="cmd", required=True)
z = sp.add_parser("day0"); z.add_argument("edit_wib")
a = sp.add_parser("dates"); a.add_argument("day0")
b = sp.add_parser("read"); b.add_argument("--vc", type=int); b.add_argument("--lead", type=int)
b.add_argument("--rows"); b.add_argument("--day0"); b.add_argument("--today-pt")
b.add_argument("--days", type=int, choices=[7, 14], required=True)
x = ap.parse_args()
if x.cmd == "day0":
    day0(x.edit_wib)
elif x.cmd == "dates":
    dates(x.day0)
elif x.rows:
    if not x.day0:
        die("--rows needs --day0")
    sys.exit(read_rows(x))
elif x.vc is not None and x.lead is not None:
    sys.exit(verdict(x.vc, x.lead, x.days, P))
else:
    die("read needs --rows FILE --day0 D, or --vc N --lead N")

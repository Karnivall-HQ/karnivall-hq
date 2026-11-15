# PEIKIRA budget-change guard check (Fuku, 2026-11-15 12:02).
# Rules from fab_advertising/reports/2026-11-18_budget_change_read_card.md (written before data, do not edit here):
#   G-a: PEIKIRA spend > Rp 1,000,000 in one day with CPL > Rp 130,000           -> RISK line on OUTBOX #1
#   G-b: PEIKIRA spend >= Rp 285,000 in a FULL day with <= 1 lead, 2 days in a row -> same line
# Input: one --day per date, PEIKIRA campaign totals (sum of the 3 ad sets) or per ad set (repeat the date,
#   rows with the same date are summed). Add :partial with the WIB hour of the pull for an intraday row.
#   python3 fuku/bin/peikira_guard.py --day 2026-11-14:309404:3 --day 2026-11-15:138427:1:partial@7
#   python3 fuku/bin/peikira_guard.py --day 2026-11-15:150000:1 --day 2026-11-15:90000:0   (ad-set rows)
# Partial days: G-a is checked on actuals (a partial day over 1M already trips it); G-b never uses a partial day.
# The pace line (spend x 24/hour) is a projection *(calc)*, not a metric (playbook §A.5: never judge intraday).
import argparse
from collections import OrderedDict

ap = argparse.ArgumentParser()
ap.add_argument("--day", action="append", required=True,
                help="DATE:SPEND:LEADS[:partial@HOUR], e.g. 2026-11-15:138427:1:partial@7")
a = ap.parse_args()

days = OrderedDict()
for raw in a.day:
    parts = raw.split(":")
    date, spend, leads = parts[0], float(parts[1]), int(parts[2])
    hour = None
    if len(parts) > 3:
        assert parts[3].startswith("partial@"), f"bad 4th field in {raw}"
        hour = int(parts[3].split("@")[1])
    d = days.setdefault(date, {"s": 0.0, "l": 0, "hour": None})
    d["s"] += spend; d["l"] += leads
    if hour is not None:
        d["hour"] = hour

GA_SPEND, GA_CPL, GB_SPEND, GB_LEADS = 1_000_000, 130_000, 285_000, 1
rp = lambda x: f"Rp {x:,.0f}"
trips = []
gb_streak = 0
for date in sorted(days):
    d = days[date]
    s, l, hour = d["s"], d["l"], d["hour"]
    cpl = s / l if l else float("inf")
    cpl_txt = rp(cpl) if l else "no leads"
    tag = f"partial to {hour:02d}:00" if hour is not None else "full day"
    line = f"{date} ({tag}): {rp(s)} / {l} = {cpl_txt} *(calc)*"
    if hour:
        line += f" | pace ≈ {rp(s * 24 / hour)}/day *(calc, projection)*"
    ga = s > GA_SPEND and cpl > GA_CPL
    if hour is None:
        gb_day = s >= GB_SPEND and l <= GB_LEADS
        gb_streak = gb_streak + 1 if gb_day else 0
    else:
        gb_day = None
    gb = gb_streak >= 2 and hour is None
    flags = []
    if ga: flags.append("G-a TRIPPED"); trips.append(f"G-a {date}")
    if gb: flags.append("G-b TRIPPED (2nd full day ≥ Rp 285k with ≤ 1 lead)"); trips.append(f"G-b {date}")
    elif gb_day: flags.append("G-b day 1 of 2")
    print(line + ("  ->  " + "; ".join(flags) if flags else "  ->  ok"))

print()
if trips:
    print("VERDICT: TRIPPED (" + ", ".join(trips) + ")")
    print('OUTBOX #1 line: "⚠️ guard ' + ", ".join(trips) + ': back to Rp 300k today (read card G-a/G-b)."')
else:
    print("VERDICT: no guard tripped. One status line on OUTBOX #1 at most; no new ask.")

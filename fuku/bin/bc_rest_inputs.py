#!/usr/bin/env python3
"""Turn one read-only BC entities pull into the exact `bc_ladder_read.py` command (Fuku, 2026-11-28 09:01 WIB).

Why: the W0 daily read needs --rest = BC total - 204 - 3-21 - N2, done by hand each 07:00 readout. This makes it
one paste. Pure arithmetic, no MCP calls, no thresholds (those live only in bc_ladder_read.py / the ladder card).

Inputs come from ONE read-only `ads_get_ad_entities` call on BC campaign 120236222888610572 (ad-set level, window =
since the cap change, full days only; day 1 split at the edit time, meta-modelling-and-planning.md §D3) plus the
204F ad row (only needed from day 14, for --parent):

  python3 fuku/bin/bc_rest_inputs.py --day 3 --bc-total 420000:6 --fab7d 1500000:17 \
      --set 120246071060620572:60000:1 --set 120250479689810572:90000:1 \
      --set "BC-W0-N2 204F Kartu JKTcity:40000:0" [--parent 30000:0]

--set ID_OR_NAME:SPEND:LEADS  repeatable; pass every ad-set row you have (unknown rows are ignored, they stay in rest)
  204  = id 120246071060620572 or a name containing "BC204"
  3-21 = id 120250479689810572 or a name containing "BC3-21"
  N2   = a name containing "W0-N2"
Exit 0 = command printed, 1 = input error (missing ladder row, rest < 0, bad format).
"""
import argparse, sys

IDS = {"120246071060620572": "204", "120250479689810572": "3-21"}
NAME_KEYS = (("W0-N2", "n2"), ("BC204", "204"), ("BC3-21", "3-21"))  # N2 first: its name may contain "204F"


def pair(t, what):
    try:
        s, l = t.rsplit(":", 1)
        return float(s), int(l)
    except ValueError:
        sys.exit(f"input error: {what} must be SPEND:LEADS, got {t!r}")


def key_of(label):
    if label in IDS:
        return IDS[label]
    for needle, k in NAME_KEYS:
        if needle.lower() in label.lower():
            return k
    return None


ap = argparse.ArgumentParser()
ap.add_argument("--day", type=int, required=True)
ap.add_argument("--bc-total", required=True)
ap.add_argument("--fab7d", required=True)
ap.add_argument("--set", action="append", default=[])
ap.add_argument("--parent", help="204F ad SPEND:LEADS, same window as N2 (day 14 only)")
a = ap.parse_args()

found, ignored = {}, []
for raw in a.set:
    try:
        label, s, l = raw.rsplit(":", 2)
        s, l = float(s), int(l)
    except ValueError:
        sys.exit(f"input error: --set must be ID_OR_NAME:SPEND:LEADS, got {raw!r}")
    k = key_of(label)
    if k is None:
        ignored.append(label)
        continue
    if k in found:
        sys.exit(f"input error: two rows map to {k} ({found[k][0]!r}, {label!r})")
    found[k] = (label, s, l)

missing = [k for k in ("204", "3-21") if k not in found]
if missing:
    sys.exit(f"input error: no row for ladder set(s) {', '.join(missing)}; a 0-spend set is still a row (KEY:0:0)")

ts, tl = pair(a.bc_total, "--bc-total")
pair(a.fab7d, "--fab7d")
used_s = sum(v[1] for v in found.values())
used_l = sum(v[2] for v in found.values())
rs, rl = ts - used_s, tl - used_l
if rs < -1 or rl < 0:  # Rp 1 slack for rounding in the tool output
    sys.exit(f"input error: rest < 0 (BC {ts:,.0f} / {tl} − rows {used_s:,.0f} / {used_l}): window mismatch?")
rs = max(rs, 0.0)

print(f"BC total Rp {ts:,.0f} / {tl} · ladder+N2 Rp {used_s:,.0f} / {used_l} · rest Rp {rs:,.0f} / {rl} *(calc)*")
if "n2" not in found:
    print("⚠️ no N2 row: N2 not built yet? (ladder card step 3 → OUTBOX one-liner, no new ask)")
if a.day >= 14 and "n2" in found and not a.parent:
    print("⚠️ day ≥ 14 with N2: pass --parent <204F ad SPEND:LEADS> for the N2 comparative")
if ignored:
    print(f"(left in rest: {len(ignored)} other row(s), e.g. 201 control)")

fmt = lambda s, l: f"{s:.0f}:{l}"
cmd = [f"python3 fuku/bin/bc_ladder_read.py --day {a.day}",
       f"--row 204:{fmt(*found['204'][1:])}", f"--row 3-21:{fmt(*found['3-21'][1:])}",
       f"--rest {fmt(rs, rl)}", f"--fab7d {a.fab7d}"]
if "n2" in found:
    cmd.append(f"--n2 {fmt(*found['n2'][1:])}")
if a.parent and "n2" in found:
    cmd.append(f"--parent {a.parent}")
print(" ".join(cmd))

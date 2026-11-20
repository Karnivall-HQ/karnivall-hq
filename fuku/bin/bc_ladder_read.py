# BC cap-ladder post-apply read (Fuku, 2026-11-20 16:02 WIB). Read-only arithmetic, no MCP calls.
# Applies the read rules of fab_advertising/reports/2026-11-20_bc_cap_ladder_card.md ("Read rules (written before
# launch)") exactly. Don't tune thresholds here: they were fixed before data (playbook meta-tests-and-proposals.md).
#
# Fuku pulls inputs with read-only calls at the 07:00 readout (full days only; day 1 split at the edit time, §D3):
#   python3 fuku/bin/bc_ladder_read.py --day 3 \
#     --row 201:120000:2 --row 204:60000:1 --row 208:40000:0 --row 3-21:90000:1 \
#     --rest 400000:6 --fab7d 1500000:17
# --day    full days since the cap change (1..7); verdict only on day >= 7
# --row    KEY:SPEND:LEADS per ladder ad set, cumulative since the change (post-change part of day 1 only)
# --rest   SPEND:LEADS of the untouched rest of BC, same window
# --fab7d  SPEND:LEADS of the whole Fab account, latest full 7 days (account guard)
# --reverted KEY  optional, repeatable: ad sets already reverted (excluded from the group)
import argparse, sys

LADDER = {"201": "BCbatch201 Manny5 `120245708232080572`", "204": "BC204 Manny6 `120246071060620572`",
          "208": "BC208 UGC `120247180846830572`", "3-21": "BC3-21 Anak Tele c10 `120250479689810572`"}
TARGET, OLD_CAP = 95_000, 94_250
KILL0, KILL1 = 2 * TARGET, 3 * TARGET          # >= 190k with 0 leads; >= 285k with <= 1 lead
COMP_X, VERDICT_SPEND = 1.3, 3 * TARGET        # comparative 1.3x and > 95k; day-7 needs >= 285k group spend
rp = lambda x: f"Rp {x:,.0f}"
cpl = lambda s, l: s / l if l else float("inf")
fmt = lambda s, l: f"{rp(s)} / {l} = {rp(cpl(s, l)) if l else 'n/a (0 leads)'}"

ap = argparse.ArgumentParser()
ap.add_argument("--day", type=int, required=True)
ap.add_argument("--row", action="append", required=True)
ap.add_argument("--rest", required=True)
ap.add_argument("--fab7d", required=True)
ap.add_argument("--reverted", action="append", default=[])
a = ap.parse_args()

pair = lambda t: (float(t.split(":")[0]), int(t.split(":")[1]))
out, revert_one, revert_all = [], [], []

# 1. Kill, per ad set
gs, gl = 0.0, 0
for raw in a.row:
    k, s, l = raw.split(":")
    s, l = float(s), int(l)
    name = LADDER.get(k, k)
    if k in a.reverted:
        out.append(f"Kill ➖ {name}: already reverted, out of the group")
        continue
    if (l == 0 and s >= KILL0) or (l <= 1 and s >= KILL1):
        out.append(f"Kill ❌ {name}: {fmt(s, l)} → revert this ad set to {rp(OLD_CAP)}")
        revert_one.append(k)
    else:
        out.append(f"Kill ✅ {name}: {fmt(s, l)} *(calc)*")
    gs += s; gl += l

rs, rl = pair(a.rest)
fs, fl = pair(a.fab7d)
g_cpl, r_cpl, f_cpl = cpl(gs, gl), cpl(rs, rl), cpl(fs, fl)

# 2. Comparative (a 0-lead group is only readable once it spent >= the 190k kill line; before that inf CPL is noise)
readable = gl > 0 or gs >= KILL0
if not readable:
    out.append(f"Comparative ➖ group {fmt(gs, gl)}: too early to compare (< {rp(KILL0)} with 0 leads)")
elif rl == 0:
    out.append(f"Comparative ⚠️ rest of BC {fmt(rs, rl)}: no baseline CPL → compare on the next readout")
else:
    ratio = g_cpl / r_cpl
    bad = ratio > COMP_X and g_cpl > TARGET
    out.append(f"Comparative {'❌' if bad else '✅'} group {fmt(gs, gl)} vs rest {fmt(rs, rl)} → {ratio:.2f}× *(calc)*"
               + (" → revert all four" if bad else ""))
    if bad:
        revert_all.append("comparative")

# 3. Account guard
guard = readable and f_cpl > TARGET and g_cpl > TARGET
out.append(f"Guard {'❌' if guard else '✅'} Fab 7d {fmt(fs, fl)} *(calc)*; group {rp(g_cpl) if gl else 'n/a'}"
           + (" → both > 95k, the ladder is the cause → revert all four" if guard else ""))
if guard:
    revert_all.append("account guard")

print(f"BC cap ladder read, day {a.day}/7 (full days since the change)")
print("\n".join(out))
print()

if revert_all:
    print(f"VERDICT: REVERT ALL ({', '.join(revert_all)}). Proposed change for Alvian/Markus: set the bid cap back to "
          f"{rp(OLD_CAP)} on every ladder ad set still at 105,000. Re-base day per playbook §D.")
    sys.exit(2)
if revert_one:
    print(f"VERDICT: REVERT {', '.join(revert_one)} only (kill rule). Proposed change: cap back to {rp(OLD_CAP)} on "
          "those ad sets; the rest keep running.")
    sys.exit(1)
if a.day < 7:
    print("VERDICT: RUNNING. No change; next read at the next 07:00 readout.")
    sys.exit(0)
# 4. Day-7 verdict (group)
if gs < VERDICT_SPEND:
    print(f"VERDICT (day 7): CLOSE LEVER. Group spent {rp(gs)} < {rp(VERDICT_SPEND)} → the cap wasn't the limiter. "
          "Revert nothing, record it in MISSIONS + lessons.")
elif g_cpl <= TARGET:
    print(f"VERDICT (day 7): KEEP. Group {fmt(gs, gl)} *(calc)* ≤ 95k on ≥ {rp(VERDICT_SPEND)} spend.")
else:
    print(f"VERDICT (day 7): REVERT ALL. Group {fmt(gs, gl)} *(calc)* > 95k. Proposed change: caps back to {rp(OLD_CAP)}.")
    sys.exit(2)

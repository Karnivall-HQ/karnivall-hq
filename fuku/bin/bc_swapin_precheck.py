# BC Wave 0 swap-in pre-check (Fuku, 2026-11-20 15:02 WIB). Read-only. Runs C1-C4 of
# fab_advertising/creatives/2026-11-20_bc_wave0_markus_sheet.md §0 in one pass, then prints the one-line ask
# (or why not to ask). Rules come from the cap-ladder card (written before data, don't tune them here).
#
# Fuku pulls the inputs with read-only MCP calls first (see the sheet §0b), then:
#   python3 fuku/bin/bc_swapin_precheck.py \
#     --log-edits 0 \
#     --row 201:94250:611993:11 --row 204:94250:376353:7 --row 208:94250:363096:6 --row 3-21:94250:637441:9 \
#     --bc7d 679253:12
# --log-edits  number of human (non-Meta) BC entries in the activity log since 2026-11-12 (C1)
# --row        KEY:CAP:SPEND:LEADS per ladder ad set, CAP = current bid (C2), SPEND/LEADS = 8 weekly rows to the
#              latest full day (C4, same window shape as the card: object_ids, time_increment 7)
# --bc7d       BC campaign 7d SPEND:LEADS (latest full 7 days): budget-binding check (CBO Rp 5M)
# --page FILE  optional saved HTML; default = live curl of the landing page (C3)
import argparse, re, subprocess, sys

LADDER = {"201": "BCbatch201 Manny5 `120245708232080572`", "204": "BC204 Manny6 `120246071060620572`",
          "208": "BC208 UGC `120247180846830572`", "3-21": "BC3-21 Anak Tele c10 `120250479689810572`"}
OLD_CAP, NEW_CAP, RATIO_MAX, BC_BUDGET = 94_250, 105_000, 0.85, 5_000_000
URL = "https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/"
rp = lambda x: f"Rp {x:,.0f}"

ap = argparse.ArgumentParser()
ap.add_argument("--log-edits", type=int, required=True)
ap.add_argument("--row", action="append", required=True)
ap.add_argument("--bc7d", required=True)
ap.add_argument("--page")
a = ap.parse_args()

out, blockers = [], []

# C1 activity log
if a.log_edits == 0:
    out.append("C1 ✅ BC activity log: no human edits since 11/12")
else:
    out.append(f"C1 ❌ BC activity log: {a.log_edits} human edit(s) since 11/12 → re-base first (playbook §D), no ask this run")
    blockers.append("C1")

# C3 page price
if a.page:
    html = open(a.page, encoding="utf-8", errors="ignore").read()
else:
    html = subprocess.run(["curl", "-sL", "--max-time", "30", URL], capture_output=True, text=True).stdout
text = re.sub(r"<[^>]+>", " ", html)
promo = len(re.findall(r"Promo Launching", text))
p750 = len(re.findall(r"Rp ?750(?:\.000|rb)", text))
p800 = len(re.findall(r"Rp ?800(?:\.000|rb)", text))
if not text.strip():
    out.append("C3 ⚠️ page fetch empty → re-run, don't ask on an unchecked page")
    blockers.append("C3")
elif promo and p750 >= p800:
    out.append(f"C3 ✅ page: 'Promo Launching' ×{promo}, Rp750 ×{p750}, Rp800 ×{p800} (tags stripped) → cards/body stay at 750")
else:
    out.append(f"C3 ❌ page: 'Promo Launching' ×{promo}, Rp750 ×{p750}, Rp800 ×{p800} → swap card 5 + body to 'mulai Rp800rb/bulan' first")
    blockers.append("C3")

# C2 + C4 per ad set
keep, grp_s, grp_l = [], 0.0, 0
for raw in a.row:
    k, cap, s, l = raw.split(":")
    cap, s, l = int(cap), float(s), int(l)
    name = LADDER.get(k, k)
    if cap != OLD_CAP:
        out.append(f"C2 ➖ {name}: cap now {rp(cap)} (not {rp(OLD_CAP)}) → drop row (already changed)")
        continue
    if l == 0:
        out.append(f"C4 ❌ {name}: {rp(s)} / 0 leads → drop row")
        continue
    cpl = s / l
    r = cpl / OLD_CAP
    ok = r < RATIO_MAX
    out.append(f"C2 ✅ C4 {'✅' if ok else '❌'} {name}: {rp(s)} / {l} = {rp(cpl)} *(calc)*, CPL ÷ cap {r:.2f}"
               + ("" if ok else " → drop row"))
    if ok:
        keep.append(k); grp_s += s; grp_l += l

# budget must not bind
bs, bl = a.bc7d.split(":")
bs, bl = float(bs), int(bl)
share = bs / 7 / BC_BUDGET
binds = share > 0.8
out.append(f"Budget {'❌' if binds else '✅'} BC 7d {rp(bs)} / {bl} = {rp(bs / 7)}/day = {share:.2%} of Rp 5M *(calc)*"
           + (" → budget binds, a cap raise won't add volume; re-think" if binds else " → cap is the limiter"))
if binds:
    blockers.append("budget")

print("\n".join(out))
print()
if blockers:
    print(f"VERDICT: HOLD ({', '.join(blockers)} failed). Don't ask; fix/re-base per the line above.")
    sys.exit(1)
if not keep:
    print("VERDICT: ladder empty → ask N2 only: \"Build N2 in BC? Sheet §2a/§2b ready.\"")
    sys.exit(0)
print(f"Ladder group: {rp(grp_s)} / {grp_l} = {rp(grp_s / grp_l)} *(calc)* over {len(keep)} ad set(s): {', '.join(keep)}")
print("VERDICT: ASK. One line for OUTBOX (swap in for the weaker of #2/#3):")
print(f"  ❓ [DECISION] Build N2 in BC + raise the bid cap {OLD_CAP:,} → {NEW_CAP:,} on {len(keep)} BC ad set(s) "
      f"({', '.join(keep)}; group {rp(grp_s / grp_l)} CPL *(calc)*)? Sheet: "
      "`fab_advertising/creatives/2026-11-20_bc_wave0_markus_sheet.md`. Recommendation: yes. Reply \"W0 done\".")

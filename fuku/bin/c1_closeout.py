#!/usr/bin/env python3
"""M-001 criterion 1 close-out (12/05 judge, window 11/28-12/04).

Feed the locked days of the judged window; prints leads still needed,
a Poisson chance of a miss at the current BC lead rate, and the pre-written
readout line. All outputs are *(calc)*.

  python3 fuku/bin/c1_closeout.py --locked SPEND LEADS DAYS [--rate SPEND_PER_DAY] [--cpl BASE_CPL]
  --locked 0 0 0  = nothing locked yet (pre-window forecast)
  --w1 YYYY-MM-DD | none   W1 (016 + 018) launch date, for the criterion-2 line

Criterion 2 (Rp 1M/day) uses the SAME window spend (base = 7d spend / 7), and
the honest-date offsets from criterion2_replan.md 11/27 12:01 (W1 12/01 ->
good 01/19, mid 02/16, low 03/30 = W1 + 49 / 77 / 119 days).
"""
import argparse, math, datetime as dt

TARGET = 95_000
WINDOW_DAYS = 7

def poisson_cdf(k, mu):
    if k < 0:
        return 0.0
    return sum(math.exp(-mu) * mu**i / math.factorial(i) for i in range(k + 1))

p = argparse.ArgumentParser()
p.add_argument("--locked", nargs=3, type=float, metavar=("SPEND", "LEADS", "DAYS"), required=True)
p.add_argument("--rate", type=float, default=140_963, help="spend/day for unlocked days (default 7d 11/21-11/27 = 986,743/7; pass the latest 7d at each readout)")
p.add_argument("--cpl", type=float, default=65_783, help="expected CPL for unlocked days (default 7d 11/21-11/27 65.8k; pass the latest 7d at each readout)")
p.add_argument("--w1", default=None, help="W1 launch date YYYY-MM-DD, or 'none' if not live")
p.add_argument("--paste", action="store_true", help="12/05 only (7 days locked, needs --w1 and --lever): print the filled branch A/B/C report + MISSIONS line from 2026-12-05_criterion1_path.md")
p.add_argument("--lever", choices=["W0", "W1", "site"], help="open volume lever named in branch B/C asks (W0 if still open, else W1/site)")
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
def k(x):  # Rp -> "65.8k"; 0 leads -> no fake number
    return "n/a (0 leads)" if x == float("inf") else f"{x/1000:.1f}k"

print(f"Window 11/28-12/04: locked {d_lock}d Rp {s_lock:,.0f} / {l_lock}; {d_left}d left at Rp {a.rate:,.0f}/day")
print(f"Projected 7d spend Rp {s_total:,.0f} -> needs >= {need_total} leads in the window (95k line) *(calc)*")
print(f"Leads still needed: {need_left} in {d_left}d; expected {mu:.1f} at {a.cpl/1000:.1f}k CPL *(calc)*")
print(f"Projected 7d CPL {k(proj)}; P(miss) = {p_miss*100:.0f}% (Poisson, INFERRED) *(calc)*")
if d_left == 0:
    cpl = s_lock / l_lock if l_lock else float("inf")
    ok = cpl <= TARGET
    print(f"VERDICT LINE: M-001 criterion 1 {'MET ✅' if ok else 'MISSED ❌'} on 12/05: 7d 11/28-12/04 Rp {s_lock:,.0f} / {l_lock} = {k(cpl)} *(calc)* vs 95k.")
elif need_left == 0:
    print("STATUS LINE: criterion 1 already safe unless spend jumps (more spend with 0 leads can still lift it; re-run if spend/day > 1.3x rate).")
else:
    print(f"STATUS LINE: criterion 1 needs {need_left} more leads in {d_left}d (expected {mu:.1f}); P(miss) {p_miss*100:.0f}% *(calc)*.")

# ---- criterion 2 line (same window numbers) ----
LEG = 1_000_000
OFFSETS = {"good": 49, "mid": 77, "low": 119}  # days after W1 launch (replan 11/27 12:01)
if a.w1 is not None:
    base = s_total / WINDOW_DAYS
    tag = "7d 11/28-12/04" if d_left == 0 else f"window proj ({d_lock}d locked)"
    if a.w1.lower() == "none":
        date_txt = "honest date not set: W1 not live (each week of delay = +7 days; from a 12/08 start mid 02/23)"
    else:
        w1 = dt.date.fromisoformat(a.w1)
        d = {k: (w1 + dt.timedelta(days=v)).strftime("%m/%d") for k, v in OFFSETS.items()}
        date_txt = f"honest date mid {d['mid']} (good {d['good']}, low {d['low']}) with W1 live {w1.strftime('%m/%d')}"
    if d_left == 0:
        verdict = ("MISSED ❌" if base < LEG else "MET ✅ (check 7d CPL ~95k)") + " on 12/05"
    else:  # before the window closes: a projection, never a past-tense verdict
        verdict = ("projected MISS ❌" if base < LEG else "projected MET (check 7d CPL ~95k)") + " for 12/05"
    print(f"CRITERION 2 LINE: M-001 criterion 2 {verdict}: {tag} Rp {base:,.0f}/day = {base/LEG*100:.0f}% of Rp 1M *(calc)*; {date_txt} *(calc, INFERRED hit rates)*.")

# ---- 12/05 paste block (branch text from 2026-12-05_criterion1_path.md, filled) ----
PRE_RATE = 140_963  # 7d 11/21-11/27 spend/day, the base branch C's "Why" compares against
LEVER_TXT = {
    "W0": "W0 (BC204 + BC3-21 cap 94,250 -> 105,000 + N2, Markus ~10 min)",
    "W1": "W1 (016 + 018 photo-free ads)",
    "site": "site W1+W2 (Jakarta Pusat -> Selatan x9 + FAQ 800 -> 750)",
}
if a.paste:
    if d_left != 0 or a.w1 is None:
        raise SystemExit("--paste needs 7 locked days and --w1")
    cpl = s_lock / l_lock if l_lock else float("inf")
    met = cpl <= TARGET
    if a.lever is None and not (met and a.w1.lower() != "none"):
        raise SystemExit("--paste: branch B/C names the open lever; add --lever W0|W1|site")
    base = s_lock / WINDOW_DAYS
    pct = f"{base/LEG*100:.0f}%"
    head2 = f"Spend Rp {base:,.0f}/day = {pct} of Rp 1M"
    print("\n---- PASTE (OUTBOX M-001 latest report; re-check the 'facts in every branch' list first) ----")
    if met:
        print(f"> 📊 **[REPORT] 12/05 · M-001 deadline: criterion 1 ✅, criterion 2 ❌.**")
        print(f"> ✅ 7d 11/28–12/04 Rp {s_lock:,.0f} / {l_lock} = **{k(cpl)}** vs 95k *(calc)*. ❌ {head2}. Reason: the 11/15 caps hold PEIKIRA at ≈ 0 and BC under 94,250; volume levers unapplied.")
        if a.w1.lower() != "none":
            print(f"> 👉 With W1 live {w1.strftime('%m/%d')}: honest Rp 1M/day date mid **{d['mid']}** (good {d['good']}, low {d['low']}) *(calc, INFERRED hit rates)*.")
            print(f"> ❓ Set criterion 2's new deadline = {d['mid']} (depends on W1 staying live)? My recommendation: yes.")
            print(f"MISSIONS: criterion 1 ✅ met 12/05 ({k(cpl)}); criterion 2 ❌ ({pct} of leg), new date {d['mid']} asked")
        else:
            print("> 👉 No honest date while nothing that adds volume is live: each week W1 waits = +7 days (from a 12/08 start: mid 02/23).")
            print(f"> ❓ Apply {LEVER_TXT[a.lever]}? My recommendation: yes.")
            print(f"MISSIONS: criterion 1 ✅ met 12/05 ({k(cpl)}); criterion 2 ❌ ({pct} of leg), date not set (W1 not live)")
    else:
        ratio = base / PRE_RATE
        why = ("lead count: spend/day stayed within ±30% of 141k "
               f"({ratio:.2f}x) *(calc)*, so the window simply drew too few leads") if 0.7 <= ratio <= 1.3 else (
               f"spend moved to {ratio:.2f}x the 141k/day base *(calc)*: name the change from the activity log here (HAND EDIT)")
        print(f"> ⚠️ **[REPORT] 12/05 · M-001 deadline: both criteria ❌.** 7d Rp {s_lock:,.0f} / {l_lock} = {k(cpl)} vs 95k *(calc)*; spend {pct} of Rp 1M (Rp {base:,.0f}/day).")
        print(f"> Why: {why}.")
        print(f"> ❓ Move criterion 1 to 12/19 (window 12/12–12/18), same 95k, with {LEVER_TXT[a.lever]} live that week? My recommendation: yes, only with the lever (rule 3).")
        print("MISSIONS: both ❌ on 12/05; criterion 1 re-date to 12/19 asked")

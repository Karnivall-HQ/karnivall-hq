# 11/20 07:00 readout: one-page fill-in (gate + ADSET-3 day-7 + message pick)
_Pre-staged 2026-11-13 14:02 WIB by Fuku (cloud heartbeat, groundwork). Read-only, propose-only. Goal: the 11/20 readout is a ~15-minute fill job, no re-thinking._
_Uses: `2026-11-20_s1_scale_card.md` (G1–G3, S1 line), `2026-11-20_gate_miss_note.md` (variants H / M1 / M2 + criterion-2 line), `2026-11-13_adset3_read_card.md` (rules 1–6), `m001_tracker.md`. Playbooks first: `meta-ads-algorithm.md`, `meta-cpl-diagnosis.md`, `meta-tests-and-proposals.md`._

## Step 0: what changed in the week (activity log, by actor_id)
Window 11/13 00:00 → 11/20 07:00 WIB, account `484578521394893`. Fill one line per human change (actor, time, object, old → new).
- Site W1/W2 applied? ☐ no ☐ yes, live since ⟨date HH:MM⟩ (re-curl `/sewa-gudang-self-storage-jakarta/`: "Jakarta Pusat" count ⟨n⟩, "Rp 800.000" count ⟨n⟩). Source: INBOX "W1 W2 done" or curl.
- ADSET-3 min daily spend (Rp 75k) applied? ☐ n/a ☐ no ☐ yes ⟨date⟩
- Ad015 (`120254063163810572`) paused? ☐ no, still ACTIVE ☐ yes, since ⟨date HH:MM⟩ (feeds gate-miss M1 "neither / only Ad015", Variant H cause, G3)
- Any budget / status / bid edit on PEIKIRA or BC: ⟨list or "none"⟩. A change inside the window → note it next to the number it moves; don't "correct" the CPL for it.

## Step 1: pulls (copy numbers from tool output; anything derived gets *(calc)*)
| # | Pull | Args | Fill |
|---|---|---|---|
| P1 | Account 7d | level=campaign, Fab account, time_range **2026-11-13 → 2026-11-19** (full days only), spend + Lead (pixel 405755485775053) | PEIKIRA Rp ⟨⟩ / ⟨⟩ · BC CBO Copy Rp ⟨⟩ / ⟨⟩ |
| P2 | PEIKIRA ad sets 7d | level=adset, `object_ids` control `120254051672430572`, PEIKIRA2 `120254276298070572`, ADSET-3 `120254400251570572`, same window | see Step 2 table |
| P3 | ADSET-3 ads 7d | level=ad, parent ADSET-3, same window, spend / leads / CTR | for rules 5–6 |
| P4 | Ad015 7d | level=ad, same window: CTR, CPL, frequency | Step 3 |
| P5 | Last 3 days | P2 again with time_range **11/17 → 11/19** | G3 + rule 1 |
| P6 | Pixel funnel (only if W1/W2 live) | dataset 405755485775053: LP views → Lead, before vs after the live date | M2 / `w1w2_lift_template.md` |

## Step 2: numbers
- **Account 7d** = (PEIKIRA + BC spend) ÷ (PEIKIRA + BC leads) = Rp ⟨x⟩ *(calc)*; Rp ⟨⟩/day *(calc)*. Prior week: Rp 103,286 (11/06–11/12).

| Ad set | Spend 7d | Leads | CPL *(calc)* | Share of PEIKIRA *(calc)* |
|---|---|---|---|---|
| Control | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩% |
| PEIKIRA2 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩% |
| ADSET-3 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨s⟩% |
| ADSET-3 delivery days d (first day with spend > Rp 5k) | ⟨d⟩ | | break-even at (s, d) from read-card table: ⟨BE⟩ *(calc)* | |

## Step 3: rule checks (tick one per line)
**ADSET-3 (read card):**
- Delivered at all? ☐ yes ☐ **no, < Rp 10k in 7d** (same line as the gate-miss note's "starved" row) → skip rules 1–3, G2 via ADSET-3 = ❌; write "ADSET-3 untested (starved), not a loser" (rule 6) and keep the min-spend ask as the one ad ask.
- Rule 2 early kill (≥ Rp 190k & 0 leads, or ≥ Rp 285k & ≤ 1 lead, cumulative): ☐ ok ☐ **fired on ⟨date⟩**
- **Rule 3 day-7:** ADSET-3 CPL ⟨⟩ vs control CPL ⟨⟩ → ratio ⟨⟩ *(calc)*
  - ≤ 1.00 → **KEEP** · 1.00–1.30 → keep, judge on 11/27 · > 1.30 with ≥ Rp 400k spent → **propose pause** · > 1.30 with < Rp 400k → too little spend, keep
- Rule 5–6 per-ad: ads with ≥ Rp 95k spend: ⟨list CPLs⟩; ads < Rp 5k: ⟨list⟩ = untested.

**Ad015:** CTR ⟨⟩ (< 1.30% = trigger) · CPL ⟨⟩ (> 120k = trigger) · freq ⟨⟩ (> 2.5 = trigger) → ☐ none ☐ ⟨which⟩ → fallback `2026-11-10_ad015_fallback.md`

## Step 4: gate (copy into the S1 card table)
_No model today: the 11/13–11/19 window is closed, so G1 is the actual 7d CPL from P1 (`gate_model_1120.py` stops on purpose with 7 locked days). Model check: 11/19 tracker Notes "model 11/20" ⟨⟩ vs actual ⟨x⟩ → error ⟨⟩ *(calc)*. If the gap is > Rp 10k, add one line to `lessons.md` with the cause (BC flat-rate assumption, the ADSET-3 share, or the PEIKIRA daily rate)._

| | Test | Result |
|---|---|---|
| G1 | account 7d CPL ⟨x⟩ ≤ 95,000 | ☐ ✅ ☐ ❌ |
| G2 | ADSET-3: CPL ≤ control **and** ≤ 95k on ≥ 3 leads · *or* control / PEIKIRA2: 7d ≤ 95k on ≥ 4 leads | ☐ ✅ (⟨which⟩) ☐ ❌ |
| G3 | no kill rule: ADSET-3 rules 1–2 (P2 + P5, cumulative) · Ad015 triggers on P4 (7d), only if Ad015 ACTIVE (paused → n/a; tripped-and-active → S1 card "G3 ❌ only because Ad015" row) | ☐ ✅ ☐ ❌ (⟨rule, date⟩) |

## Step 4b: criterion-1 last workable date (added 2026-11-14 16:01; the 12/05 window is 11/28–12/04)
_Whatever the gate says, the 11/20 note must carry criterion 1's date. Source: `2026-12-05_criterion1_path.md`; method `meta-modelling-and-planning.md` §A1–A2._
1. Run with the P1/P2 numbers (7d 11/13–11/19):
   `python3 fuku/bin/criterion1_model_1205.py --peik ⟨PEIKIRA spend⟩ ⟨leads⟩ --bc ⟨BC spend⟩ ⟨leads⟩ --p2 ⟨PEIKIRA2 spend⟩ ⟨leads⟩ --today 2026-11-20`
   - PEIKIRA2 with < 2 leads → keep the default `--p2 924806 8` and write "p2 = 11/07–11/13 base" next to the line (one lead can't set the freed-spend CPL).
   - A lever **already live** for the whole window is inside the base: read row **A** as "with what's live", and ignore the rows that add that lever again (e.g. W1/W2 live since ≤ 11/13 → ignore every "C" row).
2. Fill one line: base row A ⟨⟩ · F+C +0.5pt ⟨⟩ · **last workable date ⟨mm/dd⟩, days left ⟨n⟩** *(calc)*. If the script prints "NONE" (even 11/27 misses) → write "criterion 1 needs ADSET-3 to win (row F+E) or a move to 12/19", and put the 12/19 question on the 11/27 readout (Step 5b there), not in this note.
3. The line goes, unchanged, into whichever message Step 5 picks (S1 / H / M1 / M2), just before the criterion-2 line (gate-miss note placeholder), and into NOW.md "Current focus".

## Step 5: pick the message (exactly one M-001 "Latest report" in OUTBOX; replaces whichever M-001 report is current)
| G1 | G2 | G3 | Send | Ad ask in "Needs you"? |
|---|---|---|---|---|
| ✅ | ✅ | ✅ | S1 line (`2026-11-20_s1_scale_card.md` bottom) + a short report | yes: PEIKIRA CBO 300k → 375k |
| ✅ | ❌ | any | Variant H (`2026-11-20_gate_miss_note.md`) + ADSET-3 clause + criterion-2 line | no |
| ✅ | ✅ | ❌ | Variant H + tripped rule, re-check 11/23 | no (if ❌ only because Ad015 active: re-send ask #1(a)) |
| ❌ | any | any | W1/W2 not live → **M1**; live → **M2** (+ P6 numbers); both + criterion-2 line | no new ad ask (rule-3 pause / Ad015 fallback only if Step 3 fired) |

Extra asks only if Step 3 fired, ranked under the 3-ask cap: (1) site fix if still open, (2) rule-3 / rule-2 ADSET-3 pause or min-spend, (3) Ad015 fallback. Anything else → Parked.

## Step 6: record (same run)
- `m001_tracker.md`: weekly row for 11-13 → 11-19 (spend, /day, leads, CPL, gate, criterion-1 last workable date (Step 4b), ad-set split, ADSET-3 rule-3 line, Ad015, W1/W2 state); change-log rows from Step 0.
- Read card: "Day-7 read 11/20" line (CPL, ratio, verdict, untested ads). S1 card table ticks.
- MISSIONS.md M-001 progress line; NOW.md: if S1 sent → 3-day read on day 3; else 11/23 G3 re-check / 11/27 ADSET-3 verdict.
- If the criterion-2 line went out: next run with no answer after 24h → keep both criteria unchanged (gate-miss note fill rule).

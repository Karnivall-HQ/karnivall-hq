# 11/27 07:00: ADSET-3 day-14 verdict (fill-in)
_Pre-staged 2026-11-13 16:02 WIB by Fuku (cloud heartbeat, groundwork). Read-only, propose-only: Fuku reads, Alvian/Markus apply._
_Dry-run 2026-11-14 18:01 WIB: every ⟨⟩ / ☐ now maps to a pull row V1–V8 below (gaps found: Step 0 + Step 5 + Step 5b had no named source, V4 was vague, PEIKIRA total, new-ad rows, 0-lead wk1)._
_Rules come from `2026-11-13_adset3_read_card.md` (rules 2–6) and `fuku/memory/playbooks/meta-tests-and-proposals.md`. Read those first, plus `meta-ads-algorithm.md`. Copy every number from tool output; anything derived gets *(calc)*._

## Step 0: context since the 11/20 read
- 11/20 outcome (V7): ☐ S1 ☐ H ☐ M1 ☐ M2 · rule 3 result: ☐ KEEP ☐ pause proposed ☐ applied ⟨date⟩
- Activity log 11/20 → 11/27 (V5, by actor_id): min-spend Rp 75k ☐ never ☐ on ⟨date⟩ ☐ removed ⟨date⟩ · CBO budget ⟨300k / other⟩ · ads added/paused in ADSET-3 ⟨list⟩ · site W1/W2 live since ⟨date / no⟩ (V6).
- **If ADSET-3 was paused at or before 11/20:** skip to Step 4 and write "verdict = loser (rule 2/3)"; per-ad reads only for ads that met rule 5.
- **If V1 shows ADSET-3 14d spend < Rp 10k (still starved): use Branch A below** and skip Steps 2–4 except the V1 row + V4 D.

## Branch A: still starved (pre-written 2026-11-18 09:01 WIB; ADSET-3 Rp 0 for 11/13–11/17, 5 full days)
_Matches the 11/20 gate-miss note's "< Rp 10k spent (still starved)" clause, so the 11/20 and 11/27 messages say the same thing._
- **Verdict = UNDER-TESTED (starved)**, precedence row 4 (rule 2 can't fire at < Rp 190k). Not a loser, not a test result: the 6 ads never entered the auction. Per-ad table, per-look layer, decay check: all **n/a** (every ad < Rp 5k = untested, rule 6). Hit-rate line: "ADSET-3 winners 0 of 0 judged".
- **Cause line (pick by V5):**
  - caps still on (no undo): "Rp 105k bid caps + CBO picking the 2 old ad sets; ADSET-3 shares PEIKIRA2's audience, so it loses every shared auction (INFERRED, 11/15 14:01)."
  - undo applied ⟨date⟩, no min spend: "No cap since ⟨date⟩, but the CBO still put ≈ 0 on it: a starvation problem, not a cap problem (account data from ⟨date⟩)."
  - min spend Rp 75k set and still < Rp 10k: ⚠️ this is a delivery error, not a verdict → run `meta-cpl-diagnosis.md` (ads_get_errors on the 6 ads, review status) before writing anything.
- **Step 5 for Branch A:** no budget step. The 11/20 → 11/27 asks merge into one line; pick by #1 state:
  - #1 still open: no new ask; #1 (undo) stays first. Add to the report: "ADSET-3: Rp ⟨spend⟩ in 14 days, still untested; the min-spend fix waits behind the undo."
  - #1 applied, min spend not set: "❓ Give ADSET-3 (the team's 6 new ads) a Rp 75k daily minimum for 7 days? It got Rp ⟨spend⟩ in 14 days, so it was never tested. Read 12/04 with the same rules. My recommendation: yes; else move the 6 ads into their own ad set with a Rp 75k minimum from day 1." (Replaces #2(b); #2(a) Ad015 goes to Parked if not re-validated on fresh 7d data.)
  - Day-21 re-read 12/04 only if a min spend or own ad set went live; otherwise close the test as "never delivered" and carry the 6 ads into Wave 1 (`2026-11-20_criterion2_replan.md`).
- **Step 5b still runs** with ADSET-3 = not a WINNER (picks the "> 95k, ... ADSET-3 not WINNER" row if projected > 95k).

## Step 1: pulls (window = 14 full days ADSET-3 was live: **2026-11-13 → 2026-11-26**)
| # | Pull | Args |
|---|---|---|
| V1 | ADSET-3 + peers, 14d | level=adset, `object_ids` ADSET-3 `120254400251570572`, control `120254051672430572`, PEIKIRA2 `120254276298070572`; spend, Lead (pixel 405755485775053), CTR, frequency |
| V2 | ADSET-3 ads, 14d | level=ad, parent ADSET-3; spend, leads, CTR, CPM |
| V3 | Week split | V1 with `time_increment` 7 (wk1 = 11/13–11/19, wk2 = 11/20–11/26), **by object_ids** (lesson 2026-11-12: filtered multi-week pulls return zeros) |
| V4 | Delivery start | V1 for ADSET-3 only with `time_increment` 1, 11/13→11/26 → first day spend > Rp 5k; D = days with spend > Rp 5k |
| V5 | Activity log | `ads_account_get_activity_logs` Fab `484578521394893`, since 2026-11-20 00:00 WIB, limit ≤ 40 → group by actor_id (Markus 61594758338050, TourHub 61557670947597): Ad015 status, min spend, CBO budget, ads added/paused in ADSET-3 |
| V6 | Site status | `curl -sL` `/sewa-gudang-self-storage-jakarta/`, grep "Jakarta Pusat", "Rp 800.000" (W1 done = 0 Pusat; W2 done = 0 × 800) |
| V7 | 11/20 outcome | the filled `2026-11-20_readout_template.md` result + MISSIONS M-001 progress line of 11/20 (S1/H/M1/M2, rule 3) |
| V8 | Account 7d base | the 11/27 07:00 row in `m001_tracker.md` (routine step 1: 7d 11/20–11/26 by campaign + PEIKIRA ad sets). Run it first; Step 5 and 5b read from it |
| V1+ | PEIKIRA 14d total | V1 at level=campaign, id `120254051672440572`, same window → denominator of the share line (don't sum ad sets: a 4th ad set may exist) |

## Step 2: numbers
| Ad set | Spend 14d | Leads | CPL *(calc)* | Wk1 CPL | Wk2 CPL | Freq |
|---|---|---|---|---|---|---|
| ADSET-3 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Control | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| PEIKIRA2 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
- ADSET-3 delivery days D = ⟨⟩ of 14 (V4); share of PEIKIRA 14d spend = ⟨⟩% *(calc, V1 ÷ V1+)*.
- Rule 2 cumulative check (for LOSER): 14d spend ⟨⟩ vs Rp 190k with 0 leads / Rp 285k with ≤ 1 lead → ☐ fired ☐ not.

## Step 3: verdict (rule 4, apply as written)
| Verdict | Condition | Meaning |
|---|---|---|
| **WINNER** | 14d CPL **≤ Rp 95k on ≥ 4 leads** | proven engine: counts toward G2 / a criterion-2 step |
| **PROMISING** | CPL ≤ 95k on 2–3 leads, **or** ≤ control's 14d CPL on ≥ 4 leads but > 95k | keep running; re-read on day 21 (12/04) with the same rule. No budget step |
| **UNDER-TESTED** | spend < Rp 380k *(calc: 4 × 95k)* **and none of the rows above/below fired first (see precedence)** | too little spend to call a loser: no verdict. Cause = starvation → min-spend line below; re-read 12/04 |
| **LOSER** | ≥ Rp 380k spent and CPL > 1.3× control 14d CPL, or rule 2 fired | propose pause (budget returns to control + PEIKIRA2) |
| **NEUTRAL** | none of the above (e.g. 96k–1.3× control, ≥ 4 leads) | keep only while it isn't the worst ad set; no step, no extra ask |

**Precedence (overlap check 2026-11-15 21:01, playbook C.1; script tabulated spend 0–1.6M × 0–12 leads at control 90k and 130.9k):** the table as first written gave 2 labels in 408 cells: **WINNER+UNDER-TESTED 333** (every 4-lead win costs ≤ 380k, so "< 380k" swallowed nearly every winner), PROMISING+UNDER-TESTED 47, LOSER(rule 2)+UNDER-TESTED 28. Step 5 sends opposite asks for these (budget step vs min-spend). Apply top-down, first match wins:
1. Rule 2 fired (≥ Rp 190k & 0 leads, or ≥ Rp 285k & ≤ 1 lead) → **LOSER**.
2. ≥ 4 leads & CPL ≤ 95k → **WINNER** (any spend).
3. 2–3 leads & CPL ≤ 95k, or ≥ 4 leads & 95k < CPL ≤ control → **PROMISING**.
4. Spend < Rp 380k → **UNDER-TESTED**.
5. CPL > 1.3× control → **LOSER**.
6. Else → **NEUTRAL**.
Check rows at control 130.9k *(calc)*: 0–1 lead: 100k UNDER, ≥ 300k LOSER(r2) · 2 leads: 100k PROM, 300k UNDER, ≥ 500k LOSER · 4 leads: ≤ 300k WIN, 500k PROM, ≥ 800k LOSER · 6 leads: ≤ 500k WIN, 800k NEUTRAL, 1.2M LOSER. One label in every cell.
**Budget-state gate (added 11/15):** Step 5's "+Rp 100k/day" step assumes the CBO is ~Rp 300k. If V5 shows the CBO still at Rp 3M/day (11/15 change) or a bid cap on ADSET-3, a WINNER gets **no budget ask**; the line becomes "ADSET-3 won under the cap; keep setup" and any open 11/18 undo ask outranks it.

Decay check (WINNER/PROMISING only; n/a if wk1 had 0 leads or < Rp 95k spend): wk2 CPL > 1.5× wk1 CPL → label "decaying", count it as a winner for ≤ 1 more week (control went 81k → 173k in one week, scale plan v2) [account data].

## Step 4: per-ad keep/cut list (rule 5: only ads with ≥ Rp 95k spend; rule 6: < Rp 5k = untested)
| Ad | Spend | Leads | CPL *(calc)* | CTR | Call |
|---|---|---|---|---|---|
| FAB-20261109-003 (L3 graphic) | | | | | ⟨keep / cut / untested⟩ |
| FAB-20261109-007 (L3 graphic) | | | | | |
| FAB-20261109-010 v03 (L4 render-look) | | | | | |
| FAB-20261109-018 (L2 facility) | | | | | |
| FAB-20261109-S30 v04 (L1b home, text) | | | | | |
| AKIRA-FAB-20261103-016 (L1a home + stickers) | | | | | |
- Rows come from V2: any ad in V2 not listed above (team swaps/adds) gets its own row; a listed ad missing from V2 = "deleted/paused ⟨date from V5⟩". Spend basis = 14d; < Rp 5k in 14d = untested (rule 6).
- **Cut** = ≥ Rp 190k (2× target) with 0 leads, or CPL > 1.5× the ad set's CPL on ≥ Rp 190k. Max 2 cuts per read (limits CBO re-learning; INFERRED). Ads under Rp 95k: no call.
- **Per-look layer (read card rules 7–11, added 11/15):** map ads → looks L1–L4 via `ads_get_creatives` first, then one line per look: spend ⟨⟩ · leads ⟨⟩ · CPL ⟨⟩ *(calc)* · label ⟨works / fails / unclear / untested⟩. "Photo wave" verdict = L1a + L1b + L2 pooled only. Looks pre-mapped 11/15 17:02 (one look per ad); re-map only if V2 shows new creative IDs.
- **Keep-angle note:** for each kept ad, note subject + hook (e.g. "raw unit photo + Rp750rb") → feeds the next wave's build sheet (`2026-11-20_criterion2_replan.md`, Waves 1–6).

## Step 5: what each verdict unlocks (proposal only; Alvian/Markus apply)
- Account 7d = V8 (Fab, 11/20–11/26). CBO budget now = V5 (else Rp 300k).
- **WINNER + account 7d ≤ 95k:** one step of +Rp 100k/day on the PEIKIRA CBO (criterion-2 re-plan "Budget steps"), with the S1 card's 3-day read (≤ 110k → next step allowed; 110–125k hold; > 125k with ≥ Rp 1.1M spent → revert). If S1 already ran on 11/20, this is S2. Remove the min spend if still set.
- **WINNER, account 7d > 95k:** no budget step. Ask instead: pause the worst PEIKIRA ad set by 14d CPL (≥ 1.3× ADSET-3's) so the winner gets its share at the same Rp 300k.
- **PROMISING / UNDER-TESTED:** no ask, unless UNDER-TESTED with no min spend set → one-line ask: min daily spend Rp 75k for 7 more days.
- **LOSER:** one-line pause ask; next photo wave goes into its own ad set with min spend from day 1 (re-plan risk "CBO starvation").
- **Any verdict:** update the re-plan hit rate: ADSET-3 winners ⟨n⟩ of ⟨ads judged⟩ → record it next to the 1/5–1/3 guess.

## Step 5b: criterion-1 re-run (added 2026-11-14 13:01, same readout)
_The 11/27 readout is also the last clean date for criterion 1 (7d ≤ 95k on the 12/05 window 11/28–12/04). Source: `2026-12-05_criterion1_path.md`._
1. Run `python3 fuku/bin/criterion1_model_1205.py --peik <S> <L> --bc <S> <L> --p2 <S> <L> --today 2026-11-27 [--budget <PEIKIRA daily spend>] [--cap-throttled]` (report the LWD line **and** the CRITERION 2 line) with the V8 base (PEIKIRA2 < 2 leads → keep the default p2, as in the 11/20 Step 4b). Lock actuals per `meta-modelling-and-planning.md` §A2.
2. Fill one line: base ⟨⟩ · with what is **already live** (Ad015 paused ☐ V5 / site W1+W2 ☐ V6 / ADSET-3 verdict ⟨⟩ Step 3) ⟨⟩ *(calc)* · gap to 95k ⟨⟩.
3. Branch (pick one, replaces nothing in the 3-ask cap unless stated):
| State on 11/27 | Projected 12/04 7d | Action |
|---|---|---|
| ≤ 90k projected | on track | no ask; FYI line in the report: "criterion 1 on track for 12/05 (⟨calc⟩)". |
| 90–95k projected | coin flip | no new ask; re-push the one still-open lever (#1 or #2) as a one-liner: "live by 11/29 eve or criterion 1 slips". |
| > 95k, a lever (#1 or #2) still unapplied | ❌ unless it lands by 11/29 | re-ask that lever only, with "last workable date 11/29 eve". |
| > 95k, both levers live **or** neither live and ADSET-3 not WINNER | ❌ for 12/05 | the single ❓: **"Move criterion 1 to 12/19 (window 12/12–12/18), same Rp 95k target?"** Recommendation: yes only if paired with the missing lever(s) live that week; a move without a lever just reschedules the miss. Replaces the oldest parked M-001 ask. |
4. Record the projected number + branch in the tracker row and MISSIONS M-001 progress.

## Step 6: message + record
- Ask line (pick one, under the 3-ask cap; replace any older ADSET-3 ask):
  - WINNER: "❓ ADSET-3 won (Rp ⟨CPL⟩ on ⟨n⟩ leads, 14d). Raise the PEIKIRA CBO Rp ⟨now⟩ → ⟨+100k⟩/day? Card: `fab_advertising/reports/2026-11-20_s1_scale_card.md` (or its S2 copy if S1 already ran). My recommendation: yes; I'll read it on day 3 and revert at > 125k."
  - LOSER: "❓ Pause ADSET-3 (Rp ⟨spend⟩, ⟨n⟩ leads, CPL ⟨⟩ vs control ⟨⟩, 14d)? My recommendation: yes; budget goes back to the two ad sets that convert."
- Record: tracker row (`m001_tracker.md`), MISSIONS M-001 progress, read card "Verdict" section (append the filled Step 3 + 4), weekly 11/30 report section, journal.

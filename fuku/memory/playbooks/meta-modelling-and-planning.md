# Playbook: modelling gates/criteria and laying out multi-week plans
_Created in Retro #3 (2026-11-14) from 7 lessons (11/13–11/14, M-001); §D–§E added in Retro #4 (2026-11-16) from 8 lessons (11/15–11/16). Pairs with `meta-tests-and-proposals.md` (read rules) and the scripts `fuku/bin/gate_model_1120.py`, `fuku/bin/criterion1_model_1205.py`._

## When to use
Any scenario table ("if X goes live by date D, 7d CPL ≈ …"), break-even for a new ad set, gate/criterion call, or multi-week plan that depends on other people.

## A. Scenario models
1. **One model per judged window.** Each success criterion (and each intermediate gate) has its own 7-day window. Model each separately and state its **last workable date** before writing any "at risk / miss" message (11/14: the 11/20 gate looked lost, but criterion 1 on 11/28–12/04 was still ≈ 88k if both asks land by 11/27).
2. **Once a window is open, lock known days as actuals** and re-run on every daily readout (07:00), not on later quiet runs. One 0-lead day flipped "site fix alone opens the gate" to "no single lever works" (11/14).
3. **Sanity-check direction** before writing numbers: every improving lever must lower CPL vs "nothing" (11/14: first run had the site lift inverted). Hand-check one row.
4. Keep the model as a script in `fuku/bin/` so re-runs are reproducible; mark every output *(calc)*.

## B. New ad set inside a CBO
1. **Break-even vs what it displaces,** not vs target: compute against the CPL of the ad sets it takes spend from (11/13: bar moved ≤ 70k → ≤ 83.5k once the incumbent 116k was used).
2. **State it as a share × start-day table** (1/3, 1/2, 60% × each start date); every zero-delivery day cuts the bar ~4–6k. Re-read it the day delivery actually starts. Put it in the read card.
3. **Check delivery at the first poll after launch.** 0 impressions + no errors + approved ads = CBO starvation → pre-write the ad-set minimum daily spend fix with its removal rule; ask only if it persists to the next poll.

## C. Rules and plans
1. **Tabulate outcomes by result count** for every pre-staged read and check each rule pair for overlap (11/13: "pause if 3-wk > 105k" and "keep if week ≤ 50k" both fired at +2 leads). Write precedence before the data lands. **Order: kill rules → success → sample size.** A minimum-spend "too early" bucket (e.g. spend < 4 × target) overlaps every success bucket, because a win at target always costs less than that (11/27 verdict: 333 of 408 cells WINNER + UNDER-TESTED, 11/15).
2. **Check the object level** when reusing a fix (campaign / ad set / ad): an ad-set minimum can't help waves built as ads inside an existing ad set (11/13).
3. **Plans that need other people's inputs → dates × who × what calendar.** A decision on the same day as the input it selects is a gap; front-load those inputs (11/13: W2 pick on W2 launch day → shoot P1–P6 together).

## D. When the account structure changes (budget, cap, bid strategy, objective)
1. **Activity log before any model.** A change since the last run voids the model output even though it still prints clean numbers (11/15: overnight 300k → 3M + 105k cap). Re-base first (tracker routine step 0).
2. **Re-base on actual daily spend (`--budget`), never the CBO setting.** Under a cap the 3M CBO spent 5% of budget (11/15).
3. **Split day 1 at the change-time burst.** Project pace only from post-burst hours and quote that rate in the status line (11/15: Rp 138k overnight burst, then Rp 15–21k/day = a near-stop that "5% of budget" hid for 30 h).
4. **Judge a budget change on the engine's CPL vs target, not on spend.** With BC fixed, PEIKIRA 300k → 3M moved the 7d blend < 7k at any PEIKIRA CPL. More spend at an above-target CPL *raises* the blend (cheap BC leads shrink in the mix). A cap above target (105k > 95k) is not a target guard.
5. **Two-part criterion → report both halves every run.** Less spend made the CPL-only date look *better* (LWD 11/28 → 12/02) while the Rp 1M/day half became unreachable. Print assumed spend/day next to every date.

## E. Pre-staged cards, templates and send-ready messages
1. **The run after any structural change, grep every staged file for the old value** (budget, cap, "budget steps") and add a dated refresh block that overrides it (11/16: 11/20 gate-miss note still said Rp 300k + "5 budget steps"; S1 scale card would have sent a cosmetic +25%).
2. **Name asks by content + number** in staged files ("ask #2 (pause Ad015)"), and when OUTBOX asks are renumbered or parked, grep `OUTBOX #` across `fab_advertising/reports/` the same run (11/15: 6 files pointed at the wrong asks).
3. **No unmapped rows.** A "map at read time" row gets mapped the same day; it hid the most important ad in ADSET-3 (AKIRA-016, 11/15).

## Last validated
2026-11-16 (Retro #4: §D, §E, C1 order) · 2026-11-14 · M-001 (11/20 gate brief, 12/05 criterion-1 path, ADSET-3 read card, weekly photo calendar).

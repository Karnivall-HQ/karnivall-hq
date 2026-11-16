# Read card: PEIKIRA budget Rp 300k → Rp 3M/day + bid cap Rp 105k (change of 11/15 00:41)
_Written 2026-11-15 08:01 WIB by Fuku, before the change has a full day of data (playbook `meta-tests-and-proposals.md` §A: read rules first). Propose-only: Fuku reads, Alvian/Markus apply._

## What changed (activity log + entity read, account data)
- Campaign `120254051672440572` PEIKIRA-BID-CAP-LEADS-CAMPAIGN: daily budget **Rp 300,000 → Rp 3,000,000**; bid strategy → **bid cap Rp 105,000** on control `120254051672430572`, PEIKIRA2 `120254276298070572`, ADSET-3 `120254400251570572`. Actor "Rudi MCP" (61594758338050). Intent unconfirmed (OUTBOX #1).
- Baseline (7d 11/08–11/14, account data): PEIKIRA Rp 2,094,765 / 16 = **130.9k**, Rp 299k/day, 2.29 leads/day *(calc)*. BC Rp 348,696 / 5.
- Today to 07:05: Rp 138,427 / 1 (not a metric).
- **13:02 poll:** today Rp 143,793 / 1 (control Rp 91,613 / 0, PEIKIRA2 Rp 52,180 / 1, ADSET-3 Rp 0): only **Rp 5,366 spent 07:05→13:02** *(calc)*, pace ≈ Rp 265k/day *(calc, projection)*. The cap, not the budget, is setting spend (fits CAP-BOUND/STARVED, not overspend). Entity read: **all 3 ad sets are LEARNING, 0–1 conversions since the significant edit at 11/15 00:42** (last_sig_edit_ts), so the 11/15–11/17 read is learning-phase data; judge it against the table, but expect noise. No activity-log rows since 07:00. Guards: none tripped.
- **11/16 13:02 poll:** today to 13:00 Rp 7,959 / 0 (control 7,257, PEIKIRA2 702, ADSET-3 0; 152 impressions). 11/15 after the burst: Rp 153,555 − 138,427 = Rp 15,128 in ~17h *(calc)*. Steady capped pace ≈ Rp 15–21k/day *(calc)*, so the 11/15 13:02 "265k/day" projection was inflated by the overnight burst. Expected S3 ≈ Rp 170–190k *(calc)* → STARVED; with ≤ 1–2 leads C3 > 130.9k → STARVED-worse → pre-drafted undo line. Log: no rows since 11/15 00:42. Guards: none.

## What to expect (INFERRED, from this account's own bid-cap history)
- At Fab, bid-capped ad sets land near the cap: BC 087 Copy 7, 8 weekly rows at cap Rp 94,250 → CPL 96.1k (ratio 1.02); caps choked BC delivery to ~1.4% of budget (11/05). So the likely outcome is **PEIKIRA CPL ≈ Rp 100–110k and spend far below Rp 3M/day**: the cap, not the budget, sets spend.
- The 105k cap sits **above** the 95k target. Even if Meta delivers exactly at the cap, the account misses criterion 1 (table below: 102–104k at ≥ Rp 1M/day).
- ADSET-3 (0 conversions) may get even less under a cap (no history to bid on).

## Blended 7d account CPL by PEIKIRA spend/day × PEIKIRA CPL *(calc; BC held at its 11/08–11/14 week)*
| PEIKIRA spend/day | 85k | 95k | 105k | 115k | 130.9k (baseline) | account/day |
|---|---|---|---|---|---|---|
| Rp 300k | 82.4k | 90.3k | 97.9k | 105.3k | 116.4k | ≈ Rp 350k |
| Rp 500k | 83.3k | 92.0k | 100.4k | 108.6k | 121.3k | ≈ Rp 550k |
| Rp 750k | 83.9k | 92.9k | 101.8k | 110.5k | 124.1k | ≈ Rp 800k |
| Rp 1M | 84.1k | 93.4k | 102.5k | 111.6k | 125.7k | ≈ Rp 1.05M |
| Rp 1.5M | 84.4k | 93.9k | 103.3k | 112.7k | 127.3k | ≈ Rp 1.55M |
| Rp 3M | 84.7k | 94.4k | 104.1k | 113.8k | 129.1k | ≈ Rp 3.05M |
→ **Spend level barely moves the blend; PEIKIRA's own CPL decides it.** Criterion 1 needs PEIKIRA ≤ ~93k at any spend ≥ Rp 500k/day. Criterion 2 (Rp 1M/day at ~95k) is met only in the "Rp 1M × 95k" cell.

## Read rules (fixed now; apply as written)
Window: full days **11/15, 11/16, 11/17** (read at the 11/18 07:00 readout). Pull level=adset, campaign `120254051672440572`, time_range 11/15→11/17, fields spend, leads (pixel Lead), impressions, CPM; plus the activity log since 11/15 07:05.

**Daily guard (13:00 / 19:00 polls and each 07:00 readout, from 11/15):**
- G-a. PEIKIRA spend > **Rp 1,000,000 in one day** with CPL > **Rp 130k** → add a one-line [RISK] to OUTBOX #1: "back to Rp 300k today".
- G-b. PEIKIRA spend ≥ **Rp 285k (3× target) in a full day with ≤ 1 lead** on 2 days in a row → same line (P ≈ 20% per day if truly on target *(calc)*, so 2 days ≈ 4%).

**3-day verdict (11/18 07:00):** let S3 = PEIKIRA spend 11/15–11/17, C3 = S3 ÷ leads.
| Case | Condition | Proposal |
|---|---|---|
| CAP-BOUND | S3 < Rp 1.5M (< 500k/day) | The 3M budget is cosmetic; the cap is the real change. Judge on C3 below; no budget ask. |
| WIN | C3 ≤ Rp 95k and S3 ≥ Rp 900k | Keep. Propose nothing; log as criterion-2 progress. Re-run the 7d models on the real spend/day. |
| HOLD | 95k < C3 ≤ 115k | Keep the caps; propose **budget back to the 3-day average spend + 25%** (so a weak day can't run to 3M). Re-read 11/21. |
| REVERT | C3 > 115k on S3 ≥ Rp 900k, or ≤ 2 leads on S3 ≥ Rp 600k | Propose **budget back to Rp 300k, keep the 105k caps** (same as OUTBOX #1's rec). |
| STARVED | S3 < Rp 600k | Cap too tight for this creative (INFERRED). No raise yet; read the 7d on 11/21 before any cap change (playbook §C: ≥ 8 weekly rows before a cap proposal; this setup has 0). |
- **Comparative rule:** C3 vs PEIKIRA's baseline 130.9k. C3 > 130.9k = the change made CPL worse → REVERT regardless of the table.
- **Share rule:** report each ad set's share of S3. ADSET-3 still Rp 0 on 11/17 → the ADSET-3 min-spend item in OUTBOX #2 stays valid (cap + CBO both starve it).
- Use full days only; never judge intraday (playbook §A.5).

## Branches by Alvian's answer to OUTBOX #1
- **"revert" (back to Rp 300k, caps kept):** read window starts the day after the revert. Same table, but CAP-BOUND / WIN thresholds scale down: WIN = C3 ≤ 95k on S3 ≥ Rp 600k. Re-base the 11/20 gate model + criterion-1 model with `--budget 300000` *(see groundwork #2)*.
- **"intended" (3M stays):** this card runs as written; G-a becomes the standing stop rule. Re-base the models on the 3-day average spend, not on 3M.
- **No answer by 11/18:** run the card anyway; send only the one verdict line as the re-ask of #1 (stalled-ask rule).

## Readout line template (11/18)
"PEIKIRA 11/15–11/17 under 3M + 105k cap: Rp ⟨S3⟩ (⟨S3/3⟩/day, ⟨%⟩ of budget) / ⟨L⟩ leads = ⟨C3⟩ *(calc)* vs baseline 130.9k. Case: ⟨CAP-BOUND/WIN/HOLD/REVERT/STARVED⟩. Split: control ⟨⟩ / PEIKIRA2 ⟨⟩ / ADSET-3 ⟨⟩. Guard trips: ⟨none/G-a date/G-b dates⟩."

## Dry-run + rule-overlap check (written 11/15 20:01 WIB, before the data; playbook `meta-modelling-and-planning.md` C.1)
**Every ⟨⟩ cell → one pull:** S3, L, C3, split = one `ads_get_ad_entities` level=adset, campaign `120254051672440572`, time_range 11/15→11/17 (spend, pixel Lead). ⟨%⟩ of budget = S3 ÷ Rp 9,000,000 *(calc)*. Guard trips = the G-a/G-b lines in the 11/15 19:01 journal + the 11/16 and 11/17 07:00 readouts (11/15: none to 19:01). Pre-change bid strategy (needed by row 3 below) = `old_value` in the `extra_data` of the 11/15 00:41–00:42 activity-log rows; pull it **in the 11/16 07:00 run** (row 7 already covers that window), so 11/18 doesn't depend on it.

**Overlap found.** Tabulating S3 × leads *(calc)*: at the likely spend (11/15 pace ≈ Rp 189k/day → S3 ≈ Rp 450–570k), **STARVED and the comparative rule (C3 > 130.9k → REVERT) fire together for ≤ 3 leads (S3 450k) / ≤ 4 leads (S3 570k)**. They contradict: STARVED says "no change, re-read 11/21"; REVERT says "budget back to Rp 300k", which is moot when spend is under Rp 300k/day (the budget isn't binding). CAP-BOUND co-fires with every case below Rp 1.5M, so it is a label ("no budget ask"), not a case.

**Precedence (fixed now):**
1. **S3 ≥ Rp 600k:** the table as written; REVERT and the comparative rule agree in every cell checked (750k and 1.2M × 0–9 leads).
2. **S3 < Rp 600k → STARVED branch only;** never propose a budget change (not binding). Split by C3:
   - **STARVED-worse, C3 > 130.9k:** fewer leads (≤ 4 in 3 days vs baseline 2.29/day = 6.9 *(calc)*) **and** dearer. Proposal: **restore PEIKIRA's pre-11/15 setup on all 3 ad sets** (bid strategy = the logged `old_value`; budget Rp 300k): a known state with weeks of history, so this is not a new cap test (playbook §C's ≥ 8-row rule applies to new caps, not to undoing one). Basis is the volume loss, which is certain; the CPL gap alone is not (if the true CPL were still 130.9k, P(≤ 3 leads on Rp 450k) ≈ 55%, on Rp 570k P(≤ 4) ≈ 56% *(calc, Poisson)*) → say so in the line.
   - **STARVED-middle, 95k < C3 ≤ 130.9k:** no ask; re-read 7d on 11/21 (as written).
   - **STARVED-cheap, C3 ≤ 95k:** no ask; the cap works on cost, volume is the cost of it. Log leads/day vs 2.29; re-read 11/21.
3. Any Alvian answer to OUTBOX #1 overrides rows 1–2 per "Branches" above.
- **Most likely 11/18 line (INFERRED from the 11/15 pace + ≈ 1 lead/day):** STARVED-worse → re-ask OUTBOX #1 as one line: "Undo the 11/15 change (Rp 300k + previous bidding)? 3 days: Rp ⟨S3⟩ / ⟨L⟩ vs 6.9 leads at baseline."

## Pre-drafted STARVED-worse ask + undo change list (written 11/15 22:01 WIB, before the data)
**Pre-change state (activity log, account data; pulled 11/15 22:01, so the 11/16 run doesn't need to):**
| Object | ID | Before 11/15 00:41–00:42 (`old_value`) | After (`new_value`) |
|---|---|---|---|
| Campaign PEIKIRA-BID-CAP-LEADS-CAMPAIGN (budget) | `120254051672440572` | Rp 300,000 per day | Rp 3,000,000 per day |
| Control PEIKIRA-FAB-20261023-ADSET | `120254051672430572` | "Automatically bid for impressions", no cap amount | "Optimize bid for actions", cap Rp 105,000 |
| AKIRA-FAB-20261031-WAVE-PEIKIRA2 | `120254276298070572` | "Automatically bid for clicks", no cap amount | "Optimize bid for actions", cap Rp 105,000 |
| PEIKIRA-FAB-20261109-ADSET-3 | `120254400251570572` | "Automatically bid for actions", no cap amount | "Optimize bid for actions", cap Rp 105,000 |
- All 3 were **automatic bidding with no cap** before (`additional_value.old_value: null`). The 3 labels are Meta's translated log labels; they probably differ only by billing/optimisation event, and in Ads Manager all 3 read as **"Highest volume"** (INFERRED; Markus confirms on screen). The campaign name says "BID-CAP", but the log shows no cap amount before 11/15.
- Also logged at 00:41: the campaign went Active → Pending Process → Active (Meta re-review after the edit; not a separate change).

**One-line ask (use only if the 11/18 case = STARVED-worse; fill ⟨⟩ from the read):**
"❓ Undo the 11/15 PEIKIRA change: budget back to Rp 300k/day + remove the Rp 105k bid caps (back to Highest volume) on all 3 ad sets? 3 days under the cap: Rp ⟨S3⟩ / ⟨L⟩ leads = ⟨C3⟩ *(calc)* vs 6.9 leads and 130.9k at baseline. The volume loss is certain; the CPL gap could still be noise (≈ 55% chance *(calc)*). Reply 'undo' or 'keep'."

**Proposed changes for Alvian/Markus to apply (Fuku applies nothing):**
1. Campaign `120254051672440572` → daily budget **Rp 300,000** (from Rp 3,000,000).
2. Ad set `120254051672430572` (control) → bid strategy **Highest volume**, cap removed.
3. Ad set `120254276298070572` (PEIKIRA2) → **Highest volume**, cap removed.
4. Ad set `120254400251570572` (ADSET-3) → **Highest volume**, cap removed. If OUTBOX #2(b) is a yes, set its Rp 75,000 daily minimum in the same sitting (one learning reset, not two).
- Do it as **one edit session**: every bid edit resets learning on that ad set (11/15 showed it: all 3 LEARNING from 00:42), so batching = 1 reset.
- **Read rule after the undo (fixed now):** window starts the full day after the undo; 7d read. Success = PEIKIRA back to ≥ 2 leads/day at ≤ 130.9k (the pre-change baseline) within 7 days; fail = < 1.5 leads/day *(calc threshold)* → re-check the activity log for other edits before blaming the undo.
- **Do not use** if the case is anything other than STARVED-worse (precedence above), or if Alvian has already answered OUTBOX #1.

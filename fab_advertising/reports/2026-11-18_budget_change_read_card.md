# Read card: PEIKIRA budget Rp 300k → Rp 3M/day + bid cap Rp 105k (change of 11/15 00:41)
_Written 2026-11-15 08:01 WIB by Fuku, before the change has a full day of data (playbook `meta-tests-and-proposals.md` §A: read rules first). Propose-only: Fuku reads, Alvian/Markus apply._

## What changed (activity log + entity read, account data)
- Campaign `120254051672440572` PEIKIRA-BID-CAP-LEADS-CAMPAIGN: daily budget **Rp 300,000 → Rp 3,000,000**; bid strategy → **bid cap Rp 105,000** on control `120254051672430572`, PEIKIRA2 `120254276298070572`, ADSET-3 `120254400251570572`. Actor "Rudi MCP" (61594758338050). Intent unconfirmed (OUTBOX #1).
- Baseline (7d 11/08–11/14, account data): PEIKIRA Rp 2,094,765 / 16 = **130.9k**, Rp 299k/day, 2.29 leads/day *(calc)*. BC Rp 348,696 / 5.
- Today to 07:05: Rp 138,427 / 1 (not a metric).

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

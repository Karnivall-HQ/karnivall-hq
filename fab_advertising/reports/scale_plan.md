# M-001 scale plan: Fab to Rp 1,000,000/day at ~Rp 95k CPL
_2026-11-10 14:04 WIB, Fuku cloud heartbeat (groundwork). Read-only: nothing in the ad account was changed. Propose-only: every step below is for Alvian to apply._

Source: Rudi MCP, account `484578521394893`. Campaign weekly 2026-09-14 → 11-09, ad-set 30d, Meta trend + benchmark tools. *(calc)* = Fuku's arithmetic. Labels per `fuku/memory/playbooks/meta-ads-algorithm.md`.

## TL;DR
1. **Rp 1M/day is creative-bound, not budget-bound.** The two engines we have can absorb about **Rp 590k/day** at ≤ Rp 95k *(calc, account data)*. The other ~Rp 410k/day needs new ads that win.
2. **Proof that budget alone fails:** the week of 10/12–10/18 the account spent **Rp 6,431,717 = Rp 919k/day** *(calc)* and got 32 leads, **CPL Rp 200,991** *(calc)*, almost all through the RUDI cost-cap campaign (KENJI creatives). Same creatives, more money → 2× the CPL. [account data]
3. **Deadline math:** 5 steps of +25% every 3 days take 15 days. To reach Rp 1M by 12/05, the 7d CPL gate (≤ 95k) must open by **2026-11-20** *(calc)*. Today it is Rp 112.4k ❌.
4. **What unlocks it, in order:** (a) restore BC delivery (items 3+4 of the parked change list), (b) new phone-photo creative (batch 01 v2), (c) only then budget steps.

> ⚠️ **Superseded 2026-11-12 11:01 by `2026-11-12_scale_plan_v2.md`** (no BC cap lever; per-wave capacity Rp 100–185k/day; Rp 1M/day by 12/05 not supported by account data). Tables below kept as history.

## Need vs have
| | Now (7d 11/03–11/09) | Target |
|---|---|---|
| Spend/day | Rp 337k *(calc)* | Rp 1,000,000 |
| Leads/day | 3.0 *(calc)* | 10.5 *(calc: 1M ÷ 95k)* |
| CPL | Rp 112,369 *(calc)* | ≤ Rp 95,000 |
→ We need **3.5× the leads** *(calc)*, not just 3× the spend.

## Engine capacity (what can absorb spend at ≤ 95k)
| Engine | Proven level | Evidence | Capacity at ≤ 95k | Lever |
|---|---|---|---|---|
| **BC CBObass005 – Copy** (bid cap Rp 94,250, budget Rp 5M) | Rp 288k/day at **CPL Rp 89,659** for 4 weeks (09/14–10/11: Rp 8,069,332 / 90) *(calc)* | Now ~Rp 53k/day (11/02–11/08: Rp 373,956 / 3). Starved by the cap + 50-ad-set fragmentation. | **~Rp 290k/day** | Parked items 3 (consolidate to 5 winners) + 4 (cap → Rp 105k on 087 Copy 7 + BC204) |
| **PEIKIRA** (highest volume, Rp 300k/day) | Rp 300k/day | Control ad set Rp 81,869 CPL 11/05–11/09; whole campaign 101.6k (11/02–11/08) and 169k (10/26–11/01). Benchmark: main ad set CPR **69% worse** than peers. Leans on Ad015. | **~Rp 300k/day** if PEIKIRA2 stays throttled | Parked item 1 (drop IG Stories), PEIKIRA2 off |
| **New creative ad sets** | none yet | Raw phone photos Rp 18–68k vs AI renders Rp 200–372k (11/05 review) | **the missing ~Rp 410k/day** | Batch 01 v2 shot list (needs photos) |
| ~~RUDI cost cap~~ | Rp 880k/day at Rp 198,759 (10/12–10/18) | Paused, correctly | 0 | Keep off |

Sum of proven capacity: Rp 290k + 300k = **~Rp 590k/day** *(calc)*.

## Bid-cap math for BC batch087 Copy 7 (`120241535471900572`)
- 30d: Rp 1,341,128 / 16 leads = **Rp 83,821 CPL at a Rp 94,250 cap.** Avg CPL ÷ cap = **0.889** *(calc)*. Meta trend: CPR improving 75%, CTR +22% (GOOD).
- If the ratio holds [INFERRED; bid caps are not covered by Meta's docs, so this is account data + assumption]:
  - cap **Rp 105,000 → expected CPL ≈ Rp 93.4k** *(calc)* ✅ under 95k
  - cap Rp 110,000 → ≈ Rp 97.8k *(calc)* ❌ over
- → **Rp 105k is the highest cap consistent with the target.** Don't go above it. Stop rule unchanged: revert to Rp 94,250 if the ad set's 7d CPL > Rp 95k after 5 days.

## Step ladder (each step applied by Alvian; Fuku proposes the next one only when its gate holds)
| Step | Account spend/day | How the spend is added | Gate to take this step |
|---|---|---|---|
| S0 | Rp 337k (now) | — | — |
| S1 | ~Rp 420k | BC recovers via items 3+4 (no budget edit; BC budget is already Rp 5M) | Items 3+4 applied |
| S2 | ~Rp 525k | BC continues to fill; PEIKIRA held at 300k | 7d CPL ≤ 95k for 3 days after S1 |
| S3 | ~Rp 660k | New creative ad set(s) from batch 01 v2 go live (inside PEIKIRA or a new ABO ad set), ~Rp 130k/day | Photos shot + ads approved; 7d CPL ≤ 95k |
| S4 | ~Rp 820k | +25% on whichever engine had the lowest 7d CPL | 7d CPL ≤ 95k and new ads ≥ 3 leads at ≤ 95k |
| S5 | ~Rp 1,000k | +25% again, same rule | 7d CPL ≤ 95k |
- Steps are +25% *(calc: 337k × 1.25ⁿ)*, at most every 3 days [FOLKLORE: Meta docs give no budget-change speed].
- **Cut-back rule:** if the 7d CPL goes above **Rp 110k** after any step, go back to the previous step's level.
- S1–S2 need **no new assets and no budget edit**; they are the parked items 3+4. S3+ need photos.
- ⚠️ **11/12 08:01:** items 3 and 4 (087) are both retired (`2026-11-12_item4_bidcap_card.md`: 087 8-wk CPL 96.1k at the current cap). **S1/S2 have no lever on current creative**: BC capacity is whatever it delivers at Rp 94,250. Volume past ~Rp 330k/day now runs through new creative (S3).

## Risks
- ⚠️ **Ad015 single point of failure:** it carries ~95% of the PEIKIRA control ad set (11/09). If it fatigues, PEIKIRA's ~Rp 300k capacity falls with it. Hedge = new creative (S3). Contingency list = groundwork backlog item 2.
- ⚠️ **Post-click leak:** LP→Lead 3.9% with wrong location + price on the pages (W1/W2). Each +1pt LP→Lead ≈ −20% CPL *(calc, 11/06 audit)*. Cheapest lever on the board; applies to every step.
- ⚠️ **Deadline:** if the gate isn't open by 11/20, criterion 2 (Rp 1M/day by 12/05) is out of reach without breaking criterion 1. Fuku will say so plainly at that date rather than push spend early.

## What Fuku will do with this
- Re-raise nothing new now (OUTBOX cap). This plan backs the existing asks: photos (ask #2) are the critical path to S3; items 3+4 are next in line after the IG Stories item.
- Re-check the 11/20 gate date at each daily readout.

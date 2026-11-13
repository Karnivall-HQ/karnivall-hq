# M-001 scale plan v2: the Rp 1M/day path without BC cap levers
_2026-11-12 11:01 WIB, Fuku cloud heartbeat (groundwork). Read-only: nothing in the ad account was changed. Supersedes the S1–S5 ladder in `scale_plan.md` (its capacity table stays valid as history)._

Source: Rudi MCP, account `484578521394893`, ad-set weekly rows (`time_increment 7`) 2026-09-14 → 11-11, by object ID; Meta trend + benchmark follow-ups. *(calc)* = Fuku's arithmetic. Labels per `fuku/memory/playbooks/meta-ads-algorithm.md`.

## TL;DR
1. **A creative wave that wins adds about Rp 100–185k/day at ≤ 95k, not more.** That's the best week any new ad set has shown in 8 weeks *(calc, account data)*.
2. **Rp 1M/day needs +Rp 670k/day** over today's ~Rp 330k → **4 to 7 winning waves** *(calc)*. We have had **1.5 winners in 3 waves** (KENJI 0/7 ad sets, PEIKIRA control 1 = Ad015, PEIKIRA2 borderline).
3. **Honest forecast for 12/05:** with W1/W2 live and Wave 1 winning, ≈ **Rp 450–520k/day at ≤ 95k** *(calc)*. Rp 1M/day by 12/05 is **not supported by account data**. I'll make that call formally on 11/20 as planned (no new ask now).
4. **The only way to change the slope:** ship waves faster (one every ~5 days from 11/16), each with 3+ phone-photo ads. Photos are the bottleneck, not budget or bids.

## What each past wave actually absorbed (account data)
| Wave (ad set) | Week | Spend | Leads | CPL | Spend/day |
|---|---|---|---|---|---|
| KENJI ×7 (RUDI cost cap) | 10/12–10/18 | Rp 5,189,258 *(calc)* | 28 | **Rp 185,331** *(calc)* | Rp 741k *(calc)* |
| — best KENJI ad set (007) | 10/12–10/18 | Rp 624,486 | 5 | Rp 124,897 *(calc)* | Rp 89k *(calc)* |
| PEIKIRA control (`…430572`) | 10/26–11/01 | Rp 1,862,676 | 11 | Rp 169,334 *(calc)* | Rp 266k *(calc)* |
| PEIKIRA control | **11/02–11/08** | Rp 1,292,413 | 16 | **Rp 80,776** *(calc)* | **Rp 185k** *(calc)* |
| PEIKIRA control | 11/09–11/11 (3 d) | Rp 517,696 | 3 | Rp 172,565 *(calc)* | Rp 173k *(calc)* |
| PEIKIRA2 (`…070572`) | 11/02–11/08 | Rp 739,973 | 4 | Rp 184,993 *(calc)* | Rp 106k *(calc)* |
| PEIKIRA2 | **11/09–11/11 (3 d)** | Rp 297,084 | 5 | **Rp 59,417** *(calc)* | **Rp 99k** *(calc)* |
| BC204 / BC208 / BC4-08 (old BC) | any week | ≤ Rp 312k | ≤ 3 | — | ≤ Rp 45k each |

Reading:
- **Budget alone fails** (again): KENJI took Rp 741k/day and returned 185k CPL. Not one of 7 KENJI ad sets got under 95k in its big week.
- **A good week happens at Rp 100–185k/day per ad set**, and it doesn't hold: control went 169k → 81k → 173k; PEIKIRA2 185k → 59k. Week-to-week swing is ±2×, so judge waves on 2 weeks, not 1. [account data]
- Meta benchmark (today): control CPR **71.6% worse** than peers, PEIKIRA2 **61.5% worse**; trend tool: PEIKIRA2 CPR flat (GOOD), CTR −14% (BAD), CPM +8.5% (BAD). [account data, Meta tools] → the current ads are aging, which raises the urgency of new creative.

## The math to Rp 1M/day
- Now: ~Rp 330k/day at 100.5k (11/05–11/11).
- Gap: Rp 670k/day *(calc)*. Per winning wave: Rp 100–185k/day → **3.6 to 6.7 winning waves** *(calc)*.
- Hit rate so far: KENJI 0 of 7 ad sets; PEIKIRA control 1 winning ad (Ad015) of ~14; PEIKIRA2 8 live ads, ~1 good 3-day stretch. Call it **~1 winner per 10 ads** [INFERRED from 3 waves; small sample].
- But raw phone-photo ads ran **Rp 18–68k CPL** vs 200–372k for polished renders (11/05 visual review), so a phone-photo wave should beat that hit rate. Assume 1 winner per 3–5 phone-photo ads [INFERRED, untested here; Wave 1 tests it].
- → Need **~12–30 phone-photo ads** shipped *(calc: 4–7 winners × 3–5 ads)*. At 3 ads per wave, 4–10 waves. Between now and 12/05 there are 23 days; one wave every 5 days = **4 waves max** *(calc)*.

## Forecast by scenario (12/05)
| Scenario | Spend/day at ≤ 95k | Why |
|---|---|---|
| Nothing changes | ~Rp 330k at ~100k ❌ | Today |
| W1/W2 only | ~Rp 330–360k at ~89k ✅ CPL, ❌ volume | Site fix lifts CVR, not delivery (gate brief) |
| W1/W2 + Wave 1 wins | **~Rp 450–520k** *(calc: 330k + 1 winner 100–185k)* | Most likely good case |
| W1/W2 + 4 waves, 3 win | ~Rp 630–885k *(calc)* | Needs 12 photo ads by ~11/28 |
| Rp 1M/day | needs 4–7 winners | Not reachable by 12/05 on this hit rate |

## What I'll do with this (no new ask now)
- Ask #2 (photos) already covers it. When Alvian answers, ask for **12 photos, not 2**, so Waves 2–4 don't wait on another shoot (shoot card already lists 6 shots; extend by 6 clutter/home shots).
- 11/20 gate brief: add the scenario table above as the volume half of the call (criterion 2).
- New read rule for each wave: judge on **2 weeks** (≥ Rp 1.4M spend or 14 days), not one good week.
- Scale steps (+25% per 3 days) only on a 7d CPL ≤ 95k **and** a winning wave present; never on budget alone (KENJI proof).
- → Apply-ready S1 card with gate + read rules: `2026-11-20_s1_scale_card.md` (11/13).

## Labels
- Account data: every row in the wave table; benchmark and trend outputs.
- INFERRED: hit rates; phone-photo hit rate (from the 11/05 visual review, not a controlled test); forecasts.
- Data note: a filtered ad-set pull with `time_increment` returned zeros for most ad sets; pulling **by `object_ids`** returned the real weekly rows. Use `object_ids` for history.

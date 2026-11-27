# W1/W2 site-fix lift: measurement template
_2026-11-11 11:02 WIB, Fuku cloud heartbeat (groundwork). Read-only. Use it the day Alvian says "W1 W2 done"._

**Question:** did fixing the 2 site lines (location → Kuningan/Sudirman, price → the true 750/800) lift post-click conversion enough to open the 11/20 gate? The gate brief (`2026-11-20_gate_brief.md`) assumes +0.5pt (→ 94.6k) or +1pt (→ 85.0k) *(calc)*.

## Baseline refresh 2026-11-27 10:02 WIB (use this one; replaces the 11/11 rule numbers)
Same call (`ads_get_dataset_stats`, aggregation=`event`, granularity=`day`, PT days). 11/26 PT left out (partial day at pull time).

| Window (PT days) | ViewContent | Form | Lead | VC→Lead *(calc)* |
|---|---|---|---|---|
| 11/11–11/17 | 1,285 | 60 | 39 | 3.04% |
| 11/18–11/24 | 994 | 57 | 34 | 3.42% |
| **11/16–11/25 (10 d, caps regime)** | **1,382** | — | **49** | **3.55%** |

- **Baseline for the test = 3.55%** (11/16–11/25: same ad regime as the post-fix window will be, caps on, BC ≈ 99% of spend). Close to the old 3.72%, so no conversion drift; the site still leaks the same.
- ⚠️ **Traffic fell:** ~1,000 VC/week now *(calc, 138/day)* vs ~1,300 when the rule was written. The day-7 read is weaker:

| True post-fix VC→Lead | Leads per 1,000 VC | Day-7 power *(calc)* | Day-14 power (2,000 VC) *(calc)* |
|---|---|---|---|
| 3.55% (no lift) | 35 | 10% false alarm | — |
| 4.05% (+0.5pt) | 40 | 34% | 47% |
| 4.55% (+1pt) | 45 | 64% | 83% |
| 5.05% (+1.5pt) | 50 | 85% | — |

- **New rule (written before the fix):** day-7 "lift confirmed" = **≥ VC × 3.55% + 1.28·√(VC × 3.55%)** (≈ 43 leads per 1,000 VC). Day 14 is the main read now (≈ 82 per 2,000 VC); day 7 is directional only. Counts are browser + server events, so true noise is ~√2 larger (11/11 note) → treat both reads as upper bounds on confidence.
- ⚠️ **Counts get revised up after the day:** 11/16–11/22 read 819 VC / 31 Leads on 11/23 and 888 / 35 today. Lock each window ≥ 3 days after it ends, and re-pull baseline + post-fix in the same call.

## Pre-fix baseline (refreshed 11/11, replaces the 11/06 row for this test)
Call: `ads_get_dataset_stats` dataset `405755485775053`, aggregation=`event`, granularity=`day`. Buckets are **Pacific-time days**. (This aggregation returns smaller counts than `event_total_counts` in the 11/06 file, so compare like with like: always this call.)

| Window (PT days) | ViewContent | Lead | VC→Lead *(calc)* |
|---|---|---|---|
| 10/15–10/21 | 1,826 | 68 | 3.72% |
| 10/22–10/28 | 1,369 | 45 | 3.29% |
| 10/29–11/04 | 1,581 | 59 | 3.73% |
| 11/05–11/10 (6 d) | 1,011 | 43 | 4.25% |
| **27 days** | **5,787** | **215** | **3.72%** |

Week-to-week noise is already ±0.5pt (3.29–4.25%) with no change made. ⚠️ Pixel Leads (~8/day) are ~3× Meta-attributed leads (~3/day): the pixel includes organic/non-ad traffic. **Correction 11/11 16:02:** that ratio was double counting. Every event is sent browser + server, and this call sums both; unique Leads ≈ 4.3/day, so ≈ 73% of site Leads are ad-attributed (`2026-11-11_pixel_lead_ad_share.md`). Counts below are *received* events: the real Poisson noise is ~√2 larger than the table shows, so treat day 7 as directional and day 14 + Meta CPL as the read. Originally: INFERRED, so the pixel tells us *whether the site converts better*, and Meta CPL tells us *whether that reached the ads*.

## What a 7-day read can and can't see *(calc, Poisson, ~1,300 VC/week)*
| True post-fix VC→Lead | Expected leads/7d | z vs baseline | Readable in 7d? |
|---|---|---|---|
| 3.8% (no lift) | 49 | 0.1 | — |
| 4.4% (+0.5pt, gate case C low) | 57 | 1.0 | ❌ no, need ~14 d |
| 4.9% (+1pt, gate case C high) | 64 | 1.7 | ✅ ~90% |
| 5.5% | 72 | 2.4 | ✅ clear |

**Rule written before the fix (per `meta-tests-and-proposals.md`):**
- Day 0 = first full PT day after Alvian confirms the edit (curl the 3 Jakarta pages first: 0 × "Kelapa Gading", 0 × "Jakarta Pusat", price line matches the true price).
- **Day 7 read:** post-fix leads at the observed VC count vs `VC × 3.72%`. **≥ +1.28σ (≈ 58 leads per 1,300 VC) → "lift confirmed"**. Between 0 and +1.28σ → "unproven, extend to 14 d". Below baseline → "no lift; site wasn't the leak, look upstream (cost per LPV)".
- **Day 14 read:** same test on 14 d; this one can see +0.5pt.
- **Cross-check on the ad side (same window):** Meta 7d CPL and Meta leads ÷ landing-page views for PEIKIRA + BC vs the 11/04–11/10 base (CPL 106,779). A pixel lift with flat Meta CPL = the gain went to organic traffic, not the ads.
- **Confounders to log:** any ad change by Markus (activity log), Wave 1 launch date, budget change. If Wave 1 starts inside the window, the pixel read still holds (site-wide) but the Meta CPL cross-check doesn't isolate the site.

## What this means for the 11/20 gate
- If the fix lands 11/12, the 11/20 readout comes **before** a 14-day pixel read. A +0.5pt lift would be real but invisible in the pixel by then; the Meta 7d CPL is the gate number regardless.
- So: don't wait for pixel proof to make the scale call. The pixel read decides whether to **keep investing in site work** (W3/W4), not the gate.

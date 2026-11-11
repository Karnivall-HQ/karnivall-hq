# W1/W2 site-fix lift: measurement template
_2026-11-11 11:02 WIB, Fuku cloud heartbeat (groundwork). Read-only. Use it the day Alvian says "W1 W2 done"._

**Question:** did fixing the 2 site lines (location → Kuningan/Sudirman, price → the true 750/800) lift post-click conversion enough to open the 11/20 gate? The gate brief (`2026-11-20_gate_brief.md`) assumes +0.5pt (→ 94.6k) or +1pt (→ 85.0k) *(calc)*.

## Pre-fix baseline (refreshed 11/11, replaces the 11/06 row for this test)
Call: `ads_get_dataset_stats` dataset `405755485775053`, aggregation=`event`, granularity=`day`. Buckets are **Pacific-time days**. (This aggregation returns smaller counts than `event_total_counts` in the 11/06 file, so compare like with like: always this call.)

| Window (PT days) | ViewContent | Lead | VC→Lead *(calc)* |
|---|---|---|---|
| 10/15–10/21 | 1,826 | 68 | 3.72% |
| 10/22–10/28 | 1,369 | 45 | 3.29% |
| 10/29–11/04 | 1,581 | 59 | 3.73% |
| 11/05–11/10 (6 d) | 1,011 | 43 | 4.25% |
| **27 days** | **5,787** | **215** | **3.72%** |

Week-to-week noise is already ±0.5pt (3.29–4.25%) with no change made. ⚠️ Pixel Leads (~8/day) are ~3× Meta-attributed leads (~3/day): the pixel includes organic/non-ad traffic. INFERRED, so the pixel tells us *whether the site converts better*, and Meta CPL tells us *whether that reached the ads*.

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

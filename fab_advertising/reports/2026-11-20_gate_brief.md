# M-001: 11/20 gate brief (what gets the 7d CPL to ≤ Rp 95k by 11/20)
_2026-11-11 08:02 WIB, Fuku cloud heartbeat (groundwork). Read-only, no ad-account change. Propose-only._

**Why 11/20:** the scale plan (`scale_plan.md`) needs 5 × +25% steps, 3 days apart, to reach Rp 1M/day by 12/05. That only works if the 7d CPL is ≤ Rp 95k by the **11/20 readout (window 11/13 → 11/19)**. For a change to count for the whole window, it has to be live by **11/12 evening**.

**Base:** 7d 11/04–11/10 (11/11 readout): PEIKIRA Rp 2,020,826 / 17 leads; BC Rp 328,314 / 5 leads. Blended **Rp 106,779** *(calc)*. Per day: PEIKIRA Rp 288.7k / 2.43 leads, BC Rp 46.9k / 0.71 leads *(calc)*.

## TL;DR
- ⚠️ **11/12 08:01 correction:** on 8 weekly rows, 087 Copy 7 already runs Rp 96.1k CPL at the current cap (ratio 1.02), so scenario B lands at the **upper end (≈ 107k+)** and B+C loses its volume bonus. Item 4 is retired for 087 (`2026-11-12_item4_bidcap_card.md`).
- **Only one lever can open the gate by itself: the website fixes W1+W2** (≈ Rp 94.6k at +0.5pt LP→Lead, ≈ Rp 85.0k at +1pt) *(calc)*. They are 10 minutes of work and touch no ad.
- Item 4 (BC bid cap → Rp 105k) **alone does not** open it (≈ Rp 104k best case): it adds volume at ~95k, it does not pull the blend under 95k.
- Wave 1 photo ads open it alone **only if** they win at ≤ ~Rp 70k and are live by 11/15. That is plausible (raw phone photos ran Rp 18–68k) but it's a bet.
- **Doing nothing:** ~Rp 107k. The trend is improving (125k → 107k over 5 readouts), but noisy (105k → 112k → 107k). Gate likely ❌.
- → Tomorrow's re-ask should be the **site fix**, not only the price fact.

## Scenarios (7d CPL for window 11/13–11/19)
| # | Scenario | 7d CPL | Gate? | Assumptions |
|---|---|---|---|---|
| A | Nothing applied | **~Rp 106.8k** *(calc)* | ❌ | Same mix as 11/04–11/10 |
| B | Item 4 only (cap Rp 94,250 → Rp 105k on 087 Copy 7 + BC204) | **Rp 104.1k – 108.5k** *(calc)* | ❌ | BC spend 47k → 120k/day [INFERRED: 087 ran ~79k/day before it starved, 11/06 split]. New BC spend at Rp 93.4k (cap ratio 0.889, `scale_plan.md`) → 104.1k; at 110k → 107.3k; all BC regressing to its 4-week 89.7k → 108.5k. Adds ~Rp 73k/day of spend; doesn't lower the blend. |
| C | W1 + W2 only (site location + price lines) | **Rp 85.0k – 94.6k** *(calc)* | ✅ (just) | LP→Lead 3.9% → 4.4% (+0.5pt) = 94.6k; → 4.9% (+1pt) = 85.0k. [INFERRED: the size of the lift is a guess. Basis: Jakarta Selatan pages say "Kelapa Gading"/"Jakarta Pusat" and the form says Rp 800k vs 750rb ads, `2026-11-06_landing_page_audit.md`.] |
| D | Wave 1 photo ads only (S1/B1/B2, live 11/15, take 1/3 of PEIKIRA) | **Rp 94.6k / 102.1k / 111.0k** *(calc)* | ✅ only if they win | New ads at Rp 70k / 95k / 150k CPL, 5 of 7 window days, replacing PEIKIRA spend 1:1 (the Rp 300k budget doesn't change). [account data: phone photos Rp 18–68k, AI renders Rp 200–372k; Reels 7d 48k] |
| B+C | Item 4 + site fixes | **~Rp 92.3k** *(calc, +0.5pt case)* | ✅ | Also adds ~Rp 73k/day, i.e. starts step S1 of the ladder |
| C+D | Site fixes + Wave 1 at 70k | **~Rp 83.9k** *(calc)* | ✅ | Best case; opens S1–S3 |

## What Fuku does with this
1. **Ranking stays:** OUTBOX ask #1 (W1+W2) is the only single lever that can open the gate. Ask #2 (photos + 750/800) is the second, and its price fact also unlocks W2.
2. **11/12 07:00 (asks > 48h):** shrink to one line: *"Fix the 2 site lines today (location → Kuningan/Sudirman, price → whichever is true: 750 or 800)?"*. This covers W1, W2 and the price fact in one yes/no.
3. **11/20 readout:** compare the real 7d CPL to this table. If the gate is shut and none of B/C/D was applied, tell Alvian plainly that criterion 2 (Rp 1M/day by 12/05) is out of reach, as `scale_plan.md` commits to.

## Caveats
- 22 leads/week is a small sample. ±2 leads moves the 7d CPL by about ±10% *(calc)*. A single good or bad week can open or shut the gate by itself.
- C's lift size is the most uncertain number here. The pixel funnel (`2026-11-06_pixel_funnel_baseline.md`) will measure it within 3–4 days of the fix.

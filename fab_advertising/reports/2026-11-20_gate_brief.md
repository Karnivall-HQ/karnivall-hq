# M-001: 11/20 gate brief (what gets the 7d CPL to ≤ Rp 95k by 11/20)

## 🔄 Refresh 2026-11-14 08:01 WIB (base 116.5k, 11/13 locked in). Supersedes everything below.
**Base:** 7d 11/07–11/13: PEIKIRA Rp 2,016,453 / 14 (**144.0k**), BC Rp 313,500 / 6 (52.3k) → 116.5k *(calc)*. Inside PEIKIRA: control Rp 1,091,647 / 6 (all 6 from Ad015), PEIKIRA2 Rp 924,806 / 8 (**115.6k**), ADSET-3 Rp 0.
**Window 11/13–11/19, day 1 is already known:** 11/13 PEIKIRA Rp 293,851 / **0 leads**. Method: PEIKIRA Rp 288k/day (7d rate) at 144.0k unless changed; BC flat at its 7d rate; a change counts from the day after it goes live; site lift = LP→Lead 3.9% → 4.4% (+0.5pt) or 4.9% (+1pt), applied to PEIKIRA + BC. "Ad015 paused" = the freed spend runs at PEIKIRA2's 115.6k (optimistic; at 130k the numbers rise ~8k). Script: computed this run, numbers below are all *(calc)*.

| # | Scenario (live **11/14 eve** = 5 changed days) | 7d CPL 11/13–11/19 | Gate |
|---|---|---|---|
| A | Nothing changes | **129.8k** | ❌ |
| F | Ask #1a only: Ad015 paused | 114.2k | ❌ |
| C | Ask #2 only: site W1+W2, +0.5pt / +1pt | 117.8k / 107.8k | ❌ / ❌ |
| F+C | Ad015 paused + site +0.5pt / **+1pt** | 103.3k / **94.4k** | ❌ / ✅ just |
| E | ADSET-3 1/3 share at 70k / 95k (rest 144k) | 108.5k / 118.4k | ❌ |
| F+E | Ad015 paused + ADSET-3 1/3 at 70k / 95k | 100.8k / 109.4k | ❌ |
| F+E | Ad015 paused + ADSET-3 **60%** at 70k / 95k | **92.2k** / 105.8k | ✅ / ❌ |
| F+C+E | All three (+0.5pt), ADSET-3 1/3 at 70k / 95k / 130k | **91.0k** / 98.9k / 105.8k | ✅ / ❌ / ❌ |
| F+C+E | All three (+0.5pt), ADSET-3 60% at 70k / 95k | **83.1k** / 95.6k | ✅ / ❌ just |

**One day later (live 11/15 eve, 4 days):** F+C(+1pt) 99.8k ❌; all three at 1/3 share 96.8k ❌ even if ADSET-3 wins at 70k; all three at 60% share + ADSET-3 at 70k 89.6k ✅. **Live 11/16 eve:** only "all three, 60% share, ADSET-3 at 70k" gets close (97.1k ❌).

**ADSET-3 break-even CPL (live 11/14 eve)** *(calc)*: share 1/3 → ≤ 48.4k (Ad015 running) / ≤ 58.0k (Ad015 paused) / **≤ 81.3k with Ad015 paused + site +0.5pt**; share 60% → ≤ 68.7k / ≤ 74.5k / ≤ 93.6k. (The 11/14 07:02 NOW line "79.3k at 1/3 from 11/15" used the old 116k incumbent; the incumbent PEIKIRA is now 144k and day 1 is a locked 0-lead day, so the bar is lower.)

### What this means (INFERRED from the table)
1. **No single lever opens the gate any more.** On 11/13 the site fix alone did (93.1k); the 0-lead 11/13 day and PEIKIRA's slide to 144k took that away.
2. **The cheapest path is both open asks today:** #1 (pause Ad015) + #2 (site W1+W2) live by tonight, and then it needs the +1pt case (94.4k, ~0.6k of margin) or ADSET-3 to deliver at ≤ ~81k on a 1/3 share. Every day of delay costs ~5k.
3. **Likeliest outcome: gate ❌ on 11/20.** Nothing has been applied in 9 days of asks, and the ±10% weekly noise (20 leads) is larger than the best-case margin. Prepare the criterion-2 message ("Rp 1M/day by 12/05 out of reach") now; keep the asks open because the same changes are what lower the CPL for criterion 1 after 11/20.
4. The 11/20 read rules below still apply; numbers in the 11/13 section are superseded.

## 🔄 Refresh 2026-11-13 09:01 WIB (new base + ADSET-3 path). This section supersedes the numbers below.
**Base:** 7d 11/06–11/12 (11/13 readout, `m001_tracker.md`): PEIKIRA Rp 2,095,538 / 18 (116.4k), BC Rp 280,028 / 5 (56.0k) → **Rp 103,286** *(calc)*. Window judged on 11/20 = full days **11/13–11/19**. Method as below: per-day rates held flat, new spend replaces PEIKIRA spend 1:1 (CBO Rp 300k unchanged), BC flat. ADSET-3 assumed to deliver from 11/14 (6 of 7 days; Rp 0 / 0 impr at 08:0x 11/13).

| # | Scenario | 7d CPL (11/13–11/19) | Gate |
|---|---|---|---|
| A | Nothing changes, ADSET-3 gets no share | **Rp 103.3k** *(calc)* | ❌ |
| C | W1+W2 live, +0.5pt LP→Lead, for 6 / 5 / 3 days (live 11/13 eve / 11/14 eve / 11/16 eve) | **93.1k / 94.6k / 97.9k** *(calc)* | ✅ / ✅ just / ❌ |
| C+ | W1+W2, +1pt, 6 / 5 / 3 days | **84.7k / 87.3k / 93.1k** *(calc)* | ✅ |
| E | ADSET-3 takes **1/3** of PEIKIRA at 70k / 95k / 130k CPL | **90.1k / 98.4k / 105.7k** *(calc)* | ✅ / ❌ / ❌ |
| E | ADSET-3 takes **60%** of PEIKIRA at 70k / 95k / 130k CPL | **81.5k / 94.7k / 107.8k** *(calc)* | ✅ / ✅ just / ❌ |
| C+E | W1+W2 (+0.5pt, 6 d) + ADSET-3 1/3 at 95k / 130k | **88.6k / 95.3k** *(calc)* | ✅ / ❌ just |

**Break-even ADSET-3 CPL (opens the gate with no site fix)** *(calc)*: share 1/3 → **≤ Rp 83.5k**; share 60% → ≤ 95.7k; share 80% → ≤ 100.1k. It is easier than the 11/11 "≤ 70k" bar because the other two PEIKIRA ad sets now run 116k (control 124.9k, PEIKIRA2 109.6k): any new ad set that merely hits target pulls the blend down.

### What changed vs 11/11
1. **ADSET-3 is now a second independent path** (team-launched, not Wave 1). Its photos are new (15 images, INFERRED), so its CPL is unknown; the read card (`2026-11-13_adset3_read_card.md`) decides keep/kill. Wave 1 (scenario D) is on hold behind ask #2, so D is dropped from this table.
2. **The site fix has a deadline inside the window:** at +0.5pt it must be live by **11/14 evening** (5 days) to open the gate on its own; from 11/16 it no longer does (97.9k). At +1pt it still works if live by 11/16.
3. **Item 4 / scenario B is retired** (11/12 card). Not modelled.
4. W1/W2 still the only lever that does not depend on an untested ad set; with ADSET-3 at target, C+E gives ~6k of margin below 95k against the ±10% weekly noise *(calc)*.

### Read on 11/20
- Gate ✅ and ADSET-3 share ≥ 1/3 at ≤ 84k → credit ADSET-3 (and start S1 of the scale ladder per `2026-11-12_scale_plan_v2.md`).
- Gate ✅ with W1/W2 live and ADSET-3 ≥ 95k → credit the site; pixel LP→Lead read (`w1w2_lift_template.md`) confirms.
- Gate ❌ → tell Alvian criterion 2 (Rp 1M/day by 12/05) is out of reach, as committed.
- Caveat: 23 leads/week; ±2 leads ≈ ±10% CPL *(calc)*. One week can open or shut the gate by noise alone.

---
_Original brief (2026-11-11), kept for history:_
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
2b. **Volume half (added 11/12 11:01):** a winning creative wave adds only Rp 100–185k/day at ≤ 95k (8-wk ad-set data). Rp 1M/day needs 4–7 winners; best realistic 12/05 case with W1/W2 + Wave 1 ≈ Rp 450–520k/day *(calc)*. Use the scenario table in `2026-11-12_scale_plan_v2.md` for the criterion-2 call.
3. **11/20 readout:** compare the real 7d CPL to this table. If the gate is shut and none of B/C/D was applied, tell Alvian plainly that criterion 2 (Rp 1M/day by 12/05) is out of reach, as `scale_plan.md` commits to.

## Caveats
- 22 leads/week is a small sample. ±2 leads moves the 7d CPL by about ±10% *(calc)*. A single good or bad week can open or shut the gate by itself.
- C's lift size is the most uncertain number here. The pixel funnel (`2026-11-06_pixel_funnel_baseline.md`) will measure it within 3–4 days of the fix.

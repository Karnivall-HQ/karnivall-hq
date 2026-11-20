# M-001 criterion 2: the honest date for Rp 1M/day (BC-only path, caps kept)
_Fuku cloud heartbeat 2026-11-20 20:02 WIB. Groundwork, read-only, no new pulls. Propose-only. Not an ask._
_Inputs: branch C of `2026-11-20_criterion2_replan.md` (base, winner size, BC verification clock), `../creatives/2026-11-13_weekly_photo_calendar.md` (photos Saturday → launch Monday), 11/20 tracker row. Script: rerun the table below with `python3` on the formula in §3._

## 1. Answer (for the 11/23 weekly)
- **Rp 1M/day at ~95k is ≈ Feb 2027 in the middle case, ≈ mid-Jan only if everything goes right, ≈ April if not** *(calc, INFERRED hit rates)*. 12/05 is not reachable on any path; 01/15 only in the good case with the first photo wave live by 11/30.
- **The date is set by one input: the first Saturday the Fab team sends 3 phone photos.** Every week it slips, every row below slips 7 days. Second input: the site fix (W1+W2), which I treat as the difference between the low and mid hit rate (INFERRED).

## 2. Date table (first photo wave launch date × case) *(calc)*
| First wave launches (photos the Saturday before) | Good (1 in 3 ads wins, Rp 185k/winner, day-14 read) | Mid (1 in 4, Rp 142k, day-21 read) | Low (1 in 5, Rp 100k, day-21 read) |
|---|---|---|---|
| **11/30** (photos 11/28) | 5 waves → **01/11** | 8 waves → **02/08** | 15 waves → **03/29** |
| 12/07 (photos 12/05) | 01/18 | 02/15 | 04/05 |
| 12/14 (photos 12/12) | 01/25 | 02/22 | 04/12 |

Winners needed: good 4.3, mid 5.9, low 8.8 *(calc)*. One wave = 3 ads/week, each as its own BC ad set (cap 94,250).

## 3. How it's computed
- Base after the BC cap ladder: good 197k, mid 157k, low 117k/day (BC Rp 97.0k/day + ladder +20–100k) [branch C, *(calc)*, ladder INFERRED].
- Winners needed = (1,000k − base) ÷ winner size (100–185k/day, 8 weeks of account data; mid 142k).
- Winners per wave = 3 × hit rate (INFERRED from the 11/05 visual review: phone photos Rp 18–68k vs renders 200–372k; not a controlled test).
- Date = first launch + (waves − 1) × 7 days + read lag. Read lag = 14 days only if BC gives a new ad set a top share (≈ Rp 25–35k/day); otherwise 21 days (branch C verification clock).

## 4. What each input is worth *(calc / INFERRED)*
| Input | Who | Effect on the date |
|---|---|---|
| 3 phone photos every Saturday | Fab team (shot list ready: `../creatives/2026-11-12_shoot_card_v2.md`) | Sets day 0. Each missed Saturday = +7 days to every case. Without photos the date is **never** (only Wave 0: 1 ad from existing images). |
| Site fix W1+W2 (~10 min) | whoever edits fabwarehouses.com | Every wave lands on a page that still says "Jakarta Pusat" ×9 and "Rp 800.000" (curl 11/20 13:02). Fix ≈ −10% CPL (103.3k → 93.1k *(calc, 11/13)*) → more ads clear ≤ 95k → roughly low → mid (INFERRED): **−7 weeks** at an 11/30 start (03/29 → 02/08). |
| BC cap ladder (held card) | Markus (4 fields) | Base +20–100k/day → about 1 fewer winner needed (≈ −1 to −2 waves). Already inside the base above. |
| Wave 0 (N2 carousel, no photos) | Markus | 0–1 winner from 11/23 (one ad); moves a case by ≤ 1 wave. Not counted above. |
| Undo the 11/15 PEIKIRA change | Alvian | Adds volume at ≈ 157–199k CPL → breaks criterion 1 (≈ 114k, INFERRED). Not part of this path. |

## 5. Risks that push the date later (not in the table)
- **Winner decay:** control went 81k → 173k in one week; Ad015 lasted ~3 weeks [account data]. By wave 8+ the early winners may be gone, so the mid/low cases may need 1–3 more waves. [INFERRED]
- **BC share for new ad sets:** a brand-new BC ad set getting Rp 25–35k/day in week 1 is unproven (ADSET-3 in PEIKIRA got Rp 33 in 7 days). If BC starves new ad sets too, the read lag becomes ≈ 43 days and every date moves ≈ +3 weeks. [INFERRED]
- **Holiday weeks** 12/20–01/05: no account data for last December. [unknown]

## 6. Line for the 11/23 weekly (replaces "≈ Feb, INFERRED" in branch C)
> 📊 Criterion 2 (Rp 1M/day at ~95k): honest date ≈ **Feb** (good case mid-Jan, bad case April), and it starts the Saturday the first 3 phone photos arrive. Each week without photos = +7 days; the site fix ≈ −7 weeks. No date ask until the first BC photo wave reads.

Fill on 11/23: if no photos by 11/22, shift to the 12/07 row. Keep "no date ask" (branch C rule, and the asks-stalled rule: no new decision while #2/#3 sit).

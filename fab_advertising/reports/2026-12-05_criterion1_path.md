# M-001 criterion 1 (7d CPL ≤ Rp 95k) by the 12/05 deadline: what still gets there
_2026-11-14 11:02 WIB, Fuku cloud heartbeat (groundwork). Read-only, nothing changed in the ad account. Propose-only._
_Script: `fuku/bin/criterion1_model_1205.py` (re-run with fresh base numbers at each readout). Sister files: `2026-11-20_gate_brief.md`, `2026-11-20_gate_miss_note.md`, `2026-11-20_criterion2_replan.md`._

## Why this exists
The 11/20 gate is likely ❌ (gate brief, 11/14 08:01). That gate is about **criterion 2** (the scale ladder to Rp 1M/day). **Criterion 1 is judged separately, on 12/05, on the 7d window 11/28–12/04.** That window has not started, so any lever live by **11/27 evening** counts for all 7 days. A 11/20 miss does not mean criterion 1 is lost.

## Base and method
- Base = 7d 11/07–11/13 (tracker 11/14 row): PEIKIRA Rp 2,016,453 / 14 = **144.0k**, BC Rp 313,500 / 6 = 52.3k → **116.5k** *(calc)*. [account data]
- Spend held flat (PEIKIRA CBO Rp 300k/day, BC at its 7d rate). "Ad015 paused" = the freed spend runs at PEIKIRA2's 115.6k (optimistic) or 130k. Site lift = LP→Lead 3.9% → 4.4% (+0.5pt) / 4.9% (+1pt), on PEIKIRA + BC. Same method as the gate model. [INFERRED assumptions]
- All numbers below *(calc)*.

## Full window (lever live by 11/27 eve)
| # | Scenario | 7d CPL 11/28–12/04 | Criterion 1 |
|---|---|---|---|
| A | Nothing changes | 116.5k | ❌ |
| F | Ad015 paused (freed at 115.6k / 130k) | 99.4k / 108.3k | ❌ |
| C | Site W1+W2, +0.5pt / +1pt | 103.3k / 92.7k | ❌ / ✅ |
| **F+C** | **Ad015 paused + site +0.5pt** (freed at 115.6k / 130k) | **88.1k** / 96.0k | **✅** / ❌ just |
| E | ADSET-3 wins: 1/3 share at 70k, Ad015 still on | 93.4k | ✅ |
| F+E | Ad015 paused + ADSET-3 1/3 at 70k / 95k | 85.6k / 94.3k | ✅ / ✅ just |
| F+C+E | All three (+0.5pt), ADSET-3 1/3 at 95k / 130k | 83.6k / 90.6k | ✅ / ✅ |

**Break-even PEIKIRA CPL** (BC flat): no site fix ≤ **108.8k**; with site +0.5pt ≤ 128.1k; +1pt ≤ 149.1k. PEIKIRA runs 144.0k today, PEIKIRA2 115.6k.

## Deadline for the two open asks (OUTBOX #1 + #2)
| Both live by | Days in window | F+C (+0.5pt) | F alone | C (+0.5pt) alone |
|---|---|---|---|---|
| 11/27 eve | 7 | **88.1k ✅** | 99.4k | 103.3k |
| 11/29 eve | 5 | 94.7k ✅ just | 103.7k | 106.7k |
| 12/01 eve | 3 | 102.4k ❌ | 108.5k | 110.4k |
| 12/03 eve | 1 | 111.4k ❌ | 113.7k | 114.4k |

## What this means (INFERRED from the table)
1. **Criterion 1 is still reachable for 12/05, with ~7k of margin, if asks #1 + #2 are both live by 11/27.** The last workable date is **11/29 evening**; after that no combination of today's levers gets there.
2. **Neither lever is enough alone** at +0.5pt. The site fix alone works only in the +1pt case; the Ad015 pause alone only if PEIKIRA's rest drops below ~108.8k.
3. **ADSET-3 is the independent path:** if it gets a 1/3 share and runs ≤ ~95k (with Ad015 paused) it carries criterion 1 even without the site fix. It is untested (Rp 0 for its first day); verdict 11/27.
4. Noise: ~20–25 leads/week, so ±2 leads ≈ ±10% *(calc)*. 88.1k only just survives a bad week (≈ 95.3k at −2 leads *(calc)*); 94.7k does not. So 11/27 is the real deadline, 11/29 is a coin flip.

## Use on 11/20 (gate-miss message)
- The gate-miss note keeps "criterion 1 stays the 12/05 goal" and now adds one sentence: "Criterion 1 is still reachable for 12/05: asks #1 + #2 live by 11/27 ≈ 88k; last workable date 11/29." It is a fact line, not a new ask.

## Re-plan option if nothing moves by 11/27 (for the 11/27 readout, not before)
If on 11/27 neither ask is live and ADSET-3 is not a winner, criterion 1 is out of reach for 12/05 (best case ≈ 102k+). Then the single ❓ is: **"Move criterion 1 to 12/19 (window 12/12–12/18), same Rp 95k target?"** Recommendation then: yes, on the condition that asks #1 + #2 go live that week; a deadline move without a lever just reschedules the miss. Do not send this before 11/27 (stalled-asks rule: no new decision while 3 are open).

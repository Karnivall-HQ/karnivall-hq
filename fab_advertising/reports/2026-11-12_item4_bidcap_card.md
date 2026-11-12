# Item 4 apply-ready card: BC bid cap Rp 94,250 → Rp 105,000
_2026-11-12 08:01 WIB · cloud heartbeat · read-only · account `484578521394893`, campaign BC CBObass005 `120236222888610572`_
_Rules applied: `fuku/memory/playbooks/meta-tests-and-proposals.md` §C (bid caps: ≥ 8 weekly rows + bid-category activity log; raise only where CPL ÷ cap < ~0.85)._

## Verdict
**087 Copy 7 fails the gate. Item 4 is retired for 087.** A narrower BC204-only version passes the ratio test, but it's too small to matter for the 11/20 gate, so it stays **parked as optional**. There's no new ask.

## Data (account data, `ads_get_ad_entities` adset, 2026-09-17 → 11-11, time_increment 7)
Cap = Rp 94,250 in every row. The bid-category activity log from 09/01 has **no bid change** on either ad set (bid edits only on PEIKIRA/KENJI/AKIRA ad sets), so the cap was constant across all 8 weeks.

| Week from | 087 Copy 7 `120241535471900572` spend / leads / CPL | BC204 Manny6 `120246071060620572` spend / leads |
|---|---|---|
| 09/17 | 683,602 / 5 / 136,720 | 49,957 / 0 |
| 09/24 | 510,104 / 5 / 102,021 | 97,542 / 2 |
| 10/01 | 378,672 / 5 / 75,734 | 147,969 / 2 |
| 10/08 | 154,273 / 0 / — | 36,334 / 0 |
| 10/15 | 278,701 / 5 / 55,740 | 12,910 / 1 |
| 10/22 | 613,221 / 8 / 76,653 | 39,188 / 2 |
| 10/29 | 281,670 / 2 / 140,835 | 20,546 / 0 |
| 11/05 | 78,259 / 1 / 78,259 | 13,942 / 0 |

| Ad set | 8-wk spend / leads | 8-wk CPL | CPL ÷ cap | Last 4 wk CPL ÷ cap | Spend/day last 2 wk |
|---|---|---|---|---|---|
| 087 Copy 7 | 2,978,502 / 31 | **96,081** *(calc)* | **1.02** ❌ | 0.83 (78,241, 16 leads) | 25.7k *(calc)* |
| BC204 Manny6 | 418,388 / 7 | 59,770 *(calc)* | **0.63** ✅ | 0.31 (3 leads) | 2.5k *(calc)* |

Supporting reads (Meta, required follow-ups): trend tool: 087 CPR **GOOD** (93.5% change), CVR GOOD, CTR GOOD, CPM BAD (+29%). Benchmark: 087 CPR **14.3% worse** than peers; BC204 **58.7% better** than peers.

## Why 087 fails
- At the current cap, 087 already averages **Rp 96.1k per lead over 8 weeks**, above the 95k target. If the CPL ÷ cap ratio holds [INFERRED, same assumption as `scale_plan.md`], cap 105k → **≈ Rp 107k CPL** *(calc)*.
- The 11/05 case used a 30-day window (ratio 0.889). The 8-week window includes two weeks at 137k and 141k. Only the last 4 weeks (0.83) pass, and the playbook asks for ≥ 8 rows because spend and CPL swing this much at a fixed cap (weekly spend 683k → 78k with no bid edit).
- So for 087, raising the cap buys spend at **above-target CPL**. That's the wrong lever for a CPL gate.

## BC204-only variant (parked, optional; apply only after the site fix)
- **Lever type:** adds volume (not lowers CPL).
- **Change:** ad set `120246071060620572` "BC204 Manny6 Slide APT Bid94 JKTcity NoExcl", bid cap **Rp 94,250 → Rp 105,000**. Nothing else. Budget is campaign-level (CBO) and stays unchanged.
- **Why:** 8-wk CPL 59.8k at ratio 0.63 *(calc)*. At cap 105k → ≈ 66.6k *(calc)* [INFERRED]. Benchmark: 58.7% better than peers. Delivery is nearly starved (Rp 2.5k/day).
- **Honest size:** 7 leads in 8 weeks. Even a 5× spend jump is ≈ Rp 12k/day *(calc)*, so the blended Fab CPL barely moves. It's a cheap probe, not a gate lever.
- **Read rules (written before launch):**
  - Absolute kill: revert to Rp 94,250 if BC204 spends ≥ Rp 190k (2× target) with 0 leads, or ≥ Rp 285k (3×) with ≤ 1 lead.
  - Day-7 verdict: keep if 7d CPL ≤ Rp 95k; else revert.
  - Comparative: BC204 7d CPL vs the rest of BC (untouched, same window). Revert if BC204 is > 1.3× the rest.
  - Read on full-day data at the first readout after 07:00 WIB.
- **How to apply (Alvian or Markus):** Ads Manager → BC CBObass005 → ad set BC204 Manny6 → Bid control Rp 94,250 → Rp 105,000 → Publish. Then reply "applied BC204" in INBOX.

## Knock-on changes
- **11/20 gate brief scenario B** (item 4, ≈ 104.1–108.5k) assumed 087 delivers at 93.4k. On 8-week data, 087 at 105k would land ≈ 107k, so scenario B is now **≈ the upper end (≥ 107k)** *(calc)* and B+C loses its "+73k/day at ~target" bonus. The site fix (W1+W2) is still the only single lever that can open the gate.
- `scale_plan.md` S1 ("BC recovers via items 3+4") no longer has a lever. BC capacity on current creative = whatever it delivers at Rp 94,250. New BC volume needs new creative, not a higher cap.

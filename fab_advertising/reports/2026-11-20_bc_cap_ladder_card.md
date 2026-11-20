# BC volume lever: cap-ladder card (replaces the BC204-only probe)
_2026-11-20 08:02 WIB · cloud heartbeat · read-only · account `484578521394893`, campaign BC CBObass005 `120236222888610572` (Rp 5M/day CBO)_
_Rules applied: `meta-tests-and-proposals.md` §C (≥ 8 weekly rows + bid log; raise only CPL ÷ cap < ~0.85; budget must bind), §A (kill = spend multiples + one comparative rule). Status: **held, not asked** (stalled-ask rule: OUTBOX #2/#3 still open). Ads are propose-only: Alvian/Markus apply._

## Verdict
1. **BC's limiter is the cap, not the budget.** 7d 11/13–11/19 BC spent Rp 679,253 = Rp 97.0k/day = **1.94% of the Rp 5M budget** *(calc)*. Bid-category + all activity on the BC campaign since 11/12: **none** (log empty). Every top ad set still sits at Rp 94,250 (account data).
2. **The BC204-only probe is retired in favour of a 4-ad-set ladder.** BC204 alone went 0 leads in its last 4 weeks of 3 (4-wk Rp 86,591 / 1) and delivers Rp 1.9k/day; it can't read on its own. Four ad sets pass the 8-week ratio test and together hold 33 leads.
3. **087 Copy 7 still fails** (8-wk ratio 0.96, improved from 1.02 on 11/12 but > 0.85). Leave it.
4. **Honest size:** this adds **≈ Rp 20–100k/day** *(calc, INFERRED)*, at ≈ 60–80k CPL. Good for criterion 1, **not** a path to Rp 1M/day. Criterion 2 still needs new winning creative.

## Data: 8 weekly rows, 09/25 → 11/19 (account data, `object_ids`, `time_increment 7`, cap Rp 94,250 all weeks)

| Ad set | ID | 8-wk spend / leads | 8-wk CPL *(calc)* | CPL ÷ cap | Last 4 wk | 11/13–11/19 | Peak week spend | Pass? |
|---|---|---|---|---|---|---|---|---|
| BCbatch201 Manny5 | `120245708232080572` | 611,993 / 11 | 55,636 | **0.59** | 186,400 / 2 | 73,060 / 2 | 233,520 | ✅ |
| BC204 Manny6 | `120246071060620572` | 376,353 / 7 | 53,765 | **0.57** | 86,591 / 1 | 15,471 / 0 | 127,015 | ✅ (weak recency) |
| BC208 UGC | `120247180846830572` | 363,096 / 6 | 60,516 | **0.64** | 121,070 / 2 | 52,910 / 1 | 108,218 | ✅ |
| BC3-21 Anak Tele – Copy 10 | `120250479689810572` | 637,441 / 9 | 70,827 | **0.75** | 148,210 / 5 | 21,156 / 2 | 253,283 | ✅ |
| BC batch093 – Copy 13 | `120244142678390572` | 120,376 / 4 | 30,094 | 0.32 | 56,019 / 1 | 23,855 / 1 | 23,855 | ➖ too small (4 leads, never > Rp 24k/wk) |
| BC batch087 – Copy 7 | `120241535471900572` | 2,438,297 / 27 | 90,307 | 0.96 | 1,090,610 / 13 | 207,100 / 3 | 555,204 | ❌ |
| BC4-08 Usir – Copy 7 | `120253178717740572` | 536,536 / 5 | 107,307 | 1.14 | 39,624 / 1 | 20,045 / 1 | 176,564 | ❌ |
| BC3-13 Goal – Copy 2 | `120250129960290572` | 351,148 / 2 | 175,574 | 1.86 | 138,044 / 1 | 94,275 / 1 | 94,275 | ❌ (watch: biggest BC spender after 087 this week at 140k peer CPR) |

- The 8 ad sets above = Rp 521,394 = **76.8%** of BC 7d spend and all 12 BC leads *(calc)*; the other ~42 ad sets spent Rp 157,859 / 0 leads.
- Meta reads (required follow-ups): trend tool returned only BC3-21 c10 (CPR GOOD, CTR/CVR BAD). Benchmark (peer median CPR Rp 63,075): BC3-21 c10 **49.6% better**, BC204 **23.8% better**; BC3-13 c2 122.7% worse, 201 61.2% worse (short window), 208 / BC4-08 ≈ 9% worse, 093 in line. The tool's own window is shorter than 8 weeks; I weight the 8-week rows.

**Ladder group (201 + 204 + 208 + BC3-21 c10):** 8-wk Rp 1,988,883 / 33 = **60.3k CPL** *(calc)*; ≈ Rp 35.5k/day average over 8 weeks, ≈ Rp 17k/day the last 2 weeks *(calc)*. Their peak weeks sum to Rp 722k ≈ Rp 103k/day *(calc)* at the **same** cap, so the auction (not only the cap) sets their pace.

## Proposed changes for Alvian to apply (held; one edit session, ~3 min)
Lever type: **adds volume at ≈ target CPL.** Budget stays (CBO Rp 5M, it doesn't bind).

| # | Ad set (ID) | Bid control: now → proposed | Expected CPL if ratio holds *(calc, INFERRED)* |
|---|---|---|---|
| 1 | BCbatch201 Manny5 Bid94 JKTcity NoExcl (`120245708232080572`) | Rp 94,250 → **Rp 105,000** | ≈ 62.0k |
| 2 | BC204 Manny6 Slide APT Bid94 JKTcity NoExcl (`120246071060620572`) | Rp 94,250 → **Rp 105,000** | ≈ 59.9k |
| 3 | BC208 UGC JKTcity NoExcl (`120247180846830572`) | Rp 94,250 → **Rp 105,000** | ≈ 67.4k |
| 4 | BC3-21 Anak Tele JKTcity – Copy 10 (`120250479689810572`) | Rp 94,250 → **Rp 105,000** | ≈ 78.9k |

How: Ads Manager → BC CBObass005 → each ad set → Bid control → 105000 → Publish. Reply "ladder applied" in INBOX.
Why 105k and not "remove the cap": PEIKIRA's ad sets at 105k still starve, so 105k is a small, reversible step; uncapped BC would hand the 5M CBO to the auction at unknown CPL (the 11/15 PEIKIRA lesson in reverse).

## Read rules (written before launch)
- **Kill, per ad set:** revert that ad set to Rp 94,250 if it spends ≥ Rp 190k (2× target) with 0 leads, or ≥ Rp 285k (3×) with ≤ 1 lead.
- **Comparative:** ladder group 7d CPL vs the untouched rest of BC, same window. Revert all four if the group is > 1.3× the rest **and** > 95k.
- **Day-7 verdict (group):** keep if group CPL ≤ 95k on ≥ Rp 285k spend; spend < Rp 285k = "cap wasn't the limiter" → revert nothing, close the lever, record it.
- **Account guard:** if Fab 7d CPL crosses 95k during the window and the ladder group is the cause (group CPL > 95k), revert all four.
- Read on full-day data at the 07:00 readout; day 1 split at the edit time (playbook §D3).

## When to ask
Not now. Raise it as a one-line ask only when #2 or #3 moves, or at the 11/23 weekly if both are still stalled (swap it in for the weaker ask). Before asking, re-pull this table on the then-latest 7d (§D).

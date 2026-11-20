# Incess pick-level split pre-pull: 042 + 030 (for the 11/23 weekly)
_2026-11-20 18:02 WIB cloud heartbeat · Incess Ads `2017038114993984` · campaign OMO ADVLeads `120233576079370222` · read-only: ads_get_ad_entities level=adset, time_increment 7, 09/25–11/19; required follow-ups: trend (no data), peers (empty peer set)._
_Trigger: 3-day 11/16–11/18 Incess 41.2k > 30k → pick-level split (042 + 030 first). Monday adds only the 11/16–11/22 row and reads the table._

## 8 weekly rows (account data; CPL per row from the tool, totals *(calc)*)
| Week | 042 spend / leads | 042 CPL | 042 CTR · freq | 030 spend / leads | 030 CPL | 030 CTR · freq |
|---|---|---|---|---|---|---|
| 09/25–10/01 | 1,748,653 / 49 | 35,687 | 2.77% · 1.37 | 323,829 / 7 | 46,261 | 2.20% · 1.55 |
| 10/02–10/08 | 1,910,703 / 48 | 39,806 | 2.49% · 1.42 | 326,669 / 7 | 46,667 | 1.79% · 1.40 |
| 10/09–10/15 | 1,419,462 / 38 | 37,354 | 2.99% · 1.44 | 340,322 / 14 | 24,309 | 2.34% · 1.62 |
| 10/16–10/22 | 1,258,440 / 32 | 39,326 | 2.76% · 1.40 | 460,751 / 10 | 46,075 | 2.27% · 1.49 |
| 10/23–10/29 | 1,171,282 / 25 | 46,851 | 2.88% · 1.49 | 255,711 / 11 | 23,246 | 2.61% · 1.39 |
| 10/30–11/05 | 1,134,045 / 35 | 32,401 | 2.65% · 1.53 | 315,716 / 11 | 28,701 | 2.40% · 1.41 |
| 11/06–11/12 | 1,202,482 / 45 | 26,722 | 3.30% · 1.53 | 252,260 / 9 | 28,029 | 2.82% · 1.28 |
| 11/13–11/19 | **2,180,044 / 64** | **34,063** | 2.51% · 1.56 | **783,633 / 18** | **43,535** | 2.51% · 1.36 |
| **8-wk** *(calc)* | 12,025,111 / 336 | **35,789** | | 3,058,891 / 87 | **35,160** | |

Caps unchanged on every row: 46,000 (bid_amount). 030 last week CPL ÷ cap = 0.95 *(calc)*.

## What it says (before Monday's data)
- **Not fatigue.** Frequency ≤ 1.56 all 8 weeks; last week's CTR (2.51% both) sits inside each ad set's own 8-wk band (042 2.49–3.30%, 030 1.79–2.82%).
- **Volume expansion at constant caps.** Last week's spend vs the prior 7-wk average: 042 ×1.55, 030 ×2.41 *(calc)*. More bids won, at higher prices (INFERRED, same read as `2026-11-19_incess_bidcap_revalidate.md`).
- **Both still inside their own 8-wk CPL range** (042 26.7–46.9k, 030 23.2–46.7k), and 8-wk CPL ≈ 35–36k on both. 030 swings a lot on small counts (7–18 leads/wk).

## Monday rules (pre-set, so 11/23 is read-only + one table)
1. Add the 11/16–11/22 row for each (same call, `time_range` 11/16–11/22, no increment).
2. **Flag** an ad set only if its 7d CPL > its 8-wk max (042 > 46.9k, 030 > 46.7k) **or** CTR < its 8-wk min (042 < 2.49%, 030 < 1.79%) **or** freq > 2.0.
3. No flag → weekly says "Incess CPL up on volume, not fatigue; caps stay; no ask". A flag on 030 alone → note only (030 = 18 of the 82 leads 042+030 got last week; small counts swing); a flag on 042 → ad-level split of 042 (one live ad) + creative refresh idea in Top 3, still no ad-account ask before lead value is known.
4. Peer benchmarks: none (empty peer set); trend tool: no data. Don't wait for them.

---

## Part 2 (19:02 WIB): 047 + 026, the other 2 picks (same call shape, read-only)
`OMObatch047 UGC 1Ad IND-Bali NoExcl – Copy` `120239723303450222` (cap 46,000) · `OMObatch3 026 Manny5Ads ALLindo NoExc MaP` `120244551313580222` (cap 45,000). CPL per row *(calc)* from tool spend/leads.

| Week | 047 spend / leads | 047 CPL | 047 CTR · freq | 026 spend / leads | 026 CPL | 026 CTR · freq |
|---|---|---|---|---|---|---|
| 09/25–10/01 | 166,437 / 3 | 55,479 | 3.12% · 1.37 | 867,689 / 31 | 27,990 | 2.19% · 1.61 |
| 10/02–10/08 | 604,688 / 22 | 27,486 | 2.46% · 1.69 | 803,168 / 26 | 30,891 | 2.07% · 1.61 |
| 10/09–10/15 | 523,578 / 15 | 34,905 | 2.93% · 1.74 | 840,807 / 40 | 21,020 | 2.54% · 1.84 |
| 10/16–10/22 | 499,633 / 18 | 27,757 | 2.95% · 1.65 | 856,875 / 30 | 28,562 | 2.15% · 1.88 |
| 10/23–10/29 | 586,852 / 25 | 23,474 | 3.14% · 1.67 | 651,780 / 20 | 32,589 | 2.56% · 1.65 |
| 10/30–11/05 | 752,945 / 26 | 28,959 | 2.29% · 1.76 | 411,225 / 13 | 31,633 | 2.36% · 1.67 |
| 11/06–11/12 | 713,209 / 42 | 16,981 | 2.88% · 1.76 | 198,554 / 13 | 15,273 | 2.64% · 1.40 |
| 11/13–11/19 | **1,209,951 / 34** | **35,587** | 2.87% · 1.66 | **492,697 / 18** | **27,372** | 2.38% · 1.56 |
| **8-wk** *(calc)* | 5,057,293 / 185 | **27,337** | | 5,122,795 / 191 | **26,821** | |

Caps unchanged on every row (047 46,000; 026 45,000). Last week CPL ÷ cap: 047 0.77, 026 0.61 *(calc)*.

### What it says
- **047 = same pattern as 042/030:** spend ×2.20 vs its prior 7-wk avg *(calc)*, CPL 17.0k → 35.6k, CTR 2.87% (in band), freq 1.66. Volume expansion, not fatigue (INFERRED). Its 35.6k is the highest week with ≥ 10 leads; the 55.5k week 1 is 3 leads (noise).
- **026 is the odd one out:** spend ×0.74 of its prior avg *(calc)* (Rp 867k/wk in Sept → 199–493k since 11/06), CPL 27.4k = cheapest of the 4 picks last week. Meta is shifting the campaign's spend away from 026 toward 042/047/030 (INFERRED; caps unchanged, so not a human edit).
- **All 4 picks, 8-wk** *(calc)*: 042 35.8k · 030 35.2k · 047 27.3k · 026 26.8k.

### Monday flag lines (047 + 026; same rules as part 1, small-count weeks < 10 leads excluded from the max)
- **047:** flag if 7d CPL > 35.6k, CTR < 2.29%, or freq > 2.0.
- **026:** flag if 7d CPL > 32.6k, CTR < 2.07%, or freq > 2.0. Also note (no flag) if spend < Rp 199k (keeps shrinking).
- Same outcome rules as part 1 rule 3: a flag means an ad-level split + creative idea in Top 3, **no ad-account ask** before lead value is known.

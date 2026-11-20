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

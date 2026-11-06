# Fab CPL rise 112k → 125k is a campaign-mix shift, not an account-wide upstream drift
_2026-11-06 15:02 WIB, cloud heartbeat. Source: Rudi MCP `ads_get_ad_entities`, act 484578521394893, time_range 2026-10-23→2026-11-05, time_increment 7. *(calc)* = Fuku's arithmetic. Corrects the 14:02 note in NOW.md ("drift is upstream / cost per LP view")._

## Account level
| Week | Spend | CPM | CTR | LP views | Cost/LPV | Leads | CPL | LPV→Lead *(calc)* |
|---|---|---|---|---|---|---|---|---|
| 10/23–10/29 | Rp 1,909,467 | Rp 28,022 | 1.66% | 525 | Rp 3,637 | 17 | Rp 112,322 | 3.24% |
| 10/30–11/05 | Rp 2,503,394 | Rp 32,397 | 1.63% | 582 | Rp 4,301 | 20 | Rp 125,170 | 3.44% |
Account CPM +15.6%, cost/LPV +18.3%, CPL +11.4% *(calc)*. Read alone, this looks like "upstream got pricier".

## Campaign level (the real story)
| Campaign | Week | Spend | Share *(calc)* | CPM | Cost/LPV | Leads | CPL | LPV→Lead *(calc)* |
|---|---|---|---|---|---|---|---|---|
| PEIKIRA-BID-CAP-LEADS `120254051672440572` | 10/23–29 | Rp 963,766 | 50% | Rp 53,839 | Rp 6,218 | 5 | Rp 192,753 | 3.2% |
| | 10/30–11/05 | Rp 2,026,490 | 81% | Rp 37,921 | Rp 5,117 | 18 | Rp 112,583 | 4.5% |
| BC CBObass005 – Copy `120236222888610572` | 10/23–29 | Rp 936,595 | 49% | Rp 18,702 | Rp 2,538 | 12 | Rp 78,050 | 3.3% |
| | 10/30–11/05 | Rp 476,904 | 19% | Rp 20,010 | Rp 2,564 | 2 | Rp 238,452 | 1.1% |
(RUDI Costcap Copy: Rp 9,106 then Rp 0, ignored.)

## Reading
1. **PEIKIRA improved on every metric** (CPM −30%, cost/LPV −18%, CPL 193k → 113k *(calc)*). Not the problem.
2. **The account CPM rose only because spend moved from BC (CPM ~Rp 19–20k) to PEIKIRA (CPM ~Rp 38k).** PEIKIRA's share went 50% → 81%. Pure mix.
3. **BC is the problem:** spend halved (bid-cap starvation, as in the 11/05 diagnosis) *and* leads fell 12 → 2 at the same CPM and cost/LPV. Leads are small-n, but BC lost ~10 leads/week, which is the whole CPL gap.
   → Supports item 4 (bid cap raise on 087 Copy 7 / BC204 Manny6) and item 3 (consolidate BC to winners). No new proposal; existing items cover it.
4. BC LPV→Lead 3.3% → 1.1% may be noise (2 leads) or the W1/W2 site mismatch hitting BC's audience; re-check in the weekly report with ad-set split.

## For the Mon 11/09 weekly report
- Always show CPM / cost per LPV **per campaign**, never only account totals (mix shifts fake an "upstream" trend).
- Add a BC ad-set split (spend, leads, bid cap) to see which winners lost delivery.

## BC ad-set split (added 16:02 WIB)
Source: `ads_get_ad_entities` level=adset, campaign 120236222888610572, same two weeks, time_increment 7.
| Ad set | Week | Spend | Leads | CPM | LP views | Bid cap |
|---|---|---|---|---|---|---|
| BC batch087 – Copy 7 `120241535471900572` | 10/23–29 | Rp 555,204 | 7 | Rp 13,694 | 289 | Rp 94,250 |
| | 10/30–11/05 | Rp 260,770 | 2 | Rp 14,244 | 125 | Rp 94,250 |
| BC3-21 Anak – Copy 10 `120250479689810572` | 10/23–29 | Rp 92,631 | 2 | Rp 47,797 | 16 | Rp 94,250 |
| | 10/30–11/05 | Rp 19,999 | 0 | Rp 37,312 | 8 | Rp 94,250 |
| batch101 Copy 21 / BC202 Manny5 / BC204 Manny6 | 10/23–29 | 16,479 / 27,026 / 39,299 | 1 / 1 / 1 | | | Rp 94,250 |
| | 10/30–11/05 | 27,104 / 9,588 / 20,471 | 0 / 0 / 0 | | | Rp 94,250 |
| All other ~50 ad sets | both weeks | < Rp 30k each | 0 | | | Rp 76–94k |

Reading:
1. **One ad set is most of BC:** 087 Copy 7 = 59% → 55% of BC spend *(calc)*. Its spend fell **−53%** *(calc)* at a flat CPM (13.7k → 14.2k), so it lost auctions under the cap, not to price. That's the bid-cap starvation pattern, now pinned to one object.
2. 087's LPV→Lead went 2.4% → 1.6% *(calc)*, small n (7 → 2 leads). The other 5 leads in wk 1 came from 4 small ad sets that each had 1–2 leads; they all went to 0.
3. **Item 4 stands, and 087 Copy 7 is the one that matters.** No new ask. If Alvian only does one BC thing, it's the 087 bid cap raise Rp 94,250 → Rp 105,000.
4. Bid caps observed: Rp 76,345 (batch036/048), Rp 80,000 (062/063), Rp 94,250 (all others). The 11/05 note "caps Rp 80k/94.25k" holds.

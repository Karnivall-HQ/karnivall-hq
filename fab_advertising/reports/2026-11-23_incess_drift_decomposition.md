# Incess drift: auction or demand? CPL decomposition 11/09–11/15 vs 11/16–11/22
_2026-11-23 08:01 WIB cloud heartbeat · Incess Ads `2017038114993984` · OMO ADVLeads `120233576079370222` · read-only: ads_get_ad_entities (campaign, daily; 4 picks, weekly). Required follow-ups: trend ("no data"), peers ("no benchmark data"). Feeds the 11/30 weekly call (NOW groundwork #2)._

## Campaign, week over week (account data; ratios *(calc)*)
| Week | Spend | Leads | CPM | Link CTR | LPV ÷ click | Lead ÷ LPV | CPL |
|---|---|---|---|---|---|---|---|
| 11/09–11/15 | 5,181,245 | 196 | 24,431 | 1.82% | 90.5% | 5.60% | 26,435 |
| 11/16–11/22 | 7,137,627 | 189 | 25,425 | 1.67% | 84.1% | 4.78% | 37,765 |
| Change → CPL factor | | | ×1.041 | ×1.089 | ×1.076 | ×1.171 | **×1.429** |
| Share of the rise (log) | | | **11%** | 24% | 21% | **44%** | 100% |

CPL = CPM/1000 ÷ CTR ÷ (LPV/click) ÷ (Lead/LPV); the four factors multiply back to ×1.428 ✓ *(calc)*.

**Answer: not auction.** CPM moved +4%. About **65% of the rise is after the click** (fewer clicks become page views, fewer page views become leads); 24% is weaker CTR.

## Per pick (weekly; CVR = leads ÷ link clicks)
| Pick | CPM | Link CTR | CVR | CPL |
|---|---|---|---|---|
| 042 | 25,241 → 25,066 (−0.7%) | 1.91 → 1.60% (−16%) | 5.54 → 3.93% (**−29%**) | 23,871 → 39,835 |
| 047 | 28,219 → 27,997 (−0.8%) | 1.83 → 1.95% (+7%) | 6.19 → 3.58% (**−42%**) | 24,943 → 40,081 |
| 030 | 13,993 → 13,795 (−1.4%) | 1.58 → 1.42% (−10%) | 2.62 → 2.65% (+1%) | 33,654 → 36,579 |
| 026 | 30,454 → 27,917 (−8.3%) | 1.89 → 1.69% (−10%) | 8.46 → 5.54% (**−35%**) | 19,078 → 29,744 |
CVR fell 29–42% on 3 of 4 picks at the same time, with flat CPM. When three ad sets with different creatives drop together, the cause is probably shared: the landing page, the form, tracking, or demand (INFERRED).

## Daily: the click→LPV leak is a trend, not one bad day
LPV ÷ click: 11/09–11/15 = 87–97% · 11/16–11/18 = 85–89% · **11/19–11/22 = 78–83%**. Lead ÷ LPV held around 5%, except 3.6–4.2% on 11/14, 11/16 and 11/18.
A falling LPV ÷ click means more people click but leave before the page loads (slow page, redirect, or a broken link on some placements) (INFERRED). It is the one metric here that keeps getting worse.

## What it means for 11/30
- **No bid/cap change would fix this.** CPM is flat, so cutting caps only cuts volume. That leaves the 11/23 "cut list if > 35k" idea weak: cutting 047 throws away a pick whose CTR went *up*.
- **Better next step (read-only, no ask):** find the Incess landing page URL from one live creative (`ads_get_creatives` on 042's ad), then curl it for load time, redirects and the form. If the page is slow or broken, the fix is a site fix, not an ad change.
- **11/30 rule:** if LPV ÷ click is < 85% for the 7 days again → write a site check for Alvian (one-line [FYI], no ad change). If it's back to ≥ 88% and CPL ≤ 35k → close the watch.

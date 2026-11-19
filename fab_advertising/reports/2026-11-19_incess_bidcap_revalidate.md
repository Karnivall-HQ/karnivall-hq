# Incess bid-cap proposal: re-check on fresh 7d data (11/12–11/18)
_2026-11-19 09:01 WIB cloud heartbeat · Incess Ads `2017038114993984` · campaign OMO ADVLeads `120233576079370222` · read-only (ads_get_ad_entities ad-set level, activity log category=bid since 11/09, trend, peers)_
_Re-check of the parked proposal `2026-11-10_incess_bidcap_proposal.md` (parked-asks rule: re-check on fresh 7d before any re-ask)._

## Verdict: RETIRE the proposal (its premise is gone)
The proposal assumed the caps were holding spend down (Rp 598k/day, 12.9 picks leads/day). With **no bid edits** (activity log category=bid since 11/09: empty), the campaign now spends **Rp 1,013,750/day** *(calc)* and the 4 picks deliver **18.6 leads/day**, +44% *(calc)* over the proposal's own +15% keep bar. The volume the raise was meant to buy came anyway. The cost: CPL went up at the same caps, so a cap raise now would push CPL higher still (INFERRED).

## Numbers (7d 11/12–11/18, account data)
| Ad set | Cap | Spend | Leads | CPL | CPL ÷ cap *(calc)* |
|---|---|---|---|---|---|
| OMObatch042 | 46,000 | 2,101,684 | 64 | 32,839 | 0.71 |
| OMObatch047 – Copy | 46,000 | 1,077,889 | 36 | 29,941 | 0.65 |
| OMObatch030 Kotak | 46,000 | 759,787 | 16 | 47,487 | 1.03 |
| OMObatch3 026 Manny5Ads | 45,000 | 418,956 | 14 | 29,925 | 0.67 |
| **4 picks** *(calc)* | | **4,358,316** | **130** (18.6/day) | **33,526** | 0.73 |
| Rest of campaign *(calc)* | | 2,737,936 | 85 (12.1/day) | 32,211 | |
| **Campaign** *(calc)* | | **7,096,252** | **215** (30.7/day) | **33,006** | |

- Against the proposal's judge rules (baseline 12.9/day at 28,412): leads/day +44%, CPL +18% *(calc)*. The comparative rule says the **auction moved, not the cap**: the rest of the campaign gained even more (4.1 → 12.1 leads/day, +193% *(calc)*), with no edits.
- Against last week's pre-pull baseline (11/09–11/15, picks 18.6/day at 25,017): same volume, CPL **+34%** *(calc)*. 030 Kotak is now above its cap ratio 1.0 (47.5k).
- 019 15Ads: 33,292 (prior wk 30,346), under the 45k flag. Copy 5: 7 leads at 38,260, under its 50k keep rule.
- Trend tool (STATED): Copy 5 CVR −71.8%, 018 Copy 4 CVR −54.9% (both small). Peer benchmarks: none available.

## What this means
- **No ask.** The parked OUTBOX item moves to Resolved as retired.
- **New watch (M-002):** Incess CPL is drifting up at constant caps (picks 25.0k → 33.5k week over week *(calc)*), while volume rises. That is the auction letting more bids win at higher prices, not fatigue (to confirm at the 11/23 fatigue table). The 11/23 weekly decides: if the 11/16–11/22 campaign CPL > 35k (the old keep line), look at 030 Kotak first (only pick above cap ratio 1.0).
- Re-open a cap raise only if campaign spend falls back under ~Rp 650k/day at a CPL ≤ 30k.

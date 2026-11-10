# Incess OMO ADVLeads: apply-ready bid-cap raise (proposal only)
_2026-11-10 20:03 WIB cloud heartbeat · account Incess Ads `2017038114993984` · campaign OMO ADVLeads `120233576079370222` · read-only pulls (ads_get_ad_entities, activity log, trend, peers)_
_Fuku does not apply this. Alvian (or the team) applies it in Ads Manager._

## Verdict
The cap is the throttle, and it is binding: Rp 5.95M/day budget, ~Rp 598k/day spend. **Raise the cap only on the 4 ad sets whose CPL sits well below it** (+~10%), leave the rest alone, and judge after 7 days with the rules below.
**Gate:** do this only if Incess wants more leads at ~Rp 30–39k each. The lead value is still unknown (OUTBOX FYI), so the yes/no is a business call, not a data call.

## Evidence (account data)
**Campaign, weekly, no bid changes since 09/01** (activity log, category=bid: empty):

| Week | Spend | Leads | CPL | Spend/day *(calc)* | CPL ÷ Rp 46k cap *(calc)* |
|---|---|---|---|---|---|
| 09/14–09/20 | 4,895,032 | 133 | 36,805 | 699,290 | 0.80 |
| 09/21–09/27 | 5,190,716 | 147 | 35,311 | 741,531 | 0.77 |
| 09/28–10/04 | 5,290,928 | 160 | 33,068 | 755,847 | 0.72 |
| 10/05–10/11 | 5,533,455 | 147 | 37,643 | 790,494 | 0.82 |
| 10/12–10/18 | **6,012,594** | **205** | **29,330** | **858,942** | 0.64 |
| 10/19–10/25 | 4,602,270 | 127 | 36,238 | 657,467 | 0.79 |
| 10/26–11/01 | 4,419,896 | 121 | 36,528 | 631,414 | 0.79 |
| 11/02–11/08 | 4,187,146 | 119 | 35,186 | 598,164 | 0.77 |

- Spend fell **−30%** *(calc)* from the 10/12 peak to last week at the **same caps**, while CPL stayed flat at ~Rp 35k. The auction lets fewer bids win; the cap decides how many. [INFERRED from account data]
- The account already held Rp 859k/day at **Rp 29k CPL** for a full week on these creatives, so the extra volume exists at this price. Unlike Fab (where Rp 919k/day doubled CPL), Incess has no sign that more spend costs more per lead. [account data]
- Max frequency 1.70 across ad sets (7d); no fatigue (11/06 pre-check + 11/09 weekly).
- Peer benchmarks: none available ("empty peer_set"). Trend tool: the 4 picks below are stable or improving; 019 C5 and the 026A–F ads are declining.

**Ad sets, last 7d (to 11/09):**

| Ad set | ID | Cap (Rp) | Spend | Leads | CPL | CPL ÷ cap *(calc)* | Action |
|---|---|---|---|---|---|---|---|
| OMObatch042 UGC 1Ad IND-Bali NoExcl | 120239651281900222 | 46,000 | 1,190,211 | 32 | 37,194 | 0.81 | **raise** |
| OMObatch047 UGC 1Ad IND-Bali NoExcl – Copy | 120239723303450222 | 46,000 | 740,685 | 35 | 21,162 | 0.46 | **raise** |
| OMObatch030 Kotak 1Ad IND-Bali NoExcl | 120239636846070222 | 46,000 | 335,805 | 12 | 27,984 | 0.61 | **raise** |
| OMObatch3 026 Manny5Ads ALLindo NoExc MaP | 120244551313580222 | 45,000 | 290,349 | 11 | 26,395 | 0.59 | **raise** |
| OMObatch019 15Ads IND-Bali | 120235099939560222 | 46,000 | 900,843 | 17 | 52,991 | 1.15 | keep (already the costliest) |
| OMObatch3 007 UGC 1Ad IND-Bali NoExcl | 120240045699690222 | 46,000 | 312,410 | 8 | 39,051 | 0.85 | keep (recovering, re-check) |
| OMObatch3 019 UGC … – Copy 5 | 120240954144760222 | 46,000 | 188,023 | 1 | 188,023 | 4.09 | keep (watch; CVR −91% per trend) |
| 3 small ad sets (027, 018 C4, 020) | — | 36–46k | 85,501 | 3 | — | — | keep |

The 4 picks = Rp 2,557,050 / 90 leads = **Rp 28,412 CPL**, 63% of campaign spend *(calc)*.

## Proposed changes (for Alvian to apply)
1. **OMObatch042** `120239651281900222`: bid cap Rp 46,000 → **Rp 51,000**
2. **OMObatch047 – Copy** `120239723303450222`: Rp 46,000 → **Rp 51,000**
3. **OMObatch030 Kotak** `120239636846070222`: Rp 46,000 → **Rp 51,000**
4. **OMObatch3 026 Manny5Ads** `120244551313580222`: Rp 45,000 → **Rp 50,000**

Nothing else changes: budget stays Rp 5.95M/day (it isn't binding), no pauses, no new ads. Ads Manager → ad set → Budget & schedule → Bid control. After publishing, check each ad set still shows Active.

## Expected effect [INFERRED]
- More auctions won on the 4 cheapest ad sets → more leads/day. Size unknown; history shows the campaign swings ±30% on its own, so judge against a fixed baseline.
- CPL on the 4 rises somewhat. If the CPL÷cap ratio holds (0.46–0.81), their CPL lands ~Rp 31k *(calc: 28,412 × 51/46)* worst case, still below the campaign's Rp 35k.

## Judge after 7 days (pre-set rules)
Baseline = the 4 ad sets, 11/03–11/09: **90 leads / 7 = 12.9 leads/day, CPL Rp 28,412** *(calc)*.
- **Keep** if leads/day ≥ 14.8 (+15%) **and** CPL ≤ Rp 35,000.
- **Revert to the old caps** if CPL > Rp 40,000, or leads/day < 12.9 with higher CPL.
- **Comparative rule:** compare the 4 raised ad sets vs the untouched rest of the campaign over the same 7 days; if the rest gained as much volume, the auction moved, not the cap. Then keep the caps only if CPL stayed ≤ Rp 35k.
- Next step if kept: one more +10% on the same 4 (Rp 56k), same rules.

## Not proposed
- Budget changes (budget isn't the limit).
- Publishing the Incess drafts ("FIX OMO CostCap Increm", Rp 5M/day draft): unclear whose they are; Fuku publishes nothing.
- Pausing 019: under a bid cap the budget doesn't move to the winners, so a pause only loses 17 leads/week. Re-check at the 11/16 weekly.

# Hypothesis check: "cheap ads = remarketing, expensive ads = prospecting that fills the funnel" (2026-11-05)

Alvian's hypothesis: the expensive ads bring in cold traffic and the cheap ads convert it. Last-click attribution makes the prospecting ads look expensive.

## 1. Targeting (read from ad set settings)
All 10 ad sets I checked, cheap and expensive, have the **same targeting**:
- Jakarta city, age 18/21–65, Advantage+ audience ON
- **No custom audiences and no exclusions** ("NoExcl")
- Optimizing for website leads (OFFSITE_CONVERSIONS)

→ By setup, **there is no remarketing ad set**. Cheap and expensive ads compete for the same broad Jakarta audience. What differs is the creative, plus bid caps on the BC ad sets.

Attribution on every ad set is 7-day click + 1-day view + 1-day engaged view. Meta gives each lead to one ad, the last one the person touched. So "the last ad steals credit" is real. And because Advantage+ is free to find warm people (site visitors, engagers) in any ad set, some remarketing happens implicitly.

Bid caps confirmed: BC ad sets have `bid_amount` Rp 80,000 (Bid80) or Rp 94,250 (Bid94). That explains why BC spends ~1.4% of its Rp 5M budget.

## 2. Natural experiment: weekly spend vs leads (campaign level)
| Week | BC spend / leads (CPL) | Prospecting spend / leads (CPL) | Account CPL *(Fuku calc)* |
|---|---|---|---|
| Oct 6–12 | 1.19M / 12 (98.8k) | RUDI 1.03M / 7 (147k) | 116.6k |
| **Oct 13–19 (RUDI blitz)** | 0.27M / 5 (54k) | **RUDI 5.17M / 24 (215k)** | 187.7k |
| Oct 20–26 (week after) | 1.11M / **15 (73.8k)** | RUDI 0.11M / 1 | **76.2k** |
| Oct 27–Nov 2 | 0.62M / 7 (89k) | PEIKIRA 2.14M / 16 (134k) | 120.4k |

- ✅ Supports the idea: the week after the Rp 5.2M blitz, BC had its best week. It got 13.5 leads per Rp 1M, vs ~10–11 in other weeks *(Fuku calc)*.
- ❌ Limits it: that halo is worth roughly 3 extra leads. Even crediting them all to RUDI, its effective CPL is ~Rp 190k *(Fuku calc)*, about 2× the target.
- ⚠️ During the blitz, BC's spend fell from 1.19M to 0.27M. The campaigns compete in the same auction and audience, so they cannibalize each other.

## Verdict
The theory is right in principle, but **this account isn't built as a funnel**, so it can't work that way here.
- The expensive ads aren't designed to fill the funnel. They're cold ads that also optimize for leads, just with weaker creative.
- The real lever is still creative (raw phone photos vs renders) and bid caps.
- M-001 already measures **blended account CPL** (total spend ÷ total leads), so attribution doesn't affect how we score it: if prospecting ads truly feed the cheap ones, the account total shows it.

## If we want a real funnel (proposal, Alvian applies)
1. **Warm ad set (remarketing):** custom audiences = website visitors 30d + IG/FB engagers 60d + video viewers 50% 30d, excluding people who already became leads. Use the cheap phone-photo + price creatives. Budget ~20–30%.
2. **Cold ad set (prospecting):** broad Jakarta, **excluding the warm audiences**. Use Reels or walk-through video plus the pain hooks (C1, C4, C6 in the creative brief).
3. Judge by **blended account CPL** weekly, and if a decision depends on it, run a Meta Conversion Lift test (read-only check: `ads_experiment_check_eligibility`).
4. Still missing: lead value (close rate × months stayed × Rp 750k). At ~20% close and a 6-month stay, a lead is worth ~Rp 900k, which would make even a Rp 200k CPL profitable. *(Assumption, not data.)*

# Fab pixel Leads: how much is ads vs organic?
_2026-11-11 16:02 WIB, Fuku cloud heartbeat (groundwork backlog #1). Read-only._

**Question:** the W1/W2 template said pixel Leads (~8/day) are ~3× Meta-attributed leads (~3/day), so "most site leads are organic". If that's true, a site fix mostly lifts organic and barely moves ad CPL. Is it true?

## Data (dataset `405755485775053`, PT buckets 11/03 09:00 → 11/10 09:00 PT = 11/04 00:00 → 11/11 00:00 WIB)
| Event | BROWSER | SERVER | Sum (= what `aggregation=event` returns) |
|---|---|---|---|
| Lead | 29 | 30 | 59 |
| Form | 43 | 51 | 94 |
| ViewContent | 601 | 762 | 1,363 |

- Lead: browser and server counts are **identical on 7 of 8 days** (the 8th is 4 vs 5). Every Lead is sent twice: pixel + CAPI (account data).
- `aggregation=event` total (59) = browser + server, so this stats call counts **received events before dedup**. INFERRED: Meta dedups them for attribution (event_id), because Meta's attributed lead counts are odd numbers (PEIKIRA 17, BC 5), not doubled.
- URL split is useless: every Lead fires on `https://fabwarehouses.com/` (the URL is reported at root level).
- Lead EMQ 7.8, phone/fn/external_id 100%, fbc 75%. Healthy.

## Answer
- Unique site Leads ≈ **30 in 7 days ≈ 4.3/day** *(calc: max of browser/server per day)*, not ~8.
- Meta-attributed Fab leads, same 7 WIB days: **22** (07:02 readout).
- → **≈ 73% of site Leads are ad-attributed, ≈ 27% organic/other** *(calc)*. The old "~3×" was double counting.

## What this changes
1. **W1/W2 matters more for ads than I said.** About ¾ of any site lift lands on ad leads, not ¼. The gate brief's case C (site lift → 94.6k / 85.0k) used Meta CPL directly, so its numbers stand; the "the gain may go to organic" caveat in the lift template is now small.
2. **Lift template baseline is still valid** like-for-like (same call, both events double-counted), but the ~1,300 VC/week and ~49 leads/week are *received* counts. Real Poisson noise is on ~25 unique leads/week, so the 7-day read is **noisier than the template says**: treat the day-7 read as directional and rely on day 14 + Meta CPL. Template note added.
3. **W4 ("40% of form submits never become a Lead") stands within one source:** server Form 51 → Lead 30 (59%), browser 43 → 29 (67%) *(calc)*. Still ~1 in 3 forms with no Lead.
4. No ad-account ask. Nothing for Alvian to decide.

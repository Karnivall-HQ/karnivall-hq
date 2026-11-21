# Playbook: Weekly ads health report (M-002)
_Created 2026-11-05 22:01 WIB. **v2 2026-11-21 11:01 WIB** from runs #1 (11/09), #2 (11/16) and the 11/23 skeleton (dry runs 11/14, 11/17; pre-pulls 11/18–11/21)._

**When:** first heartbeat on Monday at/after 07:00 WIB; deliver by 09:00 WIB. Window = last complete Mon→Sun (at Mon 07:00 the last complete day is Sunday).
**Output:** `fab_advertising/reports/weekly/YYYY-MM-DD.md` (named by the Monday it is delivered) + one [REPORT] in OUTBOX that **replaces** last week's weekly report.
**Rules:** read-only, propose-only (CLAUDE.md Evolving rules). Numbers copied from tool output; computed = *(calc)*. Metric = the 7d window, never one day. Read `meta-ads-algorithm.md`, `meta-cpl-diagnosis.md`, `meta-modelling-and-planning.md` first.

## A. The week before (quiet runs, Mon–Sun)
1. **Skeleton on the first quiet run after a report** (≈ Mon 10:00): copy the template below, fill every prior-week column from the report just delivered, put `⟨…⟩` in every cell Monday must fill, and a header line saying "Monday fills ⟨…⟩, deletes the run sheet + pre-pull sections".
2. **Run sheet:** numbered table `# | call | args | fills`. Every `⟨…⟩` cell maps to one row. Pin IDs, actor_ids, pixel epochs (`date -d '2026-11-16 00:00 +0700' +%s`) and exact script commands with **explicit bases** (script defaults go stale).
3. **Dry run once mid-week:** walk every cell → row; fix gaps (cells with no source, windows that end on the wrong day, rules missing a branch). 11/14 and 11/17 dry runs each found 3–4 gaps.
4. **Pre-pull partial weeks** on quiet runs (campaign / ad-set, `time_increment=1`) and lock finished days. Monday **re-pulls the whole week anyway** (cheaper than stitching) and uses the pre-pull only as a cross-check. No verdict from < 7 days, but a pre-set trigger crossed mid-week (e.g. "> 30k → pick-level split") means the split is pre-pulled before Monday.
5. **Pre-set every rule before the data** (keep / pause / flag lines with their thresholds) and resolve rule overlaps in advance (keep wins on a tie). Flag lines only from weeks with **≥ 10 leads** (tests A10).
6. **Wire mid-week state:** when an account changes structurally mid-week (budget, cap, bid strategy, min spend, pause), add a `STATE <date> <time>` line in the tracker and a split rule (capped days / change day / after days) to the skeleton the same run.

## B. Monday run (~14–15 read-only calls, ~15 min)
1. **Activity log FIRST** (each spending account, since Mon 00:00 WIB of the window, limit ≤ 40, group by `actor_id`: Markus/Rudi MCP 61594758338050, TourHub 61557670947597). A budget/cap/min-spend/pause edit changes how every row below is read; log beats the STATE line if they disagree.
2. `ads_get_ad_accounts` → disabled/limited vs the known list (11/16: Alv Ads, WooCore Ads, For App in Audience Network Ads, Babyso Rp).
3. Campaign level per spending account: `time_range` Mon→Sun; amount_spent, lead, cost_per_lead, impressions, cpm, landing_page_view, frequency, ctr; filter amount_spent > 0. WoW vs the skeleton's prior columns *(calc)*.
4. Ad-set level for the **mix-shift guard** (share of spend per ad set; a 7d CPL change is often mix, not performance: 11/20 92.1k came from BC 56.6k carrying a capped PEIKIRA). Add bid_amount, daily_min_spend_target, learning status for any ad set with an open ask.
5. Ad level, fatigue: spend > Rp 50k. Flag = frequency > 4 or CTR down > 30% WoW. CTR up while leads fall = post-click / page, not fatigue (Ad015 11/14). New ads with no prior week = "n/a".
6. Pre-set rule rows (Ad015 trigger needs ≥ Rp 600k spent in the window, else "CPL rule n/a"; Incess keep/flag rows).
7. Pixel `event_total_counts` (Mon 00:00 → next Mon 00:00 WIB): VC, Form, Lead, VC→Lead, Form→Lead *(calc)*. Split the row at the edit date if the site changed mid-week.
8. `curl` the landing page; count the strings the open site asks target (e.g. "Jakarta Pusat", "Rp 800.000", "akan launching").
9. Models: run with the week's bases passed explicitly; copy LWD + CRITERION 2 lines verbatim.
10. Incess may return a required `object_state=draft` follow-up (~140k chars): parse the saved file with python, list names/budgets only; drafts are FYI, never published.
11. Cross-check: Fab yesterday's spend = the 06:19 "Account billed" line in the log; Monday totals vs the pre-pull locks.

## C. Write
- Fill every `⟨…⟩`, delete the run sheet + pre-pull sections, then the Summary (3 lines, result first).
- **Proposal status** table: every open/parked ask with applied? yes/no from the log, not from memory.
- **Top 3 actions** = exact object + ID, current → proposed, expected effect. Prefer asks already open; a new ask only if a pre-set rule fired, and OUTBOX stays ≤ 3 asks.
- Update `m001_tracker.md` weekly row from the Fab numbers.
- OUTBOX [REPORT]: spend, leads, CPL per account + WoW + the single most important action.

## Template
```
# Weekly ads health — week of YYYY-MM-DD (Mon–Sun)
## Summary (3 lines max)
## Accounts
| Account | Spend 7d | Leads | CPL | WoW spend | WoW CPL | Status |
## What changed this week   (log-first; mid-week STATE line; open asks applied?)
## <Account> per campaign / ad set (mix-shift guard)
| Campaign / ad set | Spend | Share | CPM | Cost/LPV | Leads | CPL | prior wk CPL |
## Pre-set rule checks   (one row per rule, threshold written in the row)
## Pixel funnel + site status
## Fatigue flags
| Account | Ad | Freq | CTR (prior, Δ) | Leads | CPL | Flag |
## Changes made this week (activity log, by actor_id)
| When (WIB) | Object | Change | Actor |
## Proposal status
## Criterion lines (model output verbatim)
## Disabled / limited accounts
## Top 3 recommended actions (for Alvian to apply)
```

## Notes
- Run #1 (11/09): ~12 calls; ad-level filter > Rp 50k fits output (~3 Fab + ~7 Incess rows). Prior-week baseline was pre-pulled in `weekly/_baseline_2026-10-26.md`.
- Run #2 (11/16): ~14 calls; every pre-set rule landed keep/no-flag → no new ask (correct: a report is not a reason to ask).
- The skeleton is a working file; once it passes ~200 lines, move per-ask detail to the ask's own card and leave a pointer.

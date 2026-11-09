# Playbook: Weekly ads health report (M-002)
_Created 2026-11-05 22:01 WIB, before the first run (Mon 2026-11-09). Refine after the first real report._

**When:** first heartbeat on Monday at/after 07:00 WIB. Deliver by 09:00 WIB.
**Output:** `fab_advertising/reports/weekly/YYYY-MM-DD.md` (template below) + one-line [REPORT] in OUTBOX.
**Rules:** read-only (propose-only for every change, see CLAUDE.md Evolving rules). Numbers copied from tool output; anything computed is marked *(calc)*.

## Steps (Rudi MCP, all read-only)
1. `ads_get_ad_accounts` → list accounts; note any newly disabled/limited ones (compare to last report).
2. Per account, `ads_get_ad_entities` `level=ad_account`, `date_preset=last_7d`, `include_additional_context=false`, spend only. Keep accounts with spend > 0.
3. For each spending account: `level=campaign`, `time_range` = last Mon→Sun, fields `amount_spent, lead, cost_per_lead, impressions, clicks, ctr, frequency`, filter `amount_spent > 0`. Repeat for the previous week → week-over-week delta *(calc)*.
4. Fatigue flags: `level=ad`, last 7d, filter `amount_spent > 50000`, fields `ctr, frequency, lead, cost_per_lead`. Flag frequency > 4 or CTR down > 30% vs. prior week (or use `ads_insights_performance_trend`).
5. Activity log per spending account, last 7d, `limit ≤ 40` or by `event_category` (budget, status, bid). Attribute by `actor_id`. Note every human edit.
6. Write the report, then the OUTBOX line: spend, leads, CPL per account + the single most important action.

## Template
```
# Weekly ads health — week of YYYY-MM-DD (Mon–Sun)
## Summary (3 lines max)
## Accounts
| Account | Spend 7d | Leads | CPL | WoW spend | WoW CPL | Status |
## Fatigue flags
| Account | Ad | Freq | CTR (WoW) | Leads | CPL | Flag |
## Changes made this week (activity log)
| When | Object | Change | Actor |
## Disabled / limited accounts
## Top 3 recommended actions (for Alvian to apply)
1. … (exact object name + ID, current → proposed value, expected effect)
```
## Notes from run #1 (2026-11-09)
- Whole run = ~12 tool calls, ~15 min. Use `time_range` Mon→Sun for both campaign and ad levels; ad-level filter `amount_spent > 50000` gives ~3 Fab + ~7 Incess rows (fits output).
- Pixel: `event_total_counts`, start = Mon 00:00 WIB, end = next Mon 00:00 WIB (`date -d '… +0700' +%s`).
- Incess returns a required `object_state=draft` follow-up read; the result is ~140k chars, so parse the saved file with python and list names/budgets only. Report drafts as FYI; never publish.
- Fab yesterday's spend = the 06:19 'Account billed' amount in the activity log (cross-check).
- Re-curl the site in the same run so the funnel row says whether W1/W2 explain any change.

Prior week (10/26–11/01) is pre-pulled in `fab_advertising/reports/weekly/_baseline_2026-10-26.md`; use it for the WoW columns on 11/09.
Also update the M-001 tracker weekly readout row from the Fab numbers.

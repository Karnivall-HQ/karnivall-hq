# Lessons

> Format: `- YYYY-MM-DD · [area] What happened → **Rule:** what I'll do differently.`
> Consolidated into playbooks during retros. Keep this file under ~100 lines; prune what's been absorbed.

- 2026-11-05 · [meta-ads] Account-level scan of 20 accounts via Rudi MCP worked well with `level=ad_account`, `include_additional_context=false`, and the default fields (spend only). Industry benchmark often returns no data or "unavailable". **Rule:** scan spend first, then deep-dive only the accounts that are spending. Don't block on benchmarks.
- 2026-11-05 · [orientation] With no missions set, a read-only scan of connected accounts produced concrete, numbers-backed mission proposals. **Rule:** when idle, look at real data from the connectors before writing generic research.
- 2026-11-05 · Cloud routines CAN push straight to `main` of alvianlim/karnivall-hq. Rule: before you edit locally, pull first (the session hook does this), or local and cloud edits to NOW.md will conflict.
- 2026-11-05 · [meta-ads] Before diagnosing CPL/delivery, the budget activity log (`event_category=budget`) showed a teammate's 5M→300k budget cut that explained the delivery drop. **Rule:** pull activity logs first in any diagnosis; never attribute a change to performance until you've ruled out human edits.
- 2026-11-05 · [meta-ads] Bid-cap campaigns can show a huge daily budget while spending ~1%: the cap, not the budget, limits delivery. **Rule:** for under-spend, check `bid_strategy`/`bid_amount` before suggesting budget changes.

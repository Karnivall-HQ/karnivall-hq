# Lessons

> Format: `- YYYY-MM-DD · [area] What happened → **Rule:** what I'll do differently.`
> Consolidated into playbooks during retros. Keep this file under ~100 lines; prune what's been absorbed.

- 2026-11-05 · [meta-ads] Account-level scan of 20 accounts via Rudi MCP worked well with `level=ad_account`, `include_additional_context=false`, and the default fields (spend only). Industry benchmark often returns no data or "unavailable". **Rule:** scan spend first, then deep-dive only the accounts that are spending. Don't block on benchmarks.
- 2026-11-05 · [orientation] With no missions set, a read-only scan of connected accounts produced concrete, numbers-backed mission proposals. **Rule:** when idle, look at real data from the connectors before writing generic research.
- 2026-11-05 · Cloud routines CAN push straight to `main` of alvianlim/karnivall-hq. Rule: before you edit locally, pull first (the session hook does this), or local and cloud edits to NOW.md will conflict.
- 2026-11-05 · [meta-ads] A `publisher_platform` + `platform_position` breakdown at campaign level found the biggest waste (IG Stories, WA Status, Threads) faster than ad-level data. Absurd ad-set frequency (100–1,000) + CPM < Rp 1k = WhatsApp Status junk delivery. Ad-level 30d output overflows the tool limit; parse the saved file with jq. **Rule:** run the placement breakdown first on every CPL diagnosis.

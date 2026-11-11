# Playbook: diagnosing high CPL in a Meta lead-gen account

**When to use:** any "why is CPL high / why is delivery low / is this ad broken" question on a Meta account (Fab first, then any client).
**Last validated:** 2026-11-05/06, M-001 (Fab, `484578521394893`). Consolidated in the first retro (2026-11-06) from 13 lessons.
**Always:** read `meta-ads-algorithm.md` first, label claims STATED / INFERRED / account data, and propose only (Alvian applies).

## Steps (in this order)
1. **Rule out human edits first.** Use the activity log with `limit ≤ 40` or filter by `event_category` (budget, status, bid). Attribute by `actor_id`, never by app name: "Rudi MCP" is an *app* that other people's AI sessions use too. Summarize with python. Delivery events put the **ad set** ID in `extra_data.campaign_id`, so check unknown IDs at ad-set level before calling something a new campaign.
2. **Check bid strategy before budget.** Under-spend with a large budget almost always means `bid_strategy`/`bid_amount` caps are binding (Fab BC: Rp 80k/94.25k caps; Incess: Rp 5.95M budget but ~Rp 585k/day spend). The lever is the cap, not the budget.
3. **Placement breakdown** (`publisher_platform` + `platform_position`, campaign level). This is the fastest way to find waste. Ad-set frequency of 100–1,000 with CPM < Rp 1k means WhatsApp Status junk delivery.
4. **Recency check on "winners" and "broken" ads.** Re-check every 30d winner against 7d delivery. Before flagging an ad issue as urgent, check that ad's 14d spend (Fab 201B: "Update Required", but Rp 0 spend for 14d, so the issue cost nothing).
5. **Targeting read** before any attribution or remarketing theory: are there custom audiences or exclusions? To test halo effects, use weekly (`time_increment=7`) blended CPL.
6. **Post-click funnel from the pixel:** `ads_get_dataset_stats` → ViewContent → Form → Lead. `event_total_counts` returns browser and server rows separately (sum them; roughly ÷2 for uniques). **`aggregation=event` also returns received browser+server, pre-dedup** (Fab: Lead 29 browser + 30 server = 59 "Leads" ≈ 30 unique, 11/11). Before comparing pixel counts with Meta-attributed leads, split by `event_source` and take the max per day. Form→Lead gaps can be by design: Fab's Lead fires only on one routed thank-you page with a 24 h window (11/11). Check routing before calling it a leak. `start_time` is Unix seconds and must be ≤ 28 days old (compute it with `date -d … +%s`). `url` aggregation strips paths.
7. **Landing page grep:** curl every page in the flow (try `/thank-you/`, `/terima-kasih/` and follow 301s too; thank-you pages are noindex and not in the sitemap) and grep `pysOptions` for `"name":"Lead"` to find where the conversion actually fires, plus location and price strings. Compare them with the live ad copy (Fab: cloned WP pages carried "Kelapa Gading" onto Jakarta Selatan pages; Rp800k vs 750 in ads).
8. **Creative review:** ad → `creative_id` → `ads_get_creatives` / `ads_get_ad_images` (hashes) full-size `url` → curl to scratchpad → PIL contact sheet → Read. `thumbnail_url` is 64×64 and useless. Fab rule: real phone photos beat AI/polished renders by 3–10× on CPL.

## Tool tips
- Account scan: `level=ad_account`, `include_additional_context=false`, spend only, then deep-dive only the accounts that are spending. Benchmarks often return nothing, so don't block on them.
- Ad-level 30d output and activity logs with limit 100 overflow the tool output. Parse the saved file with jq/python.
- Ad copy: write only from facts already in live ads (`ads_get_creatives` body/title), and flag any new claim for confirmation.
- Activity log "Active → Inactive after Ad Review" can be a human pause via the MCP app: read the entity `status` (PAUSED = human) and the parent's status before calling it a Meta action. (Retro #2)
- Test design, read rules and re-asks: see `meta-tests-and-proposals.md`.

## Output
An apply-ready change list (exact object name + ID, current → proposed value, expected effect, revert rule) in OUTBOX, and a tracker row in `fab_advertising/reports/m001_tracker.md`.

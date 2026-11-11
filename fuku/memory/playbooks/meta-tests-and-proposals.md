# Playbook: designing, reading and proposing Meta ad tests
_Created in Retro #2 (2026-11-11) from 16 lessons (11/06–11/11, M-001 + M-002). Pairs with `meta-ads-algorithm.md` (how delivery works) and `meta-cpl-diagnosis.md` (where CPL leaks)._

## When to use
Any new ad, ad set, creative wave, bid-cap or structure change that Fuku proposes, and every re-ask of a parked proposal.

## A. Before the test: write the read rules first
1. **Project spend per unit for the read window** before choosing a lead threshold. At Fab (≈ Rp 150k/day in the control ad set), 3 new ads get ≈ Rp 105k each in 7 days *(calc)*: "≥ 2 leads by day 7" can't be read. Use staged reads (delivery → early kill → verdict) and judge the pooled format before the per-ad angle. Template: `fab_advertising/reports/wave1_read_template.md`.
2. **Kill rules are spend multiples of target CPL, not bare lead counts.** E.g. pause at ≥ 2× target with 0 leads (P = 13.5% if it were on target, calc) or ≥ 3× with ≤ 1. One lead is noise and disarms a lead-count rule.
3. **Add one comparative rule** (test vs control, same window) next to the absolute ones. It survives a single good day.
4. **Shared budget (CBO):** a new ad set can take 78% of spend on day 2 (PEIKIRA2, 11/06). Check spend *share* daily; a share threshold can trip before the read date. New *ads* in an ad set with one dominant ad can starve instead (Ad007: Rp 1,487 in 7d). Check both directions.
5. **Evaluate lead thresholds on full-day data** (first readout after 07:00 WIB), never intraday.
6. **Check the detectable effect before promising a funnel read.** Compute z for the hoped-for lift at the real weekly volume. Fab pixel (~1,300 VC/wk, base 3.72%): +1pt is readable in 7 d, +0.5pt needs ~14 d (11/11). Pin one stats call (aggregation) for before and after: different aggregations give different counts.
7. Write all of it into the pre-stage doc **before** the read date, then apply it as written.

## B. Reading the account before claiming a trend
- **Split by campaign first** when 2+ campaigns spend: account totals hide mix shifts (11/06: "CPM +16%" was spend moving from cheap BC to PEIKIRA).
- **Compare a stage week-over-week**, not its absolute level, before blaming it (post-click improved 3.0 → 3.8% while CPL rose).
- **≥ 8 weekly rows** before calling a one-week CPL jump a decline. A sawtooth with flat CTR/CPM/freq is judged on 2-week blocks; the trend tool's single-period "BAD" is noise.
- **Capacity:** the highest spend an engine ever held at target CPL in its 8-week history is its ceiling on current creative; the gap above it is a creative problem, not a budget one (Fab: Rp 919k/day week cost 201k/lead).
- **One ad > 80% of an ad set's spend = no backup.** The hedge is new creative; write CTR/CPL/freq triggers before fatigue shows.

## C. Writing a proposal
- **Sort levers:** "adds volume at ~target CPL" (cap raises, budget) vs "lowers CPL on current spend" (site conversion, cheaper creative). For a CPL gate push the second kind; for a scale gate the first.
- **Bid caps:** pull ≥ 8 weekly rows + the bid-category activity log; spend can swing −30% at a fixed cap from the auction alone. Raise only ad sets with CPL ÷ cap < ~0.85, with a raised-vs-untouched comparative rule.
- **Copy consistency:** join `ads_get_ad_entities` (spend > 0, creative_id) with `ads_get_creatives` and size by spend share; an Ad Library sample undercounts (8 vs all 59).
- **Competitors:** Ad Library tells *who* advertises and how often; their website tells the offer. Comparison copy claims only checked differences.
- **Creative briefs:** view the top winner at full size first and copy its *subject*; size the ask to what it needed (Image087 = home clutter, no warehouse).

## D. Re-asking and following up
- **Before re-raising a parked ask, re-pull the same breakdown on the latest 7d** and recompute "CPL without it". If the gain is gone, retire the ask (IG Stories, 11/11).
- **When the team applies a partial version**, measure where the money went at the next readout and shrink or drop the ask instead of repeating it (ad 006 pause, 11/09–11/10).
- Stalled > 24h → one-line yes/no re-ask (CLAUDE.md Evolving rule); one push notification per re-ask per day.

## Quality bar
Every proposal names: the lever type, the read rules (absolute + comparative), the window, and labels each number account data / *(calc)* / INFERRED.

## Last validated
2026-11-11 · M-001 (Wave 1 template, 11/20 gate brief, IG Stories retirement) and M-002 (Incess 019 split).

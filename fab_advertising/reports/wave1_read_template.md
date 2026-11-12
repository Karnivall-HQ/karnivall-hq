# Wave 1 read template: S1 / B1 / B2 (phone-photo ads in the PEIKIRA control ad set)
_Fuku, 2026-11-11 10:02 WIB · cloud heartbeat groundwork · read-only template. Fuku doesn't create, pause or edit anything; every action below is a proposal for Alvian/Markus._
_Sources: `fab_advertising/creatives/2026-11-10_shoot_day_card.md` (wave plan), `2026-11-10_ad015_fallback.md` (control ad set), `2026-11-20_gate_brief.md`, lessons 2026-11-06 (shared-budget starvation) and 2026-11-10 (no backup when one ad > 80%)._

## Why a template, and the one problem it solves
The shoot card says "read after 5–7 days: keep ≤ Rp 95k with ≥ 2 leads". **At Fab's budget that rule usually can't be applied by day 7.**
- Control ad set spends ≈ **Rp 150k/day** *(calc: Ad015 7d Rp 989,546 ÷ 94% ÷ 7)*.
- If the 3 new ads win 30% of it together: ≈ Rp 15k/ad/day → **≈ Rp 105k per ad in 7 days** *(calc)* → ~1 lead each at a 95k CPL. Most ads will sit at 0–1 leads on day 7.
- So the read runs in **three stages**, uses spend-based kill rules (not "wait for 2 leads"), and judges the **format** (pooled) before the **angle** (per ad).

## Inputs to fill on launch day
| Field | Value |
|---|---|
| Launch date/time (WIB) | ____ |
| Ad IDs: S1 / B1 / B2 | ____ / ____ / ____ |
| Price on stickers (750 or 800) | ____ |
| W1/W2 site fix live? (date) | ____ (if it changes mid-read, split the read at that date) |
| Other changes in the same window (activity log) | ____ |

Account `484578521394893` · campaign `120254051672440572` · control ad set `120254051672430572` · PEIKIRA2 `120254276298070572` · pixel `405755485775053`.

## Queries (read-only, same every stage)
1. `ads_get_ad_entities` level **ad**, parent = control ad set, window = launch day → yesterday. Fields: spend, impressions, CTR (link), frequency, CPM, cost per landing-page view, leads (`actions` lead), CPL.
2. Same call level **ad set** for both PEIKIRA ad sets (spend share between control and PEIKIRA2; the Wave 1 ads must not just shift money between ad sets).
3. `ads_account_get_activity_logs` from launch (attribute any other change in the window).
4. Stage 3 only: `ads_get_dataset_stats` event_total_counts for the same window (VC→Lead vs the 11/06 baseline 3.8%), so a site change isn't credited to the creatives.
Copy numbers from tool output; mark derived ones *(calc)*; stage verdicts use the cumulative window since launch, not one day.

## Stage 0 — build check (day 1–2, before any kill rule) _(added 11/12 22:02)_
Catches a build slip before stages 1–2 judge an ad that wasn't built to spec. Read-only.
1. `ads_get_ad_entities` level ad, parent = control ad set → note each new ad's creative ID.
2. `ads_get_creatives` with `creative_ids` = the 3 new creatives + Ad015's `1718772653590165` (same call, as the reference). Fields (names from the tool's schema): `instagram_user_id`, `call_to_action_type`, `object_type`, `link_url`, `body`, `advantage_plus_creative_enhancements`.

| Check | Expected (from `2026-11-12_wave1_markus_onepager.md`) | If wrong |
|---|---|---|
| `instagram_user_id` | `17841466480733343` (same as Ad015) | one line to Alvian/Markus: fix before day 3 |
| `call_to_action_type` | `SEE_DETAILS` | same |
| `link_url` | `/sewa-gudang-self-storage-jakarta/` (the page 88% of spend lands on) | same; a homepage link sells the Rp 5jt product |
| `body` | verbatim the paste row in the Wave 1 build sheet (price = the 750/800 answer) | same |
| `advantage_plus_creative_enhancements` | must **not** list `image_text_translation` or `cv_transformation` (`image_animation` may stay, as on Ad015) | same; INFERRED risk, so flag but don't stop the read |

A slipped ad's stage-1/2 numbers are read but labelled "built off-spec"; if it's fixed by editing, its read restarts from the fix date (activity log gives the time).

## Stage 1 — delivery check (day 2–3)
Question: is Meta giving the new ads any spend at all? (Ad007 got Rp 1,487 in 7d while Ad015 ate the ad set.)
| Signal | Rule |
|---|---|
| New ads' combined share of control ad set spend | **≥ 10%** → OK, go to stage 2 · **< 10%** → "starved" |
| Any new ad disapproved / "Update Required" | flag at once to Alvian (one line) |
| Control ad set total spend vs pre-launch ≈ Rp 150k/day | drop > 30% → money moved to PEIKIRA2; note it, no action yet |

**If starved (proposal, INFERRED):** step 1, apply parked item 5 (pause the 5 dead PEIKIRA ads) so the new ads only compete with Ad015. Step 2, if still < 10% two days later: move S1/B1/B2 into their own ad set in the same campaign with an ad-set **max spend Rp 90k/day** (so it can't take 78% of the budget like PEIKIRA2 did on 11/06). Don't pause Ad015 to force delivery.

## Stage 2 — early kill (day 3–5, per ad)
Leading indicators vs Ad015's own 7d numbers (CTR 1.73%, CPL Rp 98,955, freq 1.36 on 11/04–11/10):
- **Pause early** if spend ≥ Rp 95k AND 0 leads AND link CTR < 1.0%. (Weak click-through is the clearest early sign: dead ads in this ad set ran 0.44–0.81% CTR.)
- **Pause** if spend ≥ Rp 190k AND 0 leads *(calc: if its true CPL were 95k, P(0 leads) = 13.5%)*.
- Everything else: keep running.

## Stage 3 — verdict (day 7, extend to day 14 if unread)

> **2-week rule (added 11/12 19:02, from `2026-11-12_scale_plan_v2.md`: weekly ad-set swings run ±2×).** Kill rules (❌ / PAUSE) may fire on day 7: they are spend-multiple rules and don't depend on one good week. **A ✅ / KEEP on day 7 is provisional:** it unlocks *building* Wave 2, but the ad counts as a "winner" for budget steps or the scale plan only after the **day-14 read** (≥ 14 days or ≥ Rp 1.4M pooled spend) still meets the same row. If the day-14 read falls to ⚠️ or ❌, Wave 2 stays built but unlaunched.
### 3a. Format (pooled S1+B1+B2) — decide this first
| Pooled result | Verdict | Next |
|---|---|---|
| ≥ 3 leads AND pooled CPL ≤ Rp 95k | ✅ phone-photo format works | Wave 2 goes ahead whatever the angle read says |
| ≥ 3 leads AND CPL 95–130k | ⚠️ unproven | extend to day 14 |
| Spend ≥ Rp 285k AND CPL > Rp 142.5k (or ≤ 1 lead) | ❌ format doesn't beat Ad015 here | stop waves; next lever is the site (W1/W2), not more creative *(P(≤1 lead) at a true 95k = 19.9%, calc)* |

### 3b. Angle (per ad)
| Ad result | Verdict |
|---|---|
| ≥ 2 leads AND CPL ≤ Rp 95k | KEEP · its angle is the winner |
| Spend ≥ Rp 190k AND 0 leads, or spend ≥ Rp 285k AND CPL > Rp 142.5k | PAUSE |
| Anything else | EXTEND to day 14, then apply the same rules; still unread at day 14 → KEEP if CPL ≤ 110k, else PAUSE |
Two winners → the cheaper CPL wins the Wave 2 mapping; tie → the higher CTR.

### 3c. Did the ad set get better, or did the new ads just take Ad015's leads?
Compare **control ad set** CPL for the Wave 1 window vs its 7d before launch. New ads "winning" while the ad set CPL rises = cannibalization; say so in the readout and don't add Wave 2 on top.

## Wave 2 mapping (from the shoot card)
| Winning angle | Wave 2 ads | Needs photos | Needs Alvian's confirmation |
|---|---|---|---|
| Pickup (B1) | B5, B3 | P3, P4 | pickup ✔ (+ "same-day" real?), no deposit ✔, no minimum ✔ |
| Situation (S1) | S6, S2 | P2 (have), P6 | kulkas/kasur fit a unit? |
| No deposit + pickup (B2) | B3, B4 | P4, P5 | no deposit ✔, no minimum ✔ |
Wave 2 also goes in as max 3 ads, read with this same template.

## 11/20 gate link
Wave 1 alone opens the CPL gate only if the new ads run at **≤ Rp 70k** (gate brief scenario D). A pooled CPL of 70–95k is still a ✅ format, but it's a volume win, not a gate win; say both in the readout.

## Readout line (paste into OUTBOX report)
`Wave 1 day N: S1 Rp __ / __ leads · B1 Rp __ / __ · B2 Rp __ / __ · pooled CPL Rp __ (calc) vs Ad015 Rp __ · share of ad set __% · verdict: __ · proposal: __`

## Labels
- Account data: control ad set spend, Ad015 metrics, dead-ad CTRs, PEIKIRA2's 78% day-2 share (11/06).
- *(calc)*: per-ad spend projection, Poisson probabilities, Rp 150k/day.
- INFERRED: 10% starvation line, Rp 90k/day ad-set cap, CTR < 1.0% early-kill line, the 30% share assumption.

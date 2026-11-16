# S1 scale step: apply-ready card (use only if the 11/20 gate opens)
_Pre-staged 2026-11-13 11:01 WIB by Fuku (cloud heartbeat, groundwork). Read-only: nothing in the ad account was changed. Propose-only: Alvian applies._
_Sources: `2026-11-12_scale_plan_v2.md` (capacity, +25% rule), `2026-11-13_adset3_read_card.md` (ADSET-3 rules), `2026-11-20_gate_brief.md` (gate). Labels per `fuku/memory/playbooks/meta-ads-algorithm.md`._

> **11/16 11:01 refresh (budget/cap state, from `2026-11-18_budget_change_read_card.md`).** This card was written for an *uncapped* PEIKIRA CBO at Rp 300k ("Highest volume"). Since 11/15 00:41 the CBO is Rp 3M/day with a Rp 105k bid cap on all 3 ad sets, and 11/15 spent only Rp 153,555 = 5.1% of budget (control 100,930 / 0, PEIKIRA2 52,625 / 1, ADSET-3 0) [account data]. A budget step only adds spend when the budget, not the cap, is binding. So before G1–G3, check **G0** (Step 0 activity log + last 3 full days, level=campaign):
> | 11/18 outcome → state on 11/20 | G0 | This card |
> |---|---|---|
> | "undo": Rp 300k, caps removed | ✅ | use as written |
> | "revert": Rp 300k, 105k caps kept | ✅ only if PEIKIRA 3-day avg spend ≥ 90% of budget (≥ Rp 270k/day) | if < 90%: **not sent**; the cap sets spend, +25% budget is cosmetic [INFERRED, BC precedent: caps held spend at ~1.4% of budget, 11/05]. Line instead: "CPL met; spend is cap-bound at Rp ⟨avg⟩/day, so a budget step adds nothing. Volume lever = winners, not budget." |
> | still Rp 3M + caps | ❌ | not sent (readout Step 5 already says no budget ask) |
> | other budget X | as row 2 with 90% of X | step = X → 1.25 × X; replace every "300k" / "375k" below with X / 1.25X, and the revert target with X |
> - Never propose a **cap raise** as the scale step: the cap (105k) is already above the 95k target, so a raise trades CPL for volume (`meta-tests-and-proposals.md`; cap proposals need ≥ 8 weekly rows at the cap, and this setup has 1). [account data + playbook]
> - Honest-framing numbers below assume a Rp 300k start + ~40k BC (≈ Rp 340k/day). The 11/16 base is ≈ **Rp 215k/day account** (criterion-1 model, 21% of the Rp 1M leg) *(calc)*, so S1→S4 from 11/20 reaches less than the Rp 730k quoted unless the cap stops binding. Quote the criterion-2 line from readout Step 4b instead of the 730k figure.

## When this card is sent (all three, checked at the 11/20 07:00 readout)
| # | Condition | Source | Pass? (fill 11/20) |
|---|---|---|---|
| G1 | Fab 7d CPL (11/13–11/19) **≤ Rp 95,000** | tracker | ☐ |
| G2 | **A winning engine is present in PEIKIRA**: ADSET-3 day-7 CPL ≤ control CPL (read-card rule 3) **and** ≤ 95k, on ≥ 3 leads; *or* control/PEIKIRA2 7d ≤ 95k on ≥ 4 leads. ADSET-3 < Rp 10k in 7d = starved → only the control/PEIKIRA2 branch can pass | readout P2 (7d 11/13–11/19, `object_ids`) | ☐ |
| G3 | **No kill rule tripped**: ADSET-3 rules 1–2 (cumulative, P2 + P5 11/17–11/19) · Ad015 triggers CTR < 1.30% / CPL > 120k / freq > 2.5 on its **own 7d window** (P4), counted **only if Ad015 is ACTIVE** on 11/20 (paused → n/a) | readout P2, P4, P5 + activity log | ☐ |

- G1 ✅ but G2 ❌ (the CPL came from the site fix, not from a new winner) → **don't scale**: send "hold at Rp 300k, CPL fixed, volume needs a winning wave" instead. Reason: scale plan v2, budget alone fails (KENJI Rp 741k/day → 185k CPL). [account data]
- G1 ❌ → this card is not used; the gate-miss note goes out instead.
- G1 ✅ G2 ✅ but G3 ❌ **only because Ad015 is still active and tripped** (its CPL trigger already fired 11/14: 7d 166.1k) → don't scale into it: ~90% of control spend would ride a fading ad. Re-send OUTBOX ask #2(a) (pause Ad015) as the one ask; S1 follows on the first readout after the pause where G1–G2 still pass. *(added 11/14 19:02 dry-run)*

## The change (one field, one campaign)
**PEIKIRA-BID-CAP-LEADS-CAMPAIGN** `120254051672440572` → campaign daily budget **Rp 300,000 → Rp 375,000** (+25%).
- Nothing else: no ad-set, ad, bid, audience or BC change. CBO decides the split; we read where it lands.
- Why PEIKIRA and not BC: BC already has a Rp 5M budget and spends ≈ Rp 23–53k/day under its Rp 94,250 caps; more BC budget adds nothing (item 4 retired 11/12, `2026-11-12_item4_bidcap_card.md`). [account data]
- Why +25%: scale-plan rule (+25% per ≥ 3 days, only on 7d ≤ 95k + a winner). Meta docs give no budget-change speed → the step size is [FOLKLORE], the read rules below are what protect the CPL.
- Expected *(calc)*: account Rp ⟨P1 Rp/day⟩ → **⟨P1 Rp/day + 75k⟩/day** (11/07–11/13 base: Rp 333k → ≈ Rp 408k). At the gate CPL (≤ 95k) that is ≈ +0.8 leads/day. Marginal leads usually cost more than average [INFERRED], so the read rules judge the step on the 3-day CPL, not the 7d one alone.

### Paste-ready for Alvian or Markus (Ads Manager)
1. Campaigns tab → search `PEIKIRA-BID-CAP-LEADS-CAMPAIGN` → Budget column → `375000` (IDR, daily) → Publish.
2. Reply "S1 done HH:MM" in INBOX so Fuku logs it in the tracker change log and starts the 3-day read.

## Read rules (fixed now, before the step)
Day 0 = the day S1 is applied. Compare PEIKIRA full days after S1 vs the 7 full days before it.
1. **Day 3 read:** PEIKIRA 3-day CPL ≤ Rp 110k *and* account 7d CPL still ≤ 95k → propose **S2** (Rp 375k → Rp 470k) on the same rules.
2. **Hold:** 3-day CPL Rp 110–125k → no new step; re-read on day 5.
3. **Revert:** 3-day CPL > Rp 125k with ≥ Rp 1.1M spent *(calc: 3 × 375k)*, **or** account 7d CPL > 95k on day 5 → propose back to Rp 300k.
4. **Share check:** if one ad set takes > 70% of the new PEIKIRA spend with a CPL > 120k on day 3 → flag (CBO is feeding the wrong engine; propose its pause instead of reverting budget).
5. Every step is logged in `m001_tracker.md` change log with actor + time; reads use 3 full days, never today.

## What S1 can and can't do (honest framing for Alvian)
- S1 is +Rp 75k/day. Criterion 2 needs +Rp 660k/day. Even S1→S4 every 3 days from 11/20 reaches ≈ Rp 730k/day by 12/02 *(calc: 300k × 1.25⁴ = 732k PEIKIRA + ~40k BC)* only if every step holds ≤ 95k, which no engine in 8 weeks has done above ~Rp 185k/day per ad set. [account data, scale plan v2]
- So the S1 message on 11/20 states: CPL criterion met; volume on track only if each wave keeps adding a winner.

## Ready-to-send line (11/20, if G1–G3 pass)
_Fill map: ⟨x⟩ = readout Step 2 account 7d; ⟨winner⟩ + ⟨y⟩ = the G2 branch that passed (Step 2 table CPL); criterion-1 line from readout Step 4b goes right after the first sentence._
> ❓ **[DECISION] S1: PEIKIRA CBO Rp 300k → Rp 375k/day?** 7d CPL Rp ⟨x⟩ ✅ (≤ 95k), ⟨winner⟩ at Rp ⟨y⟩/lead. One field, revert rule set (3-day CPL > 125k → back to 300k). Card: `fab_advertising/reports/2026-11-20_s1_scale_card.md`. My recommendation: **yes**.

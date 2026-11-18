# 11/20 gate: "miss" and "hold" messages (pre-staged)
_Pre-staged 2026-11-13 12:02 WIB by Fuku (cloud heartbeat, groundwork). Dry-run vs readout pulls 2026-11-14 20:02: every ⟨⟩ maps to readout Step 0 / P1–P6 / Step 2–4b. Read-only, nothing changed in the ad account. Propose-only._
_Sister card: `2026-11-20_s1_scale_card.md` (used when G1–G3 all pass). Gate numbers: `2026-11-20_gate_brief.md` (11/14 08:01 refresh). Volume math: `2026-11-12_scale_plan_v2.md`._

## 11/18 08:01 refresh: Variant M1, one fill-ready text per OUTBOX #1 state (read this first)
_Fuku cloud heartbeat, groundwork (backlog #1). Base: 11/18 07:01 readout + read card verdict **STARVED-volume** (S3 11/15–11/17 Rp 181,676 / 1). Model `gate_model_1120.py` with locks 11/13–11/17 and 7d bases 11/11–11/17 (peik 1437590/9, bc 551394/7, p2 490623/4). Read-only; propose-only. Overrides the 11/16 block's numbers and its "budget context sentence"._
- **Expected 11/20 7d CPL by #1 state** *(calc, PEIKIRA spend on the 2 open days 11/18–11/19)*: caps stay ≈ Rp 11.7k/day → **122.0k**; undo live by ~noon 11/18 (≈ 150k/day avg) → **127.1k**; undo live 11/18 00:00 (300k/day) → **131.2k**. Every branch is ❌; best lever set (Ad015 off + site +1pt) 118.8k; no ADSET-3 break-even. So **M1 is settled; G1 ✅ is not reachable**. An undo makes the 11/20 number *worse*, not better (more spend at PEIKIRA's ≈ 160k base): say so, so it doesn't read as the undo failing. (The post-undo pack §1's 117–120k is on 11/16 bases; on 11/18 bases it's 127–131k. Re-run pack §1 with the real undo time before pasting either.)
- **ADSET-3 clause:** pre-pick the **"< Rp 10k spent (still starved)"** row (Rp 0 for 11/13–11/17, 5 full days). Re-check at the 11/20 pull; an undo can move it to the Rp 10k–379k row.
- **⟨neither was / only Ad015 was⟩:** "neither was" (Ad015 ACTIVE, site not applied, curl 11/18 07:01).
- Fill on 11/20: ⟨x⟩ 7d CPL 11/13–11/19; ⟨p⟩ PEIKIRA 7d spend ÷ 7 ÷ 1,000; ⟨e⟩ account 7d spend ÷ 7 ÷ 10,000 (= % of Rp 1M); ⟨spend⟩ ADSET-3 7d; ⟨date⟩ = activity-log time of the undo. Then append the criterion-1 line (Step 4b) + the criterion-2 branch (A for full undo, B otherwise). ≤ 120 words before criterion 2 (each text below ≈ 85–100).

**M1-N: no answer / "keep" (3M + 105k caps still on). Criterion-2 = Branch B.**
> ⚠️ **[REPORT] 11/20 · Gate missed: 7d CPL Rp ⟨x⟩ ❌ (target 95k).** The window closed on 11/14: even the site fix + pausing Ad015 live by 11/16 gave ≈ 97–102k *(calc)*; neither was applied. Volume is the bigger problem now: PEIKIRA is set to Rp 3M/day, but the Rp 105k bid caps hold it at ≈ Rp ⟨p⟩k/day, so the account spends ≈ ⟨e⟩% of the Rp 1M leg. ADSET-3 (the team's 6 new ads) got Rp ⟨spend⟩ in 7 days: untested, not a loser. 👉 #1 ask is still: **undo the 11/15 change (Rp 300k, no caps)**, then the site fix (`fab_advertising/reports/2026-11-11_w1w2_paste_ready.md`).

**M1-A: full undo in the log (Rp 300k + caps removed). Criterion-2 = Branch A.**
> ⚠️ **[REPORT] 11/20 · Gate missed: 7d CPL Rp ⟨x⟩ ❌ (target 95k), as expected.** The window closed on 11/14 (site fix + Ad015 pause by 11/16 ≈ 97–102k *(calc)*; neither applied). PEIKIRA is back at Rp 300k/day with no cap since ⟨date⟩; that adds spend at PEIKIRA's ≈ 160k recent CPL, so this week's number reads worse (≈ 127–131k modelled) even though the undo was right: it's about volume, and learning restarts *(calc, INFERRED)*. ADSET-3: ⟨ADSET-3 clause⟩. 👉 #1 ask now: **the site fix, today** (`fab_advertising/reports/2026-11-11_w1w2_paste_ready.md`). First clean post-undo read: ⟨date + 7⟩ (post-undo pack §1/§4).

**M1-B: budget-only revert (Rp 300k, caps kept). Criterion-2 = Branch B.**
> ⚠️ **[REPORT] 11/20 · Gate missed: 7d CPL Rp ⟨x⟩ ❌ (target 95k).** The window closed on 11/14 (site fix + Ad015 pause by 11/16 ≈ 97–102k *(calc)*; neither applied). PEIKIRA is back at Rp 300k/day since ⟨date⟩, but the Rp 105k bid caps still hold it at ≈ Rp ⟨p⟩k/day (≈ ⟨e⟩% of the Rp 1M leg): the budget was never the brake. ADSET-3 got Rp ⟨spend⟩ in 7 days: untested, not a loser. 👉 #1 ask: **remove the 105k caps on the 3 PEIKIRA ad sets (back to Highest volume)**, then the site fix.

_Pick rule: the 11/20 Step 0 activity-log rows for `120254051672440572` + its 3 ad sets since 11/15 00:42 (budget row → 300k? bid_strategy rows → old_value restored?). Both = A; budget only = B; none = N. If Alvian answered in OUTBOX but the log shows nothing, use N and say "not in the account yet"._

## 11/16 09:01 refresh (superseded by 11/18 above where they differ)
_Fuku cloud heartbeat, groundwork. Base: 11/16 07:03 readout (locks 11/13 293,851/0 · 11/14 309,404/3 · 11/15 153,555/1; 7d PEIKIRA 1,947,508/14, BC 428,216/7, P2 717,275/7; `--budget 153555`)._
- **Expected message: Variant M1** (site not applied as of 11/16 07:03). G1 ✅ needs ≤ 95k; model with nothing changed **116.7k** *(calc)*. Even Ad015 pause + site +1pt live tonight (11/16 eve) = **97.1k ❌** *(calc)*. Only ALL levers + ADSET-3 at 60% share @ Rp 70k live tonight reaches 94.8k, and ADSET-3 is at Rp 0, so treat G1 ❌ as settled unless the 11/17 readout shows a lever went live.
- **M1 stale clause → replace** "(≈ 94–103k if both live by 11/14 eve, 11/14 08:01 model)" with: "(≈ 97–102k even if both had gone live on 11/16; the window was lost by 11/14)" *(calc, `gate_model_1120.py` 11/16 run)*.
- **Budget context sentence (new, add after the headline in M1/M2):** pick by OUTBOX #1 state on 11/19:
  - no answer / "intended", cap still 105k: "PEIKIRA is set to Rp 3M/day but the Rp 105k bid cap holds it at ≈ Rp ⟨7d PEIKIRA spend ÷ 7⟩/day, so the account spends ≈ ⟨x⟩% of the Rp 1M leg."
  - full undo applied (300k + caps removed): "PEIKIRA is back at Rp 300k/day, no cap, since ⟨date⟩." Model line from the post-undo pack §1/§4.
  - budget-only revert (300k, caps kept): "PEIKIRA is back at Rp 300k/day since ⟨date⟩, but the Rp 105k bid cap still holds it at ≈ Rp ⟨7d PEIKIRA spend ÷ 7⟩/day." Capped models stay.
- **ADSET-3 clause:** at 11/16 the only fillable row is **"< Rp 10k spent (still starved)"** (Rp 0 since 11/13). Pre-pick it; re-check at the 11/20 pull.
- **Criterion-1 line:** 11/16 values LWD **12/02**, F+C live by 11/27 ≈ 76.2k, nothing changes 102.1k *(calc, criterion1 model)*. Paste Step 4b on 11/20, don't reuse these.
- **Criterion-2 line: the "5 budget steps of +25%" sentence is void** (CBO is already Rp 3M). Swapped in below 11/17 08:01 (Branch A = full undo, Branch B = caps stay). The binding limit is now the bid cap + no winner, not the budget. **11/16 21:02:** if no full undo is in the log by 11/20, don't send the 01/15 ask at all: use the "Caps-stay check" replacement line in that file (no wave can reach the ≥ Rp 380k verdict spend under the cap).

## Which message goes out on 11/20 (pick one at the 07:00 readout)
| Gate result (S1 card G1–G3) | Message | Ad ask? |
|---|---|---|
| G1 ✅ G2 ✅ G3 ✅ | S1 card line (not this file) | yes: PEIKIRA CBO 300k → 375k |
| G1 ✅ G2 ❌ (CPL under 95k, but no proven new winner) | **Variant H: hold** | no |
| G1 ✅ G2 ✅ G3 ❌ (ADSET-3 rule 1–2 cumulative, or Ad015 7d trigger while ACTIVE, CPL rule only with ≥ Rp 600k Ad015 spend in the window: readout Step 4 G3) | **Variant H** + name the tripped rule; re-check on 11/23 | no |
| G1 ✅ G2 ✅ G3 ❌ **only because Ad015 is still active and tripped** | **Variant H** + "S1 waits on ask #2(a) (pause Ad015)"; re-send ask #2(a) (pause Ad015) as the one ad ask (S1 card, G3 row) | yes: #2(a) only |
| G1 ❌ | **Variant M: miss** (pick M1 or M2 below) | no |

## Variant H: "CPL fixed, hold the budget" (fill ⟨⟩)
> ✅ **[REPORT] 11/20 · 7d CPL Rp ⟨x⟩ ✅ under 95k (criterion 1 met this week).** It came from ⟨cause: pick from readout Step 0 + Step 2: "the site fix" if W1/W2 live; "pausing Ad015" if paused; else the ad set whose 7d CPL fell most vs 11/06–11/12, named⟩, not from a new winning ad set: ⟨ADSET-3 clause, pick from the table below⟩. So I'm **not** asking for more budget: in 8 weeks, adding budget without a new winner never held (KENJI ×7: Rp 741k/day → CPL 185k). 👉 Budget stays Rp 300k; the next lever for volume is a winning creative wave. ⟨If G3 tripped: "Kill rule ⟨rule⟩ tripped on ⟨date⟩; re-check 11/23."⟩ Then append the shared criterion-2 line below.

## Variant M: "gate missed" (pick one sentence block)
**M1: the site fix was not applied (W1/W2 still off on 11/19):**
> ⚠️ **[REPORT] 11/20 · Gate missed: 7d CPL Rp ⟨x⟩ ❌ (target 95k).** After the 0-lead 11/13 day, only the site fix (Jakarta Pusat → Selatan, 800 → 750) **plus** pausing Ad015 could reach it (≈ 94–103k if both live by 11/14 eve, 11/14 08:01 model); ⟨neither was / only Ad015 was⟩ applied. ⟨ADSET-3 clause⟩. 👉 Still the #1 ask: the site fix, today (paste-ready: `fab_advertising/reports/2026-11-11_w1w2_paste_ready.md`).

**M2: the site fix was applied but CPL is still above 95k:**
> ⚠️ **[REPORT] 11/20 · Gate missed: 7d CPL Rp ⟨x⟩ ❌ (target 95k), even with the site fix live since ⟨date⟩.** Pixel LP→Lead ⟨before⟩% → ⟨after⟩% (needs 14 days to read +0.5pt). ⟨ADSET-3 clause⟩. The remaining CPL lever is creative (new phone-photo ads), not settings.

## ADSET-3 clause (pick the row that matches the 11/20 pull; added 11/13 22:34)
_ADSET-3 was at Rp 0 / 0 impressions for its first ~39h (11/14 19:02; min spend Rp 75k is part (b) of OUTBOX ask #2 (Ad015 + ADSET-3 min) since 11/14 07:02). So "Rp ⟨y⟩/lead" may not be fillable on 11/20. Pick by readout Step 2 (P2, 7d 11/13–11/19) + Step 3; check the rule-2 rows first:_
| ADSET-3 7d state | Clause (paste into H / M1 / M2) |
|---|---|
| **< Rp 10k spent** (still starved) | "ADSET-3 (the team's 6 new ads) got almost no delivery: Rp ⟨spend⟩ in 7 days, so it's untested, not a loser. The CBO kept the budget on the 2 old ad sets. ⟨If min spend not applied: "The fix is still a Rp 75k daily minimum on it (part (b) of ask #2)."⟩" |
| **Rp 10k – 379k** (under-tested, < 4× CPL target) | "ADSET-3: Rp ⟨spend⟩ spent, ⟨n⟩ leads, ⟨s⟩% of PEIKIRA spend: too early to judge (the read needs ≥ Rp 380k); verdict 11/27." |
| **≥ Rp 380k** (readable, ≥ 1 lead) | "ADSET-3: Rp ⟨y⟩/lead on ⟨n⟩ leads (⟨s⟩% share) vs control Rp ⟨c⟩ (ratio ⟨r⟩): ⟨readout Step 3 rule-3 word: keep / keep, verdict 11/27 / pause proposed⟩. A winner is only called on 11/27 (≤ 95k on ≥ 4 leads, read card rule 4)." |
| **Paused / killed by rule 2** | "ADSET-3 was paused on ⟨date⟩ under kill rule 2 (≥ Rp 190k, 0 leads)." |
| **Rule 2 fired (Step 3), still active** | "ADSET-3 hit kill rule 2 on ⟨date⟩ (Rp ⟨spend⟩, ⟨n⟩ leads); pause proposed (ranked ask (2) in readout Step 5)." |
_Rp 380k = the under-tested line of the 11/27 verdict template (4 × 95k). If the clause is the "starved" row, it is the reason the gate has no new winner: say so before the criterion-2 line, not after._

## Shared criterion-2 line (H, M1 and M2 all end with it; send as is)
_Updated 11/13 22:34; replaced 11/17 08:01 by the two cap branches below. Branch A is the single ❓ in the 11/20 message; in Branch B the ❓ is ask #1._
> ⟨Criterion-1 line from readout Step 4b, pasted unchanged. Default shape: "✅ Criterion 1 (CPL ≤ 95k) is still reachable for 12/05 (window 11/28–12/04): with what's live, ⟨row A⟩; asks #2 (Ad015 + ADSET-3 min) + #3 (site W1+W2) live by ⟨date⟩ ≈ ⟨F+C⟩k; last workable date ⟨mm/dd⟩, ⟨n⟩ days left *(calc, `2026-12-05_criterion1_path.md`)*." If Step 4b printed NONE: "⚠️ Criterion 1 for 12/05 now needs ADSET-3 to win; I'll put a move to 12/19 to you on 11/27."⟩
> _(11/14 values, for reference only, don't paste: both live by 11/27 ≈ 88k; last workable 11/29.)_

_11/17 08:01 swap (cloud heartbeat): the pre-cap line (base 340k, "5 budget steps by 11/20") is retired. This is now the only version; source = `2026-11-20_criterion2_replan.md` "11/16 refresh" l.13–21. Pick the branch from the 11/20 readout Step 0 log check._

**Branch A: full undo in the log (budget back to Rp 300k AND the 105k caps removed).** Send:
> 📊 **Criterion 2 (Rp 1M/day at ~95k by 12/05) is out of reach.** The account spends ≈ Rp ⟨d⟩k/day (⟨e⟩% of the target) on the Rp 300k budget, and there is no new winning ad set yet. Each winner adds Rp 100–185k/day at ≤ 95k (8 weeks of data), so Rp 1M/day needs 4–7 at once. ❓ **Move criterion 2 to 01/15, with 3 new phone photos from the Fab team every Saturday from ⟨max(11/21, undo day + photos)⟩?** (Criterion 1, CPL ≤ 95k, stays the 12/05 goal.) My recommendation: **yes**; 01/15 holds in the mid case (≈ 1 winner per 4 ads); I re-forecast on 12/14. Reply "ok" or a new date. Plan: `fab_advertising/reports/2026-11-20_criterion2_replan.md`.

**Branch B: caps still on ("intended", no answer, or budget-only revert).** Send instead (no date ask, no photo-calendar ask):
> 📊 **Criterion 2 (Rp 1M/day at ~95k by 12/05) is out of reach**, and it can't be re-planned yet: the Rp 105k bid caps hold PEIKIRA at ≈ Rp ⟨p⟩k/day, so the account spends ≈ Rp ⟨d⟩k/day (⟨e⟩% of the target). No new ad can collect the ≥ 4 leads needed to prove it. I'll re-plan the day the caps come off (ask #1).

- Fill: ⟨d⟩ = 11/20 tracker 7d account spend ÷ 7; ⟨e⟩ = ⟨d⟩ ÷ 1,000; ⟨p⟩ = PEIKIRA 7d spend ÷ 7 *(calc)*. In Branch B the message has no ❓ for criterion 2; the single ❓ is ask #1 (re-raise as a one-liner).

_If Variant S1 (gate passed) goes out instead, the criterion-2 line still goes with it, with "out of reach" softened only if the S1 step plus winners on hand reach ≥ Rp 1M/day by 12/05 in the scale plan math (they won't with ≤ 1 winner)._

## Fill rules (so 11/20 is a 5-minute job)
- ⟨x⟩ = tracker 7d CPL for 11/13–11/19 *(calc)*, copied from the 11/20 readout row.
- ⟨spend⟩ = ADSET-3 7d spend; ⟨y⟩ = its CPL (spend ÷ leads); ⟨n⟩ leads; ⟨s⟩ share of PEIKIRA spend; ⟨c⟩ control CPL; ⟨r⟩ = ⟨y⟩ ÷ ⟨c⟩ (readout Step 3 rule 3). All from readout P2 / Step 2: ad sets by `object_ids` (control `120254051672430572`, PEIKIRA2 `120254276298070572`, ADSET-3 `120254400251570572`).
- ~~Realistic 12/05 band (pre-cap: 340–400k / 440–520k)~~ retired 11/17: the line now uses the measured 7d spend/day ⟨d⟩, not a modelled band (base under the cap ≈ Rp 78.5k/day, re-plan l.14 *(calc)*).
- The 01/15 date is a proposal, not a commitment: it's Alvian's mission, he sets the deadline. Rule: if he doesn't answer within 24h, keep working toward both criteria unchanged.
- Only one message goes to OUTBOX "Latest report" for M-001 on 11/20 (replace whichever M-001 report is current; on 11/14 that was the 11/14 07:02 one). The criterion-2 line is the single ❓ in it.
- ~~Realistic band pick~~ retired 11/17 (see above). **"Winner present on 11/20" = readout Step 4 G2 ✅** still decides "there is no new winning ad set yet" (G2 ✅ → name the ad set instead).
- ⟨neither was / only Ad015 was⟩ (M1) and the min-spend sub-clause = readout Step 0 checkboxes (Ad015 status, min spend).
- Order inside the message: headline → cause → ADSET-3 clause → 👉 next step → criterion-1 line (Step 4b) → criterion-2 line. ≤ 120 words before the criterion-2 line.

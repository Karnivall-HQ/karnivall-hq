# 11/20 gate: "miss" and "hold" messages (pre-staged)
_Pre-staged 2026-11-13 12:02 WIB by Fuku (cloud heartbeat, groundwork). Read-only, nothing changed in the ad account. Propose-only._
_Sister card: `2026-11-20_s1_scale_card.md` (used when G1–G3 all pass). Gate numbers: `2026-11-20_gate_brief.md` (09:01 refresh). Volume math: `2026-11-12_scale_plan_v2.md`._

## Which message goes out on 11/20 (pick one at the 07:00 readout)
| Gate result (S1 card G1–G3) | Message | Ad ask? |
|---|---|---|
| G1 ✅ G2 ✅ G3 ✅ | S1 card line (not this file) | yes: PEIKIRA CBO 300k → 375k |
| G1 ✅ G2 ❌ (CPL under 95k, but no proven new winner) | **Variant H: hold** | no |
| G1 ✅ G2 ✅ G3 ❌ (a kill rule tripped in the last 3 days) | **Variant H** + name the tripped rule; re-check on 11/23 | no |
| G1 ❌ | **Variant M: miss** (pick M1 or M2 below) | no |

## Variant H: "CPL fixed, hold the budget" (fill ⟨⟩)
> ✅ **[REPORT] 11/20 · 7d CPL Rp ⟨x⟩ ✅ under 95k (criterion 1 met this week).** It came from ⟨the site fix / Ad015 / BC⟩, not from a new winning ad set: ADSET-3 Rp ⟨y⟩/lead on ⟨n⟩ leads (needs ≤ control and ≤ 95k on ≥ 3). So I'm **not** asking for more budget: in 8 weeks, adding budget without a new winner never held (KENJI ×7: Rp 741k/day → CPL 185k). 👉 Budget stays Rp 300k; the next lever for volume is a winning creative wave. ⟨If G3 tripped: "Kill rule ⟨rule⟩ tripped on ⟨date⟩; re-check 11/23."⟩ Criterion 2 (Rp 1M/day by 12/05): ⚠️ out of reach, see the line below.

## Variant M: "gate missed" (pick one sentence block)
**M1: the site fix was not applied (W1/W2 still off on 11/19):**
> ⚠️ **[REPORT] 11/20 · Gate missed: 7d CPL Rp ⟨x⟩ ❌ (target 95k).** The one lever that could open it on its own, the site fix (Jakarta Pusat → Selatan, 800 → 750), wasn't applied; my model had it at ≈ 93k if live by 11/14. ADSET-3: Rp ⟨y⟩/lead (⟨n⟩ leads, ⟨s⟩% share). 👉 Still the #1 ask: the site fix, today (paste-ready: `fab_advertising/reports/2026-11-11_w1w2_paste_ready.md`).

**M2: the site fix was applied but CPL is still above 95k:**
> ⚠️ **[REPORT] 11/20 · Gate missed: 7d CPL Rp ⟨x⟩ ❌ (target 95k), even with the site fix live since ⟨date⟩.** Pixel LP→Lead ⟨before⟩% → ⟨after⟩% (needs 14 days to read +0.5pt). ADSET-3: Rp ⟨y⟩/lead. The remaining CPL lever is creative (new phone-photo ads), not settings.

**Both M1 and M2 end with the same honest criterion-2 line (send as is):**
> 📊 **Criterion 2 (Rp 1M/day at ~95k by 12/05) is out of reach.** To get there, 5 budget steps of +25% had to start by 11/20. A winning wave adds only ~Rp 100–185k/day at ≤ 95k (8 weeks of ad-set data), so Rp 1M/day needs 4–7 winners at once; we have ⟨0/1⟩. Realistic 12/05 ≈ **Rp ⟨400–520⟩k/day** *(calc)*. ❓ **My recommendation: keep criterion 1 (CPL ≤ 95k) as the 12/05 goal, and move Rp 1M/day to 01/15 with one new photo wave every week.** Reply "ok" or give me a new date.

## Fill rules (so 11/20 is a 5-minute job)
- ⟨x⟩ = tracker 7d CPL for 11/13–11/19 *(calc)*, copied from the 11/20 readout row.
- ⟨y⟩, ⟨n⟩, ⟨s⟩ = ADSET-3 7d spend ÷ leads, leads, share of PEIKIRA spend: pull ad sets by `object_ids` (control `120254051672430572`, PEIKIRA2 `120254276298070572`, ADSET-3 `120254400251570572`).
- Realistic 12/05 band: 300k PEIKIRA + ~40k BC + Rp 100–185k per proven winner present on 11/20 *(calc)*; 0 winners → ≈ Rp 340–400k, 1 winner → ≈ Rp 440–520k. [account data: scale plan v2]
- The 01/15 date is a proposal, not a commitment: it's Alvian's mission, he sets the deadline. Rule: if he doesn't answer within 24h, keep working toward both criteria unchanged.
- Only one message goes to OUTBOX "Latest report" for M-001 on 11/20 (replace the 11/13 report). The criterion-2 line is the single ❓ in it.

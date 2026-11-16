# Post-undo re-base pack (PEIKIRA back to Rp 300k/day, no bid cap)
_Written 2026-11-16 16:02 WIB, before any undo. Use only if the activity log shows the 11/15 change undone (budget 3M → 300k and/or bid strategy back to the logged `old_value`). Playbook: `meta-modelling-and-planning.md` §D–§E._

## 0. Trigger check (first thing in the readout after the undo)
1. Activity log since the last poll: note the **undo time (WIB)**, actor, and old/new values for the budget **and** each ad set's bid strategy. Only budget undone (caps kept) → this pack does **not** apply as written: PEIKIRA stays capped, keep `--cap-throttled` and the capped models.
2. Undo day = the day it happened. **Read window starts the next full day** (undo 11/18 → window from 11/19). Split the undo day at the undo time, as on 11/15 (§D3): don't project pace from that day.
3. Add a tracker change-log row (date, change, actor, "effect read on" = undo day + 7).
4. Same run, grep the staged files for "3M", "105k", "cap-throttled", "STARVED" (§E1) and add a one-line "undo applied ⟨date⟩" pointer to: `2026-11-18_budget_change_read_card.md`, `2026-11-20_readout_template.md`, `2026-11-20_gate_miss_note.md`, `2026-11-20_criterion2_replan.md`, `wave1_read_template.md`, `reports/weekly/2026-11-23.md`.

## 1. 11/20 gate (window 11/13–11/19): still ❌ after an undo
Run on 11/16 bases, 11/16 and 11/17 locked at the capped pace (≈ Rp 20k / 0), 11/19 at Rp 300k *(calc, `gate_model_1120.py`)*:

| 11/18 (undo day) lock | 7d model on 11/20 |
|---|---|
| Rp 20k / 0 (undo late in the day) | **117.4k** ❌ |
| Rp 150k / 1 (undo midday) | **118.3k** ❌ |
| Rp 300k / 2 (undo overnight) | **120.4k** ❌ |

The undo makes the 11/20 number slightly **worse**, not better: more PEIKIRA spend at 139.1k (above the 95k target) dilutes the cheap BC leads (§D4). Say so in the 11/20 line so the undo isn't blamed: "Gate ❌ at ⟨actual⟩; the undo was for volume, not for this window."
Command (fill the real 11/16–11/18 locks): `python3 fuku/bin/gate_model_1120.py --lock 293851 0 --lock 309404 3 --lock 153555 1 --lock ⟨11/16⟩ --lock ⟨11/17⟩ --lock ⟨11/18⟩ --peik ⟨7d⟩ --bc ⟨7d⟩ --p2 ⟨7d⟩ --budget 300000`

## 2. Criterion 1 (12/05, judged window 11/28–12/04) after an undo
`python3 fuku/bin/criterion1_model_1205.py --peik 1947508 14 --bc 428216 7 --p2 717275 7 --today 2026-11-19 --budget 300000` (no `--cap-throttled`) *(calc)*:

| Line | Capped (11/16, Rp 154k/day) | Post-undo (Rp 300k/day) |
|---|---|---|
| A nothing changes | 102.1k ❌ | **114.4k** ❌ |
| F Ad015 paused (freed at P2 102.5k) | 85.9k ✅ | **92.0k** ✅ |
| C site +0.5pt alone | 90.5k ✅ | **101.4k** ❌ |
| F+C site +0.5pt | — | **81.5k** ✅ |
| Break-even PEIKIRA CPL, no site fix | — | **107.1k** |
| LAST WORKABLE DATE | 12/02 | **11/30** (11 days from 11/19) |
| Account spend/day | 214.7k = 21% of 1M leg | **361.2k = 36%** |
| Criterion 2 (Rp 1M/day leg) | BLOCKED by cap | PEIKIRA needs 938.8k/day (**3.1×**); at 1M: nothing 129.1k ❌, F+C 87.2k ✅ (flat-CPL, INFERRED) |

What changes in the message after an undo:
- **The CPL half gets harder** (LWD 12/02 → 11/30; the site fix alone no longer clears it) **while the volume half reopens** (36% of the leg, no cap blocking it). Both halves in every line (§D5).
- **Ask #2 (Ad015 pause + ADSET-3 min Rp 75k) becomes the top lever:** it is the only single ask that clears criterion 1 at Rp 300k/day (92.0k). Re-validate on fresh 7d before re-asking (tests-and-proposals rule): Ad015 trigger = 7d CPL > 120k on ≥ Rp 600k.
- **S1 (+25% budget) stays off** until 7d spend ÷ budget ≥ 90% for 3 days after the undo (budget must bind; S1 card G0).

## 3. Read rule after the undo (copied from the 11/18 card, fixed 11/15)
Window = full days after the undo, 7d read. **Success:** PEIKIRA ≥ 2 leads/day at ≤ 130.9k. **Fail:** < 1.5 leads/day → re-check the activity log for other edits before blaming the undo. Days 1–3 may run high: removing the cap sends all 3 ad sets back into learning (INFERRED, as on 11/15); judge on days 1–7, not day 1.

## 4. Pre-filled status lines
- **Undo day:** "✅ PEIKIRA undo seen at ⟨HH:MM⟩ (⟨actor⟩): budget Rp 3M → ⟨300k⟩, bid strategy → ⟨old_value⟩ on ⟨n⟩/3 ad sets. Read window from ⟨date+1⟩; success = ≥ 2 leads/day at ≤ 130.9k over 7 days."
- **11/20 readout:** "📊 7d ⟨actual⟩ ❌ vs 95k (model 117–120k). The undo restores volume; it was never going to open this window. Criterion 1 LWD now 11/30 at Rp 300k/day; ask #2 alone gets 92.0k *(calc)*."
- **If the 11/18 answer is 'keep':** this pack doesn't apply; keep the capped models and the 11/18 card's STARVED rules.

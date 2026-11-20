# Retro #5 prep (draft, 2026-11-20 17:01 WIB)
_Groundwork so the ~11/21 retro is one pass. Source: `lessons.md` lines dated 11/16–11/20 (12 lessons since Retro #4). Delete this file when Retro #5 lands._

## Mapping (12 → 3 playbooks + ad-copy check + 1 new)
| # | Lesson (date · tag) | Target | Draft line to paste |
|---|---|---|---|
| 1 | 11/16 · read rules: readability floor | `meta-tests-and-proposals.md` §A (new 8) | **Readability floor + L = 0 row.** Spend < 3 × baseline CPL → judge volume only; dry-run every lead count L, incl. 0 (11/16: one extra lead flipped "undo" to "no ask" at Rp 180k). |
| 13 | 11/20 · tooling: ∞ CPL at 0 leads | same §A 8 (merge with #1) | …and every comparative/guard CPL rule gets a spend floor (the kill line, 2× target) before a 0-lead side counts (`bc_ladder_read.py` bug, 11/20). |
| 6 | 11/20 · tests: probe sizing | `meta-tests-and-proposals.md` §A (new 9) | **Size the probe to reach its own floor.** Projected 7d spend ≥ kill/verdict floor; if one object can't (BC204 at Rp 2k/day), pool every object passing the same gate and read the group with one comparative rule (BC ladder, 4 ad sets, 33 leads pooled). |
| 5 | 11/20 · models: per-criterion | `meta-modelling-and-planning.md` §A (new 5) + `meta-tests-and-proposals.md` §C pointer | **Model a structural ask on each criterion separately** and state the trade in the ask. When a cheap leg carries the blend, test "throttle the expensive leg + scale the cheap one" (11/20: undo helped volume, hurt CPL 92.1k → ≈ 114k *(calc)*). |
| 3 | 11/16 · plans: circular gate | `meta-modelling-and-planning.md` §C (new 4) | **Every step trigger must be reachable under the current constraint** (verdict spend ≤ capped pace × days × share); if not, the plan is void until the constraint lifts. |
| 7 | 11/20 · planning: park → dependent plans | `meta-modelling-and-planning.md` §E (new 4) | **Parking/dropping an ask = grep for plans triggered by it** and write their "ask never happens" branch the same run (criterion-2 plan sat unplanned 11/16–11/20). |
| 2 | 11/16 · branches: label drift | `meta-modelling-and-planning.md` §E (new 5) | **Branch labels carry the target's entry condition**; re-check every label the run a rec changes. |
| 4 | 11/18 · pre-staging: dated snapshot | `meta-modelling-and-planning.md` §E (new 6) | **Chained templates hand off a dated state snapshot** (every setting the next card branches on); the downstream log window starts at it. |
| 8 | 11/20 · creative: carrying ad + angle | **new** `meta-creative-build.md` §A | List the carrying ad per ad set (others ≈ Rp 0), view image + overlay, group by angle not ad-set name, judge CTR and CPL separately. |
| 9 | 11/20 · creative: existing hashes first | new playbook §A | Before blocking on photos, pull image hashes of the best live ads (`ads_get_creatives`) and build from those; ask for a shoot only for an uncovered angle (N2 buildable with 0 new assets). |
| 10 | 11/20 · meta-creative: Adv+ = parent | new playbook §B (+ tests §C "Build specs" pointer) | In each build row Adv+ enhancements = the comparison parent's; off only for order/format tests, reason stated. |
| 11 | 11/20 · copy: old sheet re-check | `ad-copy-page-check.md` (new step) | Sheet > 3 days old → re-run the page count first; convert fact gates the page already answers into its wording (STATED); keep only gates the page can't answer. |
| — | (11/05 ×3 orientation/env/learning) | keep in lessons.md | Not ads-specific; no playbook fits yet. |

## Proposed new playbook: `meta-creative-build.md`
Why: 3 creative-build lessons in one day (8, 9, 10) + `creatives/2026-11-20_bc_wave0_markus_sheet.md` is the first sheet built this way. Sections: A. Find what works (carrying ad, angle grouping, hashes) · B. Build rows (parent, Adv+ = parent, page-checked copy via `ad-copy-page-check.md`, read rules via tests §A) · Last validated: 11/20 BC Wave 0 + §2c–§2e.

## Other retro items to cover (protocol steps 2, 4, 5)
- **Score:** M-001 criterion 1 ✅ this week (92.1k, by mix); criterion 2 ❌ (≈ Rp 98k/day vs Rp 1M), honest date ≈ Feb (INFERRED). Bottleneck = Alvian/Markus apply rate: asks #2 (since 11/14) and #3 (since 11/13) unapplied 6–7 days. M-002: Incess pick split 11/23.
- **Strategy question for the retro:** 4 straight quiet runs today produced tools/sheets for asks that aren't applied. Consider: fewer new staged files until something is applied; shift groundwork toward what needs no ad-account change (site copy, WA script, M-002).
- **Evolving rules:** add 1 line for `meta-creative-build.md`; check CLAUDE.md Evolving stays ≤ 30 lines.
- **lessons.md after retro:** 23 → ≈ 6 lines (header + 3 × 11/05 + new).

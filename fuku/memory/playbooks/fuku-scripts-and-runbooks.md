# Playbook: Fuku's own scripts, runbooks and pre-written text

## When to use
Any time Fuku writes or changes a script in `fuku/bin/`, a runbook step in NOW.md / a card / a run sheet, or pre-written text that a future run will paste. These files run unattended; a stale input prints clean numbers with no error.

## Steps
1. **"Latest 7d" bases are explicit args in the runbook command.** Argparse defaults are only a fallback and get bumped at each 07:00 readout. (11/28: `c1_closeout.py` kept the 11/20–11/26 base and NOW's command omitted `--rate/--cpl` → tomorrow's status line would have been one base stale.)
2. **Every input names its source cell** ("call 5 campaign total", "ad-level CTR from call 7", "one dataset_stats call, PT day rows"). A number without a named source gets mixed from different pulls.
3. **Verdict strings branch on "window closed?".** Past tense (MET / MISSED / CLOSED) only when every day is locked; otherwise "projected …". (11/28: "MISSED ❌ on 12/05" printed 5 days early.)
4. **0-lead and missing-row paths fail loudly** (explicit fallback flag or exit 1), never ZeroDivisionError or a silent zero.
5. **Any re-scope or revised number → sweep the same run:** `fuku/bin/sweep.sh "<old value>" ["<old value 2>" …]` greps NOW, OUTBOX Open, `fab_advertising/` reports + creatives, and `fuku/bin/`. Fix every live hit or mark it dated-history. (11/27: the weekly skeleton still scoped W0 as 201/204/3-21 four days after the shrink; the ladder script still hard-coded 201 + 208.)
6. **"Paste the pre-written line from X" → open X and confirm the line exists for that date.** A line that depends on an assumption (launch date) lives in a script with the assumption as an input, not in prose. (11/27: rule 5 pointed at a 12/05 line that didn't exist.)
7. **Before sizing or re-scoping a backlog item, grep MISSIONS progress + `reports/` for its code** (W3, W4, R7 …) and carry earlier verdicts and gates forward. (11/27: W3 was called "the bigger lever" though 11/11 had gated it on routing.)
8. **Dry-run every new script on real rows + the edge cases** (L = 0, missing row, window unlocked) and hand-check one number before wiring it into a runbook. Exit codes match the printed verdict.

## Quality bar
A run 5 days from now can paste the runbook command as written and get today-correct output, or a loud error.

## Pitfalls
- Building a new script for an ask that is still unapplied (see Evolving rule "stage less, unblock more"): only build when the next readout needs it.

## Last validated
2026-11-28 (Retro #6, from 6 lessons 11/23–11/28) · M-001 (`c1_closeout.py`, `bc_ladder_read.py`, `w1w2_read.py`, 11/30 weekly run sheet).

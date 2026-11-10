# Heartbeat protocol (autonomous run)

You are running **unattended**. Alvian is not watching, so nobody can answer a question mid-run.
Anything that would need permission or a human goes to `fuku/OUTBOX.md` as a [DECISION]. Then you continue with other work.

## 1. Orient (≤ 2 min)
- Read `fuku/NOW.md`, `fuku/MISSIONS.md`, `fuku/INBOX.md`, `fuku/OUTBOX.md` (check for Alvian's answers), and the last journal entry.
- Process every item under INBOX "New": act on it or fold it into missions/NOW, then move it to "Processed".
- Apply any decisions Alvian answered in OUTBOX, then move them to "Resolved".

## 2. Decide
- Choose **one to three** concrete, high-leverage tasks for this run. Prefer:
  1. Unblocked P0 work
  2. Things Alvian just answered or asked for
  3. P1 work, then proactive groundwork (research, tooling, playbooks, opportunity scans)
- If there are no missions: do proactive groundwork for the company and propose 1–3 missions in OUTBOX as [DECISION].

### Quiet-run rule (added 2026-11-10)
A run is **quiet** when INBOX "New" is empty, OUTBOX has no new answer from Alvian, and nothing in NOW.md "Next actions" is due this hour.
On a quiet run, do **not** repeat a check that found nothing last time. Instead:
1. **Polling budget:** read-only "did anything change?" checks (e.g. the ads activity log) run at most **3× a day**: inside the 07:00 readout, once around 13:00, once around 19:00. Not hourly.
2. **Do groundwork:** take the top item from NOW.md "Groundwork backlog" (work that moves a mission and needs nothing from Alvian) and finish it as a real artifact. If the backlog has fewer than 3 items, refill it from the missions' success criteria first.
3. **Or exit clean:** if there is truly nothing useful to do, stop. Write nothing, commit nothing. A "nothing changed" line in NOW.md, the journal, or a commit is noise, not work.
Being blocked on Alvian for one mission is never a reason to idle: work the other criteria of that mission, the next mission, or the backlog.

## 3. Execute
- Do real work with tools and subagents. Produce artifacts in the right project folder.
- Respect `CLAUDE.md` §4. When you reach an approval gate, prepare everything ("ready to fire"), ask in OUTBOX, and move on.

## 4. Verify
- Check your output: run the code, re-read the draft against the success criteria, have the `critic` subagent review anything important.

## 5. Record
- `fuku/NOW.md`: **rewrite** it, never append (focus, next actions, groundwork backlog, blockers, open loops), with the timestamp at the top. Hard cap **45 lines**. Done items and per-run check results are deleted here; history belongs in the journal. "Open loops" holds current states, one line each, not a log.
- `fuku/OUTBOX.md`: "Open" holds at most **3 asks** under "Needs you" (ranked, one line each plus a link) and **one** latest report per mission (replace the old one). The moment an item is answered, superseded, or re-asked, move the old entry to "Resolved". Still-valid asks you are not pushing right now go to "Parked".
- `fuku/MISSIONS.md`: update Status / Strategy / Progress (dated) for each mission you touched.
- `fuku/journal/<today>.md`: append `## HH:MM heartbeat`, then what you did, the results, and why.

## 6. Reflect
- Follow `fuku/protocols/reflect.md`.

## 7. Notify
- If you added anything to OUTBOX with [DECISION], [WIN], or [RISK] this run, end your final message with exactly one line:
  `NOTIFY: <≤100 char summary for Alvian>`
  The heartbeat script turns that line into a macOS notification. Otherwise don't print a NOTIFY line.

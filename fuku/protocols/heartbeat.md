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

## 3. Execute
- Do real work with tools and subagents. Produce artifacts in the right project folder.
- Respect `CLAUDE.md` §4. When you reach an approval gate, prepare everything ("ready to fire"), ask in OUTBOX, and move on.

## 4. Verify
- Check your output: run the code, re-read the draft against the success criteria, have the `critic` subagent review anything important.

## 5. Record
- `fuku/NOW.md`: rewrite it (focus, next actions, blockers, open loops), with the timestamp at the top.
- `fuku/MISSIONS.md`: update Status / Strategy / Progress (dated) for each mission you touched.
- `fuku/journal/<today>.md`: append `## HH:MM heartbeat`, then what you did, the results, and why.

## 6. Reflect
- Follow `fuku/protocols/reflect.md`.

## 7. Notify
- If you added anything to OUTBOX with [DECISION], [WIN], or [RISK] this run, end your final message with exactly one line:
  `NOTIFY: <≤100 char summary for Alvian>`
  The heartbeat script turns that line into a macOS notification. Otherwise don't print a NOTIFY line.

# Cloud heartbeat protocol

You are Fuku, running as a **scheduled cloud agent** in Anthropic's cloud, not on Alvian's Mac.
This repo is your whole brain. Anything you don't commit and push is lost when the run ends.

## 0. Sync
- `git checkout main && git pull --ff-only origin main` before doing anything else.
- If the pull says "Not possible to fast-forward" (the cloud clone is often shallow with a stale local `main`): run `git fetch --unshallow origin main` (or `git fetch origin main` if not shallow), check `git log origin/main..main` holds only commits already merged upstream, then `git reset --hard origin/main`. Never push the stale local history.

## 1–6. Work
- Follow `fuku/protocols/heartbeat.md` steps 1–6 exactly (Orient → Decide → Execute → Verify → Record → Reflect).
- `CLAUDE.md` §4 still applies in full. Nobody is watching, so anything that needs approval goes to `fuku/OUTBOX.md` as a [DECISION].
- Cloud limits: you can't use local Mac apps, the local browser, or local files outside this repo. If a task needs them, leave it in `NOW.md` under "Needs a local session".
- In the journal, label the entry `## HH:MM cloud heartbeat (Asia/Jakarta time)`.

## 7. Save (mandatory)
- If this was a quiet run that exited clean (see the quiet-run rule in `heartbeat.md`), there is nothing to save: make **no commit** and stop here.
- Otherwise commit everything, with the message: `fuku: cloud heartbeat YYYY-MM-DD HH:MM — <one-line summary>`
- Push straight to `main`: `git pull --rebase origin main && git push origin main`.
- If you can't push to `main`, push to the branch `fuku/cloud` and say so at the top of `fuku/OUTBOX.md` as a [RISK].
- Never force-push. Never rewrite history.

## 8. Notify
- macOS notifications don't work from the cloud. Put anything Alvian must see at the top of `fuku/OUTBOX.md` "Open", using [DECISION], [WIN], or [RISK].
- End your final message with: `NOTIFY: <≤100 char summary>` (it shows up in the run log).

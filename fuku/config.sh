# Fuku heartbeat configuration. Edit freely, then run: fuku/bin/install.sh (to apply the interval)
HEARTBEAT_MINUTES=60        # how often Fuku wakes up
ACTIVE_HOUR_START=7         # local time; no runs before this hour
ACTIVE_HOUR_END=23          # no runs at/after this hour (set 0 and 24 for 24/7)
FUKU_MODEL="opus"           # opus | sonnet | fable | full model id
FUKU_EFFORT="high"          # low | medium | high | xhigh | max
MAX_RUN_MINUTES=45          # hard kill if a run hangs
MAX_BUDGET_USD=""           # e.g. "5" to cap API spend per run (API-key billing only); empty = no cap
NOTIFY=1                    # 1 = macOS notifications for decisions/wins/risks

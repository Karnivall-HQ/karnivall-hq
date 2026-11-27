#!/usr/bin/env python3
"""W1/W2 day-0 snapshot: freeze the site state the day Alvian's edit lands.

Curls the 2 ad-flow pages, counts the W1/W2 gate strings in visible text and
in the raw HTML (schema JSON-LD included), saves a dated JSON snapshot, and
diffs against the previous snapshot. Prints the pass/fail of the day-0 gate in
`fab_advertising/reports/w1w2_lift_template.md` (0 x "Jakarta Pusat",
0 x "800.000" in the ad flow).

Pixel numbers (PT ViewContent / Lead) can't be pulled from a script (Meta MCP
only): pass them in so the baseline sits in the same file.

  python3 fuku/bin/w1w2_snapshot.py                       # snapshot + diff
  python3 fuku/bin/w1w2_snapshot.py --vc 1382 --lead 49 --pixel-window 11/16-11/25
  python3 fuku/bin/w1w2_snapshot.py --no-save             # check only
"""
import argparse, datetime, glob, html, json, os, re, subprocess, sys

PAGES = {
    "landing": "https://fabwarehouses.com/sewa-gudang-self-storage-jakarta/",
    "wa_form": "https://fabwarehouses.com/form-chat-fab-storage-via-whatsapp/",
}
# string -> W1/W2 gate target in VISIBLE text after the edit (None = info only)
TERMS = {
    "Jakarta Pusat": 0,        # W1
    "Jakarta Selatan": None,   # W1 replacement (should rise)
    "800.000": 0,              # W2
    "750": None,               # W2 replacement / ads price
    "Kelapa Gading": None,     # footer/schema address (not in W1/W2 scope)
    "akan launching": None,    # Kuningan FAQ (parked ask)
}
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTDIR = os.path.join(ROOT, "fab_advertising", "snapshots")


def fetch(url):
    r = subprocess.run(["curl", "-sL", "--max-time", "40", "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    return code.strip(), body


def visible(raw):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    t = re.sub(r"(?s)<[^>]+>", "\n", t)
    t = html.unescape(t)
    return [l.strip() for l in t.splitlines() if l.strip()]


def snap():
    out = {}
    for name, url in PAGES.items():
        code, raw = fetch(url)
        lines = visible(raw)
        text = "\n".join(lines)
        out[name] = {
            "url": url, "http": code, "bytes": len(raw.encode()),
            "visible_lines": len(lines),
            "visible": {k: text.count(k) for k in TERMS},
            "raw": {k: html.unescape(raw).count(k) for k in TERMS},
        }
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--vc", type=int); p.add_argument("--lead", type=int)
    p.add_argument("--pixel-window")
    p.add_argument("--no-save", action="store_true")
    a = p.parse_args()

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7)))
    s = {"taken_wib": now.strftime("%Y-%m-%d %H:%M"), "pages": snap()}
    if a.vc is not None and a.lead is not None:
        s["pixel"] = {"window": a.pixel_window, "pt_vc": a.vc, "lead": a.lead,
                      "vc_to_lead_pct_calc": round(100 * a.lead / a.vc, 2) if a.vc else None}

    prev_files = sorted(glob.glob(os.path.join(OUTDIR, "w1w2_*.json")))
    prev = json.load(open(prev_files[-1])) if prev_files else None

    ok = True
    for name, d in s["pages"].items():
        print(f"[{name}] HTTP {d['http']}  {d['bytes']:,} B  {d['visible_lines']} visible lines")
        if d["http"] != "200":
            ok = False
        for k, tgt in TERMS.items():
            v, r = d["visible"][k], d["raw"][k]
            was = ""
            if prev and name in prev["pages"]:
                pv = prev["pages"][name]["visible"].get(k)
                if pv is not None and pv != v:
                    was = f"  (was {pv} on {prev['taken_wib']})"
            gate = ""
            if tgt is not None:
                passed = v == tgt
                ok &= passed
                gate = "  PASS" if passed else f"  FAIL (gate {tgt})"
            print(f"   {k:<16} visible {v:>2}  raw {r:>2}{gate}{was}")
    if "pixel" in s:
        px = s["pixel"]
        print(f"[pixel] {px['window']}: PT VC {px['pt_vc']:,} / Lead {px['lead']} = {px['vc_to_lead_pct_calc']}% (calc)")
    print("DAY-0 GATE:", "PASS - start the d7/d14 clock tomorrow" if ok else "NOT MET - W1/W2 not (fully) live")

    if not a.no_save:
        os.makedirs(OUTDIR, exist_ok=True)
        path = os.path.join(OUTDIR, f"w1w2_{now.strftime('%Y-%m-%d_%H%M')}.json")
        json.dump(s, open(path, "w"), indent=1)
        print("saved", os.path.relpath(path, ROOT))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

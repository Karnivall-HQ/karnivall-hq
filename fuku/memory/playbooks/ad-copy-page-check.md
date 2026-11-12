# Playbook: check ad copy against the landing page before it ships
_Created 2026-11-12 15:02 WIB from 4 runs in one day (Wave 1 price wording, shoot card v2, Wave 3–4 copy, Wave 1/2 build sheets). Each run caught overclaims that number-only checks missed._

## When
Before any ad copy, sticker, WA script or site replacement text is marked "paste-ready".

## Steps (one curl, ~2 min)
1. `curl` the exact URL the ad lands on (not the homepage); strip scripts/styles/tags; count phrases with a small Python loop (`python3 -I`).
2. For each row, list every **claim** (price, size, fee, deposit, contract, pickup, timing, access, lock/security, location) and count it on the page.
3. Also count the **reason to buy** (the situation the ad opens with: apartment, renovation, online seller…). 0 hits = message-match risk → rank that ad last, don't drop it silently. **Read the context of every low hit (1–2×):** it may point the audience at a *different* product (11/12: the one "online seller" hit was Fab's e-commerce warehouse line → R5 gated, not just ranked last).
4. Classify each claim: ✔ on page · ⚠️ 0× but backed by live ad data or physical fact (keep, label INFERRED, give the swap line) · ❌ 0× and not backed → rewrite to the page's wording.
5. Watch for **implied extras** a literal check misses:
   - exclusivity/"only" words ("bayar bulan pertama aja" implies no other fee; page says only "per 1 bulan");
   - timing promises ("1 hari", "hari yang sama");
   - count words ("Kuningan & Sudirman" reads as 2 sites; page names one: ITC Kuningan Ambasador);
   - vocabulary the page doesn't use ("kode FAB750" vs the page's "Harga Promo Launching").
   - **status/tense words** on the page itself ("akan launching" = will launch): a copy line that promises a survey, a move-in or "siap dipakai" needs the thing to exist now (added 11/12 18:02, WA script check).
6. Re-read numeric facts (sizes, prices) from the page every time; never reuse them from an older audit.
7. Write a "Page check" table + "What changed and why" in the deliverable, and fix the source doc too so the old wording can't come back.

## Labels
Page counts = STATED (site). Physical or ad-data backing = INFERRED. Nothing here is confirmed by Alvian until he says so.

# Jakarta self-storage competitors on Meta: angles worth testing
_2026-11-10 16:xx WIB · cloud heartbeat · read-only (Meta Ad Library via MCP + public websites). No ads touched._

## TL;DR
- 📊 Only **2 other self-storage advertisers** show up in Meta's Ad Library for Indonesia on "self storage Jakarta" / "sewa storage barang" / "gudang penyimpanan barang": **SpaceHub** (page 144592025414238) and **Gudangku Self Storage** (page 207220429143697). Fab Seller Warehouse is by far the most visible page in these searches (most of the ~93 hits for "self storage Jakarta").
- 💸 **SpaceHub undercuts Fab on headline price: "From Rp 400k / month"** (smallest unit; ladder 400k / 500k / 1.1M / 1.6M / 2.9M) vs Fab's "dari Rp750rb". SpaceHub has a **Thamrin** site (GALEON / ex-Chubb Square, Jl. M.H. Thamrin No. 9–10), ~10 min from Fab's Kuningan/Sudirman. It also lists Benhil and Daan Mogot (Tangerang).
- 🧩 SpaceHub's weaknesses vs Fab (from its own FAQ): **security deposit required**, **online self-booking + pay first**, **you move your stuff yourself** (free trolleys only), office hours Mon–Fri 09–18 for contact, English-first site. Fab's site claims (pending Alvian's confirmation): **no deposit, no minimum rental, free pickup**.
- 👉 So Fab should **not** fight on "cheapest". It should fight on **"we pick it up, no deposit, done in 1 day"**, i.e. effort and cash-up-front, for people with home clutter (our proven winner angle, BC Image087).

## What each competitor is running (Ad Library, as of 11/10)
| Advertiser | Active ads seen | Newest start (WIB) | Visible headline / CTA | Read |
|---|---|---|---|---|
| SpaceHub | 4+ storage-ish ads live; 28 total ads incl. coworking/studio | 2026-11-10 | "Chat with us!", "Book now!", "Solusi Penyimpanan Tanpa Ribet" (10/16), "Self Storage Jakarta" (08/07) | Mixed-service page (coworking 49rb/day, studio 99rb/hr). Storage ads use WA chat + booking CTAs. Refreshing creatives ~weekly (11/05, 11/09, 11/10). |
| Gudangku Self Storage | 3 live (started 11/04 ×2, 11/09) | 2026-11-09 | No link title (likely message/WA-objective ads) | Location unknown (site not reachable from cloud). Low volume. |
| Fab Seller Warehouse | ~30+ live/recent | 2026-11-05 | "Sewa Gudang Self Storage Jakarta dari Rp750rb/bulan" ×10, "Semua Barang Ini Muat di Unit Small", "Barang Bayi Masih Bagus?", "Kamar Berantakan Jadi Rapi Dalam 1 Hari", "Upgrade Apartemen 2BR vs Sewa Gudang Fab" | Plus ≥ 8 old ads (09/2026 batch) saying **"dari Rp800.000/bulan"** that the library lists under the **ACTIVE** filter → same 750 vs 800 inconsistency as the site (W2). |

Limits: the Ad Library API returned page, headline and dates only, no body copy or images, and the snapshot pages need a Facebook login. Spend and results of competitors are not public. Treat the angle reads below as **INFERRED**.

## Angles to test (ranked; all fit the home-clutter phone-photo format that wins in our account)
1. **"Kami yang angkut. Kamu tinggal tunjuk."** (free pickup) — the one thing SpaceHub makes you do yourself. Photo: pile of boxes/suitcases at home, sticker "Dijemput GRATIS 🚚". *Needs: confirm free pickup is real + its area.*
2. **"Tanpa deposit. Tanpa kontrak minimum."** — cash-up-front objection; SpaceHub asks a deposit. Sticker on clutter photo: "Bayar bulan ini aja ✅". *Needs: confirm no deposit / no minimum.*
3. **Price-anchor vs a room, not vs a competitor:** "Rp750rb/bulan < sewa kamar tambahan" (we already run "Upgrade Apartemen 2BR vs Sewa Gudang Fab"; keep the frame, phone-photo execution). Don't print SpaceHub's 400k next to ours.
4. **"Rapi dalam 1 hari"** — speed/effort; already live as a headline, extend to the photo format.
5. Defensive: if a lead asks "kok lebih mahal dari yang 400rb?", the WA reply should compare **unit size + pickup + no deposit**, not price. Add this line to `fab_advertising/creatives/2026-11-06_wa_followup_script.md` once 750 vs 800 is settled.

## Implications for M-001
- Competition on Meta is thin (2 small advertisers), so Fab's CPL problem is **not** auction pressure from storage rivals; it's creative supply + post-click (consistent with `scale_plan.md` and the pixel funnel baseline).
- The Rp 400k headline means price-led ads ("dari Rp750rb") are a weak hook for comparison shoppers. Batch 02 copy should lead with pickup / no deposit / home-clutter, price second.
- Old "Rp800.000" ads are listed ACTIVE in the library: next readout should check in-account which of them still deliver, and fold them into the W2 consistency fix (propose-only).

## Sources
- Meta Ad Library search (MCP `ads_library_search`), country ID, terms above + page_ids 144592025414238, 207220429143697; pulled 2026-11-10 ~16:05 WIB.
- https://spacehub.id/self-storage/ (prices, locations, FAQ: deposit, 1-month standard rental, 24/7 access, free trolleys, insurance from Rp39k/month), fetched 2026-11-10.

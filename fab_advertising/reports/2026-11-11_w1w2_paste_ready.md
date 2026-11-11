# W1 + W2 paste-ready edits: `/sewa-gudang-self-storage-jakarta/` + WA form page (2026-11-11 21:02 WIB, WA page added 22:02; read-only curl)

**Who it's for:** whoever edits fabwarehouses.com (Alvian or Markus). Open the page in the WordPress editor, Ctrl+F each **Find** string, replace with **Replace**. About 10 minutes. No ad-account change.

**What the curl shows (account data, page fetched 21:02, HTTP 200):**
- "Jakarta Pusat" = **9 visible lines** (list below).
- "Rp 800.000" ×3 = **1 FAQ answer**: shown once on the page, plus twice in the FAQ schema JSON-LD that the FAQ block writes itself. Edit the block once and all 3 go away *(INFERRED: Rank Math/Yoast-style FAQ block; check after saving)*.
- "Kelapa Gading" ×2 = **1 footer address line** ("Kirana Boutique, Jl. Boulevard Raya No.1 … Kelapa Gading"). It may be the company's real office address, so **don't change it blindly** (see C below).
- Title, meta description and og tags already say "Promo Rp750.000" ✅.

Target wording: **"ITC Kuningan Ambasador, Jakarta Selatan"** (the site's own `/sewa-gudang-self-storage-di-itc-kuningan-ambasador/` page and the ads say Kuningan/Sudirman, Jakarta Selatan). Keep "area Sudirman" where it reads naturally.
⚠️ Confirm before editing: the unit really is at ITC Kuningan Ambasador (INFERRED from the site + ads).

## A. W1: location (9 edits)

| # | Find (exact visible text) | Replace with |
|---|---|---|
| 1 | `Sewa Fab Self Storage di tengah Jakarta (area Sudirman, Jakarta Pusat):` | `Sewa Fab Self Storage di tengah Jakarta (ITC Kuningan Ambasador, area Sudirman, Jakarta Selatan):` |
| 2 | `Lokasi di daerah Sudirman Jakarta Pusat.` | `Lokasi di ITC Kuningan Ambasador, area Sudirman, Jakarta Selatan.` |
| 3 | `(Sudirman Jakarta Pusat)` | `(Kuningan, Jakarta Selatan)` |
| 4–6 | `(area Sudirman, Jakarta Pusat)` (3 standalone places: 2 comparison cards + section 8; Ctrl+F shows 4 because row 1 contains it too, so do row 1 first) | `(area Kuningan–Sudirman, Jakarta Selatan)` |
| 7 | `di dalam building dengan security 1x24 jam di area Sudirman, Jakarta Pusat` | `di dalam building ITC Kuningan Ambasador dengan security 1x24 jam, Jakarta Selatan` |
| 8 | `Harga Sewa Gudang Self-storage di Fab Jakarta Pusat` (heading "8️⃣") | `Harga Sewa Gudang Self-storage di Fab Jakarta Selatan` |
| 9 | `cara sewa gudang self-storage di Fab Jakarta Pusat?` (FAQ heading) | `cara sewa gudang self-storage di Fab Jakarta Selatan?` |

Fast path: a site-wide search-replace of `Jakarta Pusat` → `Jakarta Selatan` **on this page only** covers all 9. The row texts above are the nicer version.

## B. W2: price (1 edit; assumes 750 is the real price)

| Find (FAQ answer "Berapa Harga Sewa Self-Storage di Fab?") | Replace with |
|---|---|
| `Harga Sewa Gudang Pribadi di Fab Self Storage mulai dari Rp 800.000 /bulan (sewa bisa dibayar per bulan).` | `Harga Sewa Gudang Pribadi di Fab Self Storage: Promo Rp750.000/bulan (kode FAB750), sewa bisa dibayar per bulan.` |

If **800 is the real price**, don't edit this. Then the 750 ads are the problem instead (`2026-11-10_price_copy_audit.md`).
**B2. WA form page `/form-chat-fab-storage-via-whatsapp/` (1 more edit, verified by curl 11/11 22:02 WIB).** It is the only other "800" in the ad flow; the same page already shows "Rp 750rb /bulan" twice (price table + promo heading), so today it states both prices.

| Find (Elementor heading widget `859f605`, under "Gudang Pribadi di Fab Self-Storage") | Replace with |
|---|---|
| `Sewa Gudang Self-Storage di Fab,` ⏎ **`mulai dari Rp 800.000 /bulan.`** (bold, after a line break) | `Sewa Gudang Self-Storage di Fab,` ⏎ **`Promo Rp750.000/bulan (kode FAB750).`** |

This page has 0 × "Jakarta Pusat" (no W1 work here); its "Kelapa Gading" ×4 are the same footer/schema address as section C. Its price table also lists "dari Rp 1 juta/bulan" for "Layanan lainnya" (other services); leave it.

## C. Footer address (decide, don't auto-edit)

`Kirana Boutique, Jl. Boulevard Raya No.1, UG, Kelapa Gading Timur, … 14240.`
- If this is the company/office address: keep it, but add a line above it: `Lokasi gudang: ITC Kuningan Ambasador, Jakarta Selatan`.
- If it's an old storage location: replace it with the ITC Kuningan address.

Verified 21:02: each Find string occurs on the live page exactly as listed (python count on the curled text).

## D. Check after saving (Fuku does this on the next run once "W1 W2 done" lands in INBOX)
- `curl` the page: `Jakarta Pusat` = 0, `Rp 800.000` = 0 (incl. schema), `Kelapa Gading` = 0 or footer only.
- `curl` the WA form page: `Rp 800.000` = 0, `FAB750` ≥ 1.
- Start the lift read: `fab_advertising/reports/w1w2_lift_template.md` (day-7 + day-14 vs the 3.72% VC→Lead baseline).

## E. Pre-written 11/12 07:00 re-ask (if ask #1 is still unanswered, > 48h)
> ❓ ~10 min on the site: fix the location (Jakarta Pusat → Jakarta Selatan, 9 lines) and the price (800 → 750: 1 FAQ line on the page all Fab ads land on + 1 line on the WA form page)? Paste-ready: `fab_advertising/reports/2026-11-11_w1w2_paste_ready.md`. My recommendation: yes, today. It's the only lever that can bring 7d CPL under Rp 95k by 11/20 on its own.

# Wave 1 ad copy vs site price wording (2026-11-12 10:02 WIB, cloud heartbeat groundwork)
_Read-only. Live curl of `/sewa-gudang-self-storage-jakarta/` and `/form-chat-fab-storage-via-whatsapp/` (both HTTP 200, 10:02). No ad-account or site change._

## Question
When W2 lands and Wave 1 launches, will the ad and the page it lands on say the same price in the same words on day 1?

## What the live pages say (account data: curl, visible text, scripts stripped)
| Phrase | Landing page | WA form page |
|---|---|---|
| "FAB750" | **0** | **0** |
| "Promo …" (mostly "Harga Promo Launching: Rp750.000 / Rp 750rb /bulan") | 12 | 3 |
| "mulai dari Rp 750rb" (comparison table) | 1 | 1 |
| "Rp 800.000" (W2 targets) | 1 (FAQ) | 1 (heading `859f605`) |
| "Jakarta Pusat" (W1 targets) | 9 | 0 |

## Findings
1. ✅ **Number:** every Wave 1 ad (S1, B1, B2) and fallback (S6, S2) says 750rb on the sticker, body and headline. Matches the site's 750 everywhere except the 2 W2 lines.
2. ⚠️ **Word mismatch (fixed in the drafts):** the ads said "kode FAB750"; the site never mentions a code, it calls 750 a **"Harga Promo Launching"**. My 11/11 W2 replacement text *added* "(kode FAB750)" to the site, i.e. a new claim on the site that no other line backs up.
   - **W2/B2 replacements** (`2026-11-11_w1w2_paste_ready.md`) now use the site's own phrase: "Harga Promo Launching Rp750.000/bulan". Same 2 edits, no new claim. Post-save check updated.
   - **Wave 1 body price line** (A1/S1, A2/S2, A6/S6 in batch 01; B1, B2 in batch 02) now reads `💰 Harga promo launching Rp750rb/bulan (kode FAB750 via WhatsApp).` It bridges both: the site's word ("promo launching") plus the code the live PEIKIRA ads already use (Ad015 copy unchanged). Stickers and headlines unchanged ("mulai 750rb/bulan", "Mulai Rp750rb").
3. ✅ **Location:** ads say "Kuningan & Sudirman, Jakarta Selatan"; W1 replacements say "ITC Kuningan Ambasador, area Sudirman, Jakarta Selatan". Consistent. Until W1 lands, the page still says "Jakarta Pusat" ×9 (the known W1 gap).
4. ⚠️ **Open (folded into ask #2, no new ask):** does the WA team actually honour "FAB750"? If 750 is simply the launch price for everyone, the code is harmless but unnecessary. If the team doesn't recognise it, drop "(kode FAB750 via WhatsApp)" from the Wave 1 lines. If **800 is real**, swap the number on the sticker + the body line + the headline (3 places per ad), and skip W2.

## Labels
- Account data: the curl counts above; the live ad copy ("FAB750" in all PEIKIRA ads, `2026-11-10_price_copy_audit.md`).
- INFERRED: that matching the site's own wording reduces post-click doubt (same logic as the W1/W2 fix; not measured).

# Second form `/form-chat-whatsapp/`: is it a missed Lead path? (2026-11-11 18:03 WIB, cloud, read-only curl)

**Answer: no.** It's a different product. `/form-chat-whatsapp/` (post 3764) holds **Fluent Form #8** for **Gudang + Coworking Space for online sellers** (prices shown: Rp 5jt/bulan, Rp 30 juta, Rp 130 juta), not the self-storage offer. None of the self-storage pages link to it. Its page fires PageView + automatic events only (`triggerEvents: []`, no Lead). The M-001 Lead path (Form #10 → `/thank-you-self-storage-lead/`) stays the only Lead path. Nothing is missed.

## Evidence (site HTML)
Form #8 fields: Nama · No. WhatsApp · "Apakah Anda memiliki Toko Online di Shopee/Tokopedia/Lazada?" (Ada / Tidak ada) · Kebutuhan (Mau sewa Gudang + Coworking Space di Fab / Mau Download PDF Proposal / Mau tanya-tanya dulu via WA).

Links across the 13 sitemap pages (count of hrefs):

| Page | → `/form-chat-whatsapp/` (Form #8) | → `/form-chat-fab-storage-via-whatsapp/` (Form #10) |
|---|---|---|
| `/` (homepage) | 6 | 0 |
| `/about-us/` | 3 | 0 |
| `/sewa-gudang-fab-warehouse-kelapa-gading/` | 6 | 0 |
| `/sewa-gudang-self-storage-jakarta/` (ViewContent page, likely the ad landing page, INFERRED) | 0 | 6 |
| `/gudang-self-storage-jkt/` | 0 | 6 |
| `/sewa-gudang-self-storage-di-itc-kuningan-ambasador/` | 0 | 5 |
| `/sewa-gudang-self-storage-di-kelapa-gading/` | 0 | 6 |
| `/link/` | 0 | 2 |

No Form #8 thank-you page is in the sitemap, and guessed slugs (`thank-you-gudang(-lead)`, `terima-kasih-gudang`, `thank-you-warehouse-lead`) return 404. Its confirmation is server side (likely straight to WA, INFERRED).

## So what (for M-001)
1. **The self-storage funnel is clean.** Every self-storage page sends people only to Form #10, so no Lead path is missing.
2. **⚠️ Small risk (INFERRED):** the homepage sends all its form traffic to the **warehouse/coworking** form. If any Fab ad lands on the homepage (the 11/11 pixel URL split showed root only), self-storage clickers would see a Rp 5jt/bulan product. I can't read ad destination URLs (the creative API returns no `link_url`), so this is unconfirmed. Alvian/Markus can check it in seconds in Ads Manager. Folded into the parked W1/W2 note; no new ask.
3. **W1 note:** `/sewa-gudang-fab-warehouse-kelapa-gading/` is the warehouse product page, so its Kelapa Gading address is correct there. W1 only covers the 3 Jakarta **self-storage** pages.

# Fab landing page + lead-flow audit (playbook E4 / R7)
_2026-11-06 07:01 WIB · cloud heartbeat · read-only (curl of public pages + Meta pixel stats via Rudi MCP). Nothing on the site was changed or submitted._

Labels: **[data]** = pixel/site data · **[calc]** = Fuku's arithmetic · **[INFERRED]** = reasoning, not proven.

## TL;DR
1. **~4% of landing-page visitors become a Lead** [calc]. 7d pixel: ViewContent 1,577 → Form 101 → Lead 61 (browser + server events combined). LP→Lead ≈ 3.9%; Form→Lead ≈ 60%.
2. **The ad pages contradict themselves on location.** Ads say *Jakarta Selatan (Kuningan & Sudirman)*. The pages also say *"Berlokasi di Kelapa Gading, tepat di sebelah Mall of Indonesia"* and *"area Sudirman, Jakarta Pusat"*. That's leftover copy from the Kelapa Gading page. A Jakarta Selatan prospect reading "Kelapa Gading" may bounce.
3. **Price is inconsistent across the flow.** Ads: Rp750rb (FAB750). Landing page: promo Rp750.000. **The form page (the last step before WA) says "mulai dari Rp 800.000/bulan"**, and the homepage says Rp800rb.
4. **~40% of Form events don't turn into a Lead** (101 vs 61) [data]. Either people abandon after submitting or Lead only fires for some form answers. It's worth knowing which.
5. **Tracking is healthy**: browser pixel + server events (Lead arrives in ~1:1 BROWSER/SERVER pairs, so it's likely deduplicated), Lead Event Match Quality 7.8/10 with phone + name 100% coverage [data]. Not the bottleneck.
6. **Facts the site already states** (answering part of the open "3 facts" ask, so please confirm): **no minimum rental period** ("tanpa minimal lama sewa", "Tidak ada Kontrak Minimal Sewa"), pay monthly, **no deposit**, **free pickup**, weekend loading allowed. Unit sizes: Small 4.75 m³, Medium 9.5 m³, Large 19 m³.

## Pages checked (all HTTP 200, ~1.3–1.9 s server response from the cloud)
| Page | Pixel (PixelYourSite Pro, id 405755485775053) | Price shown | Location shown |
|---|---|---|---|
| `/` (homepage) | **none in HTML** | Rp800rb; Seller Warehouse Rp5jt | general |
| `/sewa-gudang-self-storage-jakarta/` (only page that fires ViewContent, likely the ad landing page [INFERRED]) | ✅ PageView + ViewContent | Promo Rp750.000 | "Sudirman, Jakarta **Selatan**" in the header **and** "Sudirman, Jakarta **Pusat**" lower down |
| `/sewa-gudang-self-storage-di-itc-kuningan-ambasador/` | ✅ PageView | Promo Rp750.000 (+ Rp800.000 shown) | ITC Kuningan, Jakarta Selatan **and** "Berlokasi di Kelapa Gading, tepat di sebelah Mall of Indonesia" (feature #5) |
| `/gudang-self-storage-jkt/` | ✅ PageView | Promo Rp750.000 | "ITC Kuningan Ambasador" **and** "Sewa Fab Self-storage di Kelapa Gading … sebelah Mall of Indonesia" |
| `/form-chat-fab-storage-via-whatsapp/` (the WA form) | ✅ PageView; Fluent Form #10 | **"mulai dari Rp 800.000/bulan"** + "Rp 750rb" in the comparison table | n/a |

The landing page links 6× to the WA form page. The form asks for **5 inputs**: name, WhatsApp number, "Untuk merapikan ruangan dimana?", "Kebutuhan", and "Pernah chat WA ke Fab sebelumnya?". Then it opens WhatsApp.

## Funnel, 7 days (2026-10-30 → 11-05, pixel 405755485775053)
| Step | Events (browser + server) | ≈ unique [INFERRED ÷2] | Step rate [calc] |
|---|---|---|---|
| ViewContent (landing page) | 1,577 | ~790 | n/a |
| Form (form submitted) | 101 | ~50 | 6.4% of LP views |
| Lead | 61 | ~30 | 60% of forms · **3.9% of LP views** |
| Ads Manager website leads (default attribution) | n/a | 20 | ~2/3 of pixel leads credited to ads |

Caveat: the pixel's URL breakdown strips paths (everything shows as `fabwarehouses.com/`), so I can't split by page. "÷2" assumes every event is sent once by the browser and once by the server, as the Lead source breakdown shows.

## Why it matters for M-001 (R7, INFERRED)
Meta prices delivery partly on predicted conversion rate. At a fixed click cost, raising LP→Lead from ~3.9% to ~5% cuts CPL by ~22% [calc: 3.9/5]. With 7d CPL Rp 125k, that's ~Rp 98k. Post-click fixes are free and don't touch the ad account, so they don't disturb the 11/10 PEIKIRA2 read.

## Proposed website changes (Alvian or the site owner applies them; Fuku doesn't edit the live site)
- **W1 · Location: one truth.** On `/sewa-gudang-self-storage-jakarta/`, `/sewa-gudang-self-storage-di-itc-kuningan-ambasador/` and `/gudang-self-storage-jkt/`, replace every "Kelapa Gading / sebelah Mall of Indonesia" line and "Jakarta Pusat" with **"ITC Kuningan Ambasador, Sudirman, Jakarta Selatan"**. 10 min. Lowest risk, clearest win.
- **W2 · Price: one number.** On `/form-chat-fab-storage-via-whatsapp/`, change "mulai dari Rp 800.000/bulan" to **"Promo Rp750.000/bulan (kode FAB750)"**, matching the ad. (This depends on the open 750 vs 800 question. If 800 is the real price, change the ads instead.)
- **W3 · Shorter form.** Drop "Pernah chat WA ke Fab sebelumnya?" (an internal question that adds friction). Keep name, WhatsApp, and Kebutuhan. Measure Form/ViewContent for 7 days before and after. [INFERRED: fewer fields → more submits; test it, don't assume.]
- **W4 · Find out why 40% of Forms aren't Leads.** Who set up the Lead event (Markus? a plugin rule?) and what triggers it? If Lead only fires on the WA redirect, people who submit but don't open WA are lost. Those are phone numbers Fab could still call back from Fluent Form entries.

## Not done / limits
- I didn't submit the form (that would create a fake lead in Fab's inbox).
- I couldn't read the exact ad destination URL (the creative API returns no `link_url` for these ads). The ViewContent page is my best inference.
- Page speed wasn't measured with a real browser (Lighthouse); server response is fine (~1.5 s for 150–290 KB HTML).

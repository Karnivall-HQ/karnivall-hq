# Karnivall Agentic Company

## What we do
- **Fab = Fab Self-storage** ("Fab Warehouses", `fabwarehouses.com`): private self-storage units (gudang) in Jakarta Selatan, Kuningan & Sudirman. Ads price it from Rp750rb/month with code FAB750 via WhatsApp (older ads: Rp800rb). Leads = website pixel leads → WhatsApp. (Source: live ad creatives, 2026-11-05.)
- Other businesses: still unknown (see OUTBOX [FYI]).

## Projects / workspaces
- `fab_advertising/`: advertising work (research, ad creatives, SOPs, context, references, reports). Purpose to be confirmed.

## Meta ad footprint (2026-11-05)
- 36 ad accounts across businesses: Karnivall (Incess Ads, Kari Ads, Venue, Rental), Incess Dress, Travell Fi (TF, FeverAlert, Uniso, Roketso, Giantso, Bikeso, Kitchenso, Babyso), The North Case Indonesia (Warehouse Storage, Sumobaby, Sumo2), GudangHub (Ghub, OMO, OMOrental, OMO AlatBerat), Jinhe Korean BBQ (Jinhe, DapurHub accounts, Kemitraan), Alvian Lim's Business.
- **"Fab ad account" = Meta "Warehouse Storage" `484578521394893`** (Alvian's name for it, 2026-11-05). This is what `fab_advertising/` is about.
- Active spenders: Incess Ads `2017038114993984` (campaign "OMO ADVLeads", website leads) and Warehouse Storage `484578521394893` (lead-gen; ad names PEIKIRA/AKIRA/KENJI-FAB-…, likely the fab_advertising workflow).
- Fab account structure (2026-11-05): PEIKIRA-BID-CAP-LEADS-CAMPAIGN (Highest volume, Rp 300k/day, 1 ad set) + BC CBObass005 OriAud45rb – Copy (CBO Rp 5M/day, bid cap Rp 94,250, ~50 ad sets, targeting JKT city). RUDI Costcap campaign paused. Optimizes website leads (pixel). **Markus Reynaldo is on Alvian's team** (confirmed 2026-11-05) and edits this account (cut PEIKIRA 5M→300k on 2026-10-26). Changes by Markus are team changes; log them in the tracker, don't flag them as a risk. Markus also launches ads via the "Rudi MCP" app (actor id 61594758338050), e.g. ad set AKIRA-FAB-20261031-WAVE-PEIKIRA2 on 2026-11-05 14:40 WIB.
- Incess "OMO ADVLeads" (`120233576079370222`) is a bid-cap campaign: Rp 5.95M/day budget but ~Rp 585k/day spend, CPL Rp 35k (7d to 2026-11-04).
- Disabled by Meta: Alv Ads, WooCore Ads, For App in Audience Network Ads, Babyso Rp.
- Unknown: which businesses are ours vs clients; what a lead is worth.

## Assets & tools available
- Claude Code with subagents, web search, and browser automation
- Meta Ads tooling (via the Rudi MCP connector: campaigns, creatives, insights, catalogs)
- Other connectors (Gmail, Calendar, Drive, Notion, Slack, ...) only after Alvian authorizes them on claude.ai

## Key numbers
- 2026-11-05 Meta, last 30d: Incess Ads Rp 21.8M → 633 leads @ Rp 34k (campaign OMO ADVLeads). Warehouse Storage Rp 12.3M → 93 leads @ ~Rp 133k. All other accounts Rp 0. Full scan: `fab_advertising/reports/2026-11-05_meta_account_scan.md`

## Fab website & tracking (2026-11-06 audit)
- fabwarehouses.com = WordPress 6.1 + PixelYourSite Pro + Fluent Forms. Pixel/dataset **405755485775053**, browser + server events, Lead EMQ 7.8.
- Flow: self-storage LP (`/sewa-gudang-self-storage-jakarta/`, promo Rp750k) → WA form page (`/form-chat-fab-storage-via-whatsapp/`, 5 fields) → WhatsApp 0899 0332 050.
- The site states: no minimum rental, monthly payment, no deposit, free pickup, weekend loading. Units (ad landing page `/sewa-gudang-self-storage-jakarta/`, 11/12): Small 1.9×1×2 m = 3.8 m³ (fits kulkas, lemari, sepeda, rak, kardus), Medium 7.6 m³ (+ kasur, sofa/piano), Large 15.2 m³. The 11/06 audit said 4.75/9.5/19; which unit the Rp750rb price buys is not stated. Also: Fab Seller Warehouse (warehouse + coworking for Shopee sellers) from Rp5jt/month; a Kelapa Gading location exists (Kirana Boutique, next to MOI).

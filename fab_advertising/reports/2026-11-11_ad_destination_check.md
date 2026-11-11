# Where do the Fab ads land? (2026-11-11 19:02 WIB, cloud, read-only)

**Answer: on `/sewa-gudang-self-storage-jakarta/`. No checked ad lands on the homepage.** That closes the 18:03 risk (homepage → Form #8, the Rp 5jt warehouse product).

## Method (new, works when `link_url` is empty)
The creative API returns no `link_url` for asset-feed / dual-format creatives. But `ads_get_ad_preview` gives a `preview_url` (business.facebook.com/ads/api/preview_iframe.php). Curl it and grep `l.php?u=`: the destination URL is in the page JSON (`navigation.link_url`).

## Result: 13 active ads = Rp 1,430,177 of Rp 1,625,846 7d spend on active ads = **88.0%** *(calc)*

| Ad | 7d spend (Rp) | Destination |
|---|---:|---|
| AKIRA-FAB-20261016-Ad015 | 989,546 | `/sewa-gudang-self-storage-jakarta?ad={{ad.name}}` |
| BC Image087 Post | 98,776 | `/sewa-gudang-self-storage-jakarta/` |
| AKIRA-FAB-20261103-009 | 95,023 | same |
| AKIRA-FAB-20261103-013 | 69,035 | same |
| ImageAd 201D | 29,174 | same |
| GUNPEI-FAB-20261031-ARG-04 | 26,913 | same |
| AKIRA-FAB-20261031-003 | 24,959 | same |
| KENJI-FAB-20261019-020 · v03 | 22,660 | `/sewa-gudang-self-storage-jakarta?ad=KENJI-FAB-20261019-020 · v03` |
| GUNPEI-FAB-20261031-ARG-01 | 21,927 | same page |
| BC Image101 / 095 / 093 / 096 Post | 52,164 | same page (creative `link_url`) |

The remaining 12% is ~80 small ads (most < Rp 10k/7d); not checked.

## So what
1. **Homepage risk closed** (for 88% of spend). The Form #8 path doesn't touch ad traffic.
2. **W1 shrinks to ONE page.** All checked ad traffic lands on `/sewa-gudang-self-storage-jakarta/`. Re-curled now: it still has **"Jakarta Pusat" ×9, "Kelapa Gading" ×2, and "Rp 800.000 /bulan" ×3** next to the 750rb promo lines. Fixing this one page covers ~all ad traffic; the other 2 Jakarta pages are optional.
3. Every ad page links only to Form #10 (6 links), so the Lead path is as mapped at 17:02.

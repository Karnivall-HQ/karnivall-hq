# Playbook: finding what works and building new Meta ad rows
_Created Retro #5 (2026-11-21) from 3 lessons of 11/20. First sheet built this way: `fab_advertising/creatives/2026-11-20_bc_wave0_markus_sheet.md`._

## When to use
Before any creative brief, "more of what works" ask, refresh row, or Markus build sheet.

## A. Find what actually works
1. **List the carrying ad per ad set.** Ad sets usually run on one ad (others ≈ Rp 0); the ad-set name ("Manny", "UGC", "Anak Tele") says little. Pull `ads_get_ad_entities` at ad level, 8 weekly rows.
2. **Look at the image + overlay text** of each carrying ad (`ads_get_creatives` → image URL, preview textData). Group by **angle** (real facility, home clutter, staged scene…), not by ad-set name: two "concepts" can be the same angle (11/20: real-facility photos 54.0k vs clutter scenes 66.7k *(calc)*).
3. **Judge CTR and CPL separately.** The best-CTR ad can have the worst CPL (11/20: staged parents scene breaking R11). CTR picks hooks; CPL picks what to scale.
4. **Existing hashes first.** Before blocking on new photos, pull the image hashes of the best live ads and build from them. Ask for a shoot only for an angle no existing image covers (11/20: N2 buildable with 0 new assets after a week read as "blocked on a shoot").

## B. Build rows
1. **One comparison parent per row**: everything except the tested element matches it (placements, CTA, IG account, destination URL).
2. **Advantage+ enhancements = the parent's.** Turn them off only for a card-order or format test, and write why in the row.
3. **Copy is paste-ready only after `ad-copy-page-check.md`**, re-run if the sheet is > 3 days old.
4. **Read rules before launch** per `meta-tests-and-proposals.md` §A (kill as spend multiple, comparative rule, readability floor, probe sized to its floor).
5. **Under a bid cap, each new angle needs its own ad set** (a new ad inside a capped/dominated ad set starves); check against `meta-modelling-and-planning.md` C4.

## Quality bar
Each row names: parent ad + its image hash, angle, the one tested element, Adv+ setting, page-check status, read rules.

## Last validated
2026-11-20 · M-001 BC Wave 0 (N2) + §2c–§2e rows, Waves 2–6 BC rows.

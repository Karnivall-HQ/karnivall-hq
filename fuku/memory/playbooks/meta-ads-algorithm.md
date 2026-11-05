# Playbook: how Meta's ads algorithm works, and what to do about it

_Fuku's working rulebook. Read this before any Meta ads analysis or proposal._
_Built 2026-11-05 from 17 Meta engineering/research docs (2023–2026) in `fuku/knowledge/meta-ads/sources/`; notes with quotes are in `fuku/knowledge/meta-ads/notes/A|B|C_*.md`._

**Evidence labels**
- **[STATED]** Meta says it in the docs.
- **[INFERRED]** our reasoning from how the system works.
- **[FOLKLORE]** common practice the docs don't cover.

**Fab check**
- ✅ Fab data agrees.
- ⚠️ Fab data conflicts.
- ❓ not tested in Fab yet.

---

## 1. The machine in one picture
```
Your targeting = hard filter → RETRIEVAL (Andromeda) → RANKING (GEM / Lattice / sequence models) → AUCTION → impression
                               tens of millions → few thousand     → top few, priced with predicted CVR
```
- **Targeting is enforced as a hard filter ("index matching") before the model scores ads.** [STATED, Andromeda 2026] A narrow audience removes chances before the smart part sees them.
- **Retrieval scores every eligible ad per person**, using event sequences, LLM-based semantic features and cross-surface co-engagement. [STATED]
- **Ranking reads the ad itself**: its text, image and landing page are turned into features by multimodal models. [STATED, GEM / LLaTTE / Lattice]
- **People are modelled from thousands of past actions** (ads and organic, across FB, IG and Reels), refreshed within hours. [STATED]
- **One shared model learns across surfaces and objectives**, with lead gen as its own objective. Conversions are treated as "sparse, delayed" signals, and learning from clicks transfers into them. [STATED, Lattice / GEM]
- **New ads aren't fully cold.** Meta describes each ad by what it's about (semantic tokens, not just an ID), so a new ad inherits learning from similar ads and past campaigns. [STATED, GenRecs 2026]
- **Training is continuous and online.** No timescale is given. [STATED]

## 2. Rules

| # | Rule | Evidence | Fab |
|---|---|---|---|
| R1 | **Creative is the targeting.** Meta says the "focus has shifted from niche targeting to creative diversification as the best lever to find the most relevant audiences." | STATED | ✅ All Fab ad sets have the *same* broad Jakarta targeting, yet CPL ranges from Rp 18k to 372k. The creative made the difference. |
| R2 | **Diversify by concept, not by variation.** Use different themes, messages and visuals (pain, price, security, size, life event). Five crops of one image add little. | STATED (diversity); INFERRED (variations add little) | ❓ BC has ~70 ad sets, mostly variants of the same few ideas. |
| R3 | **Make the ad say clearly what it is.** The model reads text and image semantically, e.g. "Gudang self-storage, Jakarta Selatan, dari 750rb/bulan". | STATED (model reads content); INFERRED (copy advice) | ✅ Every winner states the product, place and price on the image. |
| R4 | **Go broad and let the model find people.** Narrow targeting filters people out before the model can judge them. | INFERRED (strong) | ✅ Fab is already broad, so there's no change needed. |
| R5 | **Consolidate.** Fewer ad sets with more data each, since the model pools learning. Don't fragment a small budget. | INFERRED | ⚠️ BC: ~70 ad sets + bid caps → spends ~1.4% of its budget. |
| R6 | **Optimize for the deepest event that still has volume, and send every conversion back, including late ones.** Meta serves predictions from its longest attribution window. | INFERRED (strong) | ✅ Optimizing for website leads. ❓ No closed-deal / offline-conversion signal yet. This is the next big lever. |
| R7 | **Raise the real conversion rate after the click** (landing page, WhatsApp flow, offer). Predicted CVR feeds auction pricing, so a better CVR means cheaper delivery. | INFERRED (medium) | ❓ Not audited yet (fabwarehouses.com, the WA FAB750 flow). |
| R8 | **Refreshing creative is cheap. Don't fear "resetting learning".** New ads inherit learning from similar ones, so keep new concepts close in meaning to proven winners. | STATED (inheritance); INFERRED (advice) | ❓ |
| R9 | **Judge on weekly windows, never single days.** Meta's own delivery varies with spare compute, and at ~3 leads/day, daily CPL is noise. | INFERRED | ✅ Matches the M-001 7-day CPL rule. |
| R10 | **Placements: default to automatic, but cut placements the data proves broken.** The model learns across surfaces, so splitting can cost signal. | INFERRED | ⚠️ Fab data shows real waste: WhatsApp Status (frequency 789), Threads, and IG Stories in PEIKIRA. **Account data beats the general rule**: exclude what is proven broken, keep the rest automatic. |
| R11 | **Advantage+ creative / GenAI: use the enhancements, not AI-made scenes.** Meta reports +11% CTR and +7.6% CVR averages, from sales/catalog contexts. | STATED (averages) | ⚠️ In Fab, polished AI-looking renders lose 3–10× to real phone photos. Test GenAI *enhancements* on real photos; never replace real photos. |
| R12 | **Platform lift numbers are averages, not promises.** Examples: GEM +18.9% conversions, Lattice +6%, Andromeda +2.4% FB. Several are "selected segments" or cumulative. | STATED | Never quote them as an expected result for a client. |

## 2b. Prospecting vs remarketing: what the docs say
- **No doc discusses remarketing/retargeting, custom audiences or lookalikes as campaign types.** Not addressed.
- **Remarketing is built into every ad set's ranking.** Every ranking decision uses each person's own history of ad views, clicks and **conversions** (plus organic activity), across surfaces, refreshed within hours. [STATED: Sequence learning, GEM, LLaTTE] So someone who already engaged with Fab is scored higher in *any* broad ad set, with no separate remarketing ad set needed for Meta to reach warm people. [INFERRED]
- **The prospecting lever is creative.** Diverse creative "even finding new audiences they might not have realized would be interested in their product." [STATED: Creative Advantage]
- **Last-click attribution isn't discussed.** The models train on several conversion windows and serve the longest one. [STATED: Lattice/LLaTTE] How Ads Manager credits a lead to one ad is not addressed.
- → For Fab, a warm/cold split is still a valid **account test** (different message per stage, cleaner measurement), but not because the algorithm needs it. Judge by blended account CPL. (E5)

## 3. What the docs do *not* cover, so Fab data and tests decide
Learning phase / the "50 conversions" rule · bid caps & cost caps · the auction formula · attribution *settings* · retargeting vs prospecting · CBO vs ABO · budget-change speed · creative fatigue · frequency caps · lead forms vs website · dayparting · CAPI by name.

For these, treat any rule as **[FOLKLORE]** until our own account proves it. Observed so far:
- **Bid caps under ~Rp 94k starve delivery in Fab** (BC spends ~1.4% of its budget). ✅ Account data.
- **No remarketing layer exists in Fab.** A warm/cold split is untested. ❓ See `fab_advertising/reports/2026-11-05_funnel_hypothesis.md`.

## 4. Checklist before any Meta proposal
1. Is the creative **distinct, clear and real** (R1–R3, R11)?
2. Is the structure **consolidated and broad**, with bids not choking delivery (R4, R5)?
3. Is the **right event** optimized, and are all conversions fed back (R6)?
4. Is there a **post-click CVR** problem (R7)?
5. Am I judging on **≥ 7 days**, with each claim labelled STATED / INFERRED / account data (R9, R12)?
6. Is any placement **proven broken** in this account (R10)?

## 5. Open experiments for Fab (each is a proposal; Alvian applies)
- E1 · Real-photo concept batch (C1–C6) vs current → R1, R2, R11
- E2 · One consolidated BC ad set, no bid cap, the winners only → R5
- E3 · Send closed deals back to Meta as an offline/CRM conversion → R6
- E4 · Landing page + WhatsApp flow audit → R7
- E5 · Warm (site visitors/engagers, price creative) vs cold (broad excl. warm, pain/Reels creative), judged on blended CPL → §2b

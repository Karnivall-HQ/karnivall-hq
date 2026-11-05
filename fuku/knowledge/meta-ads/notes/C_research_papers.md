# C. Meta research papers: Wukong, LLaTTE, Lattice

Sources: the three plain-text extracts in `../sources/` only. Some table layouts in the extracts are garbled; numbers marked (layout garbled) should be read with care.

---

## 1. Per paper

### Wukong: Towards a Scaling Law for Large-Scale Recommendation
**2024 (arXiv Mar 2024) · Meta Platforms, Inc.**
Ranking models had not shown LLM-style "scaling laws": making them bigger mostly meant making embedding tables bigger, which stopped improving quality and used hardware poorly. Wukong replaces the interaction part of the model with stacked factorization machines, so each extra layer captures higher-order combinations of features ("dense scaling"). On an internal dataset (146B examples, 720 features, click and conversion tasks) quality kept improving across two orders of magnitude of compute: about 0.4% better log-loss for a 200x complexity increase, roughly 0.1% per 4x. The best baseline (DCNv2) needed about 40x more compute to match it. The paper does not claim a production deployment. It suggests distilling large models into small ones for serving.

### LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation
**2026 (arXiv Jan 2026) · AI at Meta**
The paper asks whether transformer models of a user's action history (ads viewed, conversions, and so on) scale predictably, and how to use big ones within millisecond latency limits. It finds that quality improves log-linearly with compute, and that sequence length (how far back in history the model looks) gives the most gain per unit of compute. Semantic content embeddings, from fine-tuned LLaMA and content-understanding models, "bend the curve": without them, extra depth mostly memorizes IDs. In production a large asynchronous upstream user model (>45x the sequence FLOPs of the online ranker) refreshes a user embedding when high-value events happen, mainly conversions. The online ranker reads that embedding alongside a short history (about 400 events per source). Upstream gains transfer about 50% to the online ranker. Deployed as "the largest user model at Meta", it gave a 0.25% NE reduction and a 4.3% conversion uplift on Facebook Feed and Reels.

### Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations
**2025 (arXiv Dec 2025) · Meta AI**
Meta ran thousands of "portfolios" (domain × objective pairs), each with its own model and dataset. That fragmented data, left small domains short of data, and was too costly to scale. Lattice merges related portfolios into a few large multi-domain, multi-objective models. **Partitioner** groups domains with overlapping users and items, and separates fast, dense signals (clicks) from delayed, sparse ones (purchases, conversions). **Zipper** mixes attribution windows into one dataset and serves only the longest-window head. **Filter** picks about 2K features out of 12K. **Networks** handle sparse, dense and sequence inputs together. **KTAP** passes precomputed teacher embeddings, valid for a few hours, to small serving models. In production it delivered +10% top-line revenue metrics, +11.5% ads quality/user satisfaction, up to +6% conversions, and 20% capacity savings.

---

## 2. Key facts

**Shared models: objectives, surfaces, conversion types**
- Lattice: portfolios were previously siloed. Quote: "Modern recommenders operate across thousands of domain-objective pairs (called portfolios), each traditionally requiring a dedicated model".
- Lattice: one model call now covers many portfolios. Quote: "a single invocation on Lattice models can simultaneously generate predictions for multiple portfolios."
- Lattice: one test model predicted about 10 objectives, with lead gen reported separately. Quote: "We predict O(10) objectives among click (CTR), conversion (CONV), and ads quality (QLT) types." The reported conversion types were "lead generation (LG) and post engagements (PE)". The LG column reads about 1% relative loss improvement over Wukong (layout garbled).
- Lattice: two surfaces whose separate CTR models had 1.33T and 0.71T parameters were merged. With the auxiliary loss, both improved (+0.13% and +0.46%) at 1.5x lower FLOPs. Without it, surface A regressed by 0.15%.
- Lattice deployment ablation, share of top-line gain: Partitioner 36%, Networks 23%, KTAP 17%, Filter 13%, Zipper 11%.

**Cross-domain learning**
- Lattice: grouping is by audience overlap. Quote: "Merges domains with substantial user/item overlap (e.g., combining "News Ads" and "Video Ads" which share users".
- Lattice: helps domains with little data. Quote: the loss keeps models from "becoming overconfident in domains with abundant data while remaining underconfident in data-sparse domains".

**Sparse or delayed conversions and attribution windows**
- Lattice: conversions arrive late. Quote: "User conversions (e.g., purchases) can occur anywhere from minutes to days after an ad impression."
- Lattice, on the trade-off. Quote: "shorter windows provide fresher training data but miss delayed conversions, while longer windows capture more conversions but introduce staleness."
- Lattice, Zipper method. Quote: each impression is randomly assigned "to one attribution window". Then: "At serving time, we use only the oracle prediction head". The oracle head is the longest window.
- Lattice: tested with 90-minute and 1-day windows, plus "additional gain on the 7d head when consolidating 90min/1d/7d combination."
- Lattice: sparse signals are grouped apart from dense ones. Quote: "Separates (1) fresh, dense feedback tasks (click, like, follow) from (2) delayed, sparse feedback tasks (purchase, conversion)."
- Lattice: real data is "sparse due to rare positive signals, and dynamic with shifting user behaviors".

**Freshness**
- Lattice KTAP: teacher embeddings expire after a short time-to-live (TTL). Quote: "checking TTL validity (typically a few hours) to ensure freshness". Reason given: "user preferences typically remain consistent within a few hours". In tests, the TTL was 6 hours and the cache hit rate was 0.6. That gave a 0.24% gain, against 0.12% for standard distillation.
- LLaTTE: the user embedding refreshes on events. Quote: "they are triggered on high-value user events (primarily user conversions)."
- LLaTTE: the online ranker "captures fresh user intent signals and leverages ad-specific interactions".

**User sequence length and composition**
- LLaTTE. Quote: "Sequence Length: This dimension exhibits the steepest scaling slope." The slope is α = 0.265, against 0.200 for depth and 0.133 for width.
- LLaTTE: experiments used sequences of "500 to 5000 actions". Online: "per-source horizon capped at T ≈ 400".
- LLaTTE: what goes into the history matters. Quote: "The balanced mixture of views and conversions performs best; both extremes are clearly suboptimal." Conversion-only histories are "temporally sparse".
- LLaTTE: the model still attends to older history. Quote: "mid- and long-range history contributes meaningfully to predictions."
- LLaTTE: daily rhythm. Quote: "attention weight spikes occur at sharp 24-hour intervals."

**Which features matter most**
- LLaTTE. Quote: "strong semantic content features are not a marginal add-on but a prerequisite for effective scaling." Content embeddings come from "fine-tuned LLaMA models" and multimodal models working on "text and images".
- LLaTTE: without content features, extra capacity "is largely spent memorizing ID patterns".
- LLaTTE: ad-side inputs include "creative attributes, landing page, advertiser metadata". Each action in a user's history records a "surface type".
- LLaTTE: predictions are used for pricing as well as ranking. Quote: "calibrated probabilities are utilized for both downstream ranking and auction pricing."
- Lattice. Quote: "tens of thousands of features characterizing users and items are available, resource constraints limit models to using only selective features (typically thousands)."

**Scale and significance**
- LLaTTE: "a reduction in NE of 0.02% is considered statistically significant". It describes the 4.3% uplift as worth "hundreds of millions of dollars in annual revenue."
- Wukong: "a 0.1% improvement for every quadrupling of complexity"; the best baseline (DCNv2) "demands a 40-fold increase in complexity to match Wukong's quality."

**New advertisers / cold start:** none of the three papers mentions new advertisers or ad-level cold start. The closest is Lattice's general point about "data scarcity in specialized domains".

---

## 3. Advertiser implications (for Fab)

None of these papers gives advice to advertisers. Every item below is **[INFERRED]** from how the system works, and is labelled with how strong the inference is.

1. **[INFERRED, strong]** Conversion volume is sparse and delayed. Fab gets about 3 leads/day (Rp 350k ÷ Rp 113k). Meta's system handles this kind of signal with separate, long-window heads. Make sure every lead is reported back to Meta as a conversion, including leads that arrive late. Missing late conversions starve the "oracle" head that is used at serving time.
2. **[INFERRED, strong]** Lead gen is a first-class objective, modeled next to clicks and quality in shared models. Optimize for the lead or conversion event, not for clicks: clicks are a separate "dense" task group.
3. **[INFERRED, strong]** Creative content is read semantically. Ad features include creative attributes and the landing page, and content embeddings from text and image models drive gains. Make creative and copy say clearly and specifically what the offer is (self-storage, Jakarta, the use case), and test creatives that are meaningfully different, not small variations.
4. **[INFERRED, medium]** Predictions are calibrated and used in auction pricing. Anything that raises Fab's true conversion rate after the click or impression (form friction, offer, landing page) should feed back into higher predicted CVR and better auction outcomes. This is a possible lever on CPL, which is currently Rp 113k against a Rp 95k target.
5. **[INFERRED, medium]** Users are modeled from long behavior histories (hundreds to thousands of actions) that are refreshed on conversions, and models share learning across surfaces. Meta's model probably finds intent better than hand-picked narrow targeting can. That argues for testing broader delivery, but the papers do not test targeting settings directly.
6. **[INFERRED, medium]** Meta treats 0.02% loss changes as significant because it has billions of examples. At about 3 leads/day, Fab's daily CPL is mostly noise. Judge changes on multi-day or weekly windows, never on single days.
7. **[INFERRED, weak]** The model already learns 24-hour behavior cycles from users' own histories. Manual dayparting may duplicate what the model does. Treat dayparting as something to test, not a default.
8. **[INFERRED, weak]** User representations refresh within hours (TTL of a few hours, event-triggered updates). The system reacts to new user behavior quickly. How quickly an advertiser's own changes take effect is not covered.

---

## 4. Not supported

| Common belief | Status in these papers |
|---|---|
| "Learning phase" needs about 50 conversions/week; edits reset learning | Not addressed |
| Budget changes (size or speed) disrupt delivery | Not addressed |
| Broad targeting beats interest targeting / Advantage+ audiences | Not addressed (only indirect support from user-sequence modeling) |
| CBO vs ABO, number of ad sets, "account consolidation" | Not addressed. Lattice's "consolidation" is about Meta's own models and datasets, not advertiser account structure |
| The advertiser's chosen attribution setting changes how delivery optimizes | Not addressed. The papers only cover windows used as training labels |
| Pixel / Conversions API / event match quality | Not addressed |
| New advertisers or new ads have a cold-start penalty | Not addressed |
| Creative fatigue | Not addressed |
| Andromeda retrieval behavior | Not addressed (cited only as a blog reference title in Lattice) |
| Dayparting improves results | Not addressed. LLaTTE only shows that the model learns daily cycles |
| Audience size minimums, lookalikes, custom audiences, frequency caps | Not addressed |
| "Meta's AI understands your creative" | Partly supported: semantic content embeddings and creative attributes are model inputs. The papers do not say how creative is scored |

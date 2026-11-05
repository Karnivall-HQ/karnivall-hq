# B — Meta ranking stack: GEM, sequence learning, Adaptive Ranking, GenRecs, HIR

Sources: 8 Meta engineering-blog extracts in `../sources/`. No other sources were used.
Pipeline note: none of the 8 docs describes the **auction**, and none uses the terms "early ranking" or "late ranking". They do mention **retrieval** (GenRecs, HIR, which names Andromeda) and **"multi-stage ranking"** (GEM 2026). The placements below come from that wording.

---

## 1. Per source

**GEM: The Central Brain** (`...GEM The Central Brain...txt`), Nov 10, 2025.
GEM is Meta's largest ads "foundation model". It is not served to users directly. It trains offline and passes what it learns to hundreds of smaller user-facing "vertical models" (VMs) that do the real-time ranking, using distillation, representation learning and parameter sharing. Its inputs are ad content plus user engagement from **both ads and organic** activity. They come as *sequence features* (activity history of up to thousands of events) and *non-sequence features* (age, location, ad format, creative representation). It learns across surfaces (e.g., Instagram video engagement improves Facebook Feed predictions). It is continuously trained online. Pipeline position: upstream teacher for the ranking models.

**GEM: Scaling the Central Model** (`...GEM Scaling the Central Model...txt`), Oct 13, 2026.
The 2026 GEM replaces separate per-surface/per-objective systems with **one central model** that jointly predicts CTR across surfaces and CVR across optimization goals (off-site conversions, app installs). It uses a new architecture (Kunlun) and longer user-history context. Knowledge reaches the serving models through LoopFM (compressed GEM representations plus a per-user history of them) and Solaris. Solaris precomputes GEM user-ad embeddings for the top candidates "as multi-stage ranking narrows a live request". Signals: engagement sequences, ad content, clicks and conversions across all surfaces. Sits upstream of the ranking stage and feeds the late stages.

**GEM Training** (`GEM Training How Meta Doubled...txt`), Aug 3, 2026.
This is a pure infrastructure post: kernels, FP8 precision, parallelism and load balancing for training GEM on thousands of GPUs. It confirms GEM's shape: trillions of sparse embedding parameters plus billions of dense parameters, with sequence and non-sequence features. User sequences range from hundreds to tens of thousands of tokens. It contains nothing about delivery behavior or advertiser levers.

**Sequence learning** (`Sequence learning...txt`), Nov 19, 2024.
This post describes the shift from hand-built aggregated "sparse features" (e.g., "ads clicked in last N days") to **event-based features**. These are ordered streams of a person's engagement and conversion events, each with attributes and a timestamp, fed to transformer-style sequence models. The aim is to understand behavior "before and after converting" and predict the next relevant ads. It sits in the ranking models, which must "rank thousands of ads in a few hundred milliseconds."

**From User Sequences to Scaling Laws** (`From User Sequences...txt`), Aug 5, 2026.
This post describes a two-stage design. An **offline user model** (deep transformer, sequences in the thousands) precomputes cached user embeddings. A fast **online ranking model** combines those embeddings with fresh user signals and ad-candidate info in real time. It is a core part of GEM. The findings: more compute gives predictable gains, mixed action types beat single-type sequences, and semantic content features help cold-start ads.

**Meta Adaptive Ranking Model** (`Meta Adaptive Ranking Model...txt`), Mar 31, 2026.
This is the serving-side runtime ranking model, LLM-scale at about 1T parameters with roughly 100 ms latency. It routes each request to a model whose complexity matches "a person's context and intent". It computes user signals once per request and shares them across all ad candidates, which makes long behavior sequences affordable. It launched on Instagram in Q4 2025. Roadmap: near-real-time model freshness through incremental weight updates. Pipeline position: real-time ranking.

**GenRecs Tokenization** (`GenRecs Tokenization...txt`), Oct 19, 2026.
This replaces per-item IDs with **semantic tokens** derived from each ad's or product's text and images (via pre-trained multimodal models) plus engagement-learned representations. Similar items share tokens, so a brand-new ad inherits what the model knows about similar ads. Used in **both retrieval and ranking**, for ads, products, pages and pixels. Main value: cold start, tail ads and cross-campaign transfer.

**Hierarchical Interest Representation (HIR)** (`Exploring Hierarchical Interest...txt`), Jul 15, 2026.
This is a **research-stage** upstream layer ("we're exploring"). It is a graph of users, ads, advertisers, campaigns, products and pixels, linked by typed, time-stamped engagement edges and enriched with LLM-processed advertiser/product content (page metadata, catalog attributes). It produces interest embeddings and "Bag-of-Meaning" tokens. Its purpose is to fix **deep-funnel signal scarcity** by extending supervision beyond the few users who convert. It is meant to feed GEM, Andromeda (retrieval) and Adaptive Ranking, "from retrieval to final stage ranking."

---

## 2. Key facts

- GEM conversion lift (2025): **+5% IG, +3% FB Feed** in Q2. (Central Brain: "delivered a 5% increase in ad conversions on Instagram and a 3% increase in ad conversions on Facebook Feed in Q2")
- GEM cumulative (2026): **+18.9% conversions, +12% CTR**, plus **+5.8% FB, +4.1% IG, +1.6% off-site** conversion uplift "for targeted users". (Scaling: "GEM has delivered 18.9% conversion improvement and 12% ad click-through rate (CTR) improvement across Meta's ad surfaces and objectives")
- GEM architecture is **4x more efficient** than the original ranking models; knowledge transfer is **2x** more effective than standard distillation. (Central Brain: "now 4x more efficient at driving ad performance gains for a given amount of data and compute")
- Trains on **ads AND organic** behavior. (Central Brain: "GEM is trained on ad content and user engagement data from both ads and organic interactions")
- Sequences of **up to thousands of events** in the 2025 GEM. (Central Brain: "processes sequences of up to thousands of events with minimal storage cost")
- Long context **2x in production**, 25x shown feasible; quality follows a **power law** in sequence length. (Scaling: "GEM scaled the long engagement context length by 2x in production")
- Clicks help conversions: click learning transfers to sparse conversion tasks. (Scaling: "The generalizable representations learned on data-rich click tasks transfer into data-sparse conversion tasks.")
- Model size: **O(trillion) sparse + O(billion) dense** params; sequences "hundreds to tens of thousands of tokens". (GEM Training: "trillions of sparse embedding parameters and billions of dense parameters")
- Training: **20–25% MFU, 4x training FLOPs** in 12 months. (GEM Training: "doubled GEM's E2E training efficiency to 20-25% MFU while scaling total training FLOPs 4x")
- GEM is **continuously trained online**. (Central Brain: "we also perform continuous online training to refresh the FMs")
- Sequence learning: **+2–4% conversions** on select segments. (Sequence learning: "2-4% more conversions on select segments")
- Ranking latency budget. (Sequence learning: "has to rank thousands of ads in a few hundred milliseconds")
- Sequences include conversion events. (Sequence learning: "learning representations directly from a person's engagement and conversion events")
- Multi-stage model: **+6% IG conversions, +3% FB conversions, +3.5% FB clicks** (cumulative, with other work). (From User Sequences: "cumulative lift of 6% in conversions on Instagram, 3% in conversions on Facebook and 3.5% in ad clicks on Facebook")
- Diverse action mix beats single-type. (From User Sequences: "A balanced mix of action types (e.g., views, clicks, conversions) yields better results than sequences composed of a single action type.")
- Content features help cold start. (From User Sequences: "especially helpful in cold-start scenarios (e.g., new ads or advertisers with limited historical engagement data)")
- Adaptive Ranking: **+3% conversions, +5% CTR** for targeted users on IG; **O(1T)** params; **O(100 ms)** latency; **35% MFU**. (Adaptive Ranking: "delivered a +3% increase in ad conversions and +5% increase in ad click through rate for targeted users")
- GenRecs: **+0.35% conversions** (Feb 2026). (GenRecs: "GenRecs Tokenization has delivered a +0.35% lift in conversions across surfaces for advertisers")
- GenRecs handles brand-new products. (GenRecs: "even when surfacing brand-new products with no past product, ad or company engagement history")
- GenRecs transfers learning across campaigns. (GenRecs: "creates a stable vocabulary that allows the models to carry insights across campaigns for advertisers")
- HIR: deep-funnel feedback is scarce; it is research stage, with **no lift numbers** given. (HIR: "ad impression opportunities are limited and deep funnel user feedback is scarce")
- HIR uses page metadata and catalogs. (HIR: "features are pulled from structured page metadata and advertiser catalog attributes and processed through vision or language models")

---

## 3. Advertiser implications

1. **Optimize for the deepest conversion event with enough volume, and keep clicks/engagement flowing.** **[INFERRED]** Meta states that conversion signals are sparse **[STATED]** and that click learning transfers into conversion prediction **[STATED]**. It does not tell advertisers which event to pick, and nothing in the docs covers lead-form or messaging objectives specifically.
2. **Send real conversion events back to Meta. Pixels are first-class entities in the model.** **[INFERRED]** Pixels appear as nodes and items in GenRecs and HIR **[STATED]**, and GEM uses "measurement signals" **[STATED]**. CAPI and offline conversions are **never mentioned**. Their value for Fab (e.g., storage booking signed) is an inference from "deep funnel user feedback is scarce."
3. **Creative content is a direct model input. Make the ad clearly say what it is (self-storage, Jakarta, the offer).** **[STATED]** Creative representation and ad content are features. Multimodal models "read each ad... including its text and images." The copy advice itself is **[INFERRED]**.
4. **New ads are not starting from zero.** **[STATED]** Semantic tokens let a new ad inherit learning from similar ads and earlier campaigns. **[INFERRED]** Refreshing creative is therefore less costly than "resetting learning" folklore suggests, and keeping new creatives semantically close to proven winners should transfer the most.
5. **Creative volume.** **[INFERRED only]** The docs say tail ads with few impressions benefit most from tokenization, but they never recommend a number of creatives.
6. **Broad targeting.** **[INFERRED]** The system models each person from thousands of ads and organic events, matches ad content to inferred interest, and HIR aims to find "people... who carry the most genuine, latent interest". Together these imply that the model, not manual interest lists, does the audience finding. **Targeting settings are never discussed** **[STATED absence]**.
7. **Adaptation speed.** **[STATED]** GEM is trained continuously online, user embeddings are cached offline with fresh online signals added, and near-real-time freshness is a roadmap item. No timescale (hours or days) is given. **[INFERRED]** Expect quick reaction to user behavior. Nothing here addresses how fast a *campaign's* performance settles.
8. **Cross-surface learning means placement splitting may cost signal.** **[INFERRED]** One model learns across FB, IG and Reels and transfers insights between them **[STATED]**.
9. **Page and website quality may feed matching.** **[INFERRED]** HIR uses structured page metadata. It is research-stage only.

---

## 4. Not supported (what these 8 docs do NOT say)

- **Learning phase / 50 conversions per week / "don't edit or it resets":** not addressed. GenRecs' cross-campaign transfer arguably cuts against strict "reset" folklore, but no doc says so.
- **Auction mechanics (bid × estimated action rate × quality, total value):** not addressed. The word "auction" does not appear.
- **Bid caps, cost caps, bidding strategies, budgets, CBO/ABO:** not addressed.
- **Attribution windows / attribution settings:** not addressed. (The docs mention only "off-site conversion" as a goal and "measurement signals" as an input.)
- **Retargeting vs prospecting:** not addressed. Pixels appear as graph entities, but custom audiences are never discussed.
- **Placements (Advantage+ vs manual):** not addressed as advertiser settings. The docs only say one model learns across surfaces.
- **Lead ads / instant forms / messaging-objective optimization:** not addressed. Conversion examples are purchase, off-site conversion and app install.
- **CAPI, offline conversions, conversion value / value optimization:** not addressed by name. "Long-term value" and "ROAS" appear only as aspirations.
- **Creative fatigue / frequency:** not addressed.
- **Lift numbers as advertiser guarantees:** the docs present them as platform-wide averages or "for targeted users", **not** per-advertiser expectations. Several are cumulative "together with broader model innovations." Do not promise Fab any of these percentages.

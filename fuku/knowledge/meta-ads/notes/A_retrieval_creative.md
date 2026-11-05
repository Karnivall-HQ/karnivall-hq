# A. Retrieval, ranking and creative diversification: notes from Meta's own sources

Scope: 6 Meta articles in `../sources/`. No outside knowledge used. Written for the Fab self-storage lead-gen account (~Rp 350k/day, CPL ~Rp 113k, target ≤ Rp 95k).

Pipeline as the sources describe it: **retrieval** (tens of millions of ads narrowed to a few thousand) → **ranking stages** ("increasingly powerful machine learning models evaluate progressively smaller candidate sets") → final ads shown. None of the sources describes the **auction** step.

---

## 1. Per source

**[S1] Meta Andromeda: Powering the Next Generation of Ads Retrieval Through Model-System Co-Design** (engineering.fb.com, Oct 28, 2026)
This is the 2026 version of Andromeda, the **retrieval** stage that runs first. It replaces the earlier model with a "retrieval mixture-of-experts": several specialised user towers, each a model of one side of a user's interests, plus a router that sends each ad to the most relevant experts. Meta says this reaches "near ranking-level" accuracy at retrieval scale. Targeting checks (index matching), scoring and top-K selection now all run on one GPU server, so the system can score *every eligible ad* at over 1B ads/sec. The stated reason for the rebuild is that GenAI creative tools have grown the ad pool to "hundreds of millions of new ads". The advertiser-facing claim is +2.4% conversions on Facebook since 2025.

**[S2] Meta Andromeda: Supercharging Advantage+ automation with the next-gen personalized ads retrieval engine** (engineering.fb.com, Dec 2, 2024)
This is the original 2024 Andromeda launch. Retrieval selects "from tens of millions of ad candidates into a few thousand", and later ranking models pick the final ads. Andromeda replaced rule-based retrieval with a deep neural network that has 10,000x more capacity, plus a hierarchical index trained together with the model. Both were built to handle the very large number of creatives coming from Advantage+ and GenAI. The article reports +6% recall and +8% ads quality on selected segments. Looking ahead, Meta says it will move to a loss function that yields "a more diverse set of ad candidates".

**[S3] The Creative Advantage: Unlocking the Power of Diversification with Meta Andromeda** (facebook.com/business, Apr 22, 2025)
This is a best-practices article for advertisers. It argues that creative diversification (many creatives with different themes, messages and visuals) has replaced niche targeting as "the best lever" for finding relevant audiences. Andromeda is presented as the system that handles the extra volume. It promotes Advantage+ sales campaigns and Advantage+ creative (including GenAI image generation), with average-lift numbers. It does not describe any pipeline mechanics beyond retrieval-level personalisation.

**[S4] AI Innovations in Meta's Ad Ranking Driving Advertiser Performance** (facebook.com/business, Mar 27, 2025)
This is a plain-language overview of four systems:
- **GEM**, a large foundation model used in ranking.
- **Lattice**, a single unified ranking architecture that works across objectives and surfaces.
- **Andromeda**, at the retrieval stage.
- **Sequence Learning**, which models the order of a user's actions before and after seeing an ad.

Each system comes with a headline lift number. The article ties Andromeda directly to advertisers uploading "more and more creatives to support a diversification strategy".

**[S5] New AI advancements drive Meta's ads system performance and efficiency** (ai.meta.com, May 11, 2023)
This article introduces **Meta Lattice**, a ranking-model architecture with trillions of parameters. It replaces many separate models that were each tuned for one objective or surface. It shares learning across surfaces (Feed, Story, Reels) and objectives (clicks, views, conversions). It is designed for "less granular data" and the "cold start" problem, and it handles delayed conversion feedback. Early results on Instagram showed ~8% better ads quality.

**[S6] Turning Opportunistic AI Inference Capacity Into Better Ads Recommendations** (engineering.fb.com, Oct 12, 2026)
This is an infrastructure article about the **ranking** stages. When spare compute is available, Meta switches on two levers:
- **Rank More Ads (RMA)** sends more candidates from retrieval into ranking.
- **Serve Better Models (SBM)** sends more requests to a more powerful ranking model, choosing requests by a predicted-engagement "request-value" signal.

These levers expand and shrink within minutes, and are cut back within milliseconds when capacity is reclaimed. The article contains no advertiser-facing guidance and no lift numbers.

---

## 2. Key facts

**Retrieval scale and funnel**
- Retrieval narrows the pool from tens of millions of ads to a few thousand, and handles about 1,000x more ads than later stages. [S2] *"selecting ads from tens of millions of ad candidates into a few thousand relevant ad candidates"*; *"Retrieval processes three orders of magnitude more ads than subsequent stages."*
- [S4] says the same: *"narrow down a pool of tens of millions of ads to the few thousand we consider showing someone."*
- The 2026 system scores every eligible ad at more than 1B ads/sec, which Meta calls a 100x lift over the 2024 version. [S1] *"scores every eligible ad … surfaces the top candidates at over one billion ads per second … a 100x lift"*
- The 2026 model uses ~300x fewer inference FLOPs (a measure of compute) than the 2024 model, and runs at over 10B ads/sec on one GPU. [S1] *"approximately 300x fewer inference-time FLOPs than the 2024 Meta Andromeda retrieval model"*
- Targeting is enforced as a hard filter (index matching) before or alongside scoring. [S1] *"index matching (i.e., enforcing advertisers' targeting rules)"*; *"evaluates complex advertiser-defined targeting logic across tens of feature categories"*
- The index updates in real time as ads are created, edited or expire. [S1] *"must support real-time index updates as ads are created, modified, or expired throughout the day"*
- Moving work onto one GPU server cut network traffic ~100x. The gating kernel got 5.3x faster, from 2.4B to over 10B ads/sec. INT8 (a lower-precision number format) gave up to 2x more throughput. [S1]

**Retrieval model quality and outcomes**
- +2.4% conversions on Facebook since 2025. [S1] *"Since 2025, Meta Andromeda has delivered a 2.4% increase in conversions on Facebook."*
- +6% recall and +8% ads quality, measured on selected segments. [S2] *"+6% recall improvement to the retrieval system, delivering +8% ads quality improvement on selected segments."* Note that [S3] and [S4] repeat the "8%" without the "selected segments" qualifier.
- 10,000x more model capacity, and model elasticity that makes inference 10x more efficient. [S2] *"enabling a meaningful increase of model capacity (10,000x)"*; *"model elasticity further boosts model inference efficiency by 10x."*
- Over 3x more QPS (queries per second) and over 100x faster feature extraction. [S2]
- Bigger models are reserved for high-value segments. [S2] *"A segment-aware design leverages higher complexity models to serve high value ads segments"*
- The user signals that feed retrieval are listed. [S1] *"sequential ad engagement events, user-cohort representations, LLM-derived semantic features, and cross-surface co-engagement signals."*
- Meta's stated direction is more diverse candidates. [S2] *"autoregressive loss function … delivers a more diverse set of ad candidates."*
- Meta expects another 1,000x increase in model complexity. [S2]

**Creative volume and Advantage+**
- More than 1M advertisers made more than 15M GenAI ads in one month, and image generation gave an estimated +7% conversions. [S2] *"more than a million advertisers used our generative AI (GenAI) tools to create more than 15 million ads in a month."*
- Advertisers turning on Advantage+ creative's AI targeting saw +22% ROAS. [S2] *"when advertisers who did not previously use Advantage+ creative turned on its AI-driven targeting features, they experienced a 22% increase in ROAS"*
- Advantage+ sales campaigns' streamlined setup averaged 9% lower CPA. [S3] *"On average, advertisers see a 9% lower cost per action when using the new streamlined setup for Advantage+ sales campaigns"*. This is a sales/ecommerce product, not lead-gen.
- Advantage+ creative image generation averaged +11% CTR and +7.6% conversion rate. [S3] *"11% higher click-through-rate and 7.6% higher conversion rate"*
- Ben & Jerry's GenAI backgrounds on a catalog ad gave +7% link clicks. [S3]
- Dribbleup testimonial: about 50 new creatives a week with "steady performance". This is a single anecdote, not a controlled result. [S3] *"ramping from 3-4 new creatives a week to almost 50 on average."*

**Ranking**
- GEM: up to +5% conversions on Reels. [S4] *"GEM has increased ad conversions by up to 5%"*
- Lattice: almost 12% better ad quality and up to +6% conversions. [S4] *"increased ad quality by almost 12% and increased ad conversions by up to 6%."* [S5] gives an earlier Instagram figure of ~8% ads quality.
- Lattice scale: trillions of parameters, hundreds of billions of training examples, thousands of data domains. [S5]
- Lattice is built to handle cold start and delayed conversions. [S5] *"particularly useful for the 'cold start' problem"*; *"capture not only a person's real-time intent from fresh signals but also long-term interest from slow, sparse, and delayed signals."*
- Sequence Learning: +3% conversions on selected segments. [S4] *"3% increase in conversions based on testing within selected segments."*
- How many candidates get ranked changes with spare compute. [S6] *"RMA increases the number of candidates evaluated by the ranking stages when opportunistic capacity is available."*
- The stronger model is routed by predicted engagement. [S6] *"group requests into segments based on predicted likelihood of user engagement with the ad."*

---

## 3. Advertiser implications

Labels:
- **[STATED]**: the source text itself tells advertisers to do this.
- **[INFERRED]**: my reasoning from how the system works. Treat these as hypotheses to test.

1. **Diversify creative by theme, message and visual, not only by small variations.** [STATED, S3] *"creating a wide range of ad creatives with different themes, messages, and visuals"*; *"uploading multiple creatives with different themes and messages."*
   - For Fab: write genuinely different concepts, for example moving house, decluttering, business inventory, renovation, student storage, and price/security/access messages, rather than 5 crops of one image.
2. **Treat creative as the main targeting lever, ahead of niche targeting.** [STATED, S3] *"the focus has shifted from niche targeting to creative diversification as the best lever to find the most relevant audiences."*
3. **Don't let the creative process be the bottleneck.** [STATED, S3] *"The biggest constraint you can put on your Meta strategy is the constraints you place on your creative process."*
4. **Try Advantage+ creative and its GenAI features (image generation, visual/copy/audio enhancements).** [STATED, S3] *"advertisers can take advantage of creative automation tools like Advantage+ creative."*
   - Caveat: the lift numbers are averages, mostly from sales/catalog campaigns. There is no lead-gen evidence.
5. **Use Advantage+ automation (targeting, budget, placements) where it is available.** [STATED in a promotional sense, S2/S3] The articles present Advantage+ as the default path, with average lifts.
   - None of the sources says this specifically for lead-gen campaigns.
6. **Broader targeting gives retrieval more people to match each creative to.** [INFERRED, S1] Targeting is a hard filter applied before the model scores. A narrow audience removes impressions before the stronger model can judge relevance. S3 states the direction ("niche targeting" → creative), but the mechanism-level claim is my inference.
7. **Ad count per ad set: no number is given anywhere.** [INFERRED] Each ad is a separate candidate scored per user (S1 "scores every eligible ad"). So several *distinct* ads give the system more ways to match different users. Near-duplicates probably add little, since the model judges relevance by content.
   - For Fab: test 6–10 distinct concepts per consolidated ad set. Treat that as a starting hypothesis, not Meta guidance.
8. **Consolidate rather than fragment.** [INFERRED, S5/S1] Lattice shares learning across surfaces and objectives, handles "limited data" and "cold start", and is built for "less granular data". Retrieval uses Meta-wide user signals. Splitting a Rp 350k/day budget into many small ad sets is therefore unlikely to help, and pooled data should help.
   - No source explicitly recommends consolidation.
9. **Conversion-signal quality matters for ranking.** [INFERRED, S5/S4] Lattice and Sequence Learning learn from "slow, sparse, and delayed" conversion signals and from action sequences around conversions. Clean, deep-funnel events give these models better targets, for example qualified leads or bookings sent back to Meta, not just form opens.
   - The sources never mention the Pixel, CAPI or lead quality.
10. **Expect some delivery noise that has nothing to do with your account.** [INFERRED, S6] How many candidates get ranked, and which model ranks them, changes minute to minute with Meta's spare compute. Small day-to-day CPL swings may be system-side, so judge on multi-day windows.
11. **Creative edits are picked up quickly by retrieval.** [INFERRED, S1] The index updates in real time ("as ads are created, modified, or expired"). This says nothing about how *ranking/learning* reacts to edits.

---

## 4. Not supported or not addressed

| Common belief | What these 6 docs say |
|---|---|
| Learning phase needs ~50 conversions/week; edits reset learning | **Not addressed.** The term "learning phase" never appears. S1 says only that the retrieval index updates in real time. |
| A specific number of ads per ad set is optimal (e.g. 3–6, or "max 50") | **Not addressed.** No number is given. Dribbleup's ~50 new creatives/week is an anecdote about weekly production, not a per-ad-set limit. |
| Bid caps or cost caps beat lowest-cost | **Not addressed.** Bidding is mentioned only as something Advantage+ automates (S2, S3). |
| Manual placements beat Advantage+ placements | **Not addressed directly.** S2 lists "dynamic placement across Meta surfaces" as an Advantage+ feature, and S5 says Lattice shares learning across Feed, Story and Reels. Neither directly compares manual against automatic placements. |
| Retargeting / custom audiences are essential | **Not addressed.** |
| Interest stacking or detailed targeting improves results | **Somewhat contradicted:** S3 says the focus "has shifted from niche targeting". There is no test data on interest targeting. |
| Andromeda "punishes" similar or duplicate creatives, or needs 10+ distinct concepts | **Not addressed.** The docs say diversity helps and that future retrieval aims for "more diverse" candidates. They never mention a penalty for similarity or a minimum count. |
| Creative fatigue or refresh cadence rules | **Not addressed.** |
| Budget levels or CBO vs ABO | **Not addressed.** "Optimal budget allocation" is mentioned only as an Advantage+ feature (S2). |
| Lead-gen-specific results (lead forms, CPL) | **Not addressed.** All lift numbers are conversions, ROAS, CPA, CTR or "ads quality", mostly from sales or catalog contexts. |
| The auction mechanics (total value, bids × estimated action rate × quality) | **Not addressed.** These docs cover retrieval and ranking only. |
| Andromeda lift is universal | **Contradicted in part:** S2's +8% quality and S4's sequence-learning +3% are for "selected segments", and S1's +2.4% is for Facebook. |

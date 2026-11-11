# Alithia: chronological event platform research

Research date: 2026-11-03. Status: provisional product thesis and literature reconnaissance, not validated product-market fit or a completed novelty review.

Founder clarification received after this brief: initial audience is professional researchers/journalists/analysts; complete chronology is the first outcome to investigate. Team is one AI student plus AI, with no allocated budget or fixed date. Alithia is a starting case, and evidence-supported pivots into other products, infrastructure, or scientific research are welcome. The handoff/correction-first recommendation below remains an earlier hypothesis, not an accepted direction. Follow the revised ALITHIA_MASTER_RESEARCH_PROMPT.md for the current mandate. Questions about audience, priority, team, budget, and date below have now been answered; retain the original analysis as a record rather than treating it as current instructions.

## Decision in view

Build a platform that maintains the evolving record of an event and explains material changes, evidence, disputes, and corrections. The founder wants a distinctive technical contribution beyond conventional retrieval, generation, and caching. These remain useful infrastructure; novelty must earn its place through measurable user benefit.

The August code review describes historical prototype behavior, not a fresh November audit. It established reusable claim extraction, search, OCR, and UI components, but did not establish reliable event tracking or verification. No new code audit was performed for this brief.

## Proposed product fit

First hypothesis: small professional news/research desks repeatedly handing off developing stories. Start with one beat, geography, and language pair that the founder can access. India and English plus one regional language are possibilities, not confirmed choices.

Job: "When I return to a developing story or take over a colleague's shift, show me what changed, what earlier understanding is obsolete, and which statements I can trace to evidence."

Input: an event seed, selected sources, and optionally the desk's notes. Output: a persistent event page with a short current brief, chronological record, changes since last visit, evidence for each assertion, unresolved disputes, and corrections. A repeat visit is the central product loop.

User: reporter/researcher/editor. Buyer hypothesis: desk lead or organization. Trigger: shift handoff, daily brief, new development, publication preparation. Existing workaround to investigate: liveblogs, source tabs, messages, notes, alerts, and manual brief updates. This is a workflow hypothesis until observed in interviews.

Why this first: it gives us observable repeated tasks and reviewable artifacts. It does not establish that newsrooms have the best budgets. Compare adjacent analyst teams in discovery; do not combine all their needs into one MVP.

| Candidate | Value hypothesis | Main unknown | First proof |
|---|---|---|---|
| News/research desks | Less re-reading and safer handoffs | Budget and integration into daily work | Repeated use on live stories and paid pilot |
| Engaged readers | Catch up without repetitive coverage | Acquisition, retention, willingness to pay | Voluntary return visits and paid conversion test |
| Risk/NGO/operations analysts | Track developments relevant to decisions | Source coverage and operational reliability | Useful brief accepted in an existing workflow |
| App builders | Stable event IDs and reliable update feeds | SLA, coverage, redistribution rights | Integration into a real downstream product |

Consumer platform remains a possible destination. A professional first wedge is a recommendation to test, not a commitment to abandon consumers.

## What already exists

- Dataminr announced automatically regenerating live event briefs in April 2024. Consequently, "self-updating event summaries" is not a new category. Its performance figures are vendor claims, not an independent comparison with Alithia. [Launch announcement](https://www.dataminr.com/press/dataminr-unveils-regenai-the-first-generative-ai-that-automatically-regenerates-in-real-time/)
- Factal combines AI detection with editorial verification and distinguishes editor-verified from automated updates. Human review must be costed as an actual operating choice. [Product explanation](https://www.factal.com/personal-app-help/)
- NewsAPI.ai offers article enrichment and event association. Treat it as both a possible input supplier and a baseline for event grouping; access does not automatically establish rights to redistribute content. [Official product](https://newsapi.ai/)
- Ground News's bias methodology operates at publication level, with a US political frame. That is different from assessing evidence for a specific claim; Alithia must not equate source labels with claim truth. [Methodology](https://ground.news/rating-system)
- The Reuters Institute reports 17% paid for online news across its 20-market pay basket in 2026. That is not an India estimate or a forecast of Alithia demand. It strengthens the case for testing a specific paying use case. [Report](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary)

This is a selected comparison, not an exhaustive competitor map. No competitor accounts were purchased or hands-on quality comparisons completed. Do not interpret undocumented features as absent features.

## The differentiated experience to investigate

Hypothetical crash example; all details below are invented for product design:

- 09:10: outlet A attributes three reported deaths to police.
- 09:20: seven outlets repeat A; no additional independent confirmation established.
- 10:00: a hospital statement gives two deaths and one critical injury.
- 10:30: police revise the initial count to two.

The useful update is "The initially reported count has been revised; here are the original statement, conflicting report, and correction." A user who saw the initial count should receive the correction. The earlier entry remains inspectable and marked superseded. A new user sees the current supported account plus the relevant history.

Store at least four distinct times: occurrence time or interval, publication time, source revision time when available, and first observation/ingestion time. Store Alithia's own assessment versions separately. A retrospective document must not silently enter an earlier 'as known then' view.

Keep these views separate: event chronology; history of reporting and revisions; current assessment. Causal explanations require attributed evidence; chronological order alone does not establish cause.

## Research opportunity

Candidate question: Can a system maintain a more faithful event record under delayed, copied, contradictory, multilingual, and corrected reports, while reducing the time a returning user needs to understand the meaningful changes?

This is a hypothesis about a contribution, not a claim of novelty. A useful system could combine:

1. Persistent event identities, with reversible merges and splits when incident boundaries change.
2. Immutable source versions and sentence-level evidence spans.
3. Attributed claims with explicit time, location, speaker, and scope.
4. Source-lineage estimates that identify shared upstream evidence; uncertain lineage stays uncertain.
5. Claim lifecycle states such as reported, corroborated, disputed, revised, retracted, and unresolved, each with explicit criteria and evidence. Store individual source assertions separately from aggregate assessment.
6. Dependency tracking so corrections invalidate or flag affected briefs, timeline entries, and alerts. Record a user's last delivered version to support correction notifications, with user controls.
7. Update selection that weighs significance, novelty, uncertainty, and user context against attention cost. Avoid optimizing for engagement alone.
8. Targeted evidence acquisition: choose the next source to inspect based on which unresolved question it may answer, within a budget. It must be permitted access, and more searches do not ensure resolution.

The plausible advantage lies in reliable reconciliation and correction behavior plus domain coverage and evaluation data. A graph database, a new acronym, or several agents do not establish an advantage.

## Literature anchors and what they actually support

The following were screened through abstracts/official summaries. Full methods, appendices, datasets, licenses, and reproducibility must be inspected before selecting a baseline or claiming novelty.

| Work | Relevant contribution | Implication |
|---|---|---|
| [Examining the State-of-the-Art in News Timeline Summarization, ACL 2020](https://aclanthology.org/2020.acl-main.122/) | Strategies, evaluation, and a longer-span TLS dataset | Establish classical baselines; the timeline task predates LLMs |
| [Background Summarization of Event Timelines, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.505/) | Background for each update and a question-answering utility measure | Catch-up comprehension deserves direct evaluation |
| [From Moments to Milestones, ACL 2024](https://aclanthology.org/2024.acl-long.390/) | Incremental clustering and timeline construction from text streams | Incremental LLM event tracking is existing work |
| [CHRONOS, NAACL Findings 2025](https://aclanthology.org/2025.findings-naacl.248/) | Iterative questioning and retrieval for open-domain timelines; Open-TLS | Closely overlaps the headline-to-story idea |
| [DTELS, 2024 preprint](https://arxiv.org/abs/2411.09297) | Timelines at different granularities | Adjustable detail alone is not novel |
| [Zep, 2025 preprint](https://arxiv.org/abs/2501.13956) | Temporal knowledge graph for agent memory | Temporal memory is prior art; its reported memory results do not validate news verification |
| [GraphRAG, Microsoft Research](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/) | Graph-based global corpus sensemaking | A useful comparison, not an event truth engine |
| [Agent Newsroom, ACL 2026](https://aclanthology.org/2026.acl-long.1149/) | Multi-agent chronological reports with coverage and resource allocation | 'AI newsroom agents' already has direct research overlap |
| [Frame In, Frame Out, *SEM 2026](https://aclanthology.org/2026.starsem-conference.25/) | Framing evaluation in news summaries | Citation support alone does not measure selective emphasis |

Three research tracks to compare:

- **Correction propagation:** measure how quickly and completely a new correction changes dependent outputs without erasing historical assertions. Failure risk: wrongly superseding a genuinely distinct claim.
- **Evidence independence:** measure whether copied reporting improperly increases corroboration. Failure risk: confidently inferring copying or independence from superficial text similarity.
- **Useful change selection:** deliver the smallest update that lets a user answer what changed correctly. Failure risk: hiding an important minority report or dispute while compressing.

Start with correction propagation plus useful change selection. Keep independence estimates conservative. Model training is justified only after an error analysis shows repeatable gains over strong existing models and simpler methods.

## Evaluation that could support 'industry leading'

Use identical source snapshots, arrival order, model access, budgets, and output lengths for controlled comparisons. Separately test end-to-end discovery quality; do not conflate better source access with better reasoning.

Baselines: chronological source feed; incremental rolling summary; retrieval plus generation; long-context synthesis; a supported graph/temporal-memory baseline; a reproduced TLS method where feasible; human-produced briefs for quality reference.

Replay each event one document version at a time. At time t, only evidence actually available by t can be accessed. Account for model pretraining contamination: use prospective collection, controlled synthetic counterfactuals, and explicit cutoff tests in addition to historical replay. Synthetic tests supplement real events.

Include changed counts, copied wire reports, same-name places, old images reused, delayed primary documents, source outages, retractions, multilingual paraphrases, changed event boundaries, unresolved disagreement, and spurious causal language.

Measures: claim-to-evidence support precision; event assignment errors; temporal ordering and interval accuracy; important-development recall; duplicate alerts per event-day; correction latency from observable arrival; stale assertions remaining in active outputs; source-independence errors; human review minutes; user catch-up time and comprehension; cost per monitored event-day.

Use held-out events and publishers, multiple annotators, explicit disagreements, uncertainty intervals, and slice-level reporting. Never use only an LLM judge or summary similarity as the success criterion.

Illustrative pilot targets, to agree before testing: halve catch-up time without reducing comprehension; at least 95% sampled assertion-to-evidence support; under 10% duplicate alerts; correction propagation within one configured monitoring cycle. These are proposed gates, not measured performance, launch guarantees, or sufficient proof for high-stakes usage.

## Product validation before scaling

Conduct 8–12 workflow interviews in one candidate segment. Recruit 3–5 pilot users; follow roughly 10–20 events over two weeks, manually reviewing outputs. Compare their existing approach against Alithia on recurring catch-up tasks. Observe voluntary return, correction use, handoff/export use, and willingness to enter a paid pilot. Pilot size is for directional learning, not population-level claims.

Stop or narrow if users prefer the source feed, rarely return, cannot trust the evidence trail, or require manual research whose cost exceeds the value they will pay for. If users value only final reports, revisit whether the continuous platform is necessary.

Cost model: source access + discovery + extraction/retries + inference + storage + human review + delivery/support. Express this per event-day and per active team. Shared public event processing may amortize across readers; private cases and custom source coverage may not. Include quiet versus breaking-news loads and peak failures. Budget and pricing remain unknown pending founder answers.

## Founder questions pending

1. Who should depend on the platform first: professionals, engaged readers, or downstream app builders?
2. Is the first promise meaningful changes, completeness of chronology, or earliest discovery?
3. Team, budget, prototype deadline, available customer/data access, first topic and geography?
4. Do we want a publishable research contribution, a proprietary commercial advantage, or both? Which takes priority when they conflict?
5. How much editorial review can the operating model support?
6. What recent event made you wish this already existed, and what exactly could you not find or understand?

## Current conclusion

Pursue a constrained test of persistent event understanding with visible correction history and useful return-visit updates. Distinctiveness and product fit remain unproven. The next decision is the first user and event domain; the next technical proof is correction-aware streaming evaluation against credible baselines.

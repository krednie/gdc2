# Alithia opportunity-discovery notebook

**Current consolidated entry point: [CURRENT_BRIEF.md](CURRENT_BRIEF.md), updated 2026-11-10.** A live six-request verifier pilot has now run: generic and role-aware arms both scored 12/12 on the development fixtures. Older statements below about no model runs describe earlier checkpoints. A research-only evidence-accounting helper and 19 unit tests are also available; the application is unchanged.

Started 2026-11-03. Team: founder plus AI; zero new spend. Initial task: professional chronology-building. Pivots remain open. This directory contains research artifacts, not application implementation.

Latest decision: see [Cycle 3 product-fit and experiment brief](CYCLE_3_PRODUCT_FIT.md). Generic chronology generation and uncertainty preservation have substantial direct prior art. Retain them as capabilities, not novelty claims. Next candidate is task-bounded chronology completion measured by omissions and total review work; neither product-market fit nor a new algorithm is established.

2026-11-09 continuation: [DART development case](DART_DEVELOPMENT_CASE.md) now supplies a five-source access-checked manifest and draft task rubric. [Implementation-level competitor notes](COMPETITOR_IMPLEMENTATION_NOTES.md) inspect Watchdog prompts and benchmarks at a pinned revision. Five source fetches succeeded; no model comparison or user study has been run. Important omission measurement is already practiced by a close competitor, so it cannot be our standalone novelty claim.

New executed audit: [natural-output regression seeds](NATURAL_FAILURE_CASES.md). Reanalyzed 18 historical outputs from six public evaluation packets: one empty fact list with no coverage-gap flag. Separately verified a summary/fact-list ordering inconsistency against the original scanned document's page 12. These are targeted regression cases, not current model rankings, a prevalence estimate, or validation of a proposed fix.

Next executed reanalysis: [coverage-proxy protocol and results](COVERAGE_PROXY_PROTOCOL.md). Across the same six documents, larger fact lists, longer summaries, and more distinct cited pages each misorder some outputs relative to published important-item judgments. Result persists when excluding the empty arm. Judgments are model-produced and the sample is small/related; the finding rules out a naive completion certificate on these artifacts, not all usefulness of these features.

Product-validation design: [review-effort study](REVIEW_EFFORT_STUDY.md). Separates content quality from review-interface effects, measures final work rather than confidence or click counts, and specifies repeat-use evidence. No recruitment, outreach, or customer validation has occurred.

Application bridge: [research-readiness findings](ALITHIA_RESEARCH_READINESS.md). An isolated probe of the existing evidence formatter shows a controlled case where source eight would receive a card but none of its text enters the model context. Other schema/version/calibration limitations are scoped code-inspection findings. No app code or user changes modified.

### Decision checkpoint, 2026-11-09

- Keep the product hypothesis: task-bounded, reviewable chronology completion for a professional assignment. No product-market fit demonstrated.
- Reject standalone novelty claims for cited timelines, atomic claim ledgers, uncertainty preservation, conservative event merging, and generic coverage evaluation. Direct prior art has been found for each.
- Worth testing: whether targeted evidence/review allocation reduces consequential omissions and total review work compared with a strong general model and existing chronology tooling. No advantage demonstrated yet.
- Practical prerequisite: instrument what is acquired, retained, actually presented to a model, emitted, checked, and accepted. Current Alithia can lose evidence between selection and model context without that being reflected in source cards.
- Research asset now available: real-source development case, natural-output regression cases, two reproducible public-artifact reanalyses, and an isolated application visibility probe. These are more concrete than an architectural proposal but are not a validated algorithm.
- Adjacent pivot screened and parked: benchmark-result comparability/provenance tooling, motivated by the competitor's corrected historical comparisons. [lm-eval's reproducibility paper](https://arxiv.org/abs/2405.14782) already addresses evaluation transparency and comparability; [AI Atlas methodology](https://www.ai-atlas.co/methodology) describes configuration-based comparability groups. Search/overview screening only. Do not relabel versioned evaluation manifests as a new invention.
- Next decisive evidence: actual predictions on unseen source packets plus independent assessment of completed user work. No paid inference, customer outreach, or current-model superiority claim is authorized or implied by this notebook.

## Cycle 1: preregistered diagnostic before execution

Question: Does the accessible Open-TLS reference format support evaluation of evidence-grounded, time-precise professional chronologies, and are there concrete annotation problems that merit a larger audit?

Prior observations motivating the test: the Apple reference appears to put Vision Pro's unveiling in 2024 rather than 2023; its iPhone date field and prose disagree. These observations were found before registration. They are targeted leads, not a random sample or evidence of a dataset-wide error rate.

Plan:

1. Resolve and record the public CHRONOS repository revision; fetch the 50 Open-TLS reference files listed in its keyword manifest. Do not execute upstream code.
2. Run a structural census: parseability, row shape, date precision/validity, chronological order, duplicate dates, sentence counts, explicit URL presence. Absence of URLs in this field does not establish absence of provenance elsewhere in the original project.
3. Flag explicit prose dates that differ from a row's date for human inspection. This is a heuristic: retrospective context and forward references are legitimate, so flags are not labeled factual errors.
4. Independently check a small, openly targeted sample against primary sources. Separate date errors, date-role ambiguity, legitimate multi-event background, and unresolved cases. Do not extrapolate prevalence.
5. Reproduce the date-set scoring behavior with a minimal independently written function. Compare a reference clone with a one-date factual repair. This tests a metric's sensitivity, not the performance or ranking of real models.

Primary outputs: reproducible structural counts; revision/file hashes; evidence-linked adjudication notes; a minimal scoring counterexample. No paid API, model training, or new package installation required.

Success criterion: at least one independently supported mismatch with a demonstrable evaluation consequence, or clear evidence that the benchmark already handles these distinctions. Either result informs baseline choice. Failure to find more errors must be reported.

Limits: no customer validation; no model comparison; no blind annotation; no claim that a benchmark intended for summarization should already solve every professional workflow. Public availability is not a redistribution license. Store derived statistics and minimal identifiers, not a redistributed corpus. This audit alone is not a novel research contribution.

Sources to inspect: https://github.com/Alibaba-NLP/CHRONOS ; https://aclanthology.org/2025.findings-naacl.248/ ; https://www.apple.com/newsroom/2023/06/introducing-apple-vision-pro/ .

## Cycle 1 results

Execution completed; see `open_tls_audit_results.json` and reproducible standard-library script `audit_open_tls.py`. Snapshot: `4dadc9707c9a4f55476ac28259510fecc0d5c8a9`. All 50 topics fetched successfully: 1,130 rows, 2,070 sentences; 579 rows contain multiple sentences. Date fields include 1,105 day-precision values, 24 month-precision values, and one formatting anomaly (an extra space before T). Month precision is not an error. No explicit URLs occur inside reference sentence text; this is a schema observation, not proof that original source information is unavailable elsewhere.

The 29 lexical descending transitions are NOT 29 chronology errors. Two references are consistently reverse chronological; another transition compares a month with a day in that month. Sorting direction and overlapping precision must be handled before interpreting this statistic. Five explicit-text/date mismatches are heuristic flags, not five confirmed mistakes. Planned dates and background references can legitimately differ from the heading date.

### Targeted adjudication

| Case | Observation | Conclusion |
|---|---|---|
| Apple, Vision Pro | Reference date 2024-06-05; Apple's contemporaneous announcement is 2023-06-05 | Independently supported reference date error |
| Apple, iPhone | Date field 2007-01-09; first sentence says January 1 | Internal inconsistency; Apple's announcement supports January 9 |
| Boeing, January 6 row | Includes the later authorization of return after inspections | Legitimate retrospective bundling; unsuitable as an atomic occurrence/as-known-then record without decomposition |
| Boeing, February 28 row | Includes delivery of a plan in late May | Same representation issue, not evidence that the summary is false |
| Starliner, August 24 row | Attributes return decision to Boeing | NASA's contemporary statement attributes the decision to NASA; actor attribution requires repair |

Primary checks: [Vision Pro announcement](https://www.apple.com/newsroom/2023/06/introducing-apple-vision-pro/), [iPhone announcement](https://www.apple.com/newsroom/2007/01/09Apple-Reinvents-the-Phone-with-iPhone/), [FAA January 24 process approval](https://www.faa.gov/newsroom/faa-halts-boeing-max-production-expansion-improve-quality-control-also-lays-out-extensive), [FAA May 30 plan](https://www.faa.gov/newsroom/faa-continues-hold-boeing-accountable-implementing-safety-and-production-quality-fixes), [NASA August 24 decision](https://www.nasa.gov/blogs/boeing-crew-flight-test/2024/08/24/nasa-decides-to-bring-starliner-spacecraft-back-to-earth-without-crew/). These cases were selected for investigation, not randomly sampled. No prevalence estimate is justified.

### Metric counterexample

Using the seven Apple reference dates, an exact reference clone scores Date F1 = 1.0. Repairing only Vision Pro's date scores 6/7 = 0.857142857 against the unchanged reference. This independently reproduces the set-intersection definition in [the released evaluator](https://raw.githubusercontent.com/Alibaba-NLP/CHRONOS/main/evaluation.py). It does not demonstrate a model-ranking reversal, invalidate all reported results, or measure a new model. The test establishes that a factual repair can be penalized by this reference and metric combination.

### Research implication

Three things need separate evaluation: matching an editorial milestone selection; extracting temporally correct assertions; respecting what evidence was available at a cutoff. A good retrospective summary can fail the last two if treated as structured ground truth without adaptation. This is a concrete motivation for an audit/benchmark extension, not yet a publishable contribution by itself.

## Evidence ledger and disconfirmation

Retrieved 2026-11-03. Reading depth is stated so later models do not mistake screening for reproduction. Performance numbers from papers remain author-reported unless explicitly labeled local results.

| ID | Primary evidence | What it establishes | Reading depth / limit |
|---|---|---|---|
| E01 | [GIJN practitioner chapter](https://gijn.org/stories/building-timelines-investigations/) | Investigators use timelines with sources and explicitly distinguished deductions; spreadsheets and documents are actual substitutes | Workflow article read; not customer interviews or willingness-to-pay evidence |
| E02 | [Bellingcat collection protocol](https://yemen-archive.bellingcat.com/methodology/collection-protocol/) | Collection, preservation, metadata, and verification are separate activities | Methodology read; specific investigation context |
| E03 | [Casefleet proposed facts](https://support.casefleet.com/en/articles/13057134-using-the-ai-assistant-to-create-facts) | Cited AI-proposed chronology facts with human approval already exist | Official help page, no hands-on evaluation |
| E04 | [CHRONOS](https://aclanthology.org/2025.findings-naacl.248/) | Iterative questions and retrieval for timelines are prior art | Method/evaluation inspected; released data audited locally, no model reproduction |
| E05 | [Active Timeline Completion](https://aclanthology.org/2026.emnlp-main.256/) | Gap-directed retrieval and dynamic completeness checklists already exist. Its logical-utility filter does not inspect source evidence directly; authors distinguish utility from entailment | Main method, experiments, limitations, and implementation appendices inspected; small human diagnostic is not a population estimate |
| E06 | [DTELS](https://aclanthology.org/2025.naacl-long.136/) | Event-atom factuality and variable granularity are existing evaluation ideas | Paper sections screened; no reproduction |
| E07 | [Timeline test-collection robustness, 2019](https://eprints.gla.ac.uk/180205/13/180205.pdf) | Incomplete labels and system misranking in timeline evaluation are longstanding problems | Relevant evaluation discussion inspected; do not claim first recognition of flawed gold labels |
| E08 | [TREK](https://arxiv.org/html/2610.25323v1) | Separates retrieval from reasoning failures under evolving evidence; includes scope and reliability distractors | Methods sections inspected; preprint results unreplicated |
| E09 | [IncrConsist](https://scifiniti.com/3104-4719/3/2026.0042) | Incremental affected-set verification for LLM-maintained knowledge is direct prior art | Methods/limits inspected; synthetic evaluation and limited lexical contradiction classes |
| E10 | [Statistical stopping, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7700715/) | Recall-aware stopping has established methods for a finite document collection | Methods inspected; assumptions do not automatically transfer to open-web search |
| E11 | [Confidence-based stopping, 2026](https://arxiv.org/abs/2606.15380) | Decision sufficiency versus document recall already has research | Abstract only; requires full reading |
| E12 | [BiTempQA dataset card](https://huggingface.co/datasets/heihei/BiTempQA/blob/main/README.md) | Public project explicitly targets event-time versus record-time reasoning | Card inspected; claimed venue/novelty not independently verified |
| E13 | [Positorium](https://github.com/Roenbaeck/positorium) | Evidence database preserving disagreement, time, and history is a close infrastructure alternative | Repository overview only; correctness/performance not tested |
| E14 | [TimelineAgent](https://arxiv.org/abs/2610.25733) | Query-focused cross-document extraction and reusable reasoning skills are close prior art | Sections 4.1-4.2 and evaluation appendix B.3 inspected; no reproduction |
| E15 | [Interval-reasoning evaluation](https://arxiv.org/abs/2610.17402) | Logical consistency can diverge from correct chronology; parser behavior can dominate apparent errors | Abstract only; controls are relevant to our experiment design |
| E16 | [Clinical occurrence grounding](https://arxiv.org/abs/2609.13062) | Stable occurrence identities and source-row temporal grounding are already studied in an adjacent domain | Abstract only; private/clinical access and deployment risks make this a poor first product for us |

## Pivot ledger

| Candidate | Origin and possible value | Closest prior art / objection | Status and next test |
|---|---|---|---|
| Source-grounded chronology audit layer | Local reference failures; help research/tool builders locate unsupported dates, actor mixups, plans presented as outcomes, hindsight contamination | Temporal extraction, DTELS, BiTempQA, TimelineAgent; a schema alone is not new | Worth testing. Build a small source-backed evaluation slice and compare generic verification with date-role-aware verification |
| Budgeted evidence-gap search | Completeness requires knowing what is still missing; could save search/review cost | ATC already has gap questions; TAR already studies stopping | Investigate after full nearest-method review. Test within a fixed corpus before making open-web claims |
| Incremental re-verification engine | Changes need not force global re-reading; infrastructure could generalize beyond news | Classical view maintenance and IncrConsist directly overlap | Parked pending a real trace showing costs and missed dependencies that existing methods fail to handle |
| Evidence-independence estimator | Repeated reporting should not count as independent confirmation | Longstanding truth-discovery/copying-detection research; copying is difficult to infer reliably | Parked. Need labeled claim-level provenance and an advantage beyond text deduplication |
| Full public news destination | Founder starting vision; accessible return-use loop | Crowded, coverage and distribution expensive, no observed demand yet | Retain as application, not immediate infrastructure commitment |
| Clinical/legal chronology product | Similar mechanisms and expensive professional work | Existing tools, access/privacy/expertise barriers; relevant research already exists | Do not pivot into deployment now. Borrow evaluation lessons only |

## Cycle 2: experiment specification (not executed yet)

Candidate: temporal-role-aware verification of generated chronologies. Potential research question: at matched evidence and inference budgets, does explicitly checking actor, event time, assertion time, modality, and evidence availability improve detection of chronology errors without rejecting valid retrospective background?

Smallest useful artifact: a source-linked diagnostic slice, initially 30-60 assertions across several public events, then an independently reviewed held-out set if the signal survives. Include correct controls; factual date errors; announcement-versus-occurrence substitutions; planned-versus-completed swaps; wrong decision-maker; date uncertainty; legitimate future references; and source versions observed after a cutoff. Label uncertainty rather than treating inaccessible historical snapshots as known.

Baselines: date-format and lexical checks; a generic claim-evidence verifier; same model with a temporal-role checklist; structured extraction plus deterministic interval/cutoff checks. Compare all on identical passages and output budgets. A manually supplied structured representation is an oracle diagnostic and must never be presented as an end-to-end model result.

Measure per-error precision/recall, false alarms on correct background, evidence-span correctness, cost, and human review effort. Separate finding evidence from judging evidence. Test narrative-order changes and paraphrases. Use event-level held-out splits; model/threshold selection must not use the test slice.

Kill/narrow criteria: if a generic verifier matches the proposed method within uncertainty, use it; if annotators cannot agree on the intended date role, improve the task definition before optimizing; if most errors are benchmark typos, release an audit rather than inventing a new algorithm. No claim of industry leadership is supported yet.

Unresolved: nearest-method full comparisons; source permissions; genuinely independent annotation; model access without new spend; adopter usefulness. Current evidence supports a low-cost experiment, not a company pivot.

## Cycle 2 checkpoint: development diagnostic executed

Created `temporal_role_probe.py` and `temporal_role_probe_results.json`: 12 deliberately authored cases grounded in three primary-source pages (Apple, FAA, NASA), with six supported controls and six unsupported transformations. Evidence is paraphrased; this is not a corpus of naturally occurring model mistakes. Cases are development fixtures, not independent or held-out observations. This is a smaller preliminary diagnostic than the proposed 30-60 assertion study, not its completion.

Both the publication-date-equality heuristic and the reject-future-dates heuristic catch 2/6 errors and incorrectly flag 2/6 correct controls. A modality-only oracle catches 4/6 errors with no false alarms, but misses an actor substitution and unsupported date precision. The oracle receives hand-assigned semantic roles, so its advantage cannot be attributed to an implemented extraction system. No generic LLM or proposed-method comparison has been run.

Interpretation: dates alone cannot determine whether a dated assertion is warranted. Future plans can be valid entries, while past-tense outcomes at the publication date can be unsupported. Modality is necessary for these selected examples but insufficient for full verification. This is a diagnostic demonstration, not a statistical estimate or novelty claim.

### Prior-art update that narrows the candidate

Read TimelineAgent sections 4.1-4.2 and evaluation appendix B.3. It already separates relevance, temporal anchoring, and eligibility, with polarity, certainty, factuality, and conditionality. Its query-specific convention can include future-tense events. Thus, 'add temporal roles/factuality to extraction' is not an adequate novelty claim. [Primary method](https://arxiv.org/html/2610.25733v1).

Narrower hypothesis to investigate: preserve a source assertion's lifecycle across successive documents and detect semantic promotion (planned to completed, conditional to unconditional, attributed to established) in downstream chronology outputs, while retaining legitimate plans. This is a hypothesis about an evaluation/control boundary, not proof it is absent from existing temporal memory, event factuality, or belief-revision research.

Next discriminating test: same-model generic-verifier versus role-aware-verifier on identical original source passages, with unseen event families and paired valid/invalid statements. Do not expand the application before establishing whether a generic verifier already handles this. A fair test requires actual model predictions; reasoning through one's own labeled examples does not substitute for that experiment.

## Cycle 3: disconfirmation and product-fit reset

The proposed semantic-promotion phenomenon is not itself a new finding. [AMRFact, NAACL 2024](https://aclanthology.org/2024.naacl-long.33.pdf), inspected at the error-generation method, already perturbs modality, actors, times, temporal order, and causal links. [Uncertainty preservation in incident summaries](https://www.frontiersin.org/journals/language-sciences/articles/10.3389/flang.2026.1953328/full), inspected at methods and limitations, directly studies stronger certainty in summaries. Its semantic interpretation is limited by marker-based measurement, a small author-annotated check, and weak agreement with a corrected model judge. These limitations motivate careful evaluation, not a claim that we discovered the problem.

The standalone novelty claim is downgraded. The generic-versus-role-aware comparison remains a useful engineering decision but is not sufficient grounds for a research contribution. No local executable was found on PATH for ollama, llama-cli, or lms. This does not prove no inference resource exists; no paid endpoint was used and no actual verifier comparison was executed.

Additional market evidence: [Watchdog](https://github.com/tomcardoso/watchdog) advertises public-record document ingestion, cited facts, a chronology, and contradiction review. Repository overview inspected, not installed or benchmarked. This is direct competitive overlap with the story-dossier concept. [Event Registry's reporting timeline](https://help.eventregistry.org/event-details-reporting-timeline/) shows article publication activity; this specific view should not be confused with occurrence chronology or treated as the limit of the entire product. [Feedly's engineering article](https://feedly.com/engineering/posts/reducing-clustering-latency) distinguishes clustering different coverage of an event from removing near-duplicate content. These are existing capabilities, not our moat.

A [2025 practitioner study](https://arxiv.org/html/2503.16011v1) interviewed eight experienced Germany-based participants. Methods, results, and limitations inspected. It supports investigation documentation, collection, and verification as relevant work, but participants saw a prototype video rather than using the tool. Its sample and elicitation design do not establish broad market demand or willingness to pay.

Further prior-art leads screened: [temporal submodular coverage, 2018](https://aclanthology.org/K18-1023/) and [incremental timeline clustering, 2024](https://aclanthology.org/2024.acl-long.390/). Abstracts only. Coverage optimization and streaming chronology are not new directions simply because an LLM is included.

Decision: do not keep inventing narrower names for familiar factuality errors. Preserve the working chronology objective and evaluate the whole task: what relevant evidence is missed, what is unsupported, and how much checking the user must do. Detailed opportunity card, matched baselines, cost model, and rejection criteria are in CYCLE_3_PRODUCT_FIT.md. Product opportunity remains a hypothesis; no interviews, willingness-to-pay tests, or independent model evaluation have occurred.

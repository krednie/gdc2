# Implementation-level competitive research

Inspected 2026-11-09. These are source-code and documentation observations, not hands-on performance measurements or adoption evidence.

## Watchdog

Pinned revision: `8cb766fa003f4bacd10f4a101f4b0f013596b35d`, resolved from the public repository tree. No upstream code was executed, software installed, or model inference purchased.

The [timeline deduplication prompt](https://raw.githubusercontent.com/tomcardoso/watchdog/8cb766fa003f4bacd10f4a101f4b0f013596b35d/src/watchdog/prompts/timeline_dedup.md) preserves distinct material information and opposing perspectives rather than collapsing all descriptions of an occurrence. The [precision prompt](https://raw.githubusercontent.com/tomcardoso/watchdog/8cb766fa003f4bacd10f4a101f4b0f013596b35d/src/watchdog/prompts/timeline_precision.md) only folds a coarse date into a precise one when occurrence identity is unambiguous. These instructions do not prove successful model compliance, but they invalidate an assumption that existing tools simply deduplicate away every disagreement.

The [contradiction writer](https://raw.githubusercontent.com/tomcardoso/watchdog/8cb766fa003f4bacd10f4a101f4b0f013596b35d/src/watchdog/pipeline/contradiction.py) provides a human-gated path for adding a reviewed contradiction into maintained notes, with document references. It is a deterministic write path, not evidence that contradiction detection is solved.

The [benchmark log](https://raw.githubusercontent.com/tomcardoso/watchdog/8cb766fa003f4bacd10f4a101f4b0f013596b35d/benchmarks/FINDINGS.md) documents important-item recall, silent extraction failures, and historical scoring artifacts caused by cross-document credit. It also distinguishes corrected from obsolete comparisons. Read selected sections; did not reproduce the runs. Do not reuse historical prices or model rankings as current procurement advice.

The [October 18 extractor report](https://raw.githubusercontent.com/tomcardoso/watchdog/8cb766fa003f4bacd10f4a101f4b0f013596b35d/benchmarks/2026-10-18-frontier-results.md) explicitly limits conclusions to a single run per arm, the extractor stage, and a particular brief/corpus. Its records include substantial omission concerns despite successfully completed calls. It uses model judges with some hand-checking, not a large independent human study. Absent citations to later pages are an output-coverage warning; alone they cannot reveal which pages a model internally considered.

### Decisions

1. Cited timelines, conservative merging, human-approved contradictions, and important-item recall are existing product practices.
2. Compare against a task-capable existing system or strong general baseline. Comparing only against naive date sorting would overstate value.
3. A successful API call, valid JSON, and numerous citations are insufficient completion checks. This is concrete engineering motivation, not a newly discovered class of problem.
4. A full competitor evaluation must run matched inputs and budgets and inspect outputs. Code inspection alone supports neither superiority nor inferiority.

## Adjacent coverage research

[Coverage of Information Extraction, EMNLP 2019](https://aclanthology.org/D19-1583/) investigates predicting whether text supplies all objects of a subject-relation pair. Abstract inspected. This concerns completeness of information in text, which must be distinguished from whether an extractor recovered everything that text contains.

[ExtractBench](https://arxiv.org/html/2607.29677v1) covers schema-guided extraction, including grounding and cost; abstract and structure screened, full methodological comparison pending. [LongExtractBench](https://github.com/micro1-research/longextract-bench) offers long-document structured-extraction evaluation; repository overview screened. These make a generic 'benchmark for extraction omissions' claim weak. Neither screening pass establishes that professional chronology completion is solved.

Side opportunity: a diagnostic that distinguishes source absence, retrieval omission, extraction omission, and deliberate task-irrelevant exclusion. Keep parked until a concrete evaluation demonstrates a gap beyond existing stage-wise diagnostics. Do not build a company around this phrasing alone.

## Further direct prior art: reviewed facts to generated prose

[CAMS](https://arxiv.org/html/2606.23989v1), inspected in sections 3.3-3.6, already uses atomic claims with provenance, conservative cross-document grouping, selection, citation-bearing rewriting, and a separate verification/repair step. Its text explicitly distinguishes encouraged faithfulness from a truth guarantee. This is a close baseline for any proposed source-to-ledger-to-summary method, not evidence that such a method would be unique to Alithia.

[FactGraph](https://aclanthology.org/2022.naacl-main.236/), abstract inspected, evaluates summary factuality through semantic representations and their relations. [Proof-Carrying Numbers](https://arxiv.org/html/2509.06902v1), protocol and scope sections inspected, places numeric matching checks in the presentation layer while excluding general reasoning correctness from its guarantee. A correct displayed amount would not by itself detect the priority-order inversion in NF01. This illustrates different verification scopes; it is not an experimental comparison against either method.

## Claim-verification vendor overlap

[Factiverse](https://www.factiverse.ai/) explicitly markets claim detection and evidence checking to media/research, intelligence, and model builders. Homepage and media/research page inspected. This is competitive overlap with Alithia's original verifier direction. Its superiority, customer, language, and security statements are vendor claims, not findings reproduced here. No account created, product tested, trial started, or purchasing recommendation made.

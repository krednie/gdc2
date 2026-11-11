# Alithia: research-readiness findings

Read-only application inspection and isolated probe, 2026-11-09. No application changes, application startup, environment-secret inspection, or external model calls. Existing user changes were left untouched.

## Executed finding: selected sources can exceed visible evidence

`backend/verifier.py` selects up to 12 chunks, clips each source body to 800 characters, and clips the assembled evidence to 6,000 characters. Source cards are then built separately from the first eight unique URLs in the selected set.

`probe_alithia_evidence_visibility.py` isolates the existing pure formatting function using Python's AST, avoiding imports that could initialize models or load credentials. Its controlled fixture supplies twelve distinct sources with 800-character bodies and ordinary metadata.

Observed:

- Six bodies survive completely.
- The seventh body is partial.
- The eighth source's title and body do not reach the formatted context.
- Under the separately inspected top-eight-card rule, that eighth source still becomes a source card.
- A second controlled input places a qualification after character 800; it is absent from the formatter output.

Results and source/function hashes: `alithia_evidence_visibility_results.json`. Three assertions passed. These are deterministic context-visibility results, not production failure rates or evidence that a model actually relied on an unseen source. The card-building rule was simulated from source inspection rather than running the full endpoint.

Implication: distinguish retrieved sources from evidence actually supplied to the verifier, and distinguish both from passages verified to support the final statement. A source card can legitimately be a research lead, but should not silently mean all three.

## Other inspected boundaries

| Current representation or behavior | Why it matters for chronology research | Appropriate next step, not implemented |
|---|---|---|
| `SourceChip` exposes title, URL, source, tier, score | Does not itself preserve the exact supporting passage or an assertion-to-span link | Record evidence IDs and actual presented spans in experiment traces |
| Retriever `Chunk` lacks event-time, observation-time, and source-version fields | Current retrieval records cannot alone support historical-version or as-known-then evaluation | Add such metadata only to a research adapter first, with explicit unknown values |
| Scraper `Article` has `scraped_at` and URL hash | Retrieval time is useful but is not occurrence time; URL identity is not content-version identity | Track content versions separately when testing updates |
| `_dedup` rejects a previously seen URL hash | In this corpus-building path, revised content at the same URL can be excluded | Test revision handling before using this path for developing-story monitoring |
| `_calibrate_confidence` adjusts an LLM label using retrieval-score thresholds | This is a heuristic; no empirical calibration follows merely from the function name | Measure reliability on labeled cases; do not present the label as a calibrated probability |
| `main.py` contains a seeded result-cache entry and fallback trending material | Demonstration output must not enter an evaluation as fresh source-backed inference | Bypass or explicitly label seeded outputs in any future benchmark |

These are scoped findings from inspected modules, not a complete security or production-readiness review. Other ingestion routes can behave differently. No claim is made that acquiring more source text requires changing every module above.

## What to reuse

The existing API/UI scaffolding, retrieval adapters, claim extraction interface, and uncertainty fallback are useful prototype assets. Keep the claim verifier available as a baseline. It answers a different question from chronology completion: judging supplied claims does not discover all missing events in an assignment.

## What not to build yet

Do not purchase a scraping service simply to feed this pipeline more text before measuring how much evidence actually reaches the decision step. Hosted extraction may improve acquisition; it cannot by itself repair truncation, provenance, event selection, or downstream rewriting.

Do not rewrite the application into a large graph or multi-agent platform on the strength of these probes. First build a research trace outside the serving path: source acquired, passage retained, passage presented, assertion emitted, assertion checked, user accepted. Treat those as distinct states and measure where task-relevant information disappears.

## Candidate technical contribution, still unproven

A budget-aware policy that allocates acquisition, interpretation, and review effort to unresolved task requirements could be useful. It must outperform strong retrieval/verification baselines under matched total cost. Evidence accounting is necessary instrumentation, not by itself a novel algorithm or a moat.

The immediate practical outcome is a reproducible failure inventory and a fair comparison setup. That is a stronger foundation for an exceptional product than adding capabilities whose effect on the final dossier is unknown.

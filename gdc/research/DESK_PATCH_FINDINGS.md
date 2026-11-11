# Edit one sentence; keep the other assignment open

Offline research prototype, 12 Nov 2026. No API requests, production changes, or human participants. The task is maintaining a current lead, not retroactively rewriting an archived article. Historical prose would need a separate correction/update policy.

Run from the repository root:

    python gdc/research/desk_patch.py gdc/research/starliner_desk_fixture.json --as-of 2024-09-07
    python gdc/research/desk_retrieval_probe.py
    python -m unittest discover -s gdc/research -p "test_*.py"

The first command prints the original sentence, a proposed replacement and inspectable primary-source evidence. No write-back is implemented. The March cutoff (2025-03-18) shows two eligible replacements against the same original draft; it does not pretend the editor accepted September's edit. “No proposed edit” means the queue received no eligible change, **not** that the sentence is true.

## What's automatic, and what is not

Release cutoff, event-key matching, exact evidence-text fingerprints, expected original sentence version, and routing of competing edits to review are automatic. Event keys, availability dates, evidence references and replacement wording in this fixture are hand-supplied. A matching fingerprint proves neither entailment nor historical availability: the packet is a modern capture of a dated release. Even perfectly matching evidence can be attached to a bad claim. The printed queue helps inspect that failure; it doesn't solve it.

## Retrieval check, including a baseline that beats us

Can we find the evidence without the supplied paragraph IDs? Use the standing draft sentence as a query over only the seven paragraphs of the incoming release. BM25 on lowercase word tokens vs the first two article paragraphs, at a matched two-paragraph budget. The reference set is the demonstrator's chosen support, not an exhaustive relevance annotation. Ranks are one-based.

| Replacement | Chosen support | BM25 ranks | First two article paragraphs | BM25 top two |
|---|---|---|---|---|
| Sept: capsule landed | D2P1 | 7th | 1/1 | 0/1 |
| March: original astronauts returned via Dragon | D3P1 + D3P2 | 5th + 4th | 2/2 | 0/2 |

September's top keyword result is D2P6: excellent background on the people and the old decision, but no landing confirmation. March's is D3P4: it recounts the crew's launch and undocking, not their splashdown. Conversely, the March lead alone gives the vehicle and mission but doesn't name the two people: the following paragraph matters. The two paragraphs together support the sentence. See the [September release](https://www.nasa.gov/news-release/nasa-boeing-welcome-starliner-spacecraft-to-earth-close-mission/) and [March release](https://www.nasa.gov/news-release/welcome-home-nasas-spacex-crew-9-back-on-earth-after-science-mission/).

These are two selected updates from press releases of one institution; a strong lead-position bias is plausible. We measured lookup, not relevance classification or latency. There is no evidence here that lexical retrieval generally fails, or that embeddings would fix it. No-change rows also have highest-ranked passages: neither ranker decides whether an edit is warranted.

## Founder decision

Keep the lead-first option. Next offline discriminating test: freeze cases from a different document form (e.g. meeting minutes with actions near the end); include related releases that **do not** change the standing sentence. Compare lead-first, lexical retrieval, and an event-aware candidate selector on the same paragraph budget. Count both sufficient support for real edits and needless alerts on unchanged items. Separate a cheap source-type heuristic from any claimed research contribution. Don't buy scraping capacity or introduce a graph store to solve this two-release example.

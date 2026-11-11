"""Small authored diagnostic, NOT a model benchmark or trained classifier.

Evidence is researcher-paraphrased from linked primary pages. Structured fields
are manually supplied oracle annotations. Negative claims are deliberate edits,
not allegations that a real system produced these errors. No inference API used.
"""
import json
from pathlib import Path

SOURCES = {
    "apple": {
        "url": "https://www.apple.com/newsroom/2024/01/apple-vision-pro-available-in-the-us-on-february-2/",
        "published": "2024-01-08",
        "evidence": "Apple announced on January 8 that U.S. availability was scheduled for February 2, with preorders starting January 19.",
    },
    "faa": {
        "url": "https://www.faa.gov/newsroom/faa-halts-boeing-max-production-expansion-improve-quality-control-also-lays-out-extensive",
        "published": "2024-01-24",
        "evidence": "On January 24 the FAA approved an inspection process. Each grounded aircraft could return to service after successfully completing that process.",
    },
    "nasa": {
        "url": "https://www.nasa.gov/blogs/boeing-crew-flight-test/2024/08/24/nasa-decides-to-bring-starliner-spacecraft-back-to-earth-without-crew/",
        "published": "2024-08-24",
        "evidence": "NASA announced an uncrewed Starliner return on August 24. The astronauts were to return on Dragon; Starliner's departure was expected in early September.",
    },
}

# Fields: ID, source, claim, target date, semantic role, annotation, error class.
# Roles and gold labels are visible; these are development fixtures, not held-out.
CASES = [
    ("A1", "apple", "Apple announced the U.S. availability schedule on January 8.", "2024-01-08", "announcement", True, "control"),
    ("A2", "apple", "Apple scheduled U.S. availability for February 2.", "2024-02-02", "planned", True, "control"),
    ("A3", "apple", "Vision Pro was already available in U.S. stores on January 8.", "2024-01-08", "completed", False, "announcement_as_occurrence"),
    ("A4", "apple", "The January 8 announcement proves the February 2 launch subsequently happened.", "2024-02-02", "completed", False, "plan_as_outcome"),
    ("F1", "faa", "The FAA approved the inspection process on January 24.", "2024-01-24", "approval", True, "control"),
    ("F2", "faa", "Return was conditional on successful inspections; the statement does not establish each aircraft's return date.", None, "conditional", True, "control"),
    ("F3", "faa", "All grounded aircraft had completed inspections and returned on January 24.", "2024-01-24", "completed", False, "condition_as_outcome"),
    ("F4", "faa", "Boeing, rather than the FAA, approved the inspection process on January 24.", "2024-01-24", "approval", False, "actor_substitution"),
    ("N1", "nasa", "NASA announced its decision on August 24.", "2024-08-24", "decision", True, "control"),
    ("N2", "nasa", "Starliner's departure was expected in early September.", "2024-09", "planned", True, "control"),
    ("N3", "nasa", "Starliner returned to Earth on August 24.", "2024-08-24", "completed", False, "decision_as_occurrence"),
    ("N4", "nasa", "The announcement establishes September 1 as the exact departure day.", "2024-09-01", "planned", False, "precision_inflation"),
]


def metrics(predictions):
    # Positive means flagged as unsupported; gold False means unsupported.
    tp = sum(flag and not case[5] for flag, case in zip(predictions, CASES))
    fp = sum(flag and case[5] for flag, case in zip(predictions, CASES))
    fn = sum(not flag and not case[5] for flag, case in zip(predictions, CASES))
    tn = sum(not flag and case[5] for flag, case in zip(predictions, CASES))
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn,
            "precision": tp/(tp+fp) if tp+fp else None,
            "recall": tp/(tp+fn) if tp+fn else None}


def main():
    # Baseline 1: source date must equal asserted target date.
    publication_match = [c[3] is not None and c[3] != SOURCES[c[1]]["published"] for c in CASES]
    # Baseline 2: no future target allowed. Month values compare lexically here;
    # no overlapping-month case is included, so this is only a toy baseline.
    reject_future = [c[3] is not None and c[3] > SOURCES[c[1]]["published"] for c in CASES]
    # Ablation: hand-provided modality only, not a complete verifier.
    # None of the three selected evidence paraphrases establishes a completed
    # physical return/availability event. Actor/date precision remain unchecked.
    oracle_modality = [c[4] == "completed" for c in CASES]
    result = {
        "scope": "12 deliberately authored development cases, three source pages, no model calls, no held-out validation",
        "sources": SOURCES,
        "cases": [dict(zip(("id", "source", "claim", "date", "oracle_role", "supported", "error_class"), c)) for c in CASES],
        "results": {"publication_date_match": metrics(publication_match),
                    "reject_future_dates": metrics(reject_future),
                    "oracle_modality_only": metrics(oracle_modality)},
        "interpretation": "Oracle modality is diagnostic only. Its inputs contain hand labels unavailable to the other baselines. These scores do not establish model superiority or novelty.",
        "unmeasured": ["automatic extraction", "generic LLM verification", "historical source-version integrity", "generalization", "human label agreement", "customer value"],
    }
    Path(__file__).with_name("temporal_role_probe_results.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result["results"], indent=2))


if __name__ == "__main__":
    main()

"""Compare cheap signals with published model-judge coverage labels.

See COVERAGE_PROXY_PROTOCOL.md. This runs no models and makes no causal claim.
"""
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
from audit_published_packets import REV, fetch_json


def ordering(a, b):
    return (a > b) - (a < b)


def classify_pair(a, b, proxy, outcome):
    p = ordering(a[proxy], b[proxy])
    q = ordering(a[outcome], b[outcome])
    if p == 0 and q == 0:
        return "both_tied"
    if p == 0:
        return "proxy_tied"
    if q == 0:
        return "outcome_tied"
    return "concordant" if p == q else "discordant"


def main():
    assert ordering(2, 1) == 1 and ordering(1, 2) == -1 and ordering(1, 1) == 0
    assert classify_pair({"p": 2, "q": 1}, {"p": 1, "q": 2}, "p", "q") == "discordant"
    mapping, mapping_hash = fetch_json("mapping.json")
    documents = []
    allowed = {"verbatim", "credited", "ungrounded"}
    for name in sorted(mapping):
        packet, packet_hash = fetch_json(f"packet-{name}.json")
        judged, judgment_hash = fetch_json(f"judgment-{name}.json")
        ids = [item["id"] for item in packet["items"]["must_not_miss"]]
        if not ids or len(ids) != len(set(ids)):
            raise ValueError(f"Invalid important-item IDs: {name}")
        outputs = []
        for arm, output in packet["arms"].items():
            tiers = [judged["judgments"][key][arm]["tier"] for key in ids]
            if not set(tiers) <= allowed:
                raise ValueError(f"Unexpected tiers in {name}: {set(tiers)}")
            facts = output["key_facts"]
            pages = {f.get("page") for f in facts if type(f.get("page")) is int and f["page"] > 0}
            outputs.append({
                "arm": arm, "fact_count": len(facts),
                "summary_characters": len(output["summary"]), "distinct_cited_pages": len(pages),
                "important_items": len(ids),
                "credited_count": sum(t in {"verbatim", "credited"} for t in tiers),
                "strict_count": tiers.count("verbatim"),
            })
        documents.append({"document": name, "packet_sha256": packet_hash,
                          "judgment_sha256": judgment_hash, "outputs": outputs})
    comparisons = []
    for outcome, proxy, exclude_empty in itertools.product(
        ["credited_count", "strict_count"],
        ["fact_count", "summary_characters", "distinct_cited_pages"], [False, True]
    ):
        counts = {key: 0 for key in ["concordant", "discordant", "proxy_tied", "outcome_tied", "both_tied"]}
        inversions = []
        for doc in documents:
            for a, b in itertools.combinations(doc["outputs"], 2):
                if exclude_empty and (a["fact_count"] == 0 or b["fact_count"] == 0):
                    continue
                kind = classify_pair(a, b, proxy, outcome)
                counts[kind] += 1
                if kind == "discordant":
                    inversions.append({"document": doc["document"], "a": a["arm"], "b": b["arm"],
                                       "proxy_values": [a[proxy], b[proxy]],
                                       "coverage_hits": [a[outcome], b[outcome]],
                                       "coverage_denominator": a["important_items"]})
        untied = counts["concordant"] + counts["discordant"]
        comparisons.append({"outcome": outcome, "proxy": proxy, "exclude_empty": exclude_empty,
                            "counts": counts, "total_pairs": sum(counts.values()),
                            "untied_pairs": untied,
                            "conditional_concordance": counts["concordant"] / untied if untied else None,
                            "inversions": inversions})
    result = {"retrieved_at_utc": datetime.now(timezone.utc).isoformat(), "revision": REV,
              "mapping_sha256": mapping_hash, "label_source": "published_model_judge_not_independent_human_gold",
              "documents": documents, "comparisons": comparisons}
    Path(__file__).with_name("coverage_proxy_results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in comparisons:
        print(row["outcome"], row["proxy"], "exclude_empty=" + str(row["exclude_empty"]), row["counts"])
        if row["inversions"]:
            print("Example", json.dumps(row["inversions"][0]))


if __name__ == "__main__":
    main()

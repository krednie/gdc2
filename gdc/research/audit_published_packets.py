"""Structural audit of public historical evaluation packets, not a model rerun."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

REV = "8cb766fa003f4bacd10f4a101f4b0f013596b35d"
BASE = f"https://raw.githubusercontent.com/tomcardoso/watchdog/{REV}/benchmarks/qualitative/"


def fetch_json(name):
    with urlopen(BASE + name, timeout=30) as response:
        raw = response.read()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def main():
    mapping, mapping_hash = fetch_json("mapping.json")
    rows = []
    for document in sorted(mapping):
        packet, packet_hash = fetch_json(f"packet-{document}.json")
        for arm, output in packet["arms"].items():
            facts = output.get("key_facts")
            summary = output.get("summary", "")
            rows.append({
                "document": document, "arm_code": arm, "arm_name": mapping[document][arm],
                "packet_sha256": packet_hash,
                "key_facts_count": len(facts) if isinstance(facts, list) else None,
                "summary_characters": len(summary) if isinstance(summary, str) else None,
                "coverage_gap_field_present": "coverage_gap" in output,
                "coverage_gap_value": output.get("coverage_gap"),
                "empty_facts_without_gap_flag": isinstance(facts, list) and not facts and not output.get("coverage_gap"),
            })
    report = {
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository_revision": REV, "mapping_sha256": mapping_hash,
        "kind": "structural_reanalysis_of_published_packets_not_fresh_model_outputs",
        "documents": len(mapping), "outputs": len(rows),
        "empty_facts_without_gap_flag_count": sum(row["empty_facts_without_gap_flag"] for row in rows),
        "rows": rows,
        "limitations": ["Nonempty facts do not prove completeness or correctness.",
                        "These historical packets are not the current product's outputs.",
                        "No inference costs, success logs, or model behavior reproduced.",
                        "A missing gap flag is not a universal product promise of completeness."]
    }
    target = Path(__file__).with_name("published_packet_audit_results.json")
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("documents", "outputs", "empty_facts_without_gap_flag_count")}))
    for row in rows:
        if row["empty_facts_without_gap_flag"]:
            print(json.dumps(row))


if __name__ == "__main__":
    main()

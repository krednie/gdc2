"""Compare visibility contracts, not model accuracy, on one controlled fixture."""
import ast
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from evidence_packet import Evidence, pack_evidence


def main():
    source_path = Path(__file__).resolve().parents[2] / "backend" / "verifier.py"
    source = source_path.read_text(encoding="utf-8")
    function = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef) and n.name == "_build_evidence_text")
    namespace = {"RetrievedChunk": SimpleNamespace}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(source_path), "exec"), namespace)
    items, chunks = [], []
    for i in range(1, 13):
        start, end = f"BODY_{i:02d}_START|", f"|BODY_{i:02d}_END"
        text = start + "x" * (800 - len(start) - len(end)) + end
        item = Evidence(f"https://example.invalid/evidence/document-{i:02d}", f"Controlled evidence document {i:02d}", text)
        items.append(item)
        chunks.append(SimpleNamespace(chunk=SimpleNamespace(url=item.url, title=item.title, text=item.text,
                                                           source=f"fixture-source-{i:02d}", source_tier="fixture")))
    old = namespace[function.name](chunks)
    new = pack_evidence(items, 6000)
    old_full = sum(f"|BODY_{i:02d}_END" in old for i in range(1, 13))
    old_started = sum(f"BODY_{i:02d}_START|" in old for i in range(1, 13))
    report = {
        "kind": "synthetic_contract_comparison_not_model_performance",
        "formatter_sha256": hashlib.sha256(ast.get_source_segment(source, function).encode()).hexdigest(),
        "input_sources": 12, "character_budget": 6000,
        "existing": {"used_characters": len(old), "complete_bodies": old_full,
                     "partial_bodies": old_started - old_full, "source_cards_under_inspected_rule": 8,
                     "cards_with_no_body": sum(f"BODY_{i:02d}_START|" not in old for i in range(1, 9))},
        "whole_chunk_baseline": {"used_characters": new["used_characters"],
                                 "complete_bodies": len(new["presented"]), "partial_bodies": 0,
                                 "source_cards": len(new["source_cards"]),
                                 "explicitly_omitted": len(new["omitted"]), "cards_with_no_body": 0},
        "interpretation": "The helper aligns cards with complete presented chunks. It may discard useful partial evidence and is not a demonstrated accuracy improvement."
    }
    assert len(new["source_cards"]) == len(new["presented"])
    assert all(json.loads(new["context"][r["context_start"]:r["context_end"]])["text"] == items[r["input_position"]].text for r in new["presented"])
    Path(__file__).with_name("evidence_packing_comparison.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

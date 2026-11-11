"""Run only Alithia's pure evidence formatter on a controlled fixture.

No application imports, environment loading, network, model calls, or app edits.
This tests context visibility, not a real model's factual accuracy.
"""
import ast
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace


def main():
    root = Path(__file__).resolve().parents[2]
    source_path = root / "backend" / "verifier.py"
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                    and node.name == "_build_evidence_text")
    namespace = {"RetrievedChunk": SimpleNamespace}
    isolated = ast.Module(body=[function], type_ignores=[])
    exec(compile(isolated, str(source_path), "exec"), namespace)
    formatter = namespace[function.name]
    chunks = []
    for i in range(1, 13):
        start, end = f"BODY_{i:02d}_START|", f"|BODY_{i:02d}_END"
        body = start + ("x" * (800 - len(start) - len(end))) + end
        chunks.append(SimpleNamespace(chunk=SimpleNamespace(
            source=f"fixture-source-{i:02d}", source_tier="fixture",
            title=f"Controlled evidence document {i:02d}",
            url=f"https://example.invalid/evidence/document-{i:02d}", text=body)))
    evidence = formatter(chunks)
    rows = []
    for i, chunk in enumerate(chunks, 1):
        start, end = f"BODY_{i:02d}_START|", f"|BODY_{i:02d}_END"
        rows.append({"source_number": i, "selected": True,
                     "displayed_by_top_eight_card_rule": i <= 8,
                     "title_visible": chunk.chunk.title in evidence,
                     "body_start_visible": start in evidence,
                     "body_end_visible": end in evidence})
    # Separate fixture: a material qualifier after the per-chunk clipping boundary.
    qualifier = "This describes a plan, not a completed event."
    long_chunk = SimpleNamespace(chunk=SimpleNamespace(
        source="fixture", source_tier="fixture", title="Late qualification",
        url="https://example.invalid/late-qualification", text="a" * 810 + qualifier))
    truncated = formatter([long_chunk])
    assert qualifier not in truncated
    assert formatter([]) == ""
    assert len(evidence) == 6000
    report = {
        "kind": "controlled_formatter_probe_not_model_benchmark",
        "source_file": str(source_path), "source_file_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "function_sha256": hashlib.sha256(ast.get_source_segment(source, function).encode()).hexdigest(),
        "selected_chunks": len(chunks), "evidence_characters": len(evidence),
        "cards_rule": "top eight unique URLs, read from verify_claim; simulated, not endpoint execution",
        "rows": rows,
        "displayed_sources_with_no_body_start": sum(r["displayed_by_top_eight_card_rule"] and not r["body_start_visible"] for r in rows),
        "displayed_sources_with_incomplete_body": sum(r["displayed_by_top_eight_card_rule"] and not r["body_end_visible"] for r in rows),
        "late_qualifier_present_in_input": True, "late_qualifier_visible_to_formatter_output": qualifier in truncated,
        "assertions_passed": 3,
        "limitations": ["Controlled 800-character bodies, not production traffic.",
                        "No claim that the model cited or relied on an unseen source.",
                        "Source cards may represent retrieved leads, but should then be labeled accordingly."]
    }
    Path(__file__).with_name("alithia_evidence_visibility_results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

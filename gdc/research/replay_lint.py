"""Review cues, not a truth classifier. Reads replay JSONL, prints JSON."""
import json
import re
import sys
from datetime import date
from pathlib import Path


def inspect(cutoff, entries):
    boundary=date.fromisoformat(cutoff)
    latest=None
    flags=[]
    for n,entry in enumerate(entries,1):
        m=re.match(r"^(\d{4}-\d\d-\d\d)(?:$|\s|/|-)",entry["date"])
        try: start=date.fromisoformat(m[1]) if m else None
        except ValueError: start=None
        if start is None:
            flags.append((n,"review_date_precision")); continue
        if latest and start<latest: flags.append((n,"out_of_order"))
        latest=max(latest,start) if latest else start
        if start>boundary and re.search(r"\b(takes place|is held|occurs|was held|concludes|took place)\b",
                                        entry["event"],re.I):
            flags.append((n,"future_row_with_occurrence_language"))
    return flags


if __name__=="__main__":
    for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
        row=json.loads(line)
        if row["status"]=="ok":
            print(json.dumps([row["cutoff"],row["arm"],inspect(row["cutoff"],row["answer"]["entries"])]))

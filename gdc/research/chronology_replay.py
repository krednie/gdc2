"""Small cutoff replay: fixed public page observations, no crawling or app writes."""
import argparse
import json
from pathlib import Path
from urllib.request import Request, build_opener
from urllib.error import HTTPError
from run_verifier_eval import credentials, ENDPOINT, NoRedirect, sha

BASE = "https://www.ntsb.gov/news/press-releases/Pages/"
# Researcher transcriptions/paraphrases; not historical copies or full pages.
PAGES = [
    ("A", "2023-05-24", BASE+"NR20230524.aspx",
     "A Norfolk Southern train derailed in East Palestine on Feb 3; hazardous material was released and fires followed. NTSB schedules a June 21 community meeting and June 22–23 investigative hearing. Topics include the emergency response, the decision about the five tank cars, and wheel bearing failures.",
     "Events: June 25 2024 East Palestine Board Meeting. News: Failed Wheel Bearing Caused Norfolk Southern Train Derailment in East Palestine, Ohio. NTSB: Decision to vent and burn hazmat tank cars unnecessary. June 25, 2024."),
    ("B", "2024-02-07", BASE+"NR20240206.aspx",
     "NTSB says a two-day investigative hearing took place last June. By today the accident docket contains over 1,800 pages, and the hearing docket over 5,000 including transcripts. A June 25 board meeting is scheduled for a vote on findings, probable cause and recommendations. Two community meetings are planned for June 24 and 25.",
     "News: September 24, 2024 illustrated digest released. June 25, 2024: failed wheel bearing caused derailment; NTSB calls the vent and burn unnecessary."),
    ("C", "2024-06-25", BASE+"NR20240625.aspx",
     "At today's East Palestine board meeting NTSB attributes the Feb 3, 2023 derailment to a defective, overheated bearing. Investigators found the local incident commander's decision three days after the derailment unnecessary and based on incomplete and misleading information from the railroad and its contractors. New safety recommendations were issued. The report abstract is available; the full report is expected in the coming weeks.",
     "News: September 24, 2024 illustrated digest released.")
]
PROMPT = ("You are handing a chronological research brief to the next local reporter on shift. "
          "Using only the supplied records, give up to 6 dated entries on the derailment and investigation "
          "as known at the cutoff, then one useful unresolved question. Include material changes and "
          "avoid hindsight. Related links may postdate the release. Cite record IDs. Return JSON "
          'as {"entries":[{"date":"...","event":"...","sources":["A"]}],"question":"..."}.')

def jobs():
    for cutoff in [p[1] for p in PAGES]:
        for arm in ("page", "body"):
            records = [{"id":i,"published":d,"text":b+("\n"+r if arm=="page" else "")}
                       for i,d,_,b,r in PAGES if d<=cutoff]
            yield cutoff, arm, {"model":"openai/gpt-oss-120b","temperature":0,"seed":731,
                "reasoning_effort":"low","max_completion_tokens":1500,"response_format":{"type":"json_object"},
                "messages":[{"role":"system","content":PROMPT},{"role":"user","content":json.dumps(
                    {"cutoff":cutoff,"records":records},ensure_ascii=False)}]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--execute",action="store_true")
    args=ap.parse_args()
    batch=list(jobs())
    reserve=sum(((len(json.dumps(p).encode())+512)*0.15+1500*0.60)/1e6 for _,_,p in batch)
    if len(batch)>6 or reserve>0.02: raise SystemExit("request reservation exceeded")
    key=credentials()[0] if args.execute else None
    if args.execute and not key: raise SystemExit("no configured provider credential")
    opener=build_opener(NoRedirect())
    with args.out.open("x",encoding="utf-8") as f:
        for cutoff,arm,payload in batch:
            row=dict(cutoff=cutoff,arm=arm,request_hash=sha(payload),reserve_batch_usd=reserve,status="dry")
            if args.execute:
                req=Request(ENDPOINT,data=json.dumps(payload).encode(),headers={
                    "Authorization":"Bearer "+key,"Content-Type":"application/json","Accept":"application/json",
                    "User-Agent":"AlithiaResearch/0.1"})
                try:
                    with opener.open(req,timeout=45) as response: result=json.load(response)
                    ch=result["choices"][0]
                    row.update(usage={k:result["usage"][k] for k in ("prompt_tokens","completion_tokens")},
                               answer=json.loads(ch["message"]["content"]))
                    if ch["finish_reason"]!="stop" or not isinstance(row["answer"]["entries"],list):
                        raise ValueError("incomplete")
                    row["status"]="ok"
                except HTTPError as exc: row.update(status="error",http=exc.code)
                except Exception as exc: row.update(status="error",error=type(exc).__name__)
            f.write(json.dumps(row,ensure_ascii=False)+"\n"); f.flush()
            print(cutoff,arm,row["status"],flush=True)
            if row["status"]=="error": break

if __name__=="__main__": main()

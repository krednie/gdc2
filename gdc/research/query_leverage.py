"""Print one compact evidence neighborhood. No provider calls or indexing side effects."""
import argparse
import json
from pathlib import Path

def neighborhood(graph, key):
    nodes=graph["nodes"]
    if key not in nodes: raise KeyError(key)
    rows=[]
    for left, relation, right in graph["edges"]:
        if left not in nodes or right not in nodes: raise ValueError("dangling edge")
        if key in (left,right):
            peer=right if key==left else left
            rows.append({"edge":[left,relation,right],"peer":nodes[peer]})
    return {"node":nodes[key],"neighbors":rows}

if __name__=="__main__":
    graph=json.loads(Path(__file__).with_name("leverage_map.json").read_text(encoding="utf-8"))
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("node",choices=sorted(graph["nodes"]))
    parser.add_argument("--brief",action="store_true",help="Compact working context; follow source pointers on demand.")
    args=parser.parse_args()
    result=neighborhood(graph,args.node)
    if args.brief:
        print(f"{args.node}: {result['node'][1]}")
        for r in result["neighbors"]:
            left, relation, right=r["edge"]
            print(f"{left} {relation} {right} | {r['peer'][2]}")
    else:
        print(json.dumps(result,indent=2,ensure_ascii=False))

import copy
import json
import unittest
from pathlib import Path
from desk_patch import index_packet, review


class DeskPatchTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parent
        f = json.loads((root/"starliner_desk_fixture.json").read_text(encoding="utf-8"))
        self.story, self.proposals = f["story"], f["proposals"]
        self.index = index_packet(json.loads((root/f["packet"]).read_text(encoding="utf-8")))

    def run_case(self, cutoff="2024-09-07"):
        return review(self.story, self.proposals, self.index, cutoff)

    def test_release_day_not_landing_day(self):
        self.assertEqual(self.run_case("2024-09-06")[0]["state"], "no_proposed_edit")

    def test_only_capsule_in_september(self):
        self.assertEqual([v["state"] for v in self.run_case()],
                         ["proposed_edit","no_proposed_edit","no_proposed_edit"])

    def test_march_preserves_decision(self):
        rows = self.run_case("2025-03-18")
        self.assertEqual([s["id"] for s in rows[1]["candidates"][0]["sources"]], ["D3P1","D3P2"])
        self.assertEqual(rows[2]["state"], "no_proposed_edit")

    def test_editor_change_prevents_clobber(self):
        self.story[0]["text"] += " Updated."
        self.assertEqual(self.run_case()[0]["state"], "needs_review")

    def test_mutated_citation(self):
        self.index["D2P1"]["text"] += " changed"
        self.assertEqual(self.run_case()[0]["candidates"], [])

    def test_foreign_or_future_ref(self):
        self.proposals[0]["refs"] = self.proposals[1]["refs"]
        self.assertEqual(self.run_case()[0]["state"], "needs_review")

    def test_competing_edits_do_not_win_by_input_order(self):
        rival = copy.deepcopy(self.proposals[0])
        rival.update(id="rival", text="A competing interpretation.")
        self.proposals.append(rival)
        self.assertEqual(self.run_case()[0]["state"], "needs_review")

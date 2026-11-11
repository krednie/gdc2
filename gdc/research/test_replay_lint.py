import unittest
from replay_lint import inspect
from chronology_replay import jobs


class ReplayTests(unittest.TestCase):
    def test_cutoff(self):
        import json
        for cutoff,arm,job in jobs():
            records=json.loads(job["messages"][1]["content"])["records"]
            self.assertTrue(all(r["published"]<=cutoff for r in records))
            self.assertEqual(any("News:" in r["text"] for r in records),arm=="page")

    def test_review_flags(self):
        entries=[{"date":d,"event":t} for d,t in [
            ("2024-06-22-2024-06-23","Hearing is held"),
            ("2024-06-24","Meeting planned"),
            ("2024-02-01","Docket available"),
            ("2024-02-30","Invalid")]]
        self.assertEqual(inspect("2024-02-07",entries),[(1,"future_row_with_occurrence_language"),
            (3,"out_of_order"),(4,"review_date_precision")])

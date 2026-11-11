import json
import unittest
from run_verifier_eval import make_jobs, validate, score, CASES


class EvaluationTests(unittest.TestCase):
    def test_jobs_no_labels(self):
        jobs = make_jobs("openai/gpt-oss-120b")
        self.assertEqual(len(jobs), 6)
        for job in jobs:
            data = json.loads(job["payload"]["messages"][1]["content"])
            self.assertEqual(set(data), {"evidence", "claims"})
            self.assertTrue(all(set(c) == {"id", "claim"} for c in data["claims"]))

    def test_valid(self):
        self.assertEqual(len(validate('{"predictions":[{"id":"a","supported":true,"reason":"ok"}]}', ["a"])), 1)

    def test_bad_ids(self):
        with self.assertRaises(ValueError):
            validate('{"predictions":[{"id":"b","supported":true,"reason":"ok"}]}', ["a"])

    def test_string_boolean(self):
        with self.assertRaises(ValueError):
            validate('{"predictions":[{"id":"a","supported":"false","reason":"ok"}]}', ["a"])

    def test_duplicate_ids(self):
        with self.assertRaises(ValueError):
            validate(json.dumps({"predictions": [{"id": "a", "supported": True, "reason": ""}] * 2}), ["a", "b"])

    def test_missing_is_not_perfect(self):
        self.assertEqual(score([])["generic"]["missing_cases"], 12)
        self.assertIsNone(score([])["generic"]["accuracy_on_scored"])

    def test_correct_confusion(self):
        rows = [{"arm": "generic", "status": "ok", "predictions": [
            {"id": c[0], "supported": c[5]} for c in CASES]}]
        result = score(rows)["generic"]
        self.assertEqual((result["tp"], result["tn"], result["fp"], result["fn"]), (6, 6, 0, 0))
        self.assertEqual(result["correct_of_planned"], 1)


if __name__ == "__main__":
    unittest.main()

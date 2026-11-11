import json
import unittest
from evidence_packet import Evidence, pack_evidence


class PacketTests(unittest.TestCase):
    def item(self, text="evidence", url="https://example.invalid/a"):
        return Evidence(url=url, title="A source", text=text)

    def test_empty(self):
        self.assertEqual(pack_evidence([])["context"], "")

    def test_zero_budget(self):
        result = pack_evidence([self.item()], 0)
        self.assertEqual(len(result["source_cards"]), 0)
        self.assertEqual(result["omitted"][0]["reason"], "budget")

    def test_exact_boundary(self):
        item = self.item()
        full = pack_evidence([item])
        self.assertEqual(len(pack_evidence([item], len(full["context"]))["presented"]), 1)
        self.assertEqual(len(pack_evidence([item], len(full["context"]) - 1)["presented"]), 0)

    def test_qualifier_not_clipped(self):
        text = "a" * 810 + " This is a plan, not completion."
        result = pack_evidence([self.item(text)])
        self.assertEqual(json.loads(result["context"])["text"], text)

    def test_duplicate(self):
        item = self.item()
        result = pack_evidence([item, item])
        self.assertEqual((len(result["presented"]), len(result["duplicates"])), (1, 1))

    def test_updated_url(self):
        result = pack_evidence([self.item("original"), self.item("revised")])
        self.assertEqual(len(result["presented"]), 2)
        self.assertNotEqual(result["presented"][0]["id"], result["presented"][1]["id"])

    def test_distinct_sources_not_independent_claim(self):
        result = pack_evidence([self.item(), self.item(url="https://example.invalid/b")])
        self.assertEqual(len(result["presented"]), 2)
        self.assertTrue(all(c["status"] == "presented_not_verified" for c in result["source_cards"]))

    def test_skip_large_keep_small(self):
        result = pack_evidence([self.item("x" * 7000), self.item("small")])
        self.assertEqual(len(result["presented"]), 1)
        self.assertEqual(len(result["omitted"]), 1)

    def test_offsets_and_card_identity(self):
        result = pack_evidence([self.item(), self.item("b")])
        for row, card in zip(result["presented"], result["source_cards"]):
            block = json.loads(result["context"][row["context_start"]:row["context_end"]])
            self.assertEqual(block["evidence_id"], card["evidence_id"])
            self.assertEqual(block["evidence_id"], row["id"])

    def test_empty_text(self):
        self.assertEqual(pack_evidence([self.item(" ")])["omitted"][0]["reason"], "empty_text")

    def test_invalid_budget(self):
        for budget in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                pack_evidence([], budget)

    def test_unicode_and_escaping(self):
        text = 'हिन्दी\n"text": "not a new record"'
        result = pack_evidence([self.item(text)])
        self.assertEqual(json.loads(result["context"])["text"], text)


if __name__ == "__main__":
    unittest.main()

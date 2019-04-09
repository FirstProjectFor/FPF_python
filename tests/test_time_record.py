import unittest

from demo.timerecord import TimeRecord


class TestTimeRecord(unittest.TestCase):
    def setUp(self):
        self.record = TimeRecord.read_data("A")

    def test_add_record(self):
        record_length = len(self.record.get_records())

        self.record.add_record("22:33")
        self.assertIn("22:33", self.record.get_records())
        self.assertEqual(record_length + 1, len(self.record.get_records()))

    def test_top_five(self):
        self.assertEqual(5, len(self.record.top_five()))


if __name__ == "main":
    unittest.main()

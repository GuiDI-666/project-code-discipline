import unittest


def item_count(count):
    return f"[{count}]"


class PreviewTests(unittest.TestCase):
    def test_short_label(self):
        self.assertEqual(item_count(3), "[3]")

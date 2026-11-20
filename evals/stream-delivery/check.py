"""验证样本确有可区分的行为；不替代对 Skill 的模型行为评估。"""

import unittest

import candidate
import reference


def observe(consume, chunks):
    applied = []
    error = None
    try:
        for chunk in chunks:
            consume(chunk, applied.append)
    except ValueError:
        error = "ValueError"
    return applied, error


class DeliveryCases(unittest.TestCase):
    def test_valid_batch(self):
        for implementation in (reference, candidate):
            self.assertEqual(observe(implementation.consume, [b"1\n2\n"]), ([1, 2], None))

    def test_valid_then_invalid_same_batch(self):
        self.assertEqual(observe(reference.consume, [b"1\ninvalid\n"]), ([1], "ValueError"))
        self.assertEqual(observe(candidate.consume, [b"1\ninvalid\n"]), ([], "ValueError"))

    def test_valid_then_invalid_separate_batches(self):
        for implementation in (reference, candidate):
            self.assertEqual(observe(implementation.consume, [b"1\n", b"invalid\n"]), ([1], "ValueError"))

    def test_invalid_first(self):
        for implementation in (reference, candidate):
            self.assertEqual(observe(implementation.consume, [b"invalid\n1\n"]), ([], "ValueError"))


if __name__ == "__main__":
    unittest.main()

import unittest

from Day_035 import removeRecursiveAdjacentDuplicates


class TestTask034(unittest.TestCase):
    def test_1_removeRecursiveAdjacentDuplicates(self):
        self.assertEqual(
            removeRecursiveAdjacentDuplicates("misssssipie"),
            "mpie"
        )

    def test_2_removeRecursiveAdjacentDuplicates(self):
        self.assertEqual(
            removeRecursiveAdjacentDuplicates("accbbcc"),
            "a"
        )

    def test_3_removeRecursiveAdjacentDuplicates(self):
        self.assertEqual(
            removeRecursiveAdjacentDuplicates("abccba"),
            "Empty String :-)"
        )

    def test_4_removeRecursiveAdjacentDuplicates(self):
        self.assertEqual(
            removeRecursiveAdjacentDuplicates("ILovePython"),
            "ILovePython"
        )

    def test_5_removeRecursiveAdjacentDuplicates(self):
        self.assertEqual(
            removeRecursiveAdjacentDuplicates("keepdoing"),
            "kpdoing"
        )


if __name__ == '__main__':
    unittest.main()

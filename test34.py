import unittest

from Day_034 import isSentencePalindrome


class TestTask034(unittest.TestCase):
    def test_1_isSentencePalindrome(self):
        self.assertEqual(
            isSentencePalindrome("Mr. Owl ate my metal worm"),
            "Given string is a palindrome :-)"
        )

    def test_2_isSentencePalindrome(self):
        self.assertEqual(
            isSentencePalindrome("Do geese see God?"),
            "Given string is a palindrome :-)"
        )

    def test_3_isSentencePalindrome(self):
        self.assertEqual(
            isSentencePalindrome("Was it a car or a cat I saw?"),
            "Given string is a palindrome :-)"
        )

    def test_4_isSentencePalindrome(self):
        self.assertEqual(
            isSentencePalindrome("I am Rakshitha"),
            "Given string is not a palindrome :-("
        )

    def test_5_isSentencePalindrome(self):
        self.assertEqual(
            isSentencePalindrome("I love python"),
            "Given string is not a palindrome :-("
        )


if __name__ == '__main__':
    unittest.main()

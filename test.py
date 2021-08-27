import unittest

from Day_012 import isVowel

class TestTask011(unittest.TestCase):
    def test_a_when_isVowel_then_True(self):
        self.assertEqual(isVowel('a'), True)
    
    def test_A_when_isVowel_then_True(self):
        self.assertEqual(isVowel('A'), True)

    def test_b_when_isVowel_then_False(self):
        self.assertEqual(isVowel("b"), False)

    def test_B_when_isVowel_then_False(self):
        self.assertEqual(isVowel("B"), False)
    
    def test_Z_when_isVowel_then_False(self):
        self.assertEqual(isVowel("Z"), False)

    def test_i_when_isVowel_then_True(self):
        self.assertEqual(isVowel("i"), True)
    
    def test_I_when_isVowel_then_True(self):
        self.assertEqual(isVowel("I"), True)
if __name__ == '__main__':
    unittest.main()

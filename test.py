import unittest

from Day_011 import getASCII

class TestTask011(unittest.TestCase):
    def test_a_when_assci_when_97(self):
        self.assertEqual(getASCII('a'), 97)
    
    def test_A_when_assci_when_65(self):
        self.assertEqual(getASCII('A'), 65)

    def test_comma_when_assci_when_44(self):
        self.assertEqual(getASCII(','), 44)

    def test_dot_when_assci_when_46(self):
        self.assertEqual(getASCII('.'), 46)
    
    def test_slash_when_assci_when_47(self):
        self.assertEqual(getASCII('/'), 47)

    def test_zero_when_assci_when_48(self):
        self.assertEqual(getASCII('0'), 48)
    
    def test_space_when_assci_when_32(self):
        self.assertEqual(getASCII(' '), 32)
if __name__ == '__main__':
    unittest.main()

import unittest

from Day_014 import isprimeFibonacciNumber

class TestTask011(unittest.TestCase):
    def test_5_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(5), (True, 'isPrimeNumber : True & isFibonacciNumber : True'))
    def test_89_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(89), (True, 'isPrimeNumber : True & isFibonacciNumber : True'))
    def test_4_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(4), (False, 'isPrimeNumber : False & isFibonacciNumber : False'))
    def test_9_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(9), (False, 'isPrimeNumber : False & isFibonacciNumber : False'))
    def test_55_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(55), (False, 'isPrimeNumber : False & isFibonacciNumber : True'))
    def test_144_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(144), (False, 'isPrimeNumber : False & isFibonacciNumber : True'))
    def test_107_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(107), (False, 'isPrimeNumber : True & isFibonacciNumber : False'))
    def test_181_isprimeFibonacciNumber(self):
        self.assertEqual(isprimeFibonacciNumber(181), (False, 'isPrimeNumber : True & isFibonacciNumber : False'))
    
if __name__ == '__main__':
    unittest.main()

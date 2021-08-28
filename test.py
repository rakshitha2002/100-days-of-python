import unittest

from Day_013 import fibonacciNumberGenerator

class TestTask011(unittest.TestCase):
    def test_5_on_fibonacciNumberGenerator(self):
        self.assertEqual(fibonacciNumberGenerator(5), [0, 1, 1, 2, 3])
        self.assertEqual(len(fibonacciNumberGenerator(5)), 5)
    
    def test_9_on_fibonacciNumberGenerator(self):
        self.assertEqual(fibonacciNumberGenerator(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(len(fibonacciNumberGenerator(9)), 9)

    def test_1_on_fibonacciNumberGenerator(self):
        self.assertEqual(fibonacciNumberGenerator(1), [0])
        self.assertEqual(len(fibonacciNumberGenerator(1)), 1)
    
    def test_25_on_fibonacciNumberGenerator(self):
        self.assertEqual(fibonacciNumberGenerator(25), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368])
        self.assertEqual(len(fibonacciNumberGenerator(25)), 25)

    def test_45_on_fibonacciNumberGenerator(self):
        self.assertEqual(fibonacciNumberGenerator(45), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733])
        self.assertEqual(len(fibonacciNumberGenerator(45)), 45)

if __name__ == '__main__':
    unittest.main()

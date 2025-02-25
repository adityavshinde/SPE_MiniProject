import unittest
from calc import square_root, factorial, natural_log, power

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), 1.414, places=3)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_natural_log(self):
        self.assertAlmostEqual(natural_log(2.718), 1, places=2)
        self.assertAlmostEqual(natural_log(1), 0, places=2)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, -1), 0.1)

if __name__ == '__main__':
    unittest.main()

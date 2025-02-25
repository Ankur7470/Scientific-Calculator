import unittest
import math
from calculator import square_root, factorial, natural_logarithm, power_function

class TestCalculator(unittest.TestCase):
    """
    Unit tests for the scientific calculator functions.
    """

    def test_square_root(self):
        # Test square root of a positive number
        self.assertAlmostEqual(square_root(25), 5.0)
        # Test square root of zero
        self.assertAlmostEqual(square_root(0), 0.0)
        # Test square root of a negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            square_root(-9)

    def test_factorial(self):
        # Test factorial of a positive integer
        self.assertEqual(factorial(5), 120)
        # Test factorial of zero
        self.assertEqual(factorial(0), 1)
        # Test factorial of a negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_natural_logarithm(self):
        # Test natural logarithm of a positive number
        self.assertAlmostEqual(natural_logarithm(1), 0.0)
        self.assertAlmostEqual(natural_logarithm(math.e), 1.0)
        # Test natural logarithm of zero or negative number (should raise ValueError)
        with self.assertRaises(ValueError):
            natural_logarithm(0)
        with self.assertRaises(ValueError):
            natural_logarithm(-2)

    def test_power_function(self):
        # Test power function with positive base and exponent
        self.assertAlmostEqual(power_function(2, 3), 8.0)
        # Test power function with zero exponent
        self.assertAlmostEqual(power_function(5, 0), 1.0)
        # Test power function with negative exponent
        self.assertAlmostEqual(power_function(2, -2), 0.25)
        # Test power function with fractional exponent
        self.assertAlmostEqual(power_function(4, 0.5), 2.0)

if __name__ == "__main__":
    unittest.main()

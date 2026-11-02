import unittest

from calculator import addition, division, multiplication, subtraction

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)              # Positive numbers
        self.assertEqual(addition(-5, -3), -8)           # Negative numbers
        self.assertEqual(addition(-5, 3), -2)            # Mixed signs
        self.assertAlmostEqual(addition(2.5, 1.5), 4.0)  # Decimals
        self.assertEqual(addition(5, 0), 5)              # Zero
        self.assertEqual(addition(0, 0), 0)              # Zeroes

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)           # Positive numbers
        self.assertEqual(subtraction(-5, -3), -2)        # Negative numbers
        self.assertEqual(subtraction(5, -3), 8)          # Mixed signs
        self.assertAlmostEqual(subtraction(5.5, 2.2), 3.3) # Decimals
        self.assertEqual(subtraction(5, 0), 5)           # Zero subtrahend
        self.assertEqual(subtraction(0, 5), -5)          # Zero minuend

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)       # Positive numbers
        self.assertEqual(multiplication(-4, 3), -12)     # Negative numbers
        self.assertEqual(multiplication(-4, -3), 12)     # Both negative
        self.assertAlmostEqual(multiplication(2.5, 2.0), 5.0) # Decimals
        self.assertEqual(multiplication(5, 0), 0)        # Multiplying by zero
        self.assertEqual(multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5.0)           # Positive numbers
        self.assertEqual(division(-10, 2), -5.0)         # Negative numerator
        self.assertEqual(division(-10, -2), 5.0)         # Both negative
        self.assertAlmostEqual(division(5.0, 2.0), 2.5)  # Decimals
        self.assertEqual(division(0, 5), 0.0)            # Zero numerator

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            division(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero.")

    def test_invalid_input_handling(self):
        invalid_inputs = ["5", None, [1, 2], {"a": 1}]

        for invalid in invalid_inputs:
            with self.subTest(invalid=invalid):
                # Test addition
                with self.assertRaises(ValueError) as context:
                    addition(invalid, 5)
                self.assertEqual(str(context.exception), "Please enter valid numbers.")

                # Test subtraction
                with self.assertRaises(ValueError):
                    subtraction(5, invalid)

                # Test multiplication
                with self.assertRaises(ValueError):
                    multiplication(invalid, invalid)

                # Test division
                with self.assertRaises(ValueError):
                    division(5, invalid)


if __name__ == "__main__":
    unittest.main()
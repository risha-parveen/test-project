import unittest
from fibonacci import fibonacci  # Assuming the function is named `fibonacci`

class TestFibonacci(unittest.TestCase):

    def test_first_ten_numbers(self):
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected in enumerate(expected_values):
            with self.subTest(i=i):
                self.assertEqual(fibonacci(i), expected)

    def test_edge_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            fibonacci(5.5)

if __name__ == '__main__':
    unittest.main()
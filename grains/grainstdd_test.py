import unittest

from grains import (
    square,
    total
)


class GrainsTestSquare(unittest.TestCase):
    def test_square_1(self):
        self.assertEqual(square(1), 1)

    def test_square_2(self):
        self.assertEqual(square(2), 2)

    def test_square_3(self):
        self.assertEqual(square(3), 4)

    def test_square_4(self):
        self.assertEqual(square(4), 8)

    def test_square_is_invalid_0(self):
        with self.assertRaises(ValueError) as err:
            square(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "square must be between 1 and 64")

    def test_square_is_invalid_65(self):
        with self.assertRaises(ValueError) as err:
            square(65)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "square must be between 1 and 64")


class GrainsTestTotal(unittest.TestCase):
    def test_total_of_grains(self):
        self.assertEqual(total(), 18446744073709551615)
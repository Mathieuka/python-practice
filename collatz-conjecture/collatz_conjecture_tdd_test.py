# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/collatz-conjecture/canonical-data.json
# File last updated on 2023-07-20

import unittest

from collatz_conjecture import (
    steps,
)


class CollatzConjectureTest(unittest.TestCase):
    def test_zero_steps_for_one(self):
        """Test that the number of steps for 1 is zero."""
        self.assertEqual(steps(1), 0)

    def test_zero_steps_for_2(self):
        """Test that the number of steps for 2 is 1."""
        self.assertEqual(steps(2), 1)

    def test_large_number_of_even_and_odd_steps(self):
        self.assertEqual(steps(1000000), 152)

    def test_raise_error_if_value_lower_than_0(self):
        with self.assertRaises(ValueError) as err:
            steps(0)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0],"Only positive integers are allowed" )


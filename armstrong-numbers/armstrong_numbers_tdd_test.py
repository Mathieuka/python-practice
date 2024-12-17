# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/armstrong-numbers/canonical-data.json
# File last updated on 2023-07-20

import unittest

from armstrong_numbers import (
    is_armstrong_number,
)

class ArmstrongNumbersTest(unittest.TestCase):
    def test_zero_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(0), True)

    def test_1_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(1), True)

    def test_153_is_an_armstrong_number(self):
        self.assertIs(is_armstrong_number(153), True)
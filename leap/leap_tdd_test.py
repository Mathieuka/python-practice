# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/leap/canonical-data.json
# File last updated on 2023-07-19

import unittest

from leap import (
    leap_year,
)


class LeapTest(unittest.TestCase):
    def test_year_not_divisible_by_4_in_common_year(self):
        self.assertIs(leap_year(4), True)

    def test_year_not_divisible_by_100_in_common_year(self):
            self.assertIs(leap_year(400), True)
            self.assertIs(leap_year(100), False)
            self.assertIs(leap_year(2000), True)
            self.assertIs(leap_year(1900), False)
            self.assertIs(leap_year(2024), True)

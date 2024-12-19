# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/triangle/canonical-data.json
# File last updated on 2023-07-19

import unittest

from triangle import (
    equilateral,
    isosceles,
    scalene,
)


class EquilateralTriangleTest(unittest.TestCase):
    def test_all_sides_are_equal(self):
        self.assertIs(equilateral([2, 2, 2]), True)



class IsoscelesTriangleTest(unittest.TestCase):
    def test_last_two_sides_are_equal(self):
        self.assertIs(isosceles([3, 4, 4]), True)


class ScaleneTriangleTest(unittest.TestCase):
    def test_no_sides_are_equal(self):
        self.assertIs(scalene([5, 4, 6]), True)


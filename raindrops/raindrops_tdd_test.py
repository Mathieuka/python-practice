# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/raindrops/canonical-data.json
# File last updated on 2023-07-19

import unittest

from raindrops import (
    convert,
)


class RaindropsTest(unittest.TestCase):
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1")

    def test_the_sound_for_number_divisible_by_3_is_Pling(self):
        self.assertEqual(convert(3), "Pling")

    def test_the_sound_for_number_divisible_by_5_is_Plang(self):
        self.assertEqual(convert(5), "Plang")

    def test_the_sound_for_number_divisible_by_3_and_5_is_PlingPlang(self):
        self.assertEqual(convert(15), "PlingPlang")

    def test_the_sound_for_number_divisible_by_7_is_PlingPlang(self):
        self.assertEqual(convert(7), "Plong")

    def test_the_sound_for_number_divisible_by_3_and_7_is_PlingPlong(self):
        self.assertEqual(convert(21), "PlingPlong")

    def test_the_sound_for_number_divisible_by_3_and_5_and_7_is_PlingPlong(self):
        self.assertEqual(convert(105), "PlingPlangPlong")

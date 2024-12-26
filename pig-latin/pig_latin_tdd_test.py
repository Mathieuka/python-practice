# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pig-latin/canonical-data.json
# File last updated on 2023-07-19

import unittest

from pig_latin import (
    translate,
    begin_with_vowel,
    begin_with_xr,
    begin_with_yt,
    begin_with_consonants,
    contain_qu,
    consonants_preceding_y
)

class WordBeginWithVowel(unittest.TestCase):
    def test_word_begin_with_vowel(self):
        self.assertEqual(begin_with_vowel("a"), "a")
    def test_word_not_begin_with_vowel(self):
        self.assertEqual(begin_with_vowel("g"), False)

class WordBeginWithXR(unittest.TestCase):
    def test_word_begin_with_xr(self):
        self.assertEqual(begin_with_xr("xray"), True)

    def test_word_not_begin_with_xr(self):
        self.assertEqual(begin_with_xr("eday"), False)


class WordBeginWithYT(unittest.TestCase):
    def test_word_begin_with_yt(self):
        self.assertEqual(begin_with_yt("ytay"), True)

    def test_word_not_begin_with_yt(self):
        self.assertEqual(begin_with_yt("eday"), False)

class WordBeginWithConsonants(unittest.TestCase):
    def test_word_begin_with_consonants(self):
        self.assertEqual(begin_with_consonants("mliay"), "iayml")

    def test_word_not_begin_with_consonants(self):
        self.assertEqual(begin_with_consonants("iay"), False)

class WordContainQu(unittest.TestCase):
    def test_word_starting_with_consonants_contain_qu(self):
        self.assertEqual(contain_qu("qu"), "qu")
        self.assertEqual(contain_qu("zquo"), "zqu")

    def test_word_starting_with_consonants_followed_by_vowels_contain_qu(self):
        self.assertEqual(contain_qu("zaquo"), False)

    def test_word_starting_with_vowels_contain_qu(self):
        self.assertEqual(contain_qu("aquo"), False)

    def test_word_not_contain_qu(self):
        self.assertEqual(contain_qu("zauo"), False)

class WordContainY(unittest.TestCase):
    def test_word_starting_with_consonants_followed_by_y(self):
        self.assertEqual(consonants_preceding_y("my"),  "ymay")
        self.assertEqual(consonants_preceding_y("mjy"),  "ymjay")
        self.assertEqual(consonants_preceding_y("mjay"),  False)

    def test_word_not_starting_with_consonants_followed_by_y(self):
        self.assertEqual(consonants_preceding_y("mjay"),  False)

class PigLatinTest(unittest.TestCase):
    def test_word_beginning_with_a(self):
        self.assertEqual(translate("apple"), "appleay")

    def test_word_beginning_with_xr(self):
        self.assertEqual(translate("xray"), "xrayay")

    def test_word_begin_with_ml(self):
        self.assertEqual(translate("mliay"), "iaymlay")

    def test_word_beginning_with_yt(self):
        self.assertEqual(translate("ytay"), "ytayay")

    def test_word_thrush(self):
        self.assertEqual(translate("thrush"), "ushthray")

    def test_word_chair(self):
        self.assertEqual(translate("chair"), "airchay")

    def test_word_quick(self):
        self.assertEqual(translate("quick"), "ickquay")

    def test_word_square(self):
        self.assertEqual(translate("square"), "aresquay")

    def test_word_ym(self):
        self.assertEqual(translate("my"), "ymay")
        self.assertEqual(translate("y"), "yay")
        self.assertEqual(translate("yy"), "yyay")

    def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster(self):
        self.assertEqual(translate("rhythm"), "ythmrhay")

    def test_a_whole_phrase(self):
        self.assertEqual(translate("quick fast run"), "ickquay astfay unray")



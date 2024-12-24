# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pig-latin/canonical-data.json
# File last updated on 2023-07-19

import unittest

from pig_latin import (
    translate,
    begin_with_vowel,
    begin_with_xr,
    begin_with_yt,
    begin_with_consonants
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







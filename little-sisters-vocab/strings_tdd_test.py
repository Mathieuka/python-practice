import unittest
from strings import (add_prefix_un,
                     make_word_groups,
                     remove_suffix_ness,
                     adjective_to_verb)


class LittleSistersVocabTest(unittest.TestCase):

    def test_add_prefix_un(self):
                self.assertEqual(add_prefix_un('happy'), 'unhappy')
                self.assertEqual(add_prefix_un('manageable'), 'unmanageable')

    def test_make_words_group(self):
        self.assertEqual(make_word_groups(['un', 'happy', 'manageable']), 'un :: unhappy :: unmanageable')
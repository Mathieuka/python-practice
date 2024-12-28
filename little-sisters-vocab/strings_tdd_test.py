import unittest
from strings import (add_prefix_un,
                     make_word_groups,
                     remove_suffix_ness,
                     adjective_to_verb)


class LittleSistersVocabTest(unittest.TestCase):

    def test_add_prefix_un(self):
                self.assertEqual(add_prefix_un('happy'), 'unhappy')
                self.assertEqual(add_prefix_un('manageable'), 'unmanageable')
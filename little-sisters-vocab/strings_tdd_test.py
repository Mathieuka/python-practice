import unittest
import pytest
from strings import (add_prefix_un,
                     make_word_groups,
                     remove_suffix_ness,
                     adjective_to_verb)


class LittleSistersVocabTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_add_prefix_un(self):
        input_data = ['happy', 'manageable', 'fold', 'eaten', 'avoidable', 'usual']
        result_data = [f'un{item}' for item in input_data]

        for variant, (word, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', word=word, expected=expected):

                actual_result = add_prefix_un(word)
                error_message = (f'Called add_prefix_un("{word}"). '
                                f'The function returned "{actual_result}", but the '
                                f'tests expected "{expected}" after adding "un" as a prefix.')

                self.assertEqual(actual_result, expected, msg=error_message)
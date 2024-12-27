import unittest
import pytest

from black_jack import (
                        value_of_card,
                        higher_card,
                        value_of_ace,
                        is_blackjack,
                        can_split_pairs,
                        can_double_down
                        )


class BlackJackTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_value_of_card(self):
        test_data = [('2', 2), ('5', 5), ('8', 8),
                     ('A', 1), ('10', 10), ('J', 10),
                     ('Q', 10), ('K', 10)]

        for variant, (card, expected) in enumerate(test_data, 1):
            with self.subTest(f'variation #{variant}', card=card, expected=expected):
                actual_result = value_of_card(card)
                error_msg = (f'Called value_of_card({card}). '
                             f'The function returned {actual_result} as the value of the {card} card, '
                             f'but the test expected {expected} as the {card} card value.')

                self.assertEqual(actual_result, expected, msg=error_msg)


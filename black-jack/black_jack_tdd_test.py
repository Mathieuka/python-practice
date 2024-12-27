import unittest

from black_jack import (
                        value_of_card,
                        higher_card,
                        value_of_ace,
                        is_blackjack,
                        can_split_pairs,
                        can_double_down
                        )


class BlackJackTest(unittest.TestCase):
    def test_value_of_card(self):
        self.assertEqual(value_of_card("2"), 2)
        self.assertEqual(value_of_card("A"), 1)
        self.assertEqual(value_of_card("5"), 5)
        self.assertEqual(value_of_card("8"), 8)
        self.assertEqual(value_of_card("10"), 10)
        self.assertEqual(value_of_card("J"), 10)
        self.assertEqual(value_of_card("Q"), 10)
        self.assertEqual(value_of_card("K"), 10)

    def test_returning_two_values(self):
        self.assertEqual(higher_card("5","2"), "5", msg="One card is greater than other")
        self.assertEqual(higher_card("J","J"), ("J", "J"), msg="Both card value is equal")

    def test_value_of_ace(self):
        self.assertEqual(value_of_ace("10", "10"), 1)
        self.assertEqual(value_of_ace("5", "5"), 11)
        self.assertEqual(value_of_ace("A", "10"), 1)
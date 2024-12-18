import unittest
#import pytest
from arcade_game import eat_ghost, score, lose, win



class GhostGobbleGameTest(unittest.TestCase):

 #   @pytest.mark.task(taskno=1)
    def test_ghost_gets_eaten(self):
        actual_result_true_true = eat_ghost(True, True)
        error_message = ('Called eat_ghost(True, True).'
                        f'The function returned {actual_result_true_true}, but the '
                        f'tests expected that the ghost gets eaten (True).')

        self.assertIs(actual_result_true_true, True, msg=error_message)

        actual_result_true_false = eat_ghost(True, False)
        self.assertIs(actual_result_true_false, False, msg=error_message)

        actual_result_false_true = eat_ghost(False, True)
        self.assertIs(actual_result_false_true, False, msg=error_message)

    def test_touching_power_pellet_or_touching_dot(self):
        result_true_true = score(True, True)
        self.assertIs(result_true_true, True)

        result_false_true = score(False, True)
        self.assertIs(result_false_true, True)

        result_false_false = score(False, False)
        self.assertIs(result_false_false, False)

    def test_lose_when_pacman_touch_ghost_without_power_pellet(self):
        result_true_true = lose(True, True)
        self.assertIs(result_true_true, False)

        result_false_true = lose(False, True)
        self.assertIs(result_false_true, True)

        result_false_true = lose(True, False)
        self.assertIs(result_false_true, False)

    # test_dont_win_if_all_dots_eaten_but_touching_a_ghost
    def test_win_when_all_dots_have_been_eaten(self):
        result_true_true_false = win(True, True, False)
        self.assertIs(result_true_true_false, True)

        result_true_true_true = win(True, True, True)
        self.assertIs(result_true_true_true, True)

        result_true_false_false = win(True, False, False)
        self.assertIs(result_true_false_false, True)

        result_true_false_true = win(True, False, True)
        self.assertIs(result_true_false_true, False)


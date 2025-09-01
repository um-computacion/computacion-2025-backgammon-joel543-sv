import unittest
from unittest.mock import MagicMock
from core.player import Player
from core.checker import Checker

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("white")
        self.mock_board = MagicMock()

    def test_initial_state(self):
        self.assertEqual(self.player.color, "white")
        self.assertEqual(len(self.player.checkers), 15)
        self.assertEqual(self.player.bar, [])
        self.assertEqual(self.player.home, [])

    def test_has_checkers_on_bar_false(self):
        self.assertFalse(self.player.has_checkers_on_bar())

    def test_has_checkers_on_bar_true(self):
        self.player.bar = [Checker("white")]
        self.assertTrue(self.player.has_checkers_on_bar())

    def test_move_from_bar_success(self):
        checker = Checker("white")
        self.player.bar = [checker]
        self.mock_board.get_entry_point.return_value = 1
        self.mock_board.can_place_checker.return_value = True

        result = self.player.move_from_bar(self.mock_board, 3)
        self.assertTrue(result)
        self.assertNotIn(checker, self.player.bar)
        self.mock_board.place_checker.assert_called_with(1, checker)

    def test_move_from_bar_failure(self):
        checker = Checker("white")
        self.player.bar = [checker]
        self.mock_board.get_entry_point.return_value = 1
        self.mock_board.can_place_checker.return_value = False

        result = self.player.move_from_bar(self.mock_board, 3)
        self.assertFalse(result)
        self.assertIn(checker, self.player.bar)
        self.mock_board.place_checker.assert_not_called()

    def test_select_checker_found(self):
        checker = self.player.checkers[0]
        self.mock_board.can_move_checker.return_value = True
        result = self.player.select_checker(self.mock_board, 4)
        self.assertEqual(result, checker)

    def test_select_checker_not_found(self):
        self.mock_board.can_move_checker.return_value = False
        result = self.player.select_checker(self.mock_board, 4)
        self.assertIsNone(result)

    def test_move_checker_valid_to_home(self):
        checker = self.player.checkers[0]
        self.mock_board.is_checker_home.return_value = True
        self.mock_board.move_checker = MagicMock()

        self.player.move_checker(self.mock_board, checker, 6)
        self.assertIn(checker, self.player.home)
        self.assertNotIn(checker, self.player.checkers)
        self.mock_board.move_checker.assert_called_with(checker, 6)

    def test_move_checker_invalid(self):
        other_checker = Checker("white")
        self.mock_board.is_checker_home.return_value = False
        with self.assertLogs(level="INFO") as log:
            self.player.move_checker(self.mock_board, other_checker, 6)
        self.mock_board.move_checker.assert_not_called()

    def test_has_won_false(self):
        self.assertFalse(self.player.has_won())

    def test_has_won_true(self):
        self.player.home = [Checker("white") for _ in range(15)]
        self.assertTrue(self.player.has_won())

if __name__ == "__main__":
    unittest.main()

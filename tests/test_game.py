import unittest
from unittest.mock import MagicMock, patch
from core.game import Game
from core.checker import Checker

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_state(self):
        self.assertEqual(self.game.current_turn, "white")
        self.assertIn("white", self.game.players)
        self.assertIn("black", self.game.players)

    def test_switch_turn(self):
        self.game.current_turn = "white"
        self.game.switch_turn()
        self.assertEqual(self.game.current_turn, "black")
        self.game.switch_turn()
        self.assertEqual(self.game.current_turn, "white")

    def test_is_game_over_false(self):
        self.game.board.all_checkers_home = MagicMock(return_value=False)
        self.assertFalse(self.game.is_game_over())

    def test_is_game_over_true_white(self):
        self.game.board.all_checkers_home = MagicMock(side_effect=lambda color: color == "white")
        with patch("builtins.print") as mock_print:
            self.assertTrue(self.game.is_game_over())
            mock_print.assert_any_call("\n¡Victoria para WHITE!")

    def test_is_game_over_true_black(self):
        self.game.board.all_checkers_home = MagicMock(side_effect=lambda color: color == "black")
        with patch("builtins.print") as mock_print:
            self.assertTrue(self.game.is_game_over())
            mock_print.assert_any_call("\n¡Victoria para BLACK!")

    @patch("core.game.Dice.roll", return_value=[3, 4])
    def test_play_turn_with_valid_checker(self, mock_roll):
        mock_checker = Checker("white", 1)
        self.game.players["white"].select_checker = MagicMock(return_value=mock_checker)
        self.game.board.move_checker = MagicMock()

        with patch("builtins.print"):
            self.game.play_turn()

        self.assertEqual(mock_roll.call_count, 1)
        self.assertEqual(self.game.board.move_checker.call_count, 2)

    @patch("core.game.Dice.roll", return_value=[2])
    def test_play_turn_with_no_checker(self, mock_roll):
        self.game.players["white"].select_checker = MagicMock(return_value=None)
        self.game.board.move_checker = MagicMock()

        with patch("builtins.print") as mock_print:
            self.game.play_turn()
            mock_print.assert_any_call("No hay fichas disponibles para mover con ese valor.")
            self.assertEqual(self.game.board.move_checker.call_count, 0)

if __name__ == "__main__":
    unittest.main()

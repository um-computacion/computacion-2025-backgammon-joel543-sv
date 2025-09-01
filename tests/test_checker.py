import unittest
from core.checker import Checker
from core.board import Board

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_state(self):
        checker = Checker("white", 5)
        self.assertEqual(checker.color, "white")
        self.assertEqual(checker.position, 5)
        self.assertFalse(checker.on_bar)
        self.assertFalse(checker.home)

    def test_capture_sets_bar_state(self):
        checker = Checker("black", 10)
        checker.capture()
        self.assertEqual(checker.position, "bar")
        self.assertTrue(checker.on_bar)

    def test_get_entry_point_white(self):
        checker = Checker("white")
        self.assertEqual(checker.get_entry_point(), 1)

    def test_get_entry_point_black(self):
        checker = Checker("black")
        self.assertEqual(checker.get_entry_point(), 24)

    def test_str_representation_on_board(self):
        checker = Checker("white", 6)
        self.assertEqual(str(checker), "White - P6")

    def test_str_representation_on_bar(self):
        checker = Checker("black")
        checker.capture()
        self.assertEqual(str(checker), "Black - Bar")

    def test_move_from_bar_success(self):
        checker = Checker("white")
        checker.capture()
        self.board.points[1] = []  # Entry point libre
        checker.move(0, self.board)
        self.assertEqual(checker.position, 1)
        self.assertFalse(checker.on_bar)
        self.assertIn(checker, self.board.points[1])

    def test_move_from_bar_blocked(self):
        checker = Checker("white")
        checker.capture()
        self.board.points[1] = [Checker("black"), Checker("black")]  # Bloqueado
        checker.move(0, self.board)
        self.assertTrue(checker.on_bar)  # No se movió

    def test_move_normal_success(self):
        checker = Checker("white", 5)
        self.board.points[5] = [checker]
        self.board.points[7] = []
        checker.move(2, self.board)
        self.assertEqual(checker.position, 7)
        self.assertIn(checker, self.board.points[7])
        self.assertNotIn(checker, self.board.points[5])

    def test_move_normal_blocked(self):
        checker = Checker("white", 5)
        self.board.points[5] = [checker]
        self.board.points[7] = [Checker("black"), Checker("black")]
        checker.move(2, self.board)
        self.assertEqual(checker.position, 5)  # No se movió

    def test_move_to_home(self):
        checker = Checker("white", 23)
        self.board.points[23] = [checker]
        checker.move(2, self.board)
        self.assertTrue(checker.home)
        self.assertNotIn(checker, self.board.points[23])

if __name__ == "__main__":
    unittest.main()

import unittest
from core.board import Board
from core.checker import Checker

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_positions(self):
        self.assertEqual(len(self.board.points[1]), 2)
        self.assertEqual(self.board.points[1][0].color, "black")
        self.assertEqual(len(self.board.points[6]), 5)
        self.assertEqual(self.board.points[6][0].color, "white")

    def test_can_place_checker_empty_point(self):
        self.board.points[5] = []
        self.assertTrue(self.board.can_place_checker(5, "white"))

    def test_can_place_checker_same_color(self):
        self.board.points[5] = [Checker("white")]
        self.assertTrue(self.board.can_place_checker(5, "white"))

    def test_can_place_checker_capture(self):
        self.board.points[5] = [Checker("black")]
        self.assertTrue(self.board.can_place_checker(5, "white"))

    def test_place_checker_no_capture(self):
        checker = Checker("white")
        self.board.points[5] = []
        self.board.place_checker(5, checker)
        self.assertIn(checker, self.board.points[5])
        self.assertEqual(checker.position, 5)

    def test_place_checker_with_capture(self):
        enemy = Checker("black")
        self.board.points[5] = [enemy]
        checker = Checker("white")
        self.board.place_checker(5, checker)
        self.assertIn(checker, self.board.points[5])
        self.assertIn(enemy, self.board.bar["black"])

    def test_remove_checker(self):
        checker = Checker("white")
        self.board.points[5] = [checker]
        self.board.remove_checker(5, checker)
        self.assertNotIn(checker, self.board.points[5])

    def test_move_checker_normal(self):
        checker = Checker("white")
        checker.position = 5
        self.board.points[5] = [checker]
        self.board.points[7] = []
        self.board.move_checker(checker, 2)
        self.assertIn(checker, self.board.points[7])
        self.assertEqual(checker.position, 7)

    def test_move_checker_to_home(self):
        checker = Checker("white")
        checker.position = 23
        self.board.points[23] = [checker]
        self.board.move_checker(checker, 2)
        self.assertIn(checker, self.board.home["white"])
        self.assertTrue(checker.home)

    def test_all_checkers_home_false(self):
        self.assertFalse(self.board.all_checkers_home("white"))

    def test_all_checkers_home_true(self):
        self.board.home["white"] = [Checker("white") for _ in range(15)]
        self.assertTrue(self.board.all_checkers_home("white"))

if __name__ == "__main__":
    unittest.main()

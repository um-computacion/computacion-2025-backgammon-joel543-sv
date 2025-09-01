import unittest
from unittest.mock import patch
from core.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    @patch("random.randint")
    def test_roll_normal(self, mock_randint):
        mock_randint.side_effect = [3, 5]
        moves = self.dice.roll()
        self.assertEqual(self.dice.values, [3, 5])
        self.assertFalse(self.dice.is_double)
        self.assertEqual(moves, [3, 5])
        self.assertEqual(self.dice.moves, [3, 5])

    @patch("random.randint")
    def test_roll_double(self, mock_randint):
        mock_randint.side_effect = [4, 4]
        moves = self.dice.roll()
        self.assertEqual(self.dice.values, [4, 4])
        self.assertTrue(self.dice.is_double)
        self.assertEqual(moves, [4, 4, 4, 4])
        self.assertEqual(self.dice.moves, [4, 4, 4, 4])

    def test_use_move_success(self):
        self.dice.moves = [2, 3, 5]
        result = self.dice.use_move(3)
        self.assertTrue(result)
        self.assertEqual(self.dice.moves, [2, 5])

    def test_use_move_failure(self):
        self.dice.moves = [2, 3]
        result = self.dice.use_move(6)
        self.assertFalse(result)
        self.assertEqual(self.dice.moves, [2, 3])

    def test_has_moves_left_true(self):
        self.dice.moves = [1]
        self.assertTrue(self.dice.has_moves_left())

    def test_has_moves_left_false(self):
        self.dice.moves = []
        self.assertFalse(self.dice.has_moves_left())

    def test_reset(self):
        self.dice.values = [2, 2]
        self.dice.is_double = True
        self.dice.moves = [2, 2, 2, 2]
        self.dice.reset()
        self.assertEqual(self.dice.values, [])
        self.assertFalse(self.dice.is_double)
        self.assertEqual(self.dice.moves, [])

    def test_str_representation_normal(self):
        self.dice.values = [2, 5]
        self.dice.moves = [2, 5]
        self.dice.is_double = False
        expected = "Tirada: [2, 5] | Movimientos disponibles: [2, 5] (normal)"
        self.assertEqual(str(self.dice), expected)

    def test_str_representation_double(self):
        self.dice.values = [6, 6]
        self.dice.moves = [6, 6, 6, 6]
        self.dice.is_double = True
        expected = "Tirada: [6, 6] | Movimientos disponibles: [6, 6, 6, 6] (doble)"
        self.assertEqual(str(self.dice), expected)

if __name__ == "__main__":
    unittest.main()

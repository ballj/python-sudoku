"""Unit testing for the sudoku game engine"""
import unittest
import game_engine


class SetItem(unittest.TestCase):
    """Tests the __setitem__ method"""
    def setUp(self):
        initial_board = [0 for x in range(0, 81)]
        self.sudoku = game_engine.Sudoku(initial_board)

    def test_value_too_low(self):
        """Tests item too low"""
        self.assertRaises(ValueError, self.sudoku.__setitem__, 1, 0)

    def test_value_too_high(self):
        """Tests item too high"""
        self.assertRaises(ValueError, self.sudoku.__setitem__, 1, 10)

    def test_value_valid(self):
        """Test setting values 0-9"""
        test_values = range(1, 10)
        for value in test_values:
            self.sudoku[0] = value
            self.assertEqual(self.sudoku[0], value)


if __name__ == '__main__':
    unittest.main()

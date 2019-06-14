#!/usr/bin/env python
"""Module to control all board functions"""


class Sudoku():
    """Class implementation of a Sudoku game board"""
    def __init__(self, board_file='board.txt'):
        file_handler = open(board_file, 'r')
        self.board_init = tuple(map(
            int, file_handler.read().replace(',', '').split()))
        self.board_current = list(self.board_init)
        file_handler.close()

    def __str__(self, board='board_current'):
        """Print the current board"""
        board_out = '{}'.format(self.board_current)
        return board_out

    def __setitem__(self, key, item):
        """sets the value of a position on the current board"""
        if 0 < item < 10:
            self.board_current[key] = item
        else:
            raise ValueError('Item must be greater than 0 and less than 10')

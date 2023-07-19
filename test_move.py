import unittest

from board import Board
from move import Move
from tile import Tile


class TestMoveMethods(unittest.TestCase):

    def test_move_up(self):
        board = Board()
        board.board = [[Tile(1), None, Tile(2), None],
                       [None, Tile(2), None, Tile(3)],
                       [None, Tile(1), Tile(1), Tile(2)],
                       [Tile(2), None, None, Tile(1)]]
        move = Move(board)
        move.move_up()
        self.assertEqual(board.board, [[Tile(1), Tile(2), Tile(2), Tile(3)],
                                       [None, Tile(1), Tile(1), Tile(2)],
                                       [Tile(2), None, None, Tile(1)],
                                       [None, None, None, None]])

    def test_move_down(self):
        board = Board()
        board.board = [[Tile(1), None, Tile(2), None],
                       [None, Tile(2), None, Tile(3)],
                       [None, Tile(1), Tile(1), Tile(2)],
                       [Tile(2), None, None, Tile(1)]]
        move = Move(board)
        move.move_down()
        self.assertEqual(board.board, [[None, None, None, None],
                                       [Tile(1), None, Tile(2), None],
                                       [None, Tile(2), None, Tile(3)],
                                       [Tile(2), Tile(1), Tile(1), Tile(3)]])

    def test_move_left(self):
        board = Board()
        board.board = [[Tile(1), None, Tile(2), None],
                       [None, Tile(2), None, Tile(3)],
                       [None, Tile(1), Tile(1), Tile(2)],
                       [Tile(2), None, None, Tile(1)]]
        move = Move(board)
        move.move_left()
        self.assertEqual(board.board, [[Tile(1), Tile(2), None, None],
                                       [Tile(2), None, Tile(3), None],
                                       [Tile(1), Tile(1), Tile(2), None],
                                       [Tile(2), None, Tile(1), None]])

    def test_move_right(self):
        board = Board()
        board.board = [[Tile(1), Tile(2), None, None],
                       [Tile(1), Tile(2), None, None],
                       [Tile(3), Tile(3), None, None],
                       [Tile(2), None, None, None]]
        move = Move(board)
        move.move_right()
        self.assertEqual(board.board, [[None, Tile(1), Tile(2), None],
                                       [None, Tile(1), Tile(2), None],
                                       [None, Tile(3), Tile(3), None],
                                       [None, Tile(2), None, None]])

    def test_merge_tiles(self):
        board = Board()
        board.board = [[Tile(1), None, Tile(2), None],
                       [None, Tile(2), None, Tile(3)],
                       [None, Tile(1), Tile(1), Tile(2)],
                       [Tile(2), None, None, Tile(1)]]
        move = Move(board)
        move.move_right()
        self.assertEqual(board.board, [[None, Tile(1), None, Tile(2)],
                                       [None, None, Tile(2), Tile(3)],
                                       [None, None, Tile(1), Tile(3)],
                                       [None, Tile(2), None, Tile(1)]])

    def test_proper_merge(self):
        board = Board()
        board.board = [[Tile(3), Tile(6), Tile(12), Tile(24)],
                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                       [Tile(3), Tile(6), Tile(12), Tile(24)]]
        move = Move(board)
        move.move_left()  # no tiles should move
        self.assertEqual(board.board, [[Tile(6), Tile(12), Tile(24), Tile(48)],
                                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                                       [None, None, None, None]])

    def test_no_move(self):
        board = Board()
        board.board = [[Tile(3), Tile(6), Tile(12), Tile(24)],
                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                       [Tile(3), Tile(6), Tile(12), Tile(24)]]
        move = Move(board)
        move.move_left()  # no tiles should move
        self.assertEqual(board.board, [[Tile(3), Tile(6), Tile(12), Tile(24)],
                                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                                       [Tile(3), Tile(6), Tile(12), Tile(24)],
                                       [Tile(3), Tile(6), Tile(12), Tile(24)]])

    def test_ones_and_twos_merge_to_three(self):
        board = Board()
        board.board = [[Tile(1), Tile(2), None, None],
                       [Tile(2), Tile(1), None, None],
                       [None, None, None, None],
                       [None, None, None, None]]
        move = Move(board)
        move.move_left()  # ones and twos should merge into threes
        self.assertEqual(board.board, [[Tile(3), None, None, None],
                                       [Tile(3), None, None, None],
                                       [None, None, None, None],
                                       [None, None, None, None]])


if __name__ == '__main__':
    unittest.main()

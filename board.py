import itertools
import random
from tile import Tile


class Board:
    def __init__(self):
        self.board: list[list[Tile | None]] = [[None] * 4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()

    def __str__(self):
        board_string = ""
        board_string += "-" * 25 + "\n"
        for row in self.board:
            row_strs = []
            for tile in row:
                if tile is None:
                    row_strs.append(' ' * 5)
                else:
                    row_strs.append(str(tile.get_value()).center(5))
            board_string += "|" + "|".join(row_strs) + "|" + "\n"
        board_string += "-" * 25 + "\n"
        return board_string

    def add_new_tile(self):
        indices = [
            (i, j)
            for i, j in itertools.product(range(4), range(4))
            if not self.board[i][j]
        ]
        row, col = random.choice(indices)
        self.board[row][col] = Tile(random.choice([1, 2, 3]))

    @staticmethod
    def is_in_bounds(row, col):
        return 0 <= row < 4 and 0 <= col < 4

    def can_merge_with_neighbor(self, row, col, tile):
        indices = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for neighbor_row, neighbor_col in indices:
            if self.is_in_bounds(neighbor_row, neighbor_col):
                continue

            from_tile = self.board[neighbor_row][neighbor_col]
            if not from_tile:
                continue

            if from_tile.can_merge(tile):
                return True

        return False

    def is_game_over(self):
        for r in range(4):
            for c in range(4):
                if self.board[r][c] is None:
                    return False

                tile = self.board[r][c]
                if self.can_merge_with_neighbor(r, c, tile):
                    return False

        # no empty spaces and no possible merges
        return True

    def get_score(self):
        return sum(tile.get_value() for row in self.board for tile in row if tile)

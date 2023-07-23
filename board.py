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
        r, c = random.choice(
            [(i, j) for i in range(4) for j in range(4) if not self.board[i][j]])
        self.board[r][c] = Tile(random.choice([1, 2, 3]))

    def check_game_over(self):
        for r in range(4):
            for c in range(4):
                # If there is an empty space, return False (game is not over)
                if self.board[r][c] is None:
                    return False

                # If the current tile can merge with a neighbor, return False (game is not over)
                tile_value = self.board[r][c].get_value()
                if self.can_merge_with_neighbor(r, c, tile_value):
                    return False

        # If there are no empty spaces and no possible merges, return True (game is over)
        return True

    def can_merge_with_neighbor(self, r, c, value):
        # Check above
        if r > 0 and self.board[r - 1][c] and self.board[r - 1][c].get_value() == value:
            return True
        # Check below
        if r < 3 and self.board[r + 1][c] and self.board[r + 1][c].get_value() == value:
            return True
        # Check left
        if c > 0 and self.board[r][c - 1] and self.board[r][c - 1].get_value() == value:
            return True
        # Check right
        if c < 3 and self.board[r][c + 1] and self.board[r][c + 1].get_value() == value:
            return True

        # Special check for 1s and 2s being able to merge
        if value == 1:
            if r > 0 and self.board[r - 1][c] and self.board[r - 1][c].get_value() == 2:
                return True
            if r < 3 and self.board[r + 1][c] and self.board[r + 1][c].get_value() == 2:
                return True
            if c > 0 and self.board[r][c - 1] and self.board[r][c - 1].get_value() == 2:
                return True
            if c < 3 and self.board[r][c + 1] and self.board[r][c + 1].get_value() == 2:
                return True

        if value == 2:
            if r > 0 and self.board[r - 1][c] and self.board[r - 1][c].get_value() == 1:
                return True
            if r < 3 and self.board[r + 1][c] and self.board[r + 1][c].get_value() == 1:
                return True
            if c > 0 and self.board[r][c - 1] and self.board[r][c - 1].get_value() == 1:
                return True
            if c < 3 and self.board[r][c + 1] and self.board[r][c + 1].get_value() == 1:
                return True

        return False

    def get_score(self):
        return sum(tile.get_value() for row in self.board for tile in row if tile)

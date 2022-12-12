from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class Board:
    def __init__(self, dimension=4):
        self.dimension = dimension
        self.tiles = [[0] * dimension for _ in range(dimension)]

    def __getitem__(self, item):
        i, j = item
        return self.tiles[i][j]

    def __setitem__(self, key, value):
        if not self.is_in_bounds(key):
            return
        row, col = key
        self.tiles[row][col] = value

    def __repr__(self):
        value = ""
        for row in self.tiles:
            row_str = " | ".join(map(str, row)) + "\n"
            value += row_str
            value += "-"*len(row_str) + "\n"
        return value

    def is_in_bounds(self, index):
        row, col = index
        is_in_row_bounds = 0 <= row < self.dimension
        is_in_col_bounds = 0 <= col < self.dimension
        return is_in_row_bounds and is_in_col_bounds

    def shift(self, direction):
        board = Board()
        row_shift, col_shift = direction.value
        for row in range(self.dimension):
            for col in range(self.dimension):
                board[row + row_shift, col + col_shift] = self[row, col]
        return board


if __name__ == '__main__':
    board = Board()
    print(board)

    board[1, 1] = 1
    print(board)
    print(board.shift(Direction.UP))
    print(board.shift(Direction.DOWN))
    print(board.shift(Direction.LEFT))
    print(board.shift(Direction.RIGHT))

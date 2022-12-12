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
        i, j = key
        self.tiles[i][j] = value

    def __repr__(self):
        value = ""
        for row in self.tiles:
            value += str(row) + '\n'
        return value

    def is_in_bounds(self, index):
        i, j = index
        return 0 <= i < self.dimension and 0 <= j < self.dimension

    def shift(self, direction):
        i, j = direction.value
        for row in range(self.dimension):
            for col in range(self.dimension):
                new_row = row + i
                new_col = col + j
                index = row, col
                new_index = new_row, new_col
                print(index, '->', new_index)
                if not self.is_in_bounds(new_index):
                    continue
                self[new_index] = self[index]
                self[index] = 0


if __name__ == '__main__':
    board = Board()

    board[1, 1] = 1
    print(board)
    board.shift(Direction.UP)
    print(board)
    board.shift(Direction.DOWN)
    print(board)
    board.shift(Direction.LEFT)
    print(board)
    board.shift(Direction.RIGHT)
    print(board)

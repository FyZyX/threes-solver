from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def opposite(self):
        match self:
            case Direction.RIGHT:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.RIGHT
            case Direction.DOWN:
                return Direction.DOWN
            case _:
                return Direction.UP


class Board:
    def __init__(self, dimension=4):
        self.dimension = dimension
        self.tiles = [[0] * dimension for _ in range(dimension)]

    def __getitem__(self, key):
        if not self.is_in_bounds(key):
            return
        i, j = key
        return self.tiles[i][j]

    def __setitem__(self, key, value):
        if not self.is_in_bounds(key):
            return
        row, col = key
        self.tiles[row][col] = value

    def __add__(self, other):
        if not isinstance(other, Board):
            raise ValueError
        board = Board()
        for row in range(self.dimension):
            for col in range(self.dimension):
                current = self[row, col]
                new = other[row, col]
                tile = self[row, col]
                if current == 0:
                    tile = other[row, col]
                elif self[row, col] == other[row, col]:
                    tile = self[row, col] + 1
                else:
                    tile = self[row, col]
                board[row, col] = tile

    def __repr__(self):
        value = ""
        for row in self.tiles:
            row_str = " | ".join(map(str, row)) + "\n"
            value += row_str
            value += "-" * len(row_str) + "\n"
        return value

    def is_in_bounds(self, index):
        row, col = index
        is_in_row_bounds = 0 <= row < self.dimension
        is_in_col_bounds = 0 <= col < self.dimension
        return is_in_row_bounds and is_in_col_bounds

    def rotate_index(self, row, col, direction):
        match direction:
            case Direction.RIGHT:
                return col, self.dimension - 1 - row
            case Direction.LEFT:
                return self.dimension - 1 - col, row
            case Direction.DOWN:
                return self.dimension - 1 - row, self.dimension - 1 - col
            case _:
                return row, col

    def rotate(self, direction):
        board = Board()
        for row in range(self.dimension):
            for col in range(self.dimension):
                board[self.rotate_index(row, col, direction)] = self[row, col]
                # match direction:
                #     case Direction.RIGHT:
                #         board[col, self.dimension - 1 - row] = self[row, col]
                #     case Direction.LEFT:
                #         board[row, col] = self[col, self.dimension - 1 - row]
                #     case Direction.DOWN:
                #         board[row, col] = self[self.dimension - 1 - row,
                #                                self.dimension - 1 - col]
                #     case _:
                #         continue
        return board

    def shift(self, direction):
        current_board = self.rotate(direction)
        print("******")
        print(current_board)
        board = Board()
        merged = set()
        for row in range(1, self.dimension):
            print("~~~~~~~~~")
            print(board)
            print(merged)
            for col in range(self.dimension):
                print(row, col)
                destination_row = row - 1
                destination_col = col
                destination_tile = current_board[destination_row, destination_col]
                current_tile = current_board[row, col]
                if destination_tile is None:
                    continue
                if (destination_row, destination_col) in merged:
                    board[destination_row, destination_col] = current_tile
                    merged.add((row, col))
                    continue
                if destination_tile == 0:
                    board[destination_row, destination_col] = current_tile
                    merged.add((row, col))
                elif current_tile == destination_tile:
                    board[destination_row, destination_col] = current_tile + 1
                    merged.add((row, col))
                else:
                    board[destination_row, destination_col] = destination_tile
                    board[row, col] = current_tile
        return board.rotate(direction.opposite())


if __name__ == '__main__':
    board = Board()
    # for row in range(4):
    #     for col in range(4):
    #         board[row, col] = 4 * row + col
    board[0, 0] = 1
    board[0, 1] = 1
    board[0, 2] = 1
    board[0, 3] = 1
    board[1, 0] = 0
    board[1, 1] = 0
    board[1, 2] = 0
    board[1, 3] = 0
    board[2, 0] = 2
    board[2, 1] = 2
    board[2, 2] = 2
    board[2, 3] = 2
    board[3, 0] = 0
    board[3, 1] = 0
    board[3, 2] = 0
    board[3, 3] = 0
    print(board)
    # print(board.shift(Direction.UP))
    # print(board.shift(Direction.DOWN))
    # print(board.shift(Direction.LEFT))
    print(board.shift(Direction.RIGHT))

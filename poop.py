import itertools
import random


class Tile:
    def __init__(self, value=0):
        self.value = value


class Index:
    def __init__(self, row=None, col=None):
        self.row = random.randint(0, 3) if row is None else row
        self.col = random.randint(0, 3) if col is None else col

    def rotate(self, direction):
        if direction.lower().startswith("u"):
            return Index(self.row, self.col)
        elif direction.lower().startswith("d"):
            return Index(3 - self.row, 3 - self.col)
        elif direction.lower().startswith("l"):
            return Index(3 - self.col, self.row)
        elif direction.lower().startswith("r"):
            return Index(self.col, 3 - self.row)
        else:
            print("Invalid direction")


class Board:
    def __init__(self):
        # Initialize the game board as a 4x4 grid of zeroes
        self.tiles = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        # self.tiles = [[Tile() for _ in range(4)] for _ in range(4)]

    def __getitem__(self, index: Index):
        return self.tiles[index.row][index.col]

    def __setitem__(self, index: Index, value):
        self.tiles[index.row][index.col] = value

    def spawn(self, direction):
        while True:
            index = Index(row=3).rotate(direction)
            if self[index] == 0:
                break
        self[index] = random.choice([1, 2])

    def slide(self, direction):
        for row, col in itertools.product(range(1, 4), range(4)):
            source_index = Index(row, col).rotate(direction)
            destination_index = Index(row - 1, col).rotate(direction)
            source = self[source_index]
            destination = self[destination_index]
            if source == 0:
                continue
            destination_is_empty = destination == 0
            destination_is_equal = destination == source
            if destination_is_empty or destination_is_equal:
                self[destination_index] = source + destination
                self[source_index] = 0

    def move(self, direction):
        self.slide(direction)
        self.spawn(direction)

    def show(self):
        # Print the current game board
        for row in self.tiles:
            print(row)


def play():
    board = Board()
    board[Index()] = random.choice([1, 2])
    board[Index()] = random.choice([1, 2])
    # Game loop
    while True:
        board.show()
        # Get input from the user for the next move
        move_dir = input("Enter direction to move (up, down, left, right): ")
        # Move the tiles and add a new tile
        board.move(move_dir)


if __name__ == '__main__':
    play()

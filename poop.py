import itertools
import random


class Tile:
    def __init__(self, value=0):
        self.value = value

    def is_empty(self):
        return self.value == 0

    def clear(self):
        self.value = 0

    def merge(self, destination: 'Tile'):
        if destination.is_empty() or self.value == destination.value:
            destination.value += self.value
            self.clear()

    def __str__(self):
        return str(self.value)


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
        self.tiles = [[Tile() for _ in range(4)] for _ in range(4)]
        self[Index()] = Tile(random.choice([1, 2]))
        self[Index()] = Tile(random.choice([1, 2]))

    def __getitem__(self, index: Index):
        return self.tiles[index.row][index.col]

    def __setitem__(self, index: Index, value: Tile):
        self.tiles[index.row][index.col] = value

    def spawn(self, direction):
        while True:
            index = Index(row=3).rotate(direction)
            if self[index].is_empty():
                break
        self[index] = Tile(random.choice([1, 2]))

    def slide(self, direction):
        for row, col in itertools.product(range(1, 4), range(4)):
            source_index = Index(row, col).rotate(direction)
            destination_index = Index(row - 1, col).rotate(direction)
            source = self[source_index]
            destination = self[destination_index]
            if source.is_empty():
                continue
            source.merge(destination)

    def move(self, direction):
        self.slide(direction)
        self.spawn(direction)

    def show(self):
        for row in self.tiles:
            print(" ".join(map(str, row)))


def play():
    board = Board()
    # Game loop
    while True:
        board.show()
        # Get input from the user for the next move
        while True:
            direction = input("Enter direction to move (up, down, left, right): ")
            if direction in ["u", "d", "r", "l"]:
                break
        # Move the tiles and add a new tile
        board.move(direction)


if __name__ == '__main__':
    play()

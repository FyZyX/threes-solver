import itertools
import random

# Initialize the game board as a 4x4 grid of zeroes
board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


def random_index(row=None, col=None):
    row = random.randint(0, 3) if row is None else row
    col = random.randint(0, 3) if col is None else col
    return row, col


# Function to add a new tile to the board
def rotate_index(row, col, direction):
    if direction.upper() == "UP":
        return row, col
    elif direction.upper() == "DOWN":
        return 3 - row, 3 - col
    elif direction.upper() == "LEFT":
        return 3 - col, row
    elif direction.upper() == "RIGHT":
        return col, 3 - row
    else:
        print("Invalid direction")
    return row, col


def add_tile(row=None, col=None):
    # Choose a random location on the board that is currently empty
    x, y = random_index(row, col)
    while board[x][y] != 0:
        x, y = random_index(row, col)
    # Add a new tile with a value of either 1 or 2
    board[x][y] = random.choice([1, 2])


def spawn(direction):
    while True:
        row, col = random_index(row=3)
        x, y = rotate_index(row, col, direction)
        if board[x][y] == 0:
            break
    add_tile(x, y)


def slide(direction):
    for row, col in itertools.product(range(1, 4), range(4)):
        source_row, source_col = rotate_index(row, col, direction)
        destination_row, destination_col = rotate_index(row - 1, col, direction)
        source = board[source_row][source_col]
        destination = board[destination_row][destination_col]
        if source == 0:
            continue
        destination_is_empty = destination == 0
        destination_is_equal = destination == source
        if destination_is_empty or destination_is_equal:
            board[destination_row][destination_col] = source + destination
            board[source_row][source_col] = 0
    spawn(direction)


def move(direction):
    slide(direction)


def play():
    add_tile()
    add_tile()
    # Game loop
    while True:
        # Print the current game board
        for row in board:
            print(row)
        # Get input from the user for the next move
        move_dir = input("Enter direction to move (up, down, left, right): ")
        # Move the tiles and add a new tile
        move(move_dir)


if __name__ == '__main__':
    play()

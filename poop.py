# Initialize the game board as a 4x4 grid of zeroes
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Function to add a new tile to the board
def add_tile(row=None, col=None):
    import random
    # Choose a random location on the board that is currently empty
    x = row or random.randint(0, 3)
    y = col or random.randint(0, 3)
    while board[x][y] != 0:
        x = row or random.randint(0, 3)
        y = col or random.randint(0, 3)
    # Add a new tile with a value of either 1 or 2
    board[x][y] = random.choice([1, 2])


def rotate_index(row, col, direction):
    if direction == "UP":
        return row, col
    elif direction == "DOWN":
        return 3 - row, 3 - col
    elif direction == "LEFT":
        return 3 - col, row
    elif direction == "RIGHT":
        return col, 3 - row
    else:
        print("Invalid direction")
    return row, col


def slide(direction):
    for row in range(1, 4):
        for col in range(4):
            r, c = rotate_index(row, col, direction)
            source = board[r][c]
            destination = board[r - 1][c]
            if source == 0:
                continue
            destination_is_empty = destination == 0
            destination_is_equal = destination == source
            if destination_is_empty or destination_is_equal:
                board[r - 1][c] = source + destination
                board[r][c] = 0
    add_tile(3)


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
        move("UP")


if __name__ == '__main__':
    play()

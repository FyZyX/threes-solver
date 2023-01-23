# Initialize the game board as a 4x4 grid of zeroes
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Function to add a new tile to the board
def add_tile():
    import random
    # Choose a random location on the board that is currently empty
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while board[x][y] != 0:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    # Add a new tile with a value of either 1 or 2
    board[x][y] = random.choice([1, 2])


# Function to move tiles in a given direction
def move_old_2(direction):
    if direction == "up":
        # Move tiles up and combine if possible
        for x in range(1, 4):
            for y in range(4):
                if board[x][y] != 0:
                    for i in range(x, 0, -1):
                        if board[i - 1][y] == 0:
                            board[i - 1][y] = board[i][y]
                            board[i][y] = 0
                            break
                        elif board[i - 1][y] == board[i][y]:
                            board[i - 1][y] *= 2
                            board[i][y] = 0
                            break
    elif direction == "down":
        # Move tiles down and combine if possible
        for x in range(2, -1, -1):
            for y in range(4):
                if board[x][y] != 0:
                    for i in range(x, 3):
                        if board[i + 1][y] == 0:
                            board[i + 1][y] = board[i][y]
                            board[i][y] = 0
                            break
                        elif board[i + 1][y] == board[i][y]:
                            board[i + 1][y] *= 2
                            board[i][y] = 0
                            break
    elif direction == "left":
        # Move tiles left and combine if possible
        for x in range(4):
            for y in range(1, 4):
                if board[x][y] != 0:
                    for i in range(y, 0, -1):
                        if board[x][i - 1] == 0:
                            board[x][i - 1] = board[x][i]
                            board[x][i] = 0
                            break
                        elif board[x][i - 1] == board[x][i]:
                            board[x][i - 1] *= 2
                            board[x][i] = 0
                            break
    elif direction == "right":
        # Move tiles right and combine if possible
        for x in range(4):
            for y in range(2, -1, -1):
                if board[x][y] != 0:
                    for i in range(y, 3):
                        if board[x][i + 1] == 0:
                            board[x][i + 1] = board[x][i]
                            board[x][i] = 0
                            break
                        elif board[x][i + 1] == board[x][i]:
                            board[x][i + 1] *= 2
                            board[x][i] = 0
                            break


def move_old(direction):
    if direction == "up":
        for row in range(1, 4):
            for col in range(4):
                if board[row][col] == 0:
                    continue
                if board[row - 1][col] == 0:
                    board[row - 1][col] = board[row][col]
                    board[row][col] = 0
                elif board[row - 1][col] == board[row][col]:
                    board[row - 1][col] *= 2
                    board[row][col] = 0


def slide():
    for row in range(1, 4):
        for col in range(4):
            if board[row][col] == 0:
                continue
            source = board[row][col]
            destination = board[row - 1][col]
            destination_is_empty = destination == 0
            destination_is_equal = destination == source
            if destination_is_empty or destination_is_equal:
                board[row - 1][col] = source + destination
                board[row][col] = 0


def move(direction):
    if direction == "up":
        for row in range(1, 4):
            for col in range(4):
                if board[row][col] == 0:
                    continue
                if board[row - 1][col] == 0:
                    board[row - 1][col] = board[row][col]
                    board[row][col] = 0
                elif board[row - 1][col] == board[row][col]:
                    board[row - 1][col] *= 2
                    board[row][col] = 0


def play():
    add_tile()
    add_tile()
    # Game loop
    while True:
        # Print the current game board
        for row in board:
            print(row)
        # Get input from the user for the next move
        move_dir = input(
            "Enter direction to move (up, down, left, right): ")
        # Move the tiles and add a new tile
        move(move_dir)
        add_tile()


if __name__ == '__main__':
    play()

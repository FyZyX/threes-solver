class Move:
    def __init__(self, board):
        self.board = board

    def move_and_merge(self, from_row, from_col, to_row, to_col):
        from_tile = self.board.board[from_row][from_col]
        to_tile = self.board.board[to_row][to_col]

        # If the tile is empty, we simply move
        if not to_tile:
            self.board.board[to_row][to_col] = from_tile
            self.board.board[from_row][from_col] = None
        # Merge if possible
        elif to_tile.can_merge_with(from_tile):
            to_tile.merge(from_tile)
            self.board.board[from_row][from_col] = None

    def move_up(self):
        # Only try to move tile if it is not on the first row
        for row in range(1, 4):
            for col in range(4):
                self.move_and_merge(row, col, row-1, col)

    def move_down(self):
        # Only try to move tile if it is not on the last row
        for row in range(2, -1, -1):
            for col in range(4):
                self.move_and_merge(row, col, row+1, col)

    def move_left(self):
        # Only try to move tile if it is not in the first column
        for col in range(1, 4):
            for row in range(4):
                self.move_and_merge(row, col, row, col-1)

    def move_right(self):
        # Only try to move tile if it is not in the last column
        for col in range(2, -1, -1):
            for row in range(4):
                self.move_and_merge(row, col, row, col+1)

    def execute_move(self, direction):
        if direction.upper() == 'W':
            self.move_up()
        elif direction.upper() == 'A':
            self.move_left()
        elif direction.upper() == 'S':
            self.move_down()
        elif direction.upper() == 'D':
            self.move_right()
        else:
            print("Invalid input!")

        self.board.add_new_tile()

class Move:
    def __init__(self, board):
        self.board = board

    def move_up(self):
        for _ in range(4):  # ensures that all tiles have opportunity to move
            for r in range(1, 4):
                for c in range(4):
                    self.move_merge(r, c, r-1, c)

    def move_down(self):
        for _ in range(4):
            for r in range(2, -1, -1):
                for c in range(4):
                    self.move_merge(r, c, r+1, c)

    def move_left(self):
        for _ in range(4):
            for c in range(1, 4):
                for r in range(4):
                    self.move_merge(r, c, r, c-1)

    def move_right(self):
        for _ in range(4):
            for c in range(2, -1, -1):
                for r in range(4):
                    self.move_merge(r, c, r, c+1)

    def move_merge(self, r1, c1, r2, c2):
        # Get the Tile objects at (r1, c1) and (r2, c2)
        tile1 = self.board.board[r1][c1]
        tile2 = self.board.board[r2][c2]

        # If the tile at (r1, c1) is None or the tile at (r2, c2) is not None and their values do not match, return
        if not tile1 or (tile2 and tile1.get_value() != tile2.get_value()):
            return

        # If both tiles are not None and their values are equal, merge them
        if tile1 and tile2:
            tile2.set_value(tile1.get_value() + tile2.get_value())
            self.board.board[r1][c1] = None
        # If the tile at (r2, c2) is None, move the tile at (r1, c1) to (r2, c2)
        elif not tile2:
            self.board.board[r2][c2] = tile1
            self.board.board[r1][c1] = None

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

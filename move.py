class Move:
    def __init__(self, board):
        self.board = board

    def move_up(self):
        for r in range(1, 4):
            for c in range(4):
                self.move_merge(r, c, r - 1, c)

    def move_down(self):
        for r in range(2, -1, -1):
            for c in range(4):
                self.move_merge(r, c, r + 1, c)

    def move_left(self):
        for c in range(1, 4):
            for r in range(4):
                self.move_merge(r, c, r, c - 1)

    def move_right(self):
        for c in range(2, -1, -1):
            for r in range(4):
                self.move_merge(r, c, r, c + 1)

    def move_merge(self, r1, c1, r2, c2):
        tile1 = self.board.board[r1][c1]
        tile2 = self.board.board[r2][c2]

        # If the tile at (r1, c1) is None, return
        if not tile1:
            return

        # If the tile at (r2, c2) is None, move the tile at (r1, c1) to (r2, c2)
        if not tile2:
            self.board.board[r2][c2] = tile1
            self.board.board[r1][c1] = None
        # If both tiles are not None and their values are equal, merge them
        elif tile1.get_value() == tile2.get_value():
            tile2.set_value(tile1.get_value() + tile2.get_value())
            self.board.board[r1][c1] = None
        # If one tile is 1 and the other is 2, merge them to create 3
        elif {tile1.get_value(), tile2.get_value()} == {1, 2}:
            tile2.set_value(3)
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

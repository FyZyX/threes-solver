import itertools


class Move:
    def __init__(self, board):
        self.board = board

    def move_and_merge(self, from_row, from_col, to_row, to_col):
        from_tile = self.board.board[from_row][from_col]
        to_tile = self.board.board[to_row][to_col]

        if from_tile:
            if to_tile:
                if to_tile.can_merge(from_tile):
                    self.board.board[to_row][to_col] = from_tile + to_tile
                    self.board.board[from_row][from_col] = None
            else:
                self.board.board[to_row][to_col] = from_tile
                self.board.board[from_row][from_col] = None

    def iterate_over_grid(self, row_range, col_range, target):
        for row, col in itertools.product(row_range, col_range):
            target(row, col)

    def move_up(self):
        self.iterate_over_grid(
            range(1, 4), range(4),
            lambda row, col: self.move_and_merge(row, col, row - 1, col),
        )

    def move_down(self):
        self.iterate_over_grid(
            range(2, -1, -1), range(4),
            lambda row, col: self.move_and_merge(row, col, row + 1, col),
        )

    def move_left(self):
        self.iterate_over_grid(
            range(4), range(1, 4),
            lambda row, col: self.move_and_merge(row, col, row, col - 1),
        )

    def move_right(self):
        self.iterate_over_grid(
            range(4), range(2, -1, -1),
            lambda row, col: self.move_and_merge(row, col, row, col + 1),
        )

    def execute_move(self, direction):
        move_mapping = {'W': self.move_up, 'A': self.move_left, 'S': self.move_down,
                        'D': self.move_right}
        move_func = move_mapping.get(direction.upper())

        if move_func:
            move_func()
            self.board.add_new_tile()
        else:
            print("Invalid input!")

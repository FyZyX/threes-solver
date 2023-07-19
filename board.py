import random

class Board:
    def __init__(self):
        self.board = [[0]*4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(i,j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.board[x][y] = random.choice([1, 2, 3])

    def rotate_board(self):
        self.board = [list(t) for t in zip(*self.board[::-1])]

    def compress_board(self):
        # empty grid
        new_board = [[0]*4 for _ in range(4)]
        for i in range(4):
            pos = 0
            for j in range(4):
                if self.board[i][j] != 0:
                    new_board[i][pos] = self.board[i][j]
                    pos += 1
        self.board = new_board

    def merge_board(self):
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == 1 and self.board[i][j+1] == 2 or self.board[i][j] == 2 and self.board[i][j+1] == 1:
                    self.board[i][j] = 3
                    self.board[i][j+1] = 0
                elif self.board[i][j] >= 3 and self.board[i][j] == self.board[i][j+1]:
                    self.board[i][j] *= 2
                    self.board[i][j+1] = 0
        self.compress_board()

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if (self.board[i][j] == 1 and self.board[i][j+1] == 2) or (self.board[i][j] == 2 and self.board[i][j+1] == 1) or (self.board[i][j] >= 3 and self.board[i][j] == self.board[i][j+1]):
                    return True
        return False

    def move(self, direction):
        old_board = [x[:] for x in self.board]
        for _ in range(direction % 2, 4, 2):  # 0: up, 1: right, 2: down, 3: left
            self.rotate_board()
        self.compress_board()
        self.merge_board()
        self.compress_board()
        for _ in range((4 - direction) % 2, 4, 2):
            self.rotate_board()
        if old_board != self.board:
            self.add_new_tile()

    def check_for_end(self):
        if any(0 in row for row in self.board):
            return False
        for _ in range(2):
            if self.can_merge():
                return False
            self.rotate_board()
        return True

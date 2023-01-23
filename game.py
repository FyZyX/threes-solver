import random


class ThreesGame:
    def __init__(self):
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if
                       self.board[i][j] == 0]
        if empty_cells:
            value = 3 if random.random() < 0.9 else 6
            i, j = random.choice(empty_cells)
            self.board[i][j] = value

    def slide(self, direction):
        if direction == "up":
            for j in range(4):
                for i in range(1, 4):
                    if self.board[i][j] != 0:
                        for k in range(i - 1, -1, -1):
                            if self.board[k][j] == 0:
                                self.board[k][j] = self.board[k + 1][j]
                                self.board[k + 1][j] = 0
                            elif self.board[k][j] == self.board[k + 1][j]:
                                self.board[k][j] = self.board[k][j] * 2
                                self.board[k + 1][j] = 0
        elif direction == "down":
            for j in range(4):
                for i in range(2, -1, -1):
                    if self.board[i][j] != 0:
                        for k in range(i + 1, 4):
                            if self.board[k][j] == 0:
                                self.board[k][j] = self.board[k - 1][j]
                                self.board[k - 1][j] = 0
                            elif self.board[k][j] == self.board[k - 1][j]:
                                self.board[k][j] = self.board[k][j] * 2
                                self.board[k - 1][j] = 0
        elif direction == "left":
            for i in range(4):
                for j in range(1, 4):
                    if self.board[i][j] != 0:
                        for k in range(j - 1, -1, -1):
                            if self.board[i][k] == 0:
                                self.board[i][k] = self.board[i][k + 1]
                                self.board[i][k + 1] = 0
                            elif self.board[i][k] == self.board[i][k + 1]:
                                self.board[i][k] = self.board[i][k] * 2
                                self.board[i][k + 1] = 0
        elif direction == "right":
            for i in range(4):
                for j in range(2, -1, -1):
                    if self.board[i][j] != 0:
                        for k in range(j + 1, 4):
                            if self.board[i][k] == 0:
                                self.board[i][k] = self.board[i][k - 1]
                                self.board[i][k - 1] = 0
                            elif self.board[i][k] == self.board[i][k - 1]:
                                self.board[i][k] = self.board[i][k] * 2
                                self.board[i][k - 1] = 0

    def play(self):
        while True:
            print("Score:", self.score)
            for row in self.board:
                print(row)
            move = input("Enter move (up, down, left, right): ")
            if move in ('up', 'down', 'left', 'right'):
                self.slide(move)
            else:
                print("Invalid move")


if __name__ == '__main__':
    game = ThreesGame()
    game.play()

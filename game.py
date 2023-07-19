from board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def print_board(self):
        for row in self.board.board:
            print(row)
        print()

    def get_user_move(self):
        moves = ['up', 'right', 'down', 'left']
        direction = input("Enter direction (up, right, down, left): ")
        if direction in moves:
            return moves.index(direction)
        else:
            print("Invalid direction! Please enter again.")
            return self.get_user_move()

    def play(self):
        while not self.board.check_for_end():
            self.print_board()
            direction = self.get_user_move()
            self.board.move(direction)
        print("Game Over")
        self.print_board()

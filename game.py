from board import Board
from move import Move


def main():
    board = Board()
    move = Move(board)

    while True:
        board.display_board()
        direction = input("Enter direction (W/A/S/D): ")
        move.execute_move(direction)

        if board.check_game_over():
            print("Game Over!")
            break


if __name__ == "__main__":
    main()

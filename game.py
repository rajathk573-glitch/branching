"""Play Tic-Tac-Toe against the computer in a terminal."""

import random


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def display_board(board):
    """Print the current board, using cell numbers for empty spaces."""
    cells = [mark if mark else str(index + 1) for index, mark in enumerate(board)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}")
    print()


def winner(board):
    """Return the winning mark, or None if nobody has won."""
    for first, second, third in WINNING_LINES:
        if board[first] and board[first] == board[second] == board[third]:
            return board[first]
    return None


def computer_move(board):
    """Choose a winning move, then a blocking move, otherwise a random move."""
    for mark in ("O", "X"):
        for position in range(9):
            if board[position]:
                continue
            board[position] = mark
            if winner(board) == mark:
                board[position] = ""
                return position
            board[position] = ""

    empty_positions = [index for index, mark in enumerate(board) if not mark]
    return random.choice(empty_positions)


def play_round():
    """Play one round and return whether the player wants another round."""
    board = [""] * 9
    print("You are X. Choose a square from 1 to 9.")

    while True:
        display_board(board)
        while True:
            choice = input("Your move: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= 9:
                position = int(choice) - 1
                if not board[position]:
                    break
            print("Choose an empty square numbered 1 to 9.")

        board[position] = "X"
        if winner(board) or all(board):
            break

        position = computer_move(board)
        board[position] = "O"
        print(f"The computer chose square {position + 1}.")
        if winner(board) or all(board):
            break

    display_board(board)
    result = winner(board)
    if result == "X":
        print("You win!")
    elif result == "O":
        print("The computer wins!")
    else:
        print("It's a draw!")

    return input("Play again? (y/n): ").strip().lower() == "y"


def main():
    """Start the game and repeat rounds until the player quits."""
    print("Welcome to Tic-Tac-Toe!")
    while play_round():
        pass
    print("Thanks for playing!")


if __name__ == "__main__":
    main()

import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def human_move(player):
    # Repeats until it gets valid numbers
    print(f"Player {player}'s turn")

    row = int(input("Enter row (1, 2, 3): "))
    while row < 1 or row > 3:
        print("That number is out of range!")
        row = int(input("Enter row (1, 2, 3): "))

    col = int(input("Enter column (1, 2, 3): "))
    while col < 1 or col > 3:
        print("That number is out of range!")
        col = int(input("Enter col (1, 2, 3): "))

    return row-1, col-1


def ai_move(board):
    print(f"AI's turn")
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(available_moves)


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def main():
    # defines the board by creating a three-dimensional array
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]

    # Decide who you're going to play with
    print("Select game mode:")
    print("1. Play against AI")
    print("2. Play against another person")
    game_mode = int(input("Enter choice (1 or 2): "))

    current_player = 0

    while True:
        print_board(board)

        if game_mode == 2:
            row, col = human_move(players[current_player])
        else:
            if players[current_player] == "X":
                row, col = human_move(players[current_player])
            else:
                row, col = ai_move(board)

        # first, we check if the cell is empty
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            # check if there's a winner
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            # declares tie
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            # change player in case the game continues
            else:
                current_player = 1 - current_player
        else:
            print("Cell already taken. Try again.")


if __name__ == "__main__":
    main()

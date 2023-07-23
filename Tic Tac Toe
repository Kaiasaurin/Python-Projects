import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

def create_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def player_move(player, board):
    while True:
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player.symbol
            break
        else:
            print("Invalid move. Try again.")

def computer_move(player, board):
    valid_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                valid_moves.append((i, j))

    row, col = random.choice(valid_moves)
    board[row][col] = player.symbol

def check_winner(board):
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for condition in win_conditions:
        if condition.count(condition[0]) == 3 and condition[0] != " ":
            return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    
    player1_name = input("Enter Player 1 name: ")
    player1 = Player(player1_name, "X")
    
    mode = input("Choose the game mode: 1. Play against another player, 2. Play against computer: ")
    
    if mode == "1":
        player2_name = input("Enter Player 2 name: ")
        player2 = Player(player2_name, "O")
    else:
        player2 = Player("Computer", "O")

    board = create_board()
    display_board(board)

    current_player = player1 if random.choice([True, False]) else player2

    while True:
        print(f"It's {current_player.name}'s turn.")
        
        if current_player == player1 or (current_player == player2 and mode == "1"):
            player_move(current_player, board)
        else:
            computer_move(current_player, board)

        display_board(board)

        if check_winner(board):
            print(f"Congratulations! {current_player.name} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1

play_game()
#Open Use

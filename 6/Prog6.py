# Simple Tic-Tac-Toe Game

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check for a win
def check_winner(player):
    win_pos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in win_pos:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Main game loop
def play_game():
    current = 'X'
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current}, enter position (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = current

        if check_winner(current):
            print_board()
            print(f"Player {current} wins!")
            return
        current = 'O' if current == 'X' else 'X'
    print_board()
    print("It's a draw!")

# Run the game
play_game()

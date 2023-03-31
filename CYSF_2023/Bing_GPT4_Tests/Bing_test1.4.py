#Q1: “can you make me a tic tac toe game in python?”
#Q2: “can you add cells to make this code more visual?”
#Q3: “the game crashes when I input the wrong coordinate. Can you make it so it does not crash?”
#Q4: “can you add appropriate comments to the code?#

def print_board(board):
    # Print column labels
    print('  0 1 2')
    # Print horizontal line
    print(' +-+-+-+')
    for i, row in enumerate(board):
        # Print row label and row contents
        print(i, '|', '|'.join(row), '|')
        # Print horizontal line
        print(' +-+-+-+')

def make_move(board, x, y, player):
    # Check if the cell is already occupied
    if board[x][y] != ' ':
        return False
    # Make the move
    board[x][y] = player
    return True

def has_winner(board):
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # No winner found
    return None

def play_game():
    # Initialize the game board
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    # Set the starting player
    player = 'X'

    while True:
        # Print the current state of the game board
        print_board(board)
        try:
            # Get the user's move
            x = int(input('Enter x coordinate: '))
            y = int(input('Enter y coordinate: '))
        except ValueError:
            # Handle invalid input
            print('Invalid input! Please enter numbers only.')
            continue
        # Check if the move is valid
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Invalid coordinates! Please enter values between 0 and 2.')
            continue
        if not make_move(board, x, y, player):
            print('Invalid move!')
            continue
        # Check if there is a winner
        winner = has_winner(board)
        if winner:
            # Print the final state of the game board and announce the winner
            print_board(board)
            print(winner, 'wins!')
            break
        # Switch to the other player
        player = 'X' if player == 'O' else 'O'

# Start the game
play_game()
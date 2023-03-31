#Q1, Can you make me a tic tac toe game in python?
#Q2: Can you add comments to the code you provided?

def print_board(board):
    # This function prints the current state of the game board to the console
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_win(board):
    # This function checks whether there is a winner on the current board
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            # if there is a winner in a row, return the winning symbol
            return board[i][0]
        # check columns
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            # if there is a winner in a column, return the winning symbol
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        # if there is a winner in the top-left to bottom-right diagonal, return the winning symbol
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        # if there is a winner in the top-right to bottom-left diagonal, return the winning symbol
        return board[0][2]
    # if there is no winner yet, return None
    return None

def tic_tac_toe():
    # This function implements the main game loop
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    # create a 2D list to represent the game board, with empty cells represented by spaces
    player = "X"
    # set the first player to be "X"
    while True:
        # loop until the game ends
        print_board(board)
        # print the current state of the game board
        row = int(input("Enter row (1-3) for " + player + ": "))
        col = int(input("Enter column (1-3) for " + player + ": "))
        # prompt the current player to enter the row and column for their move
        if board[row-1][col-1] != " ":
            # check whether the chosen cell is already occupied
            print("This cell is already occupied. Try again.")
            continue
            # if it is, prompt the player to choose again
        board[row-1][col-1] = player
        # update the game board with the current player's move
        winner = check_win(board)
        # check whether there is a winner on the current board
        if winner:
            # if there is, print the board and the winner, then end the game
            print_board(board)
            print(winner + " wins!")
            break
        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            # check whether the board is full (i.e., no more empty cells)
            print_board(board)
            print("It's a tie!")
            break
            # if it is, print the board and announce a tie, then end the game
        player = "O" if player == "X" else "X"
        # switch to the other player for the next turn

tic_tac_toe()
# start the game!

#Q1, Can you make me a tic tac toe game in python?

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_win(board):
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        # check columns
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    while True:
        print_board(board)
        row = int(input("Enter row (1-3) for " + player + ": "))
        col = int(input("Enter column (1-3) for " + player + ": "))
        if board[row-1][col-1] != " ":
            print("This cell is already occupied. Try again.")
            continue
        board[row-1][col-1] = player
        winner = check_win(board)
        if winner:
            print_board(board)
            print(winner + " wins!")
            break
        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            print_board(board)
            print("It's a tie!")
            break
        player = "O" if player == "X" else "X"

tic_tac_toe()

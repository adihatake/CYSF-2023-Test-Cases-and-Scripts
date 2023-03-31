## Python tic tac toe

def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
    print("\n")
    
##Code above is hint provided
    
    
# Function to print the winner
def print_winner(winner):
    print("\t--------------------------------")
    print("\t              WINNER           ")
    print("\t--------------------------------")
 
    players = list(winner.keys())
    print("\t   ", players[0], "\t    ", winner[players[0]])
    print("\t   ", players[1], "\t    ", winner[players[1]])
 
    print("\t--------------------------------\n")
    print("\n")
    
# Function to check if the game is over
def is_game_over(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True
 
# Function to check if the player has won
def is_player_won(board, player):
    for i in range(9):
        for j in range(9):
            if board[i][j] == player:
                return True
    return False
 
# Function to check if the computer has won
def is_computer_won(board, computer):
    for i in range(9):
        for j in range(9):
            if board[i][j] == computer:
                return True
    return False




# Main function
def tic_tac_toe(board):
    print_tic_tac_toe(board)
    player = 1
    computer = 2
    while not is_game_over(board) and not is_player_won(board, player) and not is_computer_won(board, computer):
        if player == 1:
            player = 2
            computer = 1
        else:
            player = 1
            computer = 2
            print_tic_tac_toe(board)
            player = 1
            computer = 2
            print_tic_tac_toe(board)
            player = 1
            computer = 2
            print_tic_tac_toe(board)
            player = 1
            computer = 2
            print_tic_tac_toe(board)
            player = 1
            computer = 2
            print_tic_tac_toe(board)
        print_scoreboard(board)
    if is_game_over(board):
        print_winner(board)
    else:
        print_winner(board)
    
    return board

# Driver code
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],

                                                                                                                                                                                                       
                                                                                            
                                                                                                                                                                                                                                                    
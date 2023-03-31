#Q1: “Can you make me a tic tac toe game in python and an appropriate READme file?”
#Q2: “Can you add detailed comments to this code?”"


# Initialize the board as a list of 10 empty spaces
board = [' ' for x in range(10)]

# Function to insert a letter (either 'X' or 'O') into a given position on the board
def insertLetter(letter,pos):
    board[pos] = letter

# Function to check if a given position on the board is free (i.e. not occupied by either 'X' or 'O')
def spaceIsFree(pos):
    return board[pos] == ' '

# Function to print the current state of the board
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# Function to check if a given letter ('X' or 'O') has won the game by getting three in a row
def isWinner(bo, le):
    # Check all possible winning combinations
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo
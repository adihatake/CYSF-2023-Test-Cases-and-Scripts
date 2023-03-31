## Python tic tac toe

import random

board = [
    "", "", "",
    "", "", "",
    "", "", ""
]

def print_board(board):
    for i in range(3):
        print(board[i])
        print()


def check_win(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" and board[i][j+1] == "X" and board[i][j+2] == "X":
                return True
            elif board[i][j] == "O" and board[i][j+1] == "O" and board[i][j+2] == "O":
                return True
            elif board[i][j] == "X" and board[i+1][j] == "X" and board[i+2][j] == "X":
                return True
            elif board[i][j] == "O" and board[i+1][j] == "O" and board[i+2][j] == "O":
                return True
            elif board[i][j] == "X" and board[i+1][j+1] == "X" and board[i+2][j+2] == "X":
                return True
            elif board[i][j] == "O" and board[i+1][j+1] == "O" and board[i+2][j+2] == "O":
                return True
            elif board[i][j] == "X" and board[i+1][j+1] == "X" and board[i+2][j+2] == "X":
                return True
            elif board[i][j] == "O" and board[i+1][j+1] == "O" and board[i+2][j+2] == "O":
                return True
            elif board[i][j] == "X" and board[i+1][j+1] == "X" and board[i+2][j+2] == "X":
                return True
            elif board[i][j] == "O" and board[i+1][j+1] == "O" and board[i+2][j+2] == "O":
                return True
        return False


##Code above is hint provided

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                return False
    return True


def print_board(board):
    for i in range(3):
        print(board[i])
        print()
        
        if i == 0 or i == 1 or i == 2:
            print("---------")
        if i == 0 or i == 2 or i == 1:
            print("---------")
            
        if i == 0 or i == 1 or i == 2:
            print("---------")
            
        if i == 0 or i == 2 or i == 1:
            print("---------")
            
    print("---------")


def print_board(board):
    for i in range(3):
        print(board[i])
        print()
        
        if i == 0 or i == 1 or i == 2:
            print("---------")
        if i == 0 or i == 2 or i == 1:
            print("---------")
            
        if i == 0 or i == 1 or i == 2:
            print("---------")
            
        if i == 0 or i == 2 or i == 1:
            print("---------")
            
    print("---------")


def print_board(board):
    for i in range(3):
        print(board[i])
        print()
        
        if i == 0 or i == 1 or i == 2:
            print("---------")
        if i == 0 or i == 2 or i == 1:
            print("---------")
            
        if i == 0 or i == 1 or i == 2:
            print("---------")
            
        if i == 0 or i == 2 or i == 1:
            print("---------")
            
    print("---------")
        

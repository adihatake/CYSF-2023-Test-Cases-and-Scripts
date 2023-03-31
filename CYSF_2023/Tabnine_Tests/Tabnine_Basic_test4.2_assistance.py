## Python tic tac toe
import random

board = [
    "", "", "",
    "", "", "",
    "", "", ""
]

winner = ""
full_board = False


def verify_winner(board):

    if board[0] == board[1] == board[2] != "":
        return board[0]
    if board[3] == board[4] == board[5] != "":
        return board[3]
    if board[6] == board[7] == board[8] != "":
        return board[6]

    if board[0] == board[3] == board[6] != "":
        return board[0]
    if board[1] == board[4] == board[7] != "":
        return board[1]
    if board[2] == board[5] == board[8] != "":
        return board[2]

    if board[0] == board[4] == board[8] != "":
        return board[0]
    if board[2] == board[4] == board[6] != "":
        return board[2]

##Code above is hint provided


def check_full_board():
    counter = 0

    for box in board:
        if box:
            counter += 1
    if counter == 9:
        return True
    return False


def print_board(board):
    for i in range(9):
        print(board[i], end=" ")
    print()


def print_winner(winner):
    print(f"Congratulations, {winner} has won!")
    print_board(board)
    print()
    if check_full_board():
        print("It's a tie!")
        print_board(board)
        print()
        print_board(board)
        print()
        print_board(board)
        print()
        print_board(board)
        print()
        print_board(board)


def play_game():
    print_board(board)
    while True:
        player_input = input("Enter your move: ")
        if player_input == "exit":
            print("Thanks for playing!")
            print_board(board)
            break
        elif player_input == "1":
            if board[0] == "":
                board[0] = "X"
                print_board(board)
            elif board[0] == "X":
                board[0] = "O"
                print_board(board)
            elif board[0] == "O":
                board[0] = ""
                print_board(board)
        elif player_input == "2":
            if board[1] == "":
                board[1] = "X"
                print_board(board)
                print()
                print_board(board)
                print()
                print_board(board)
                
                
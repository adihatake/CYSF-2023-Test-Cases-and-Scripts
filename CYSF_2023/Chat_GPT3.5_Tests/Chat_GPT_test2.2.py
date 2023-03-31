#Q1: “Can you make me a tic tac toe game in python and create the appropriate READme file?
#Q2: “Can you change it so that the players are represented by “X”s and “O”s instead of numbers?”

import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.full((3,3), " ")
        self.current_player = "X"

    def play(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        else:
            return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return " "

    def is_full(self):
        return np.all(self.board != " ")

    def print_board(self):
        print("\n" + "-"*9)
        for row in self.board:
            print("| " + " ".join(row) + " |")
        print("-"*9)

game = TicTacToe()

while True:
    game.print_board()
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if game.play(row, col):
        winner = game.check_winner()
        if winner != " ":
            print(f"Player {winner} wins!")
            break
        elif game.is_full():
            print("Game Over. It's a tie!")
            break
    else:
        print("Invalid move. Try again.")

#Q1: “Can you make me a tic tac toe game in python and create the appropriate READme file?

import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3,3))
        self.current_player = 1

    def play(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = -self.current_player
            return True
        else:
            return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        return 0

    def is_full(self):
        return np.all(self.board != 0)

    def print_board(self):
        for row in self.board:
            print(row)

game = TicTacToe()

while True:
    game.print_board()
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    if game.play(row, col):
        winner = game.check_winner()
        if winner != 0:
            print("Player", winner, "wins!")
            break
        elif game.is_full():
            print("Game Over. It's a tie!")
            break
    else:
        print("Invalid move. Try again.")

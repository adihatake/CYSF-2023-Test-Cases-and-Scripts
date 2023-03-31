## Python tic tac toe

import random
import time

class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = "X"
        self.winner = None

    def print_board(self):
        for i in range(3):
            print(self.board[i])

    def print_winner(self):
        if self.winner == "X":
            print("X WINS!")
        elif self.winner == "O":
            print("O WINS!")
        else:
            print("TIE!")

    def make_move(self, move):
        if self.board[move[0]][move[1]] == 0:
            self.board[move[0]][move[1]] = self.turn
            self.turn = "X" if self.turn == "O" else "O"
            self.print_board()
            if self.check_win():
                self.winner = self.turn
                self.print_winner()
                return True
            else:
                return False
        else:
            return False
    
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.turn:
                self.winner = self.turn
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] == self.turn:
                self.winner = self.turn
                return True
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.turn:
                self.winner = self.turn
                return True
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.turn:
                self.winner = self.turn
                return True
        return False
    
    def reset(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = "X"
        self.winner = None
        self.print_board()
        return True
    
    def get_winner(self):
        return self.winner
    
    def get_board(self):
        return self.board
    
    def get_turn(self):
        return self.turn

def main():
    ttt = TicTacToe()
    while True:
        move = input("Enter a move: ")
        if ttt.make_move(move):
            if ttt.check_win():
                ttt.print_winner()
                break
            else:
                ttt.reset()
        else:
            print("Invalid move!")

if __name__ == "__main__":
    main()
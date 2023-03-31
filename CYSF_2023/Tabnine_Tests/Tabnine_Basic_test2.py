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
            self.turn = "X" if self.
            self.print_board()
            if self.check_win():
                self.winner = self.turn
                self.print_winner()
                return True
            self.turn = "O" if self.
            self.print_board()
            if self.check_win():
                self.winner = self.turn
                self.print_winner()
                return True
            return False
        else:
            return False

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                self.winner = self.board[i][0]
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                self.winner = self.board[0][i]
                return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                self.winner = self.board[0][0]
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                self.winner = self.board[0][2]
                return True
            if self.board[2][0] == self.board[1][1] == self.board[0][2]:
                self.winner = self.board[2][0]
                return True

        return False
    
    def reset(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = "X"
        self.winner = None
        self.print_board()
        self.print_winner()
        return True
    
    def play_game(self):
        while True:
            move = self.get_move()
            if move:
                self.make_move(move)
            else:
                self.reset()
            if self.check_win():
                return True
        return False
    
    def get_move(self):
        while True:
            try:
                move = [int(i) for i in input().split()]
                if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2 or move[2] < 0 or move[2] > 2:
                    raise ValueError
                return move
            except ValueError:
                print("Please enter a valid move.")
                continue
            except IndexError:
                print("Please enter a valid move.")
                continue
            except KeyboardInterrupt:
                print("Game Over!")
                return False
            except Exception as e:
                print(e)
                continue

if __name__ == "__main__":
    ttt = TicTacToe()
    while True:
        if ttt.play_game():
            break
    ttt.reset()
    ttt.print_board()
    ttt.print_winner()
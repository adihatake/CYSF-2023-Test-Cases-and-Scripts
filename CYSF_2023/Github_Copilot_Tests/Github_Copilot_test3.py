#this script is used to create a tic tac toe game  

import random


class TicTacToe:

    def __init__(self):
        self.board = []
        self.player = 1
        
        for i in range(3):
            self.board.append([" "] * 3)
        
        
"""A tic-tac-toe game built with Python and Tkinter."""

import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

class TicTacToe(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Tic Tac Toe")
        self.geometry("400x400")
        self.configure(background="white")
        self.grid()
        self.create_board()
        self.create_players()
        self.create_buttons()
        self.create_labels()
        self.create_buttons()
    
    def create_board(self):
        self.board = tk.Canvas(self, width=BOARD_SIZE*3, height=BOARD_SIZE*3)
        self.board.grid(row=0, column=0, columnspan=BOARD_SIZE, rowspan=BOARD_SIZE)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.board.create_rectangle(col*30, row*30, (col+1)*30, (row+1)*30, fill="black")
    
    def create_players(self):
        for player in DEFAULT_PLAYERS:
            self.board.create_text(player.col*30, player.row*30, text=player.label, fill=player.color)
    
    def create_buttons(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.board.create_rectangle(col*30, row*30, (col+1)*30, (row+1)*30, fill="black")
                self.board.create_text(col*30, row*30, text="", fill="black")
    
    def create_labels(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.board.create_text(col*30, row*30, text="", fill="black")
    
    def create_move(self, player: Player, move: Move):
        self.board.itemconfig(move.label, fill=player.color)
        self.board.itemconfig(move.label, text=move.label)
        self.board.coords(move.label, move.col*30, move.row*30)
        self.board.coords(move.label, move.col*30, (move.row+1)*30)
        self.board.coords(move.label, (move.col+1)*30, move.row*30)
        self.board.coords(move.label, (move.col+1)*30, (move.row+1)*30)
    
    def check_win(self, player: Player) -> bool:
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board.itemcget(f"{row}{col}", "fill") == player.color:
                    return True
        return False
    
    def check_draw(self) -> bool:
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board.itemcget(f"{row}{col}", "fill") == "white":
                    return False
        return True
    
    def check_tie(self) -> bool:
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board.itemcget(f"{row}{col}", "text") == "":
                    return False
        return True
    
    def check_winner(self) -> Player:
        if self.check_win(DEFAULT_PLAYERS[0]):
            return DEFAULT_PLAYERS[0]
        elif self.check_win(DEFAULT_PLAYERS[1]):
            return DEFAULT_PLAYERS[1]
        elif self.check_draw():
            return DEFAULT_PLAYERS[0]
        elif self.check_tie():
            return DEFAULT_PLAYERS[0]
        else:
            return DEFAULT_PLAYERS[0]
    
    def check_move(self, player: Player, move: Move) -> bool:
        if self.board.itemcget(move.label, "fill") == player.color:
            return True
        else:
            return False
        
    def play(self, player: Player, move: Move):
    
        if self.check_move(player, move):
            self.board.itemconfig(move.label, fill=player.color)
            self.board.itemconfig(move.label, text=move.label)
            self.board.coords(move.label, move.col*30, move.row*30)
            self.board.coords(move.label, move.col*30, (move.row+1)*30)
            self.board.coords(move.label, (move.col+1)*30, move.row*30)
            self.board.coords(move.label, (move.col+1)*30, (move.row+1)*30)
            if self.check_win(player):
                return True
            elif self.check_draw():
                return True
            elif self.check_tie():
                return True
            else:
                return False
    
    def reset(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.board.itemconfig(f"{row}{col}", fill="white")
                self.board.itemconfig(f"{row}{col}", text="")
                self.board.coords(f"{row}{col}", col*30, row*30)
                self.board.coords(f"{row}{col}", col*30, (row+1)*30)
                self.board.coords(f"{row}{col}", (col+1)*30, row*30)
                self.board.coords(f"{row}{col}", (col+1)*30, (row+1)*30)
    
    def play_again(self):
        self.reset()
        self.create_board()
        self.create_players()
        self.create_buttons()
        self.create_labels()
        self.create_buttons()
        self.create_move(self.check_winner(), Move(row=0, col=0))
        self.create_move(self.check_winner(), Move(row=0, col=1))
        self.create_move(self.check_winner(), Move(row=0, col=2))
        self.create_move(self.check_winner(), Move(row=1, col=0))
        self.create_move(self.check_winner(), Move(row=1, col=1))
    
    def play_again_button(self):
        self.play_again_button = tk.Button(self, text="Play Again", command=self.play_again)
        self.play_again_button.grid(row=1, column=0)
        self.play_again_button.focus_set()
        self.play_again_button.bind("<Return>", self.play_again)
        self.play_again_button.bind("<Button-1>", self.play_again)
        self.play_again_button.bind("<Button-3>", self.play_again)
    
    def quit(self):
        self.quit()
        self.destroy()
        
if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
    

        
        
                
    
    
#a python tic tac toe program using tkinter

import tkinter as tk
import tkinter.font
import sys
import math
import random

#global variables
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
#rgb
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

#board
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]]
player = "X"

#game fonts
X_WIN = ('Comic Sans MS', 40)
O_WIN = ('Comic Sans MS', 40)
TIE = ('Comic Sans MS', 40)

#game loop
def game_loop(player):
    running = True
    while running:
        for event in tk.event.get():
            if event.type == tk.QUIT:
                running = False
                tk.quit()
                sys.exit()
            if event.type == tk.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0] #x
                mouse_y = event.pos[1] #y
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    player = next_turn(player)
                    draw_figures()
                if check_winner(board, "X"):
                    draw_winner("X")
                    running = False
                if check_winner(board, "O"):
                    draw_winner("O")
                    running = False
                if check_tie():
                    draw_tie()
                    running = False
        tk.update()

#draw board
def draw_board():
    #draw vertical lines
    tk.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    tk.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    #draw horizontal lines
    tk.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    tk.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    
#draw figures
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                tk.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                tk.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == "O":
                tk.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                
#mark square
def mark_square(row, col, player):
    board[row][col] = player

#available square
def available_square(row, col):
    return board[row][col] == ""

#next turn
def next_turn(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return player

#check winner
def check_winner(board, player):
    #check horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    #check vertical
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    #check diagonal
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    return False

#check tie

def check_tie():   
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "":
                return False
    return True

#draw winner
def draw_winner(player):
    if player == "X":
        winner = X_WIN.render("X WINS!", 1, RED)
    elif player == "O":
        winner = O_WIN.render("O WINS!", 1, RED)
    screen.blit(winner, (WIDTH // 2 - winner.get_width() // 2, HEIGHT // 2 - winner.get_height() // 2))
    tk.display.update()
    tk.time.delay(3000)
    
#draw tie
def draw_tie():
    tie = TIE.render("TIE!", 1, RED)
    screen.blit(tie, (WIDTH // 2 - tie.get_width() // 2, HEIGHT // 2 - tie.get_height() // 2))
    tk.display.update()
    tk.time.delay(3000)
    
#main
def main():
    global screen
    tk.init()
    screen = tk.display.set_mode((WIDTH, HEIGHT))
    tk.display.set_caption("Tic Tac Toe")
    screen.fill(BG_COLOR)
    draw_board()
    game_loop(player)
    tk.quit()
    
main()
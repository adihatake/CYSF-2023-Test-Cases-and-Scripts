#a python tic tac toe program using pygame
# how to use: run the program and click on the board to place your mark


import pygame
import sys
import math
import random

pygame.init()

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

#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

#board
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]]

player = "X"

#game fonts
X_WIN = pygame.font.SysFont('comicsans', 40)
O_WIN = pygame.font.SysFont('comicsans', 40)
TIE = pygame.font.SysFont('comicsans', 40)

#game loop
def game_loop(player):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0] #x
                mouse_y = event.pos[1] #y
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    player = next_turn(player)
                    check_winner()
        draw_board()
        pygame.display.update()

#draw board
def draw_board():
    #draw vertical lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    #draw horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    
#mark square
def mark_square(row, col, player):
    board[row][col] = player
    print(f'{board}')
    
#available square
def available_square(row, col):
    return board[row][col] == ""
    
#next turn
def next_turn(player):
    if player == "X":
        return "O"
    else:
        return "X"
    
#check winner
def check_winner():
    #check horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != "":
            pygame.draw.line(screen, RED, (0, (row + 1) * SQUARE_SIZE - SQUARE_SIZE // 2), (WIDTH, (row + 1) * SQUARE_SIZE - SQUARE_SIZE // 2), LINE_WIDTH)
            winner = board[row][0]
            print(winner)
            win(winner)
    #check vertical
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != "":
            pygame.draw.line(screen, RED, ((col + 1) * SQUARE_SIZE - SQUARE_SIZE // 2, 0), ((col + 1) * SQUARE_SIZE - SQUARE_SIZE // 2, HEIGHT), LINE_WIDTH)
            winner = board[0][col]
            win(winner)
    #check diagonal
    if board[0][0] == board[1][1] == board[2][2] != "":
        pygame.draw.line(screen, RED, (50, 50), (550, 550), LINE_WIDTH)
        winner = board[0][0]
        win(winner)
    if board[2][0] == board[1][1] == board[0][2] != "":
        pygame.draw.line(screen, RED, (50, 550), (550, 50), LINE_WIDTH)
        winner = board[2][0]
        win(winner)
    #check tie
    if all([all(row) for row in board]) and winner == None:
        draw_tie()
        
#win
def win(winner):
    if winner == "X":
        win_text = X_WIN.render("X WINS!", 1, CROSS_COLOR)
    else:
        win_text = O_WIN.render("O WINS!", 1, CIRCLE_COLOR)
    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)
    game_loop()
    
#draw tie
def draw_tie():
    tie_text = TIE.render("TIE!", 1, CROSS_COLOR)
    screen.blit(tie_text, (WIDTH // 2 - tie_text.get_width() // 2, HEIGHT // 2 - tie_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)
    game_loop()
 
game_loop(player)

## needed to feed it the positional argument, 'player' to avoid errors
#Q1: Can you give me the code for a tic tac toe game in pygame?

import pygame
import sys
import time

# initialize Pygame
pygame.init()

# set window size and title
WINDOW_SIZE = (300, 300)
WINDOW_TITLE = 'Tic Tac Toe'
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

# define game variables
board = ['', '', '', '', '', '', '', '', '']
player = 'X'
game_over = False
font = pygame.font.Font(None, 50)

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# define functions
def draw_board():
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            x = j * 100
            y = i * 100
            pygame.draw.rect(window, WHITE, (x, y, 100, 100), 3)
            if board[index] == 'X':
                pygame.draw.line(window, WHITE, (x + 10, y + 10), (x + 90, y + 90), 3)
                pygame.draw.line(window, WHITE, (x + 90, y + 10), (x + 10, y + 90), 3)
            elif board[index] == 'O':
                pygame.draw.circle(window, WHITE, (x + 50, y + 50), 40, 3)

def check_win(player):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == player and board[i+1] == player and board[i+2] == player:
            return True
    # check columns
    for i in range(3):
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True
    # check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False

def draw_text(text, x, y):
    surface = font.render(text, True, WHITE)
    window.blit(surface, (x, y))

# main game loop
while not game_over:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # get board index
            row = mouse_y // 100
            col = mouse_x // 100
            index = row * 3 + col
            # update board
            if board[index] == '':
                board[index] = player
                if check_win(player):
                    draw_text(player + ' wins!', 50, 150)
                    game_over = True
                elif '' not in board:
                    draw_text('Tie!', 100, 150)
                    game_over = True
                else:
                    player = 'O' if player == 'X' else 'X'
    
    # draw the board
    draw_board()
    
    # update the display
    pygame.display.update()

time.sleep(4)
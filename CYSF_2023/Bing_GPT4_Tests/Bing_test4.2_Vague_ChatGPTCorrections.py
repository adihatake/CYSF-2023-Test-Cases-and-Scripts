#Q1: “Can you make me a tic tac toe game in pygame?” 
#Q2: "Can you create this project’s README file that includes diagrams and sample cases?""
#Q3: “Can you show me how to add an AI opponent?”

import pygame
import sys
from pygame.locals import *

pygame.init()

# Set up the display
window_size = (300, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Tic Tac Toe')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the board
board = [[None, None, None], [None, None, None], [None, None, None]]

# Set up the game variables
current_player = 'X'

def draw_board():
    # Draw the grid lines
    for x in range(1, 3):
        pygame.draw.line(screen, black, (x * 100, 0), (x * 100, 300))
        pygame.draw.line(screen, black, (0, x * 100), (300, x * 100))

    # Draw the X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, black, (col * 100 + 20, row * 100 + 20), (col * 100 + 80, row * 100 + 80))
                pygame.draw.line(screen, black, (col * 100 + 80, row * 100 + 20), (col * 100 + 20, row * 100 + 80))
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, black, (col * 100 + 50,row * 100 +50),40)
                
def minimax(board, depth, is_maximizing):
    if check_for_winner() == 'X':
        return -10
    elif check_for_winner() == 'O':
        return 10
    elif check_for_winner() == 'Tie':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == None:
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == None:
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = None
                    best_score = min(score, best_score)
        return best_score

def make_move(row,col):
    global current_player

    # Make sure the move is valid
    if board[row][col] != None:
        return

    # Make the move
    board[row][col] = current_player

    # Check for a winner
    winner = check_for_winner()
    if winner:
        print(winner + ' wins!')
        pygame.quit()
        sys.exit()

    # Switch players
    if current_player == 'X':
        current_player = 'O'
        # Make the AI move
        best_score = -float('inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if board[row][col] == None:
                    board[row][col] = 'O'
                    score = minimax(board, 0, False)
                    board[row][col] = None
                    if score > best_score:
                        best_score = score
                        best_move = (row,col)
        if best_move:
         make_move(*best_move)

    else:
        current_player = 'X'

def check_for_winner():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != None:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != None:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
        return True

    return False

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            row = y // 100
            col = x // 100
            make_move(row,col)

    # Draw the screen
    screen.fill(white)
    draw_board()
    pygame.display.update()
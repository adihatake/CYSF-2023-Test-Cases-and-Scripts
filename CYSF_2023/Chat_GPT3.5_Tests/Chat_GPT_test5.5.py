#Q1: “Can you make me a tic tac toe game in pygame?” 
#Q2: “Continue this code”
#Q3: "the code does not work, can you fix it?’
#Q4: “continue”
#Q5: "The code incorrectly tells me which turn it is. Can you fix it?”
#Q6: "continue this code"
#Q7: “The code does not account for ties. Can you fix this?”
#Q8: "continue this code"
#Q9: “where do I put this code in the program?”
#Q10: "continue this code"

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up the fonts
font = pygame.font.SysFont(None, 24)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the board
board = [['', '', ''], ['', '', ''], ['', '', '']]

# Set up the players
player1 = 'X'
player2 = 'O'
current_player = None
turn = None

# Set up the game state
game_over = False
winner = None

# Draw the board
def draw_board():
    # Fill the background
    screen.fill(WHITE)
    # Draw the grid lines
    pygame.draw.line(screen, BLACK, (SCREEN_WIDTH/3, 0), (SCREEN_WIDTH/3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (2*SCREEN_WIDTH/3, 0), (2*SCREEN_WIDTH/3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (0, SCREEN_HEIGHT/3), (SCREEN_WIDTH, SCREEN_HEIGHT/3), 5)
    pygame.draw.line(screen, BLACK, (0, 2*SCREEN_HEIGHT/3), (SCREEN_WIDTH, 2*SCREEN_HEIGHT/3), 5)

# Draw the pieces
def draw_pieces():
    for row in range(3):
        for col in range(3):
            if board[row][col] == player1:
                pygame.draw.circle(screen, BLACK, (int((col + 0.5) * SCREEN_WIDTH/3), int((row + 0.5) * SCREEN_HEIGHT/3)), int(SCREEN_WIDTH/6) - 10, 5)
            elif board[row][col] == player2:
                pygame.draw.line(screen, BLACK, (col * SCREEN_WIDTH/3 + 10, row * SCREEN_HEIGHT/3 + 10), ((col + 1) * SCREEN_WIDTH/3 - 10, (row + 1) * SCREEN_HEIGHT/3 - 10), 5)
                pygame.draw.line(screen, BLACK, ((col + 1) * SCREEN_WIDTH/3 - 10, row * SCREEN_HEIGHT/3 + 10), (col * SCREEN_WIDTH/3 + 10, (row + 1) * SCREEN_HEIGHT/3 - 10), 5)

# Check for a winner or a tie
def check_game_over():
    global game_over, winner
    # Check for a winner
    for symbol in [player1, player2]:
        # Check rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == symbol:
                winner = symbol
                game_over = True
        # Check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == symbol:
                winner = symbol
                game_over = True
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] == symbol:
            winner = symbol
            game_over = True
        if board[0][2] == board[1][1] == board[2][0] == symbol:
            winner = symbol
            game_over = True
    # Check for a tie
    if all(board[i][j] != '' for i in range(3) for j in range(3)) and not game_over:
        game_over = True
        winner = 'Tie'

# Set up the first turn
if random.randint(0, 1) == 0:
    current_player = player1
    turn = 'Player 1'
else:
    current_player = player2
    turn = 'Player 2'

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_player == player1:
                # Player 1's turn
                row = int(event.pos[1] // (SCREEN_HEIGHT/3))
                col = int(event.pos[0] // (SCREEN_WIDTH/3))
                if board[row][col] == '':
                    board[row][col] = player1
                    current_player = player2
                    turn = 'Player 2'
            else:
                # Player 2's turn
                row = int(event.pos[1] // (SCREEN_HEIGHT/3))
                col = int(event.pos[0] // (SCREEN_WIDTH/3))
                if board[row][col] == '':
                    board[row][col] = player2
                    current_player = player1
                    turn = 'Player 1'

    # Draw the board and pieces
    draw_board()
    draw_pieces()

    # Check for a winner or a tie
    check_game_over()

    # Draw the turn text
    if not game_over:
        text = font.render(turn + "'s turn (" + current_player + ")", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 15))
    else:
        print("Game over! " + winner + "wins!")
        text = font.render("Game over! " + winner, True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 15))
    screen.blit(text, text_rect)

    # Update the screen
    pygame.display.update()

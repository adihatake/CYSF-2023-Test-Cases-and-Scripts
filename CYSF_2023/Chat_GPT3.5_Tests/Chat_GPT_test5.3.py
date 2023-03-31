#Q1: “Can you make me a tic tac toe game in pygame?” 
#Q2: “Continue this code”
#Q3: "the code does not work, can you fix it?’
#Q4: “continue”
#Q5: "The code incorrectly tells me which turn it is. Can you fix it?”


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Define the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the font for the text
font = pygame.font.SysFont(None, 48)

# Define the players
player1 = 'X'
player2 = 'O'
current_player = player1

# Set up the initial game state
board = [['', '', ''], ['', '', ''], ['', '', '']]
game_over = False
winner = None

# Set the initial player and turn
if random.choice([True, False]):
    player1 = 'X'
    player2 = 'O'
    current_player = player1
    turn = 1
else:
    player1 = 'O'
    player2 = 'X'
    current_player = player2
    turn = 2


# Define the game over flag and the winner
game_over = False
winner = None

# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Draw the board function
def draw_board():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (SCREEN_WIDTH/3, 0), (SCREEN_WIDTH/3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (2*SCREEN_WIDTH/3, 0), (2*SCREEN_WIDTH/3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (0, SCREEN_HEIGHT/3), (SCREEN_WIDTH, SCREEN_HEIGHT/3), 5)
    pygame.draw.line(screen, BLACK, (0, 2*SCREEN_HEIGHT/3), (SCREEN_WIDTH, 2*SCREEN_HEIGHT/3), 5)

# Draw the pieces function
def draw_pieces():
    for row in range(3):
        for col in range(3):
            if board[row][col] == player1:
                pygame.draw.circle(screen, BLACK, (int((col+0.5)*SCREEN_WIDTH/3), int((row+0.5)*SCREEN_HEIGHT/3)), int(SCREEN_WIDTH/6)-10, 5)
            elif board[row][col] == player2:
                pygame.draw.line(screen, BLACK, (col*SCREEN_WIDTH/3+SCREEN_WIDTH/15, row*SCREEN_HEIGHT/3+SCREEN_HEIGHT/15), ((col+1)*SCREEN_WIDTH/3-SCREEN_WIDTH/15, (row+1)*SCREEN_HEIGHT/3-SCREEN_HEIGHT/15), 5)
                pygame.draw.line(screen, BLACK, ((col+1)*SCREEN_WIDTH/3-SCREEN_WIDTH/15, row*SCREEN_HEIGHT/3+SCREEN_HEIGHT/15), (col*SCREEN_WIDTH/3+SCREEN_WIDTH/15, (row+1)*SCREEN_HEIGHT/3-SCREEN_HEIGHT/15), 5)

# Check for a winner function
def check_winner():
    global game_over, winner
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            game_over = True
            winner = board[row][0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            game_over = True
            winner = board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        game_over = True
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        game_over = True
        winner = board[0][2]

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the game is over
            if game_over:
                # Restart the game
                board = [['', '', ''], ['', '', ''], ['', '', '']]
                game_over = False
                winner = None
                current_player = player1
            else:
                # Get the position of the mouse click
                x, y = pygame.mouse.get_pos()
                # Get the row and column of the click
                row = int(y // (SCREEN_HEIGHT / 3))
                col = int(x // (SCREEN_WIDTH / 3))
                # Check if the square is already occupied
                if board[row][col] == '':
                    # Update the board
                    board[row][col] = current_player
                    # Check for a winner
                    check_winner()
                    # Switch players
                    if current_player == player1:
                        current_player = player2
                    else:
                        current_player = player1

    # Draw the board and pieces
    draw_board()
    draw_pieces()

    # Check if the game is over
    if game_over:
        # Display the winner
        if winner is None:
            text = font.render("Tie!", True, BLACK)
        else:
            text = font.render(f"{winner} wins!", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
    else:
        # Display the current player
        text = font.render(f"Turn: {turn-1} - Player {current_player}'s turn", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/6))
        screen.blit(text, text_rect)


    # Update the display
    pygame.display.update()

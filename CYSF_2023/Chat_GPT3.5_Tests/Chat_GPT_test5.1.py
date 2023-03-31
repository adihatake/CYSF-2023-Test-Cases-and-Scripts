# Q1: “Can you make me a tic tac toe game in pygame?” 
# Q2: “Continue this code”


import pygame

# Initialize Pygame
pygame.init()

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the game
pygame.display.set_caption("Tic Tac Toe")

# Set the font for text on the screen
font = pygame.font.SysFont('Calibri', 40)

# Define the board
board = [['', '', ''], ['', '', ''], ['', '', '']]

# Define the players
player1 = 'X'
player2 = 'O'
current_player = player1

# Define the game state
game_over = False
winner = None

# Define the functions for drawing the board and the pieces
def draw_board():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (SCREEN_WIDTH/3, 0), (SCREEN_WIDTH/3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (2*SCREEN_WIDTH/3, 0), (2*SCREEN_WIDTH/3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, BLACK, (0, SCREEN_HEIGHT/3), (SCREEN_WIDTH, SCREEN_HEIGHT/3), 5)
    pygame.draw.line(screen, BLACK, (0, 2*SCREEN_HEIGHT/3), (SCREEN_WIDTH, 2*SCREEN_HEIGHT/3), 5)
    
def draw_pieces():
    for row in range(3):
        for col in range(3):
            if board[row][col] == player1:
                pygame.draw.circle(screen, BLACK, (int(col*SCREEN_WIDTH/3 + SCREEN_WIDTH/6), int(row*SCREEN_HEIGHT/3 + SCREEN_HEIGHT/6)), 60, 5)
            elif board[row][col] == player2:
                pygame.draw.line(screen, BLACK, (col*SCREEN_WIDTH/3 + SCREEN_WIDTH/15, row*SCREEN_HEIGHT/3 + SCREEN_HEIGHT/15), (col*SCREEN_WIDTH/3 + 2*SCREEN_WIDTH/15, row*SCREEN_HEIGHT/3 + 2*SCREEN_HEIGHT/15), 5)
                pygame.draw.line(screen, BLACK, (col*SCREEN_WIDTH/3 + 2*SCREEN_WIDTH/15, row*SCREEN_HEIGHT/3 + SCREEN_HEIGHT/15), (col*SCREEN_WIDTH/3 + SCREEN_WIDTH/15, row*SCREEN_HEIGHT/3 + 2*SCREEN_HEIGHT/15), 5)

# Define the function for checking if there is a winner
def check_winner():
    global game_over, winner
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            game_over = True
            winner = board[row][0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            game_over = True
            winner = board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        game_over = True
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        game_over = True
        winner = board[0][2]

def reset_board():
    global board, game_over, winner, current_player
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    game_over = False
    winner = None
    current_player = player1
    
draw_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                # Get the coordinates of the mouse click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Get the row and column of the cell clicked
                row = int(mouse_y // (SCREEN_HEIGHT/3))
                col = int(mouse_x // (SCREEN_WIDTH/3))
        # Check if the cell is empty
        if board[row][col] == '':
        # Place the current player's piece on the board
            board[row][col] = current_player
        # Check for a winner
        check_winner()
        # Switch to the other player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    
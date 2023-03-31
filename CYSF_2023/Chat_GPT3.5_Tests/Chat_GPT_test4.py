#Q1: “Can you make me a tic tac toe game in pygame?”
#Q2: "Continue"

import pygame

# Initialize the game
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Set up the game board
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the font
font = pygame.font.Font(None, 100)

# Set up the game loop
running = True
turn = "X"

# Define a function to draw the game board
def draw_board():
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, WHITE, (i * 200, j * 200, 200, 200), 2)
            if board[i][j] is not None:
                text_surface = font.render(board[i][j], True, BLACK)
                screen.blit(text_surface, (i * 200 + 50, j * 200 + 50))

# Define a function to handle player turns
def handle_turn(x, y):
    global turn
    i = x // 200
    j = y // 200
    if board[i][j] is None:
        board[i][j] = turn
        turn = "O" if turn == "X" else "X"

# Define a function to check for a winner
def check_winner():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    # No winner yet
    return None

# Define a function to reset the game
def reset_game():
    global board, turn
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    turn = "X"

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                handle_turn(*event.pos)
            elif event.button == 3:
                reset_game()

    # Game logic
    winner = check_winner()
    if winner is not None:
        winner_text = font.render(f"{winner} wins!", True, BLACK)
        screen.blit(winner_text, (150, 250))
        pygame.display.update()
        pygame.time.wait(2000)
        reset_game()
    elif all(board[i][j] is not None for i in range(3) for j in range(3)):
        tie_text = font.render("Tie!",True, BLACK)
        screen.blit(tie_text, (250, 250))
        pygame.display.update()
        pygame.time.wait(2000)
        reset_game()
        
    # Draw the screen
    screen.fill(BLACK)
    draw_board()
    pygame.display.update()

pygame.quit()

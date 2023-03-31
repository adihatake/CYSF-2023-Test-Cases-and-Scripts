import pygame
tic_tac_toe = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

def draw_board(board):
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(tic_tac_toe, (255, 255, 255), (j*100, i*100, 100, 100))
            pygame.draw.rect(tic_tac_toe, (0, 0, 0), (j*100+100, i*100+100, 100, 100))
            pygame.draw.rect(tic_tac_toe, (0, 0, 0), (j*100, i*100, 100, 100))
            pygame.draw.rect(tic_tac_toe, (0, 0, 0), (j*100+100, i*100+100, 100, 100))
            pygame.draw.rect(tic_tac_toe, (0, 0, 0), (j*100, i*100, 100, 100))
            pygame.draw.rect(tic_tac_toe, (0, 0, 0), (j*100+100, i*100+100, 100, 100))
            pygame.draw.rect(tic_tac_toe, (0, 0, 0), (j*100, i*100, 100, 100))
            pygame.draw.rect(tic_tac_toe, (0, 0, 0), (j*100+100, i*100+100, 100, 100))



def check_win(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                return True
    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T':
                return True
    return False

def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D':
                return True
    return False

def check_draw_2(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R':
                return True
    return False

def check_draw_3(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L':
                return True
    return False

def check_draw_4(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U':
                return True
    return False

def check_draw_5(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F':
                return True
    return False

def check_draw_6(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B':
                return True
    return False

def check_draw_7(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G':
                return True
    return False

def check_draw_8(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W':
                return True
    return False

def check_draw_9(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K':
                return True
    return False

def check_draw_10(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K' or board[i][j] == 'J':
                return True
    return False

def check_draw_11(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K' or board[i][j] == 'J' or board[i][j] == 'Q':
                return True
    return False

def check_draw_12(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K' or board[i][j] == 'J' or board[i][j] == 'Q' or board[i][j] == 'X':
                return True
    return False

def check_draw_13(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K' or board[i][j] == 'J' or board[i][j] == 'Q' or board[i][j] == 'X' or board[i][j] == 'Y':
                return True
    return False

def check_draw_14(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K' or board[i][j] == 'J' or board[i][j] == 'Q' or board[i][j] == 'X' or board[i][j] == 'Y' or board[i][j] == 'Z':
                return True
            else:
                return False
    return

def check_draw_15(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K' or board[i][j] == 'J' or board[i][j] == 'Q' or board[i][j] == 'X' or board[i][j] == 'Y' or board[i][j] == 'Z' or board[i][j] == 'A':
                return True
            else:
                return False
    return

def check_draw_16(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O' or board[i][j] == 'T' or board[i][j] == 'D' or board[i][j] == 'R' or board[i][j] == 'L' or board[i][j] == 'U' or board[i][j] == 'F' or board[i][j] == 'B' or board[i][j] == 'G' or board[i][j] == 'W' or board[i][j] == 'K' or board[i][j] == 'J' or board[i][j] == 'Q' or board[i][j] == 'X' or board[i][j] == 'Y' or board[i][j] == 'Z' or board[i][j] == 'A' or
            board[i][j] == 'B' or board[i][j] == 'C' or board[i][j] == 'D' or board[i][j] == 'E' or board[i][j] == 'F' or board[i][j] == 'G' or board[i][j] == 'H' or board[i][j] == 'I' or board[i][j] == 'J' or
            board[i][j] == 'K' or board[i][j] == 'L' or board[i][j] == 'M' or board[i][j] == 'N' or board[i][j] == 'O' or board[i][j] == 'P' or board[i][j] == 'Q' or board[i][j] == 'R' or board[i][j] == 'S' or
            board[i][j] == 'T' or board[i][j] == 'U' or board[i][j] == 'V' or board[i][j] == 'W' or board[i][j] == 'X' or board[i][j] == 'Y' or board[i][j] == 'Z' or board[i][j] == 'A' or board[i][j] == 'B' or
            board[i][j] == 'C' or board[i][j] == 'D' or board[i][j] == 'E' or board[i][j] == 'F' or board[i][j] == 'G' or board[i][j] == 'H' or board[i][j] == 'I' or board[i][j] == 'J' or
            board[i][j] == 'K' or board[i][j] == 'L' or board[i][j] == 'M' or board[i][j] == 'N' or board[i][j] == 'O' or board[i][j] == 'P' or board[i][j] == 'Q' or board[i][j] == 'R' or board[i][j] == 'S' or
            board[i][j] == 'T' or board[i][j] == 'U' or board[i][j] == 'V' or board[i][j] == 'W' or board[i][j] == 'X' or board[i][j] == 'Y' or board[i][j] == 'Z' or board[i][j] == 'A' or board[i][j] == 'B' or
            board[i][j] == 'C' or board[i][j] == 'D' or board[i][j] == 'E' or board[i][j] == 'F' or board[i][j] == 'G' or board[i][j] == 'H' or board[i][j] == 'I' or board[i][j] == 'J' or

###continues to generate code and reaches a saturation point
#Q1: Can you make me a python tic tac toe game with appropriate code 
# comments and a READme file that includes a summary of the project, 
# its dependencies, usage examples, diagrams and setup?

#Q2: Can you generate the code?

board = [' ' for _ in range(9)]

def draw_board():
    row1 = '|'.join(board[0:3])
    row2 = '|'.join(board[3:6])
    row3 = '|'.join(board[6:9])
    print(row1)
    print('-' * 5)
    print(row2)
    print('-' * 5)
    print(row3)

def check_win(player):
    for i in range(0, 9, 3):
        if board[i:i+3] == [player] * 3:
            return True
    for i in range(3):
        if board[i::3] == [player] * 3:
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

def get_move(player):
    valid_move = False
    while not valid_move:
        move = input(f"Player {player}, choose your move (1-9): ")
        try:
            move = int(move) - 1
            if move < 0 or move > 8:
                print("Invalid move, please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("That space is already taken, please choose another.")
            else:
                valid_move = True
        except ValueError:
            print("Invalid move, please enter a number between 1 and 9.")
    board[move] = player

def play_game():
    players = ['X', 'O']
    current_player = players[0]
    game_over = False
    while not game_over:
        draw_board()
        get_move(current_player)
        if check_win(current_player):
            draw_board()
            print(f"Congratulations, Player {current_player} wins!")
            game_over = True
        elif ' ' not in board:
            draw_board()
            print("The game ends in a tie.")
            game_over = True
        else:
            current_player = players[(players.index(current_player) + 1) % 2]

if __name__ == '__main__':
    play_game()

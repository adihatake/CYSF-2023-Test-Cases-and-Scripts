# python tic tac toe game

board = [' ' for x in range(10)]

#this function will insert the letter into the board
def insertLetter(letter, pos):
    board[pos] = letter
    
# this function will check if the space is free
def spaceisfree(pos):
    return board[pos] == ' '

#this function will print the board
def printboard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


#this function will check if the player is winner
#takes the board and the letter as the parameter
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

#this function will check if the player wants to play again
def playerMove():
    run = True
    while run:
        move = input('Please select a position to enter the X between 1 to 9')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisfree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# this function will check if the computer is winner
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

#this function will select the random move 
#uses the random module

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# this function will check if the board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    
# this function will run the main program
def main():
    print('Welcome to the game')
    printboard(board)
    
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printboard(board)
        else:
            print('Sorry, O\'s won this time!')
            break
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print(' ')
            else:
                insertLetter('O', move)
                print('Computer placed an O on position', move, ':')
                printboard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

#this function will ask the user if he wants to play again
while True:
    x = input('Do you want to play again? (y/n)')
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
    
import random

# input variable for the board
board  = [' ' for x in range(10)]

# this function is for getting user input
def insertLetter(letter,pos):
    board[pos] = letter

# a function that will check if the space is free
def isSpaceFree(pos):
    return board[pos] == ' '
# function to print out the board and get input from user
def printBoard(board):
    print('  1 |  2 |  3 ')
    print(' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('    |    |   ')
    print('-------------')
    print('  4 |  5 |  6 ')
    print(' ' + board[4] + '  |  ' + board[5] + ' |  ' + board[6])
    print('    |    |   ')
    print('-------------')
    print('  7 |  8 |  9 ')
    print(' ' + board[7] + '  |  ' + board[8] + ' |  ' + board[9])
    print('    |    |    ')
    print('-------------')

# function to count empty spaces in the board
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# function to determine a winner
def isWinner(board,letter):
            # Vertical spaces
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
           (board[4] == letter and board[5] == letter and board[6] == letter) or
           (board[7] == letter and board[8] == letter and board[9] == letter) or
        #    horizontal spaces
           (board[1] == letter and board[4] == letter and board[7] == letter) or
           (board[2] == letter and board[5] == letter and board[8] == letter) or
           (board[3] == letter and board[6] == letter and board[9] == letter) or
        #    daigoanl spaces
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter) )
        
# function for player move
def playerMove():
    run = True
    while run:
        move = input('Please select a position to enter X between 1 and 9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please enter number between 1 and 9')
        except:
                print('Please enter number between 1 and 9')

# AI like computer move
def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter ==  ' ' and x != 0 ]
    move = 0

    for x in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = x
            if isWinner(boardcopy, x):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    if i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move 


# function
def selectRandom(li):
    ln = len(li)
    rand = random.randrange(0,ln)
    return li[rand]

def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(isWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('computer placed an o on position' , move , ':')
                printBoard(board)
        else:
            print("you win!")
            break

    if isBoardFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
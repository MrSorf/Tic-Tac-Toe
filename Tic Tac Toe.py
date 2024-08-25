import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

currentPlayer = "Y"
winner = None 
gameRunning = True

#printing the game board
def printBoard(board):
      print(board[0] + " | " + board[1] + " | " + board[2])
      print("-------------")
      print(board[3] + " | " + board[4] + " | " + board[5]) 
      print("-------------")
      print(board[6] + " | " + board[7] + " | " + board[8])
    
printBoard(board)

#take player input
def playerInput (board):
    player = int(input("Enter a number 1-9: "))
    if player >= 1 and player <= 9 and board[player-1]== "_":
        board[player-1] = currentPlayer
    else:
        print("Spot already taken!")
        

#check for win or tie
#Horizontal 
def checkHorizontal(board):
    global winner 
    if board[0] == board[1]  == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
#Vertical 
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True

#diagonal 
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

#Check for Tie
def checkTie(board):
    if "_" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    if checkDiagonal or checkHorizontal or checkVertical:
        print(f"The winner is{winner}")
    
        
#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X" 


# computer 
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "0"
            switchPlayer()
        
#check for win or tie again

while gameRunning: 
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
    

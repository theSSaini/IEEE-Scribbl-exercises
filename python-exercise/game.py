# Tic tac toe python game  practice

# Feel free to delete anything below, it's just a template.

# @authors: Name1, Name2, ...

# @Roles:
#   Name1 did ___ method
#   Name2 did ___ method
#   ...

# Find a way to call main on launch
def call_main_on_launch:
    # Fill in

board = [][]

def main():
    for r in range (0,2):
        for c in range (0,2):
            board[r][c] = " "
    printer(board)
    playermove = input("Your move:")
    updateBoard(playermove[0], playermove[1], "O")
    ## Fill in
            
def printer(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-----")
    ## Fill in
          
def updateBoard(X, Y, sign):
    board[X][Y] = sign;

def chooseRandomMove():
    ## Fill in

def gameoverDetector():
    ## Fill in
    
# Add other methods as necessary

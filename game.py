from constants import BOARD_SIZE

def play_game():
    pass

def check_rows(board,player):
# This checks every row, god damn it
    for i in range(BOARD_SIZE):
        if all(board[i][j]==player for j in range(BOARD_SIZE)):
            return True


def check_col(board,player):
# This checks every column, I don't even know how all() actually works.
    for i in range(BOARD_SIZE):
        if all(board[j][i]==player for j in range(BOARD_SIZE)):
            return True
    
def check_diagonal(board,player):
# Now I have to make a function to check every diagonal.
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[2][2] == board[0][2] == player:
        return True
    
    return False

def check_winner(board,player):
# This will produce a winner
    if check_rows(board,player) or check_col(board,player) or check_diagonal(board,player):
        return True
        
    
def check_draw(board):
   
# This will check the draw I still don't know how to write these by my own.
   return all(col != " " for row in board for col in row)

def switch_user():
    pass

def game_over():
    pass
    
    

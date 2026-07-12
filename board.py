import colorama 
from colorama import Fore, Style
colorama.init(autoreset=True)
from constants import BOARD_SIZE

def create_board():

    board=[[" "for _ in range(BOARD_SIZE)] for _ in range (BOARD_SIZE)]

    return board

def display_board(board):

    for i, row in enumerate(board):
        print(Style.BRIGHT+Fore.RED+f" {row[0]} | {row[1]} | {row[2]} ")
        if i<BOARD_SIZE-1:
            print(Style.BRIGHT+Fore.RED+"---+---+---")

def place_mark(board, row, col, symbol):
# Okay so this places the mark
    board[row][col] = symbol

def position_empty(board, row ,col):
# Now this will check if the square is empty
    
    return board[row][col] == " "

def board_full(board):

#This checks if the board is full or not. 
#It takes me time to even write correct for loops.

    for row in board:
        for  cell in row:
           if cell  == " ":
               return False
    else:
        return True
        

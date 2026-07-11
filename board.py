import colorama 
from colorama import Fore, Style
colorama.init(autoreset=True)

def create_board():

    board=[[" "for _ in range(3)] for _ in range (3)]

    return board

def display_board(board):

    for i, row in enumerate(board):
        print(Style.BRIGHT+Fore.RED+f" {row[0]} | {row[1]} | {row[2]}")
        if i<2:
            print(Style.BRIGHT+Fore.RED+"---+---+---")

def place_mark():
    pass
def position_empty():
    pass
def board_full():
    pass


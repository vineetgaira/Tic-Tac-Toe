import colorama
from colorama import Fore
from board import position_empty
from constants import BOARD_SIZE
colorama.init(autoreset=True)

def get_player_move(board):
    while True:
        try:
            move=input(Fore.BLUE+"Please enter a row and column (row, column) (eg.,0 2):").split()
            
            if len(move)!=2:
                print(Fore.RED+"Please enter exactly two numbers!")
                continue

            row, col = int(move[0]), int(move[1])

            if row not in range(BOARD_SIZE) or col not in range(BOARD_SIZE):
                print(Fore.RED+"Please enter a valid number!")
                continue
            
            if not position_empty(board,row,col):
                print(Fore.RED+"That place is already taken.")
                continue

        except ValueError:
            print(Fore.RED+"Please enter a valid integer.")
            continue
        return row, col

def game_mode():
    while True:
        choice = input(Fore.BLUE+"Choose mode : (1) Player v/s Player (2) Player v/s Computer: ").strip()
        if choice in ("1","2"):
            return choice
        print(Fore.RED+"Please enter 1 or 2.")
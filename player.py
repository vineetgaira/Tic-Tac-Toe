import colorama
from colorama import Fore
from board import create_board
colorama.init(autoreset=True)

def get_player_move(board):
    while True:
        try:
            move=input(Fore.BLUE+"Please enter a row and column (row, column) (eg.,0 2):").split()
            
            if len(move)!=2:
                print(Fore.RED+"Please enter exactly two numbers!")
                continue

            row, col = int(move[0]), int(move[1])

            if row not in range(3) or col not in range(3):
                print(Fore.RED+"Please enter a valid number!")
                continue
            
            if board[row][col] != " ":
                print(Fore.RED+"That place is already taken.")
                continue

        except ValueError:
            print(Fore.RED+"Please enter a valid integer.")
            continue
        break

board=create_board()
get_player_move(board)
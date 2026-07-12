import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

def welcome():
    print(Style.BRIGHT+Fore.BLUE+r"""
  T I C   T A C   T O E 
 -------+-------+-------
    T   |   T   |   T   
 -------+-------+-------
    I   |   A   |   O   
 -------+-------+-------
    C   |   C   |   E   
""")

def show_menu():
    print(Fore.BLUE+"Welcome to Tic-Tac-Toe....\n" \
    "You have to enter row and column (eg.,0 2) to put the symbol there.\n" \
    "If three of the symbols are same in a row, column, or diagonal you win.")

def show_winner(winner):
    print(Fore.GREEN+f"{Fore.MAGENTA+winner} Wins the Game!")

def show_draw():
    print(Fore.GREEN+"It's a tie!")

def show_turn(player):
    print(Fore.CYAN+f"It's {Fore.MAGENTA+player}'s turn.")

def goodbye():
    print(Fore.CYAN+"Thanks for playing the gam...")


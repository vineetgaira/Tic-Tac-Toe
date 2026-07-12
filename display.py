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
    "You have to enter row and column to put the symbol there.\n" \
    "If three of the symbols are same in a row, column, or diagonal you win.")

def show_winner():
    pass

def show_draw():
    pass

def show_turn():
    pass

def goodbye():
    pass

welcome()
show_menu()
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

def welcome():
    print(Style.BRIGHT+Fore.RED+r"""
  T I C   T A C   T O E 
 -------+-------+-------
    T   |   T   |   T   
 -------+-------+-------
    I   |   A   |   O   
 -------+-------+-------
    C   |   C   |   E   
""")

def show_menu():
    pass

def show_winner():
    pass

def show_draw():
    pass

def show_turn():
    pass

def goodbye():
    pass

welcome()
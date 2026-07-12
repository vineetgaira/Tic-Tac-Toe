
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def clear_screen():

        print("\033[H\033[J", end="")

def play_again():

    while True:
        user_exit=input(Fore.BLUE+"Do you wanna play again? y/n:").lower().strip()
        if user_exit=="y":
            return True
        elif user_exit=="n":
            return False
        else:
            print(Fore.RED+"Please enter y/n.")





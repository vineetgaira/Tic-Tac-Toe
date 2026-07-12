from board import create_board, display_board, place_mark
from game import check_winner ,check_draw, switch_player
from display import welcome, show_menu, show_winner, show_draw, show_turn, goodbye
from player import get_player_move, game_mode
from ai import easy_move
from utils import clear_screen, play_again

def play_round(vs_ai):
# This is the main game loop.

    board=create_board()
    current_player = "X"

    while True:
        clear_screen()
        welcome()
        display_board(board)
        show_turn(current_player)

        if vs_ai and current_player=="O":
            row, col=easy_move(board)
        else:
            row,col=get_player_move(board)
        place_mark(board,row,col,current_player)

        if check_winner(board,current_player):
            display_board(board)
            show_winner(current_player)
            break 

        if check_draw(board):
            display_board(board)
            show_draw()
            break

        current_player=switch_player(current_player)

def main():
    show_menu()
    vs_ai=game_mode()=="2"
    while True:
        play_round(vs_ai)
        if not play_again():
            break
    goodbye()
        

         
if __name__=="__main__":
    main()


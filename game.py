from constants import BOARD_SIZE

def play_game():
    pass

def check_rows(board,player):

    for i in range(BOARD_SIZE):
        if all(board[i][j]==player for j in range(BOARD_SIZE)):
            return True


def check_col(board,player):
    pass

def check_diagonal():
    pass

def check_winner():
    pass

def check_draw():
    pass

def switch_user():
    pass

def game_over():
    pass
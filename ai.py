import random
from constants import BOARD_SIZE
from board import position_empty


def easy_move(board):
    empty_cells=[
        (row,col)
        for row in range(BOARD_SIZE)
        for col in range(BOARD_SIZE)
        if position_empty(board, row, col)
    ]
    return random.choice(empty_cells)
    

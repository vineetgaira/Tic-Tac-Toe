def create_board():

    board=[[" "for _ in range(3)] for _ in range (3)]

    return board

def display_board():

    board= create_board()

    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]}")
        if i<2:
            print("---+---+---")

def place_mark():
    pass
def position_empty():
    pass
def board_full():
    pass

display_board()
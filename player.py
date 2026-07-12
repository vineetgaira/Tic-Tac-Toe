from board import create_board

def get_player_move(board):
    while True:
        try:
            move=input("Please enter a row and column (row, column) (eg.,0 2):").split()
            
            if len(move)!=2:
                print("Please enter exactly two numbers!")
                continue

            row, col = int(move[0]), int(move[1])

            if row not in range(3) or col not in range(3):
                print("Please enter a valid number!")
                continue
            
            if board[row][col] != " ":
                print("That place is already taken.")
                continue

        except ValueError:
            print("Please enter a valid integer.")
            continue


# Demo code for bomb erasing map
from math import sqrt

board = [[".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "."]]

# These need to be one less the actual dimensions because reasons
# 6x6 grid = 5 and 5. stupid dumb.
board_width = 86
board_height = 24

# Gets distance given two sets of coordinates, (x1, y1) and (x2, y2)
# First set of coordinates is bomb target coordinates
# Second set of coordinates is targeted array cell
def get_dist(x1, x2, y1, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# Just prints the board
def print_board(board):
    for row in board:
        print(row)

# Bombage
def bomb(x, y, r, board):
    for i in range(target_x - r, target_x + r + 1):
        for j in range(target_y - r, target_y + r + 1):
            if get_dist(i, x, j, y) <= r and 0 <= i <= board_width and 0 <= j <= board_height:
                board[j][i] = "X"

# fun stuff
print("Before bomb:")
print_board(board)

target_x = 3
target_y = 3
radius = 1

bomb(target_x, target_y, radius, board)

print("After bomb:")
print_board(board)
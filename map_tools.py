from math import sqrt
from time import sleep
import animation
# These need to be one less the actual dimensions because reasons
# 6x6 grid = 5 and 5. stupid dumb.
board_width = 86
board_height = 24

worldMap = [
'................................#.#....................................................',
'.................##...##....########.....................#####.........................',
'....##################..##..#####..........#####..#############################........',
'.#################....#.....#............##.###############################..##........',
'.......############.#####.............#...#.############################.....#.........',
'.......################...............#####################################............',
'......##############.................#.##...##....#.######################..#..........',
'......############..................##....#..#######.##################..#..#..........',
'......##########....................#######.##..########################...............',
'........###........................#############.####..##################..............',
'.........##..#....................###############.#####.....###..####..................',
'............###...................###################.......##.....###.................',
'...............######..............##################..............#...................',
'................########..................##########...............##..##..............',
'................##########................########..................#..#.....###.......',
'................#############..............#######.......................#....##.......',
'.................###########..............########..#.......................####.......',
'...................########...............#######..##....................########......',
'...................######..................#####.......................###########.....',
'...................#####....................###........................##########......',
'...................####......................................................##........',
'....................##.......................................................#.........',
'....................##.................................................................',
'.....................#.................................................................',
'.......................................................................................']

# ----------- #
#    BASIC    #
# ----------- #

# Gets the character at (x, y) coordinates
def get_char(x, y):
    return worldMap[y][x]

# Swaps a character on the map given (x, y) coordinates and the character to replace with
# Returns the old character, probably useful for animation
def swapchar(xcoord,ycoord,char):
    temp = list(worldMap[ycoord])
    oldChar = temp[xcoord]
    temp[xcoord] = char
    worldMap[ycoord] = ''.join(temp)
    return oldChar

# Returns a list of all points within the radius of a point
# Takes in (x, y), radius, and board
def get_coords_in_circle(x, y, r):
    coords_list = []
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if get_dist(i, x, j, y) <= r and 0 <= i <= board_width and 0 <= j <= board_height:
                coords_list.append((i, j))
    return coords_list

# Gets the distance between two (x, y) coordinates
def get_dist(x1, x2, y1, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# i wonder what this does
def print_map():
    letters = ['A|','B|','C|','D|','E|','F|','G|','H|','I|','J|','K|','L|','M|','N|','O|','P|','Q|','R|','S|','T|','U|','V|','W|','X|','Y|']
    print('  012345678901234567890123456789012345678901234567890123456789012345678901234567890123456')
    print('  0---------1---------2---------3---------4---------5---------6---------7---------8------')
    for row in range(0,len(worldMap)):
        print(letters[row],end = '')
        print(worldMap[row])

# ------- #
#   WAR   #
# ------- #

def print_tension(tension):
    print(f"{'TENSION [' + '●' * (tension) + '○' * (9 - tension) + ']':^89}")

# Bombs the target (x, y) coordinates with desired radius
# Does not affect water
def bomb(x, y, r):
    # Parabola will be unused for now, I want to get the game actually working
    #   before adding fancy animations. it's just clutter right now
    # parabola_coords = animation.parabola(x, y, -6, -3)
    # for coords in animation.parabola(x, y, -6, -3):
    #     swapchar(*coords, "⥀")
    for coords in get_coords_in_circle(x, y, r):
        if get_char(*coords) != ".":
            swapchar(*coords, "⌗")

# def coup_scan(x, y, r):
#     for coords in get_coords_in_circle(x, y, r):
#         if get_char(*coords) != ".":
    
def build_factory(x, y):
    if get_char(x, y) != ".":
        swapchar(x, y, "◇")

def build_base(x, y):
    if get_char(x, y) != ".":
        swapchar(y, x, "□")

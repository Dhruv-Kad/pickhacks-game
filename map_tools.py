from math import sqrt
from time import sleep
import animation
import key
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
            swapchar(*coords, key.land_nuked)
'''
def coup_scan(x, y, r):
    for coords in get_coords_in_circle(x, y, r):
        if get_char(*coords) != ".":
'''
def coup(x,y,level):
    radius = 0
    if(level == 1):
        radius = 3
    elif(level == 2):
        radius = 2
    else:
        radius = 1
    coup_coords = get_coords_in_circle(x,y,radius)
    


# places factory character on the map and adds a new factory to the correct list of buildings    
def build_factory(x, y, player):
    if(player == 1):
        swapchar(x, y, key.p1_factory)

def build_base(x, y):
    if get_char(x, y) != key.water:
        swapchar(y, x, key.p1_base)

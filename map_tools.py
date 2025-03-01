from math import sqrt
from time import sleep
import animation
import key
from building_info import building
import re
from random import randint
from random import choice
import os

# These need to be one less the actual dimensions because reasons
# 6x6 grid = 5 and 5. stupid dumb.
board_width = 86
board_height = 24

p1_bases = []
p2_bases = []
p1_factories = []
p2_factories = []

worldMap = [
'................................#.#....................................................',
'.................##...##....########.....................#####.........................',
'....##################..##..#####..........#####..#############################........',
'..################....#.....#............##.###############################..##........',
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

def modify_tension(tension, amount):
    return tension + amount
# Swaps a character on the map given (x, y) coordinates and the character to replace with
# Returns the old character, probably useful for animation
def swapchar(xcoord,ycoord,char):
    temp = list(worldMap[ycoord])
    oldChar = temp[xcoord]
    temp[xcoord] = char
    worldMap[ycoord] = ''.join(temp)
    return oldChar, xcoord, ycoord

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

# Prompts the user for coordinates with the message parameter
# Returns x, y coordinates
# EX: C20 -> 20, 2
# Does not allow water or radiation placement
def coordinate_entry(message):
    while True:
        inpt = input(message)
        regex = re.search(r"([A-Ya-y])(\d+)", inpt)
        try:
            x = int(regex.group(2))
            y = ord(regex.group(1).upper()) - 65
            if get_char(x, y) not in [key.water, key.land_nuked]:
                return x, y
        except:
            continue

# ------- #
#   WAR   #
# ------- #

def print_tension(tension):
    print(f"{'TENSION [' + '●' * (tension) + '○' * (9 - tension) + ']':^89}")

# Bombs the target (x, y) coordinates with desired radius
# Does not affect water
def bomb(x, y, r):
    # surprised this worked on the first attempt
    parabola_coords = animation.parabola(x, y, -6, -3)
    old_char, old_x, old_y = key.water, 0, 0
    for coords in animation.parabola(x, y, -6, -3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_map()
        swapchar(old_x, old_y, old_char)
        old_char, old_x, old_y = swapchar(*coords, "⥀")
        print(old_char)
        sleep(0.075)
    
    # actual non animation bomb code
    for coords in get_coords_in_circle(x, y, r):
        if get_char(*coords) != ".":
            swapchar(*coords, key.land_nuked)

def coup(x,y,level,player):
    radius = 0
    challenge = False
    savedX = 0
    savedY = 0

    if(level == 1):
        #50/50 chance
        radius = 3
    elif(level == 2):
        #70% chance
        radius = 2
    else:
        #90% chance
        radius = 1
    coup_coords = get_coords_in_circle(x,y,radius)
    
    for coords in coup_coords:
        for base in p2_bases:
            if((base.xcoord == coords[0]) and (base.ycoord == coords[1])):
                savedX = coords[0]
                savedY = coords[1]
                challenge = True

    if(challenge):
        success = True
        if(level == 1):
            # if(randint(1,2) == 1):
            #     success = False
            if randint(1, 2) == 1: success = False
        elif(level == 2):
            # temp = randint(1,10)
            # if(temp == 1 or temp == 2 or temp == 3):
            #     success = False
            if randint(1, 10) in [1, 2, 3]: success = False
        else:
            # temp = randint(1,10)
            # if(temp == 1):
            #     success = False
            if randint(1, 10) == 1: success = False

        if(success):
            build_base(x,y,player)
            #delete player 2 base where conflict is
            baseIndex = 0
            for i in range(0,len(p2_bases)):
                if((savedX == p2_bases[i].xcoord) and (savedY == p2_bases[i].ycoord)):
                    baseIndex = i
                
            p2_bases.pop(baseIndex)
            swapchar(savedX,savedY,'#')
            return False
        else:
            swapchar(savedX,savedY,'▣')
            return True
    else:
        build_base(x,y,player)
        return False

# places factory character on the map and adds a new factory to the correct list of buildings    
def build_factory(x, y, player):
    base_connection = get_coords_in_circle(x,y,10)
    valid_placement = False
    if(player == 1):
        for coords in base_connection:
            for base in p1_bases:
                if((coords[0] == base.xcoord) and (coords[1] == base.ycoord)):
                    valid_placement = True
    
        swapchar(x, y, key.p1_factory)
        factory = building(x, y, "factory", True, 1)
        p1_factories.append(factory)
        return
    
    swapchar(x, y, key.p2_factory)
    factory = building(x, y, "factory", True, 2)
    factory = building(x, y, "factory", True, 2)
    p2_factories.append(factory)
    return

# Constructs a base for the given player at given x, y coordinates
def build_base(x, y, player):
    if(player == 1):
        swapchar(x, y, key.p1_base)
        base = building(x, y, "base", True, 1)
        p1_bases.append(base)
        return
    
    swapchar(x, y, key.p2_base)
    base = building(x, y, "base", False, 2)
    p2_bases.append(base)
    return

def spy_addition(numberofspies, oldprice):
    oldprice += 500
    numberofspies += 1  

def spy_work(numberofspies):
    
    spy_find_nums = []
    if (numberofspies > 0):
        i = 1
        while (i <= numberofspies):
            spy_find_nums.append(i)
            spy_find_nums.append(i + 50)
            i += 1
        selected = randint(1,100)
        if (selected in spy_find_nums):
            found_base = choice(p2_bases)
            swapchar(found_base.xcoord, found_base.ycoord, key.p2_base)
        else:
            print("Your spies have found nothing so far.")
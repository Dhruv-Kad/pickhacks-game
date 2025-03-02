import map_tools
import os
import key
import re

char_to_num = {'A': '0', 'B': '1', 'C': '2', 'D': '3', 'E': '4', 'F': '5', 'G': '6', 'H': '7', 'I': '8', 'J': '9', 'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24'}

difficulties = ["EASY", "MEDIUM", "HARD"]

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'|':-^59}")
    print(f"{'   /\\':<29} {'/\\   ':>29}")
    print(f"  /  \\{'Non-Proliferation':^47}/  \\   ")
    print(f"{' /    \\':<29} {'/    \\ ':>29}")
    print(f"{'|':-^59}")
    print(f"{'1. 1 Player':^59}")
    print(f"{'2. 2 Player (probably unused)':^59}")
    print(f"{'3. Exit':^59}")
    choice = input("Please select an option(type a number): ")
    if (choice == "1"):
        return setup1()
    elif (choice == "2"):
        setup2()

#ASks for coordinate for stater base
def p1coord_validation():
    os.system('cls' if os.name == 'nt' else 'clear')
    map_tools.print_map()
    while (True):
        x, y = map_tools.coordinate_entry("Please select the coordinates for your first base: ")
        map_tools.swapchar(x, y, key.p1_base)
        break

def setup1():
#asks for difficulty
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Please select a difficulty")
    print ()
    print ("-----------Easy-----------")
    print ("----------Medium----------")
    print ("-----------Hard-----------")
    print()

    difficulty = input("Difficulty: ")
    while (difficulty.upper() not in difficulties):
        difficulty = input("Please select a valid difficulty: ")

    p1coord_validation()

    return difficulty.lower()

#unused
def setup2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Please select a difficulty")
    print ()
    print ("-----------Easy-----------")
    print ("----------Medium----------")
    print ("-----------Hard-----------")
    print()

    difficulty = input("Difficulty: ")
    while (difficulty.upper() not in difficulties):
        difficulty = input("Please select a valid difficulty: ")

    p1coord_validation()

    print()
    print ("Please select the coordinates for your character")
    p2xcoord = int(input("X Coordinate: "))
    while (p2xcoord < 1 or p2xcoord > 24):
        p2xcoord = int(input("Please select a valid coordinate: "))
    p2ycoord = int(input("Y Coordinate: "))
    while (p2ycoord < 1 or p2xcoord > 87):
        p2ycoord = int(input("Please select a valid coordinate: "))
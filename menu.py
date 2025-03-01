import map_tools
import os
import key

# def char_to_num(char):
#     return ord(char) - 65
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
    print(f"{'2. 2 Player':^59}")
    print(f"{'3. Exit':^59}")
    choice = input("Please select an option(type a number): ")
    if (choice == "1"):
        setup1()
    elif (choice == "2"):
        setup2()

#ASks for coordinate for stater base
def p1coord_validation():
    os.system('cls' if os.name == 'nt' else 'clear')
    map_tools.print_map()
    while (True):
        print ("Please select the coordinates for your base")
        p1ycoord = input("Y Coordinate: ")
        while ((p1ycoord.upper() not in char_to_num.keys()) or (not p1ycoord.isalpha()) ):
            os.system('cls' if os.name == 'nt' else 'clear')
            map_tools.print_map()
            p1ycoord = input("Please select a valid Y coordinate: ")
        
        p1yletter_coord = char_to_num[p1ycoord.upper()]

        p1xcoord = input("X Coordinate: ")
        while ((not p1xcoord.isnumeric()) or (int(p1xcoord) < 0) or (int(p1xcoord) > 86)):
            os.system('cls' if os.name == 'nt' else 'clear')
            map_tools.print_map()
            p1xcoord = (input("Please select a valid X coordinate: "))
        if (map_tools.get_char(int(p1xcoord), int(p1yletter_coord)) != key.land):
            os.system('cls' if os.name == 'nt' else 'clear')
            map_tools.print_map()
            print ("Not a vlid placement coordinate.")
            print ("please try again.")
        else:
            map_tools.swapchar(int(p1xcoord), int(p1yletter_coord), "B")
            break
        
        # os.system('cls' if os.name == 'nt' else 'clear')
        # map_tools.print_map()

def setup1():
#asks for difficulty
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Please select a difficulty")
    print ("                        ")
    print ("----------Easy----------")
    print ("---------Medium---------")
    print ("----------Hard----------")
    print()

    difficulty = input("Difficulty: ")
    while (difficulty.upper() not in difficulties):
        difficulty = input("Please select a valid difficulty: ")

    p1coord_validation()

    
            
    

#unused
def setup2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("Please select a difficulty")
    print ("                        ")
    print ("----------Easy----------")
    print ("---------Medium---------")
    print ("----------Hard----------")
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
# menu()
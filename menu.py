import worldMap

def menu():
    print ("-----------------------------|-----------------------------")
    print ("   /\                                                 /\   ")
    print ("  /  \               Non-Proliferation               /  \  ")
    print (" /    \                                             /    \ ")
    print ("-----------------------------|-----------------------------")
    print ("                        1. 1 Player                        ")
    print ("                        2. 2 Player                        ")
    print ("                        3.   Exit                          ")
    print()
    choice = input("Please select an option(type a number): ")
    if (choice == "1"):
        setup1()
    elif (choice == "2"):
        setup2()


def setup1():
    print()
    print ("Please select a difficulty")
    print ("------------------------")
    print ("----------Easy----------")
    print ("---------Medium---------")
    print ("----------Hard----------")
    print ("Please select the coordinates for your character")
    p1xcoord = int(input("X Coordinate: "))
    while (p1xcoord < 1 or p1xcoord > 24):
        p1xcoord = int(input("Please select a valid coordinate: "))
    p1ycoord = int(input("Y Coordinate: "))
    while (p1ycoord < 1 or p1xcoord > 87):
        p1ycoord = int(input("Please select a valid coordinate: "))

def setup2():
    print ("Please select the coordinates for your character")
    p1xcoord = int(input("X Coordinate: "))
    while (p1xcoord < 1 or p1xcoord > 24):
        p1xcoord = int(input("Please select a valid coordinate: "))
    p1ycoord = int(input("Y Coordinate: "))
    while (p1ycoord < 1 or p1xcoord > 87):
        p1ycoord = int(input("Please select a valid coordinate: "))

    print()
    print ("Please select the coordinates for your character")
    p2xcoord = int(input("X Coordinate: "))
    while (p2xcoord < 1 or p2xcoord > 24):
        p2xcoord = int(input("Please select a valid coordinate: "))
    p2ycoord = int(input("Y Coordinate: "))
    while (p2ycoord < 1 or p2xcoord > 87):
        p2ycoord = int(input("Please select a valid coordinate: "))
menu()
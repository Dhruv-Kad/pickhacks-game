

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
    print ("Please select the coordinates for your character")
    p1xcoord = input("X Coordinate: ")
    p1ycoord = input("Y Coordinate(A-Y): ")

def setup2():
    print()
    print ("Please select the coordinates for your character Player 1")
    p1xcoord = input("X Coordinate: ")
    p1ycoord = input("Y Coordinate(A-Y): ")

    print()
    print ("Please select the coordinates for your character Player 2")
    p2xcoord = input("X Coordinate: ")
    p2ycoord = input("Y Coordinate(A-Y): ")

menu()
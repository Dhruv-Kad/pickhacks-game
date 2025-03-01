from map_tools import *
import os

# max value = 9
tension = 0

p1_money = 750
p1_income = 250
p1_spies = 0

# the interpreter shits itself if i don't have this as a parameter
def thing():
    print("1. nuke")
    print("2. spy")
    print("3. factory")
    print("4. coup (do not use)")

    choice = int(input("pick something "))

    match choice:
        case 1:
            x = int(input("enter nuke x: "))
            y = int(input("enter nuke y: "))
            bomb(x, y, 3)
            tension = 9

        case 2:
            global p1_spies
            p1_spies += 1

        case 3:
            x = int(input("enter factory x: "))
            y = int(input("enter factory y: "))
            build_factory(x, y)
            global p1_income
            p1_income += 150

def print_data():
    print(f"${p1_money} | +${p1_income}/t")
    print(f"{p1_spies ** 1.1:.2f}% chance to reveal enemy base")
    print()

while True:
    # this just clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    p1_money += p1_income

    print_map()
    print_tension(tension)

    print_data()
    print(p1_spies)

    thing()
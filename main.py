from map_tools import *
import os
import menu

# max value = 9
tension = 0

p1_money = 750
p1_income = 250
p1_spies = 0

nuke_price = 5000
p1_spy_price = 1000
p1_factory_price = 1000
coup_price = 1500

p1_factory_coords = []
p1_base_coords = []
p2_factory_coords = []
p2_base_coords = []

def shop():
    print(f"---SHOP---")
    print(f"1. nuke    | ${nuke_price}")
    print(f"2. spy     | ${p1_spy_price}")
    print(f"3. factory | ${p1_factory_price}")
    print(f"4. coup    | ${coup_price}")

    choice = int(input("pick something "))

    match choice:
        case 1:
            x = int(input("enter nuke x: "))
            y = int(input("enter nuke y: "))
            bomb(x, y, 2)
            global tension
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

        case 4:
            x = int(input("enter coup x: "))
            y = int(input("enter coup y: "))

# Prints the hud
# Contains (top to bottom) world map, tension meter, income, spy effectiveness
def print_hud():
    print_map()
    print_tension(tension)
    print(f"${p1_money} | +${p1_income}/t")
    print(f"{p1_spies * 1:.2f}% chance to reveal enemy base")
    print()



# show menu
coordinate_entry("enter in format A1: ")
menu.menu()


while True:
    # this just clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    p1_money += p1_income

    print_hud()
    
    shop()
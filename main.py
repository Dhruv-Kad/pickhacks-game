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
coup_base_price = 1500

p1_factory_coords = []
p1_base_coords = []
p2_factory_coords = []
p2_base_coords = []

def shop():
    print(f"---SHOP---")
    print(f"1. nuke    | ${nuke_price}")
    print(f"2. spy     | ${p1_spy_price}")
    print(f"3. factory | ${p1_factory_price}")
    print(f"4. coup    | ${coup_base_price} / {round(coup_base_price * 1.5)} / {coup_base_price * 2}")

    choice = int(input("pick something "))

    match choice:

        case 1:
            global p1_money
            if p1_money >= nuke_price:
                p1_money -= nuke_price
                x, y = coordinate_entry("Enter nuke coordinates: ")
                bomb(x, y, 2)
                global tension
                tension = 9

        case 2:
            if p1_money >= p1_spy_price:
                p1_money -= p1_spy_price
                global p1_spies
                p1_spies += 1

        case 3:
            if p1_money >= p1_factory_price:
                p1_money -= p1_factory_price
                x, y = coordinate_entry("Enter factory coordinates: ")
                build_factory(x, y, 1)
                global p1_income
                p1_income += 150

        case 4:
            coup_level = int(input("Enter coup level (1-3): "))
            if p1_money >= (coup_base_price * (0.5 * coup_level + 0.5)):
                p1_money -= (coup_base_price * (0.5 * coup_level + 0.5))
                x, y = coordinate_entry("Enter coup coordinates: ")

# Prints the hud
# Contains (top to bottom) world map, tension meter, income, spy effectiveness
def print_hud():
    print_map()
    print_tension(tension)
    print(f"${p1_money} | +${p1_income}/t")
    print(f"{p1_spies * 1:.2f}% chance to reveal enemy base")
    print()

# show menu
menu.menu()

while True:
    # this just clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    p1_money += p1_income

    print_hud()
    
    shop()
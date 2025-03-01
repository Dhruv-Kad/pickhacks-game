from map_tools import *
import os
import menu
import building_info
from random import randint

f = open("log.txt", "w")

# max value = 9
tension = 0
turn_counter = 0

current_player = 2

p1_money = 5000
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
def returnmoney():
    return p1_money
def shop():
    print(f"---SHOP---")
    print(f"1. nuke    | ${nuke_price}")
    print(f"2. spy     | ${p1_spy_price}")
    print(f"3. factory | ${p1_factory_price}")
    print(f"4. coup    | ${coup_base_price} / {round(coup_base_price * 1.5)} / {coup_base_price * 2}")
    print(f"5. pass")

    # input validation
    choice = input("Select an item to buy: ")
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input("Select an item to buy: ")

    match int(choice):
        # nuke case
        case 1:
            global p1_money
            if p1_money >= nuke_price:
                p1_money -= nuke_price
                x, y = coordinate_entry("Enter nuke coordinates: ")
                bomb(x, y, 2)
                global tension
                tension = 9
                f.write(f"Nuke -> {x}, {y}\n")
        # spy case
        case 2:
            if p1_money >= p1_spy_price:
                p1_money -= p1_spy_price
                global p1_spies
                spy_addition(p1_spies, p1_spy_price)
                p1_spies += 1
                f.write(f"Spy purchased\n")
        # factory case
        case 3:
            if p1_money >= p1_factory_price:
                p1_money -= p1_factory_price
                x, y = coordinate_entry("Enter factory coordinates: ")
                # hardcoded to p1 right now
                build_factory(x, y, 1)
                global p1_income
                p1_income += 150
                f.write(f"Factory -> {x}, {y}\n")
        # coup case
        case 4:
            coup_level = int(input("Enter coup level (1-3): "))
            if p1_money >= (coup_base_price * (0.5 * coup_level + 0.5)):
                p1_money -= (coup_base_price * (0.5 * coup_level + 0.5))
                x, y = coordinate_entry("Enter coup coordinates: ")
                # hardcoded to p1 right now
                coup(x, y, coup_level, 1)
                f.write(f"Coup {coup_level} -> {x}, {y}\n")
        # cat named windex case
        case 5:
            f.write("Pass\n")
            pass

# Prints the hud
# Contains (top to bottom) world map, tension meter, income, spy effectiveness
def print_hud():
    print_map()
    print_tension(tension)
    print(f"{'TURN ' + str(turn_counter):^89}")
    print()
    print(f"${p1_money} | +${p1_income}/t")
    print(f"{p1_spies * 2:.2f}% chance to reveal enemy base")
    spy_work(p1_spies)
    print()

# show menu and set difficulty
difficulty = menu.menu()

match difficulty:
    case "easy":
        difficulty = 1
    case "medium":
        difficulty = 2
    case "hard":
        difficulty = 3

# place enemy bases into random positions i'm so tired
for i in range(difficulty):
    x, y = randint(0, 86), randint(0, 24)
    while get_char(x, y) != key.land:
        x, y = randint(0, 86), randint(0, 24)
    starting_enemy_base = building_info.building(x, y, "bunker", True, 2)
    p2_bases.append(starting_enemy_base)

while True:
    # this just clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    current_player = (current_player % 2) + 1

    if current_player == 1:
        p1_money += p1_income
        turn_counter += 1
        f.write(f"Turn {turn_counter} - Player {current_player} - ")
        print_hud()
        shop()

    # if current_player == 2:


f.close()

from map_tools import *
import os
import menu
import building_info
from random import randint
import enemyai
import loss
import win

f = open("log.txt", "w")

# max value = 9
tension = 0
turn_counter = 0

current_player = 2

p1_money = 500
p1_income = 500
p1_spies = 0
p2_money = 750
p2_income = 500
p2_spies = 0

nuke_price = 3000
p1_spy_price = 1000
p1_factory_price = 1000
p2_spy_price = 1000
p2_factory_price = 1000
coup_base_price = 1500

p1_factory_coords = []
p1_base_coords = []
p2_factory_coords = []
p2_base_coords = []

ai_choice = 0

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
                validity = build_factory(x, y, 1)
                while(validity != True):
                    x, y = coordinate_entry("Enter factory coordinates: ")
                    validity = build_factory(x, y, 1)
                global p1_income
                p1_income = 500 + 250 * len(p1_factories)
                p1_income = 500 + 250 * len(p1_factories)
                f.write(f"Factory -> {x}, {y}\n")
        # coup case
        case 4:
            coup_level = int(input("Enter coup level (1-3): "))
            if p1_money >= (coup_base_price * (0.5 * coup_level + 0.5)):
                p1_money -= (coup_base_price * (0.5 * coup_level + 0.5))
                x, y = coordinate_entry("Enter coup coordinates: ")
                # hardcoded to p1 right now
                if(coup(x, y, coup_level, 1)):
                    tension += 1
                else:
                    tension += 2
                f.write(f"Coup {coup_level} -> {x}, {y}\n")
        # cat named windex case
        case 5:
            f.write("Pass\n")
            pass

# Prints the hud
# Contains (top to bottom) world map, tension meter, income, spy effectiveness
def print_hud(ai_choice):

    spy_detection = spy_work(p1_spies)
    print_map()
    print_tension(tension)
    print(f"{'TURN ' + str(turn_counter):^89}")
    
    print()
    print(f"${p1_money} | +${p1_income} per round")
    print(f"{p1_spies * 2:.2f}% chance to reveal enemy base")
    print(ai_choice)
    if (ai_choice == 2):
        print ("The enemy has hired a spy!")
        ai_choice = 0
    elif (ai_choice == 3):
        print ("The enemy has built a factory!")
        ai_choice = 0
    elif (ai_choice == 4):
        print ("The enemy has built a base!")
        ai_choice = 0
    print(ai_choice)

    if (spy_detection == 1):
        print("Your spies have found a base!")
    elif (spy_detection == 0):
        print("Your spies have found nothing so far.")
    else:
        print()
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
    # uncomment for seeing intial enemy base
    # swapchar(x, y, "A")
    p2_bases.append(starting_enemy_base)

while True:
    # this just clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    current_player = (current_player % 2) + 1

    if current_player == 1:
        p1_money += p1_income
        turn_counter += 1
        f.write(f"Turn {turn_counter} - Player {current_player} - ")
        print_hud(ai_choice)
        shop()

    if current_player == 2:
        enemy_choice, priceofsel = enemyai.enemyturn(len(p1_factories), len(p1_bases), difficulty, tension, p2_money, p2_spy_price, p2_factory_price, nuke_price)
        f.write(f"Turn {turn_counter} - Player 2 - ")
        match enemy_choice:
            case 1:
                # nuke if tension = 9, coup otherwise
                x, y = enemyai.confirmarea()
                if tension == 9:
                    p2_money -= priceofsel
                    bomb(x, y, 2)
                    f.write(f"Nuke -> {x}, {y}\n")
                    ai_choice = 1
                else:
                    build_base(x, y, 2)
                    f.write(f"Coup -> {x}, {y}\n")
                    ai_choice = 4
            case 2:
                # while True:
                #     print("hi")
                p2_money -= priceofsel
                spy_addition(p2_spies, p2_spy_price)
                p2_spies += 1
                f.write(f"Spy purchased\n")
                # spy case
                ai_choice = 2
            case 3:
                
                # while True:
                #     print("hi")
                # factory cas
                p2_money -= priceofsel
                x, y = enemyai.confirmarea()
                aivalidty = build_factory(x, y, 2)
                while aivalidty == False:
                    x, y = enemyai.confirmarea()
                    aivalidty = build_factory(x, y, 2)
                p2_income = 500 + 250 * len(p2_factories)
                f.write(f"Factory -> {x}, {y}\n")
                ai_choice = 3

                

    if p1_bases == []:
        loss.youlose()
        f.write("Player 2 Wins")
        break
    if p2_bases == []:
        win.youwin()
        f.write("Player 1 Wins")
        break
f.close()
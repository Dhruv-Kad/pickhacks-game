from map_tools import *

p1_money = 750
p1_income = 250

while True:
    p1_money += p1_income
    print_map()
    print(f"${p1_money} | +${p1_income}/t")
    x = int(input("enter nuke x: "))
    y = int(input("enter nuke y: "))
    bomb(x, y, 3)


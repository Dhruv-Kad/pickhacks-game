# hmmmm
# ok.

import time
import map_tools
import key
import os

# start with (-3, 3)  _  offset on (8, 8)
# this should make a / \ looking shape
# and give points (8, 8), (5, 5), and (3, 8)
# Provides the a, b, and c values for ax^2 + bx + c
#   that passes through the desired point.
def parabola(ex, ey, x_offset, y_offset):
    p1 = (ex, ey)
    p2 = (round(ex / 2), ey + y_offset)
    # p3 = (ex + (x_offset * 2), ey)
    p3 = (0, 24)

    amatrix = [
        [(p1[0] ** 2), p1[0], 1, p1[1]],
        [(p2[0] ** 2), p2[0], 1, p2[1]],
        [(p3[0] ** 2), p3[0], 1, p3[1]],
    ]

    amatrix_backup_a = amatrix
    amatrix[0] = [x / amatrix[0][0] for x in amatrix[0]]
    tmp = [amatrix[1][0] * x for x in amatrix[0]]
    amatrix[1] = [a - b for a, b in zip(amatrix[1], tmp)]
    tmp = [amatrix[2][0] * x for x in amatrix[0]]
    amatrix[2] = [a - b for a, b in zip(amatrix[2], tmp)]
    amatrix_backup_b = amatrix
    amatrix[1] = [x / amatrix[1][1] for x in amatrix[1]]
    tmp = [amatrix[2][1] * x for x in amatrix[1]]
    amatrix[2] = [a - b for a, b in zip(amatrix[2], tmp)]

    z = amatrix[2][3] / amatrix[2][2]
    y = (amatrix_backup_b[1][3] / amatrix_backup_b[1][1]) - (amatrix_backup_b[1][2] / amatrix_backup_b[1][1]) * z
    x = (amatrix_backup_a[0][3] / amatrix_backup_a[0][0]) - (amatrix_backup_a[0][1] / amatrix_backup_a[0][0]) * y - (amatrix_backup_a[0][2] / amatrix_backup_a[0][0]) * z

    coord_list = []
    # map width
    for i in range(ex + 1):
        # ax^2 + bx + c
        fx = x * (i ** 2) + (y * i) + z
        # map height - 1
        if 0 <= fx <= 24:
            coord_list.append((i, round(fx)))

    return coord_list

def flash_ending():
    count = 0
    original_map = map_tools.worldMap
    blinker = "\n\n"
    for row in original_map:
        blinker = blinker + "  "
        for char in row:
            if char != key.land_nuked:
                blinker = blinker + " "
            else:
                blinker = blinker + "X"
                count += 1
        blinker = blinker + "\n"
    
    show_end_toggle = False
    
    for i in range(101):
        os.system('cls' if os.name == 'nt' else 'clear')
        show_end_toggle = not show_end_toggle
        if show_end_toggle:
            print(blinker)
        else:
            map_tools.print_map()
        time.sleep(0.01)
    time.sleep(2)
    print(f"Percent of earth destroyed: {(count / 649) * 100:.2f}%")
    time.sleep(2)
import random

battlefield = []
battlefield_copy = []
game_size = 7

def create_battlefield(length):
    for x in range(length):
        add_list = []
        if x == 0:
            add_list.append(" ")
            for y in range(length - 1):
                add_list.append(chr(y + 65))
        else:
            add_list.append(x)
            for z in range(length - 1):
                add_list.append("#")
        battlefield.append(add_list)

    battlefield_copy = battlefield

    for item in battlefield:
        print(*item)

def set_ship(ship_length):
    ship_setting = True
    while ship_setting == True:
        x_coordinate = random.randrange(game_size - 1) + 1
        y_coordinate = random.randrange(game_size - 1) + 1
        direction = random.randrange(2)
        all_valid = True
        if direction == 0:
            for x in range(ship_length):
                if battlefield_copy[y_coordinate][x_coordinate + x] != "#":
                    all_valid = False
                    break
            if all_valid == True:
                for z in range(ship_length):
                    battlefield_copy[y_coordinate][x_coordinate + z] = "X"
                ship_setting = False



def main():
    create_battlefield(game_size)
    set_ship(1)
    for item in battlefield_copy:
        print(*item)

main()
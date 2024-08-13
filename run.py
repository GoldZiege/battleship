import random

battlefield = []
battlefield_copy = []
game_size = 7

def create_battlefield(length):
    global battlefield
    global battlefield_copy
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

    battlefield_copy = battlefield.copy()

    for item in battlefield:
        print(*item)

def set_ship(ship_length):
    global battlefield_copy
    ship_setting = True
    while ship_setting == True:
        x_coordinate = random.randrange(game_size - 1) + 1
        y_coordinate = random.randrange(game_size - 1) + 1
        direction = random.randrange(2)
        all_valid = True
        if direction == 0:
            if x_coordinate + ship_length >= game_size:
                continue
            for x in range(ship_length):
                if battlefield_copy[y_coordinate][x_coordinate + x] != "#":
                    all_valid = False
                    break
            if all_valid == True:
                for z in range(ship_length):
                    battlefield_copy[y_coordinate][x_coordinate + z] = "X"
                ship_setting = False
        if direction == 1:
            if y_coordinate + ship_length >= game_size:
                continue
            for x in range(ship_length):
                if battlefield_copy[y_coordinate + x][x_coordinate] != "#":
                    all_valid = False
                    break
            if all_valid == True:
                for z in range(ship_length):
                    battlefield_copy[y_coordinate + z][x_coordinate] = "X"
                ship_setting = False



def main():
    create_battlefield(game_size)
    set_ship(2)
    for item in battlefield_copy:
        print(*item)

main()
print(random.randrange(2))
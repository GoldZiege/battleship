import random
from copy import deepcopy

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

    battlefield_copy = deepcopy(battlefield)

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

def player_turn():
    global battlefield
    turn = 18
    hits = 0
    while turn > 0:
        print(f"You have {turn} turns left.")
        player_input = [*input("Enter your target coordinates:\n")]
        print(player_input)

        x_coordinate = player_input[0].upper()
        x_coordinate = ord(x_coordinate) - 64
        if x_coordinate < game_size and x_coordinate >= 1:
            try:
                y_coordinate = int(player_input[1])
                if y_coordinate < game_size and y_coordinate >= 1:
                    if battlefield_copy[y_coordinate][x_coordinate] == "X":
                        print("It's a hit!" )
                        battlefield[y_coordinate][x_coordinate] = "X"
                        hits += 1
                        if hits >= 9:
                            print("Congratulations. You sank all ships!")
                            break
                    else:
                        print("You missed.")
                        battlefield[y_coordinate][x_coordinate] = "O"
                else:
                    print("Please enter valid coordinates (e.g. B2)")
                    continue
            except ValueError:
                print("Please enter valid coordinates (e.g. B2)")
                continue
        else:
            print("Please enter valid coordinates (e.g. B2)")
            continue
        for item in battlefield:
            print(*item)
        turn -= 1

def main():
    create_battlefield(game_size)
    set_ship(3)
    set_ship(4)
    set_ship(2)
    for item in battlefield_copy:
        print(*item)
    player_turn()
main()
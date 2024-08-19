import random
from copy import deepcopy
import os

battlefield = []
battlefield_copy = []
game_size = 7

# taken from https://www.delftstack.com/howto/python/python-clear-console/
def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)

def create_welcome_screen():
    welcome_screen = True
    while welcome_screen:
        print("""
          ____        _   _   _           _     _       
         |  _ \      | | | | | |         | |   (_)      
         | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  
         |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
         | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
         |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                                 | |    
                                                 |_|   
        """)
        option = input("Enter 'e' for explanation or 'g' to start the game:\n")
        if option == "e":
            clearConsole()
            explanation()
            clearConsole()
        elif option == "g":
            clearConsole()
            break
        else:
            clearConsole()        
        
def explanation():
    print("""
    Explanation:

    This is explanation text test!
    """)
    input("Press Enter to go back to start screen.\n")

def create_battlefield(length):
    """
    Creates the game grid.
    """
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
    """
    Sets a ship with the size of ship_length on the game grid.
    """
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
    """
    Takes in the players coordinates, validates them and
    checks wether the shot hits or misses.
    """
    global battlefield
    turn = 3
    hits = 0
    while turn > 0:
        print(f"You have {turn} shots left.")
        player_input = [*input("Enter your target coordinates:\n")]
        if not player_input or len(player_input) > 2:
            print("Please enter valid coordinates (e.g. B2)")
            continue
        else:
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
                                print("You Win!")
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
            clearConsole()
            for item in battlefield:
                print(*item)
            turn -= 1

    if turn == 0:
        print("You are out of ammuniton. You lose.")

def main():
    """
    Run all programm functions
    """
    game_running = True
    create_welcome_screen()
    while game_running:
        create_battlefield(game_size)
        set_ship(3)
        set_ship(4)
        set_ship(2)
        player_turn()
        while True:
            option = input("Enter 'g' to start new game or 'e' to exit:")
            if option == "g":
                clearConsole()
                break
            elif option == "e":
                game_running = False
                break
            else:
                print("please enter either 'g' or 'e'")

main()
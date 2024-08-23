import random
from copy import deepcopy
import os

# Global variables
battlefield = []
battlefield_copy = []
game_size = 7


# taken from https://www.delftstack.com/howto/python/python-clear-console/
def clearConsole():
    """
    Clears the screen
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


def create_welcome_screen():
    """
    Shows the welcome screen and leads the player
    either to the game or an explanation of the game
    """
    welcome_screen = True
    while welcome_screen:
        print("""
          ____        _   _   _           _     _
         |  _ \\      | | | | | |         | |   (_)
         | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __
         |  _ < / _` | __| __| |/ _ \\/ __| '_ \\| | '_ \\
         | |_) | (_| | |_| |_| |  __/\\__ \\ | | | | |_) |
         |____/ \\__,_|\\__|\\__|_|\\___||___/_| |_|_| .__/
                                                 | |
                                                 |_|
        """)
        option = input("Enter 'e' for explanation or \
'g' to start the game:\n").lower()
        if option == "e":
            clearConsole()
            explanation()
            clearConsole()
        elif option == "g":
            clearConsole()
            break
        else:
            clearConsole()
            print("Please enter either 'e' or 'g' to move on.")


def explanation():
    """
    Puts explanation text on screen
    """
    print("""
    Explanation:

    You are the commander of a battleship and have to destroy
    the enemy ships.
    There are three enemy ships with different lengths:

    Battleship with length 4
    Submarine with length 3
    Destroyer with length 2

    To fulfill your task you have 18 missiles to shoot at
    your targets. Simply enter target coordinates in the
    form of a letter plus a number (e.g. A3).

    Sink all your targets and you win. Run out of ammunition
    and you lose.

    Good luck.
    """)
    press_enter = input("Press Enter to go back to start screen.\n")
    if press_enter:
        clearConsole()
        print("Please press the Enter key to move on.")
        explanation()


def create_battlefield(length):
    """
    Creates the game grid by creating a list of lists
    and printing the lists content to the console.
    """
    global battlefield
    global battlefield_copy
    battlefield = []
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
    Sets a ship with the size of ship_length on the game grid. And makes 
    checks so the ship won't go over the edge of the game grid and is not at 
    the same spot as another ship.
    """
    global battlefield_copy
    ship_setting = True
    while ship_setting:
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
            if all_valid:
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
            if all_valid:
                for z in range(ship_length):
                    battlefield_copy[y_coordinate + z][x_coordinate] = "X"
                ship_setting = False


def player_turn():
    """
    Takes in the players coordinates, validates them via several 'if'
    and 'try' statements. Then it compares the coordinates to a copy of
    the game grid to check wether the shot hits a ship or misses. At the end
    it tells the player when the game is over.
    """
    global battlefield
    turn = 18
    hits = 0
    while turn > 0:
        print(f"You have {turn} shots left.")
        player_input = [*input("Enter your target coordinates:\n")]
        if not player_input or len(player_input) != 2:
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
                            clearConsole()
                            print("It's a hit!")
                            battlefield[y_coordinate][x_coordinate] = "X"
                            hits += 1
                            if hits >= 9:
                                for item in battlefield:
                                    print(*item)
                                print("Congratulations. You sank all ships!")
                                print("You Win!")
                                break
                        else:
                            clearConsole()
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

    if turn == 0:
        print("You are out of ammuniton. You lose.")
        print("Here is where the ships were:")
        for item in battlefield_copy:
            print(*item)


def main():
    """
    Run all programm functions and loops back to a new game or the
    welcome screen on player input.
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
            option = input("Enter 'g' to start new game or 'e' to exit:\n")\
                .lower()
            if option == "g":
                clearConsole()
                break
            elif option == "e":
                clearConsole()
                main()
            else:
                print("please enter either 'g' or 'e'")


main()

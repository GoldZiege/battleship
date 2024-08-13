import random

battlefield = []
battlefield_copy = []

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

    for item in battlefield:
        print(*item)

def set_ship():
    global battlefield_copy
    battlefield_copy = battlefield


def main():
    create_battlefield(7)

main()
print(random.randrange(6) + 1)
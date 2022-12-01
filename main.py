# TODO: Make a character creator, 
#       dice system, loot generator, 

import sys
import os

def clear():
    if (sys.platform == "win32"):
        os.system("cls")
    else:
        os.system("clear")


def main():
    print("work")


def menu():
    clear()

    print("\nWelcome to the Dungeon and Dragons!")
    print("D&D - board game, but we are transferred it to PC.")
    print("\nschool project by David, Mikhael\n")

    menu_tabs = [
        "Create a new character",
        "Roll the dice",
        "Exit"
    ]

    for i, name in enumerate(menu_tabs):
        print(f"[{i + 1}]", name)

    selected_tab = input("Select a tab, and press Enter: ")

    if (selected_tab == "1"):
        create_new_character()
    elif (selected_tab == "2"):
        roll_the_dice()
    elif (selected_tab == "3"):
        raise SystemExit


def create_new_character():
    clear()
    

def roll_the_dice():
    clear()


if __name__ == "__main__":
    main()

    while True:
        Menu = menu()
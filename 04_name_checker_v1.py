import easygui

# Dictionary for monster lists
card_list = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}


def main():
    while True:
        menu_choices = ["Add monster", "Delete monster", "Search monster",
                        "View monster", "Exit"]
        choice = easygui.buttonbox(msg="Welcome to Monster card game\n"
                                       "Choose what do you want to do.",
                                   title="Monster Card Game", choices=menu_choices)

        if choice == "Add monster":
            # add_monster_card()
            exit()

        elif choice == "View monster":
            display_monsters()

        elif choice == "Delete monster":
            # delete_monster()
            exit()

        elif choice == "Search monster":
            name = name_checker()
            if name is not None:
                easygui.msgbox(f"{name} is availiable.")

        elif choice == "Exit":
            easygui.msgbox("Thank you for playing monster card game!")
            break

        else:
            easygui.msgbox("This function has not finished yet!")


def name_checker():
    while True:
        name = easygui.enterbox("Enter the name of the monster:")

        if name is None:
            easygui.msgbox("Going back to main menu.")
            return

        name = name.capitalize()

        if not name:
            easygui.msgbox("Error: Name cannot be empty.")

        else:
            return name


def display_monsters():
    msg = "List of monsters:\n"

    # give the dictionary a value of 'monster_name' and 'monster_stat'
    for monster_name, monster_stat in card_list.items():
        msg += f"\n {monster_name} \n"

        # for subvalue in monster_stat (dictionary)
        for stat in monster_stat:
            msg += f'   {stat}: {monster_stat[stat]} '

    # print the message using easygui
    easygui.msgbox(msg)


main()

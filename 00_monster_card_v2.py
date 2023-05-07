""""""

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

        if choice == "View monster":
            display_monsters()

        elif choice == "Exit":
            easygui.msgbox("Thank you for playing monster card game!")
            break

        else:
            easygui.msgbox("This function has not finished yet!")


def display_monsters():
    msg = "List of monsters:\n"
    for monster_name, monster_stat in card_list.items():
        msg += f"\n {monster_name} \n"
        for stat in monster_stat:
            msg += f'   {stat}: {monster_stat[stat]}, '

    easygui.msgbox(msg)


main()

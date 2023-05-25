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


def name_checker():
    while True:
        monster_name = easygui.enterbox("Enter the name of the monster:")

        if monster_name is None:
            easygui.msgbox("Returning back...")
            break

        monster_name = monster_name.capitalize()

        if not monster_name:
            easygui.msgbox("Error: Name cannot be empty.")

        else:
            return monster_name


def search_monster():
    while True:
        monster_name = name_checker()

        if monster_name in card_list:
            msg = f"{monster_name}'s stat: \n\n"
            for stat, value in card_list[monster_name].items():
                msg += f"{stat}: {value}\n"
            break
        else:
            easygui.msgbox(f"{monster_name} is not on the list.")
    confirmation = easygui.buttonbox(f"{monster_name}'s stat:\n\n"
                                     f"{msg}"
                                     "Are these details all correct?", choices=["Confirm", "Change stats"])
    if confirmation == "Confirm":
        return
    else:
        # change_stat(monster_name)
        easygui.msgbox("link to the change_stat() function")


display_monsters()
search_monster()
display_monsters()

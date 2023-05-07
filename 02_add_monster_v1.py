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


def add_monster_card():
    name = easygui.enterbox("Enter the name of the monster:")
    strength = int(easygui.enterbox("Enter the strength of the monster:"))
    speed = int(easygui.enterbox("Enter the speed of the monster:"))
    stealth = int(easygui.enterbox("Enter the stealth of the monster:"))
    cunning = int(easygui.enterbox("Enter the cunning of the monster:"))
    msg = f"The following monster card has been added:\n\nName: " \
          f"{name}\nStrength: {strength}\nSpeed: {speed}\nStealth: " \
          f"{stealth}\nCunning: {cunning}\n\nIs this information correct?"
    if easygui.ynbox(msg):
        card_list[name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
        easygui.msgbox("Monster card added successfully!")

    else:
        # If the user wants to make a change, remove the card from the dictionary
        easygui.msgbox("Monster card not added.")


def display_monsters():
    msg = "List of monsters:\n"
    for monster_name, monster_stat in card_list.items():
        msg += f"\n {monster_name} \n"
        for stat in monster_stat:
            msg += f'   {stat}: {monster_stat[stat]} '

    easygui.msgbox(msg)


display_monsters()  # call the function to display the monsters
add_monster_card()
display_monsters()


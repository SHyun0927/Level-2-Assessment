"""
02_add_monster_v2.py is an improved version of v1 of this program,
which has error prevention that the user cannot type stat value that lower than 1, and higher than 25.
"""
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


# Function that adds monster card into the dictionary.
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


# Function that adds monster card into the dictionary.
def add_monster_card():
    monster_name = name_checker()

    card_list[monster_name] = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}

    stats = ["Strength", "Speed", "Stealth", "Cunning"]

    values = []

    for stat in stats:
        while True:
            value = easygui.integerbox(f"Enter the {stat} of the monster (1-25):\n"
                                       f"Press 'Cancel' to go back to main menu.",
                                       lowerbound=1, upperbound=25)
            if value is None:
                easygui.msgbox("Returning to main menu...")
                return
            else:
                values.append(value)
                break

    card_stats = dict(zip(stats, values))

    card_list[monster_name].update(card_stats)

    msg = f"The following monster card has been added:\n\nName: {monster_name}\n"

    for stat, value in card_list[monster_name].items():
        msg += f"{stat}: {value}\n"

    choice = easygui.buttonbox(msg + "\nWhat would you like to do?",
                               choices=["Confirm", "Change Stats"])

    if choice == "Confirm":
        easygui.msgbox("Monster card added successfully!")

    elif choice == "Change Stats":
        # change_stats(monster_name)
        easygui.msgbox("Change stats()") 


# Function to display list of monsters in the dictionary
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


display_monsters()
add_monster_card()
display_monsters()

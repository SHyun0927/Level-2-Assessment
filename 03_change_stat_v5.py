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


def change_stats(monster_name):
    # Get the current stats for the monster from the card_list dictionary
    current_stats = card_list[name]

    # Create a list of choices that includes the name of the monster and all its stats
    choices = list(current_stats.keys()) + ["Change name", "Exit"]

    while True:

        # Ask the user which stat they want to change
        stat_choice = easygui.buttonbox(f"Which stat do you want to change for {monster_name}?",
                                        choices=choices)

        # If the user chose to change the name, ask for the new name and update the dictionary
        if stat_choice == "Change name":
            new_name = name_checker()
            if new_name is not None:
                card_list[new_name] = current_stats
                del card_list[monster_name]
                easygui.msgbox(f"The name of the monster has been changed to {new_name}. ")
        elif stat_choice == "Exit":
            easygui.msgbox("Returning to the main menu.")
            return
        else:
            # Ask for the new value for the chosen stat
            new_value = easygui.integerbox(f"Enter the new {stat_choice} value for {name} (1-25): ",
                                           lowerbound=0, upperbound=25)

            while new_value is not None:
                # Update the chosen stat in the card_list dictionary
                current_stats[stat_choice] = new_value

                # Display a message to confirm that the stat has been updated
                easygui.msgbox(f"The {stat_choice} stat has been updated to {new_value} for {name}.")
                break


display_monsters()
while True:
    name = name_checker()

    if name not in card_list:
        easygui.msgbox("Name not found in the list")

    else:
        break
change_stats(name)
display_monsters()

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
def add_monster_card():
    while True:
        # Asks name of the monster, then capitalize first letter.
        name = easygui.enterbox("Enter the name of the monster:").capitalize()

        # Check if the monster name is already in the dictionary
        if name in card_list:
            # If it is, display an error message and ask the user to enter a different name
            easygui.msgbox("Error: A monster with that name already exists.")
        else:
            # If not, break out of the loop and add the monster with default values of 0 for each stat
            card_list[name] = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}
            break

    # List of 4 stats in the dictionary.
    stats = ["Strength", "Speed", "Stealth", "Cunning"]

    # Values for 4 stats.
    values = []

    for stat in stats:
        # Asks for the integer value for the stats
        value = int(easygui.enterbox(f"Enter the {stat} of the monster (1-25):"))

        # If stat is below 1 or higher than 0, program asks user to type again.
        while value < 1 or value > 25:
            value = int(easygui.enterbox(f"Invalid input. "
                                         f"Enter the {stat} of the monster (1-25):"))

        # if value is appropirate, append the value.
        values.append(value)

    # Combine the stats and values lists into a dictionary using dict(zip())
    card_stats = dict(zip(stats, values))

    # Update the monster's stats in the card_list dictionary
    card_list[name].update(card_stats)

    # Creating msg value for easygui, to confirm if the user typed correctly.
    msg = f"The following monster card has been added:\n\nName: {name}\n"

    # Searching each stat and value and adds into the msg value.
    for stat, value in card_list[name].items():
        msg += f"{stat}: {value}\n"

    # Give the user the option to confirm the information or make a change
    choice = easygui.buttonbox(msg + "\nWhat would you like to do?", choices=["Confirm", "Change Stats"])

    if choice == "Confirm":
        easygui.msgbox("Monster card added successfully!")
    elif choice == "Change Stats":
        change_stats(name)
        return name, stats


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


def change_stats(name, stats):
    # Get the current stats for the monster from the card_list dictionary
    current_stats = card_list[name]

    # Ask the user if they want to change the name of the monster
    choice = easygui.buttonbox(f"Do you want to change the name of {name}?", choices=["Yes", "No"])

    if choice == "Yes":
        # Ask for the new name of the monster
        new_name = easygui.enterbox("Enter the new name of the monster:")

        # Check if the new name is already in the dictionary
        if new_name in card_list:
            # If it is, display an error message and return
            easygui.msgbox("Error: A monster with that name already exists.")
            return
        else:
            # If not, update the name of the monster in the card_list dictionary
            card_list[new_name] = current_stats
            del card_list[name]
            name = new_name

    # Create a list to hold the new values for the stats
    new_values = []

    # Loop through the stats and ask the user to enter a new value for each one
    for stat in stats:
        # Ask for the new value for the stat
        new_value = int(easygui.enterbox(f"Enter the new {stat} value for {name} (1-25):"))

        # If the new value is not between 1 and 25, keep asking until a valid value is entered
        while new_value < 1 or new_value > 25:
            new_value = int(easygui.enterbox(f"Invalid input. Enter the new {stat} value for {name} (1-25):"))

        # Add the new value to the list of new values
        new_values.append(new_value)

    # Combine the stats and new values into a dictionary using dict(zip())
    new_stats = dict(zip(stats, new_values))

    # Update the monster's stats in the card_list dictionary
    current_stats.update(new_stats)

    # Display a message to confirm that the stats have been updated
    msg = f"The following stats have been updated for {name}:\n\n"

    for stat, value in new_stats.items():
        msg += f"{stat}: {value}\n"

    easygui.msgbox(msg)


display_monsters()
add_monster_card()
display_monsters()


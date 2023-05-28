"""
Monster Card Game.py
This code now includes:
display_monster(), add_monster(), change_stats(), name_checker(),
delete_monster(), search_monster() with link with the main routine function.
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


def main():
    # Main loop for the game
    while True:
        # List of menu choices
        menu_choices = ["Add monster", "Delete monster", "Search monster",
                        "View monster", "Edit monster", "Exit"]
        # Display the menu and get the user's choice
        choice = easygui.buttonbox(msg="Welcome to Monster card game\n"
                                       "Choose what do you want to do.",
                                   title="Monster Card Game",
                                   choices=menu_choices)

        # If the user chooses to add a monster,
        # call the add_monster_card function
        if choice == "Add monster":
            add_monster_card()

        # If the user chooses to view the monsters,
        # call the display_monsters function
        elif choice == "View monster":
            display_monsters()

        # If the user chooses to exit,
        # display a message and break out of the loop
        elif choice == "Exit":
            easygui.msgbox("Thank you for playing monster card game!",
                           "Exiting program")
            break

        # If the user chooses to edit a monster, call the change_stats function
        elif choice == "Edit monster":
            while True:
                # Get the name of the monster to edit
                monster_name = name_checker()

                # If the user cancels, break out of the loop
                if monster_name == "InvalidValue":
                    break

                # If the monster is not in the dictionary,
                # display an error message
                elif monster_name not in card_list:
                    easygui.msgbox("'{monster_name}' not found in the list",
                                   title="Error! Please try again.")

                # If the monster is in the dictionary,
                # call the change_stats function
                else:
                    change_stats(monster_name)
                    break

        # If the user chooses to delete a monster,
        # call the delete_monster function
        elif choice == "Delete monster":
            delete_monster()

        # If the user chooses to search for a monster,
        # call the search_monster function
        else:
            search_monster()


def name_checker():
    # Loop until the user enters a valid name or cancels
    while True:
        # Get the name of the monster from the user
        name = easygui.enterbox("Enter the name of the monster:",
                                title="Enter name!")

        # If the user cancels, return "InvalidValue"
        if name is None:
            easygui.msgbox("You have pressed cancel.",
                           title="Returning to the menu...")
            return "InvalidValue"

        # Capitalize the name
        name = name.capitalize()

        # If the name is empty, display an error message
        if not name:
            easygui.msgbox("Error: Name cannot be empty.",
                           title="Error! Please try again.")

        # If the name is valid, return it
        else:
            return name


# Function that adds monster card into the dictionary.
def add_monster_card():
    # Loop until the user enters a valid name
    # that is not already in the dictionary
    while True:
        monster_name = name_checker()

        # If the name is already in the dictionary, display an error message
        if monster_name in card_list:
            easygui.msgbox(f"{monster_name} already exists. Try again.",
                           title="Error! Monster already exists.")

        # If the user cancels, return
        elif monster_name == "InvalidValue":
            return

        # If the name is valid and not in the dictionary, break out of the loop
        else:
            break

    # Add the monster to the dictionary with default stats of 0
    card_list[monster_name] = {"Strength": 0, "Speed": 0,
                               "Stealth": 0, "Cunning": 0}

    # List of stats to get from the user
    stats = ["Strength", "Speed", "Stealth", "Cunning"]

    # List to store the values entered by the user
    values = []

    # Loop through the stats and get the value for each one from the user
    for stat in stats:
        value = easygui.integerbox(f"Enter the {stat} of the monster (1-25):\n"
                                   f"Press 'Cancel' to go back to main menu.",
                                   lowerbound=1, upperbound=25,
                                   title="Enter stat")
        # If the user cancels, return to the main menu
        if value is None:
            easygui.msgbox("Returning to main menu...",
                           title="Returning to the menu")
            return
        # If the user enters a valid value, add it to the list of values
        else:
            values.append(value)

    # Create a dictionary from the stats and values lists
    card_stats = dict(zip(stats, values))

    # Update the monster's stats in the dictionary
    card_list[monster_name].update(card_stats)

    # Display a message with the details of the new monster
    msg = f"The following monster card has been added:\n\n" \
          f"Name: {monster_name}\n"

    for stat, value in card_list[monster_name].items():
        msg += f"{stat}: {value}\n"

    # Give the user the option to confirm or change
    # the stats of the new monster
    choice = easygui.buttonbox(msg + "\nWhat would you like to do?",
                               choices=["Confirm", "Change Stats"],
                               title="Confirmation")

    # If the user chooses to confirm, display a success message
    if choice == "Confirm":
        easygui.msgbox("Monster card added successfully!",
                       title="Card added successfully!")

    # If the user chooses to change the stats, call the change_stats function
    elif choice == "Change Stats":
        change_stats(monster_name)


def change_stats(monster_name):
    # Get the current stats for the monster from the card_list dictionary
    current_stats = card_list[monster_name]

    # Create a list of choices that includes
    # the name of the monster and all its stats
    choices = list(current_stats.keys()) + ["Change name", "Exit"]

    while True:
        # Ask the user which stat they want to change
        stat_choice = easygui.buttonbox(f"Which stat do you want to change for"
                                        f" {monster_name}?", choices=choices,
                                        title="Changing stat...")

        # If the user chooses to change the name,
        # get the new name and update the dictionary
        if stat_choice == "Change name":
            new_name = name_checker()

            # If the user cancels, return to the main menu
            if new_name == "InvalidValue":
                break

            # If the new name is valid,
            # update the dictionary and display a success message
            else:
                card_list[new_name] = current_stats
                del card_list[monster_name]
                easygui.msgbox(f"The name of the monster has been changed to "
                               f"{new_name}. ",
                               title="Changed name")
                monster_name = new_name

        # If the user chooses to exit, return to the main menu
        elif stat_choice == "Exit":
            easygui.msgbox("Returning to the main menu.",
                           title="Returning to main menu")
            return

        # If the user chooses a stat to change,
        # get the new value and update the dictionary
        else:
            new_value = easygui.integerbox(f"Enter the new {stat_choice} value"
                                           f" for {monster_name} (1-25): ",
                                           lowerbound=1, upperbound=25,
                                           title="Enter stat...")

            # Loop until the user enters a valid value or cancels
            while new_value is not None:
                # Update the chosen stat in the card_list dictionary
                current_stats[stat_choice] = new_value

                # Display a message to confirm that the stat has been updated
                easygui.msgbox(f"The {stat_choice} stat has been updated to "
                               f"{new_value} for {monster_name}.",
                               title="Stat updated!")
                break


# Function that deletes a monster card from the dictionary.
def delete_monster():
    while True:
        # Ask the user to enter the name of the monster to be deleted
        monster_name = name_checker()
        if monster_name in card_list:
            break

        elif monster_name == "InvalidValue":
            return

        else:
            easygui.msgbox(f"{monster_name} does not exist.",
                           title="Error! Please try again.")

    if monster_name in card_list:
        # Ask the user to confirm the deletion of the monster card
        confirmation = easygui.ynbox(f"Do you really want to delete "
                                     f"{monster_name}?",
                                     title="Confirmation")

        if confirmation == 1:
            # Delete the monster card from the dictionary
            del card_list[monster_name]

            easygui.msgbox(f"{monster_name} has successfully deleted.",
                           title="Successfully deleted monster.")

        else:
            easygui.msgbox("Returning to main menu.",
                           title="Returning to the main menu...")


# Function that searches for a monster card in the dictionary.
def search_monster():
    while True:
        # Ask the user to enter the name of the monster to be searched
        monster_name = name_checker()

        if monster_name in card_list:
            # Display the stats of the monster card
            msg = f"{monster_name}'s stat: \n\n"
            for stat, value in card_list[monster_name].items():
                msg += f"{stat}: {value}\n"
            break
        elif monster_name == "InvalidValue":
            return

        else:
            easygui.msgbox(f"'{monster_name}' is not on the list.",
                           title="Error! Please try again.")
    # Ask the user to confirm the displayed stats of the monster card
    confirmation = easygui.buttonbox(f"{msg}"
                                     "\nAre these details all correct?",
                                     choices=["Confirm", "Change stats"],
                                     title="Search monster")
    if confirmation == "Confirm":
        easygui.msgbox("Return to main menu...",
                       title="Returning to the menu..")
        return
    else:
        # Call the change_stats() function
        # to change the stats of the monster card
        change_stats(monster_name)


# Function that displays all the monster cards in the dictionary.
def display_monsters():
    msg = "List of monsters:\n"
    for monster_name, monster_stat in card_list.items():
        msg += f"\n {monster_name} \n"
        for stat in monster_stat:
            msg += f'   {stat}: {monster_stat[stat]} '

    easygui.msgbox(msg, title="List of monsters")


# calls main routine function
main()

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
                        "View monster", "Edit monster", "Exit"]
        choice = easygui.buttonbox(msg="Welcome to Monster card game\n"
                                       "Choose what do you want to do.",
                                   title="Monster Card Game", choices=menu_choices)

        if choice == "Add monster":
            add_monster_card()

        elif choice == "View monster":
            display_monsters()

        elif choice == "Exit":
            easygui.msgbox("Thank you for playing monster card game!")
            break

        elif choice == "Edit monster":
            while True:
                monster_name = name_checker()

                if monster_name not in card_list:
                    easygui.msgbox("Name not found in the list")

                else:
                    break
            change_stats(monster_name)
        elif choice == "Delete monster":
            while True:
                monster_name = name_checker()
                if monster_name in card_list:
                    break
                else:
                    easygui.msgbox("Monster does not exist.")
            delete_monster(monster_name)

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


# Function that adds monster card into the dictionary.
def add_monster_card():
    monster_name = name_checker()

    card_list[monster_name] = {"Strength": 0, "Speed": 0, "Stealth": 0, "Cunning": 0}

    stats = ["Strength", "Speed", "Stealth", "Cunning"]

    values = []

    for stat in stats:
        value = easygui.integerbox(f"Enter the {stat} of the monster (1-25):\n"
                                   f"Press 'Cancel' to go back to main menu.",
                                   lowerbound=1, upperbound=25)
        if value is None:
            easygui.msgbox("Returning to main menu...")
            return
        else:
            values.append(value)

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
        change_stats(monster_name)


def change_stats(monster_name):
    # Get the current stats for the monster from the card_list dictionary
    current_stats = card_list[monster_name]

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
            new_value = easygui.integerbox(f"Enter the new {stat_choice} value for {monster_name} (1-25): ",
                                           lowerbound=1, upperbound=25)

            while new_value is not None:
                # Update the chosen stat in the card_list dictionary
                current_stats[stat_choice] = new_value

                # Display a message to confirm that the stat has been updated
                easygui.msgbox(f"The {stat_choice} stat has been updated to {new_value} for {monster_name}.")
                break


def delete_monster(monster_name):
    if monster_name in card_list:
        confirmation = easygui.ynbox(f"Do you really want to delete {monster_name}?")

        if confirmation == 1:
            del card_list[monster_name]

            easygui.msgbox(f"{monster_name} has successfully deleted.")

        else:
            easygui.msgbox("Returning to main menu.")



def display_monsters():
    msg = "List of monsters:\n"
    for monster_name, monster_stat in card_list.items():
        msg += f"\n {monster_name} \n"
        for stat in monster_stat:
            msg += f'   {stat}: {monster_stat[stat]} '

    easygui.msgbox(msg)


main()

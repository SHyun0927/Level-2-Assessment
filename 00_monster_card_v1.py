"""
00_monster_card_v1.py
Main menu of the monster card game.
"""
import easygui

menu_choices = ["Add monster", "Delete monster", "Search monster",
                "View monster", "Exit"]
choice = easygui.buttonbox(msg="Welcome to Monster card game\n"
                      "Choose what do you want to do.",
                  title="Monster Card Game", choices=menu_choices)

if choice == "Add monster":
    easygui.msgbox("Adding monster")

elif choice == "Delete monster":
    easygui.msgbox("Delete monster")

elif choice == "Search monster":
    easygui.msgbox("Search monster")

elif choice == "View monster":
    easygui.msgbox("List of monsters")

else:
    easygui.msgbox("Thank you for using this program!")

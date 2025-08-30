# This is a simple project to watch for updates in Excel files.
# It is run by a user, and checks a list of files specified by the user.
# The program will notify the user of any changes made to these files.
# It uses hashing to detect changes in the files, and logs its activity

# made by @Felikious

from hash_manager import hash_manager
from pathlib import Path
from menu import menu
from list_manager import list_manager
from hash_manager import hash_manager

def main():
    menu = menu()
    watchlist = watchlist_manager()
    hasher = hash_manager()

    while True:
        menu.display()
        choice = menu.get_choice()

        if choice == "1":
            # Check for changes
            pass
        elif choice == "2":
            # Mark changes as reviewed
            pass
        elif choice == "3":
            # View watchlist
            pass
        elif choice == "4":
            # Add to watchlist
            pass
        elif choice == "5":
            # Remove from watchlist
            pass
        elif choice == "6":
            # Exit
            break
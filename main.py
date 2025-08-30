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
    print("Excel File Update Watcher")
    m_menu = menu()
    m_list_manager = list_manager()

    while True:
        m_menu.display()
        choice = m_menu.get_choice()

        if choice == "1":
            # Check for changes
            m_list_manager.check_for_changes()
            return
        
        elif choice == "2":
            # Update hash list
            m_list_manager.update_hash_list()
            return
        
        elif choice == "3":
            # View watchlist
            m_list_manager.view_watchlist()
            return
        
        elif choice == "4":
            # Add to watchlist
            alias = input("Enter the file alias: ")
            path = input("Enter the file path: ")
            YorN = input("Do you want to add this file to the watchlist? (y/n): ")

            if YorN.lower() == "y":
                m_list_manager.add_to_watchlist(alias, path)
            return
        
        elif choice == "5":
            # Remove from watchlist based on index
            index = int(input("Enter the index of the file to remove: "))
            
            m_list_manager.remove_from_watchlist(index)


        elif choice == "6":
            # Exit
            break

main()
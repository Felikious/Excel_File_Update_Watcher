"""
This is a simple project to watch for updates in Excel files.
It is made to be user friendly, and checks a list of files specified by the user.
For this example I used 3 example files, already present in the working directory,
and I'm using them to demonstrate the functionality.

The user runs the program and specifies the files to watch. 
The user can add or remove files from the watchlist at any time.
The user when the program is actively running can check for changes,
since the app saves the current state and loads it on startup.

That way, the user has full control over the monitoring process,
and the program does not run in the background, to avoid unnecessary resource usage.

The program will notify the user of any changes made to these files.
It uses hashing with SHA-256 to detect changes in the files, ignoring metadata changes.
This way you can be sure that only actual content changes are flagged when you run the program.
Enjoy!

    made by @Felikious
"""


"""
Dependencies:
    when A imports (thus depends on) B A->B

main.py -> menu.py -> NO DEPENDENCIES
main.py -> list_manager.py

list_manager.py -> hash_manager.py          
list_manager.py -> pickle

hash_manager.py -> hashlib 
hash_manager.py -> zipfile
hash_manager.py -> pathlib 

"""

from menu import menu
from list_manager import list_manager

def main():
    print("\nExcel File Update Watcher\n")

    # Initialize menu and list manager  
    m_menu = menu()
    m_list_manager = list_manager()

    while True:
        # Main loop for the program (user interaction)

        # Display menu and get user choice
        m_menu.display()
        choice = m_menu.get_choice()

        if choice == "1":
            # Check for changes
            m_list_manager.check_for_changes()
        
        elif choice == "2":
            # Update hash list
            m_list_manager.update_hash_list()
            
        
        elif choice == "3":
            # View watchlist
            m_list_manager.view_watchlist()
        
        elif choice == "4":
            # Add to watchlist

            alias = input("Enter the file alias: ")
            path = input("Enter the file path: ")
            confirmation = input("Do you want to add this file to the watchlist? (y/n): ")

            if confirmation.lower() == "y":
                m_list_manager.add_to_watchlist(alias, path)
        
        elif choice == "5":
            # Remove from watchlist based on index
            m_list_manager.view_watchlist()
            index = int(input("Enter the index of the file to remove: "))
            m_list_manager.remove_from_watchlist(index)

        elif choice == "6":
            # Clear watchlist
            confirmation = input("By clearing the watchlist, you will remove all files from the watchlist.\n If you are sure, type \"clear\": ")

            if confirmation.lower() == "clear":
                m_list_manager.clear_watchlist()

        elif choice == "7":
            # Exit 
            # Save data before exiting
            m_list_manager.save_data()

            print("Thank you for using the Excel File Update Watcher!")
            wait = input("Press Enter to exit...")
            break

main()
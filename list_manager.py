"""
list_manager.py
This module contains a class that manages all the list operations for this project.
It is also using hash_manager for file hashing.
It also saves the watchlist to a file and loads it on startup.

- provides list operations for managing the watchlist
- using hash_manager for file hashing
    - hash_all_files: Hashes all files in the watchlist

- using Python pickle for saving and loading watchlist data
    - save_data: Saves the current watchlist to a file 
    - load_data: Loads the watchlist from a file
"""

from hash_manager import hash_manager
import pickle as pkl


class list_manager:
    """
    A class to manage the watchlist of files.

    This class contains functions to add, remove, and view files in the watchlist.
    It also handles file hashing and data persistence.

    List operations:
    - add_to_watchlist: Adds a file to the watchlist
    - remove_from_watchlist: Removes a file from the watchlist
    - view_watchlist: Displays all files in the watchlist
    - clear_watchlist: Clears the entire watchlist
    - check_for_changes: Checks for changes in the watched files

    Hash operations:
    - hash_all_files: Hashes all files in the watchlist
    - update_hash_list: Updates the hash list for all files in the watchlist
    - check_for_changes: Checks for changes using hash_all_files and __check_for_changes (assistant method)
    - add_to_watchlist: Calls hasher.hash_file() to get the hash of the added file

    Data operations:
    - save_data: Saves the current watchlist to file "EFUW_data.pkl"
    - load_data: Loads the watchlist from the file "EFUW_data.pkl"
    """

    def __init__(self):
        # Initialize the hash manager and lists
        # load existing data
        self.hash_manager = hash_manager()
        self.file_aliases_list = []
        self.file_paths_list = []
        self.hash_list=[]
        self.load_data() 

    #-------------------------------------------------
    #---------------- List Operations ----------------
    #-------------------------------------------------

    def add_to_watchlist(self, alias,path,):
        # Adds a file and its hash to the watchlist
        # Since the watchlist is 3 parallel lists, 
        # we need to append to all three

        self.file_aliases_list.append(alias)
        self.file_paths_list.append(path)
        self.hash_list.append(self.hash_manager.hash_file(path))

    def remove_from_watchlist(self, index):
        # Removes a file and its hash from the watchlist after confirmation
        # This way we maintain the integrity of the parallel lists

        confirmation = input(f"Are you sure you want to remove {self.file_aliases_list[index]} at index {index}? (y/n)")
        if confirmation.lower() == "y":
            del self.file_aliases_list[index]
            del self.file_paths_list[index]
            del self.hash_list[index]

    def view_watchlist(self):
        # Displays all files in the watchlist
        # This function iterates through the watchlist and prints each file's details
        # it also shows the index of each file, making it easy to identify and remove files

        print("\nCurrent Watchlist:")
        for i, alias in enumerate(self.file_aliases_list):
            print(f"{i}: {alias} - {self.file_paths_list[i]}")


    def clear_watchlist(self):
        # Clears the entire watchlist
        # This function clears all three parallel lists

        self.file_aliases_list.clear()
        self.file_paths_list.clear()
        self.hash_list.clear()

    #-------------------------------------------------
    #---------------- Hash Operations ----------------
    #-------------------------------------------------

    def hash_all_files(self):
        # Hashes all files in the watchlist
        # and returns a list of their hashes

        current_hashes = [self.hash_manager.hash_file(path) for path in self.file_paths_list]
        return current_hashes

    def __check_for_changes(self):
        # Compares the current hashes with the stored hashes
        # Returns a list with the aliases of all changed files

        changes = []
        current_hashes = self.hash_all_files()
        for i, path in enumerate(self.file_paths_list):
            if current_hashes[i] != self.hash_list[i]:
                changes.append(self.file_aliases_list[i])
        return changes
    
    def check_for_changes(self):
        # Uses __check_for_changes to find any modified files
        # Prints the aliases of all changed files

        changes = self.__check_for_changes()
        if changes:
            print("\nChanges detected in the following files:")
            for alias in changes:
                print(f" - {alias}")
        else:
            print("\nNo changes detected.")


    def update_hash_list(self):
        # Updates the hash list with the current hashes of all files
        self.hash_list = self.hash_all_files()
        self.save_data()



    #-------------------------------------------------
    #---------------- Data Operations ----------------
    #-------------------------------------------------

    def save_data(self):
        # Saves the current state of the watchlist to a file
        # This includes the aliases, paths, and hashes of all watched files
        # This way, we can restore the watchlist later when the program restarts

        data_to_save = {
            "aliases": self.file_aliases_list,
            "paths": self.file_paths_list,
            "hashes": self.hash_list
        }

        try:
            with open("EFUW_data.pkl", "wb") as f:
                pkl.dump(data_to_save, f)
                print("Data saved successfully.")

        # Error Handling
        except Exception as e:
            print(f"Error saving data: {e}")


    def load_data(self):
        # Loads the watchlist from the data file "EFUW_data.pkl"
        # Restoring the previous state of the watchlist,
        # makes it able to detect changes in the files on demand,
        # without running on the background
        try:
            with open("EFUW_data.pkl", "rb") as f:
                # loads the pickled data
                # updates the watchlist

                data_loaded = pkl.load(f)
                self.file_aliases_list = data_loaded.get("aliases", [])
                self.file_paths_list = data_loaded.get("paths", [])
                self.hash_list = data_loaded.get("hashes", [])
                print("Data loaded successfully.")

        # Error Handling
        except FileNotFoundError:
            print("No saved data found. Starting with an empty watchlist.")
        except Exception as e:
            print(f"Error loading data: {e}")

            

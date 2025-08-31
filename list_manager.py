from hash_manager import hash_manager
import pickle as pkl

class list_manager:

    def __init__(self):
        self.hash_manager = hash_manager()
        self.file_aliases_list = []
        self.file_paths_list = []
        self.hash_list=[]
        self.load_data()

    def add_to_watchlist(self, alias,path,):
        self.file_aliases_list.append(alias)
        self.file_paths_list.append(path)
        self.hash_list.append(self.hash_manager.hash_file(path))

    def remove_from_watchlist(self, index):
        confirmation = input(f"Are you sure you want to remove {self.file_aliases_list[index]} at index {index}? (y/n)")
        if confirmation.lower() == "y":
            del self.file_aliases_list[index]
            del self.file_paths_list[index]
            del self.hash_list[index]

    def view_watchlist(self):
        print("\nCurrent Watchlist:")
        for i, alias in enumerate(self.file_aliases_list):
            print(f"{i}: {alias} - {self.file_paths_list[i]}")


    def clear_watchlist(self):
        self.file_aliases_list.clear()
        self.file_paths_list.clear()
        self.hash_list.clear()

    def hash_all_files(self):
        current_hashes = [self.hash_manager.hash_file(path) for path in self.file_paths_list]
        return current_hashes

    def check_for_changes(self):
        changes = []
        current_hashes = self.hash_all_files()
        for i, path in enumerate(self.file_paths_list):
            if current_hashes[i] != self.hash_list[i]:
                changes.append(self.file_aliases_list[i])
        return changes


    def save_data(self):
        data_to_save = {
            "aliases": self.file_aliases_list,
            "paths": self.file_paths_list,
            "hashes": self.hash_list
        }
        try:
            with open("EFUW_data.pkl", "wb") as f:
                pkl.dump(data_to_save, f)
                print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")


    def load_data(self):
        try:
            with open("EFUW_data.pkl", "rb") as f:
                data_loaded = pkl.load(f)
                self.file_aliases_list = data_loaded.get("aliases", [])
                self.file_paths_list = data_loaded.get("paths", [])
                self.hash_list = data_loaded.get("hashes", [])
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found. Starting with an empty watchlist.")
        except Exception as e:
            print(f"Error loading data: {e}")

"""
Class used for displaying and managing the menu options
It displays the available options and handles user input.
it can be extended to include more options as needed.
"""

class menu:
    def __init__(self):
        # Initializes the menu options
        self.options = {
            "1": "Check for changes",
            "2": "Mark changes as reviewed",
            "3": "View watchlist",
            "4": "Add to watchlist",
            "5": "Remove from watchlist",
            "6": "Clear watchlist",
            "7": "EXIT",
        }


    def display(self):
        # Displays the menu options
        print("\nSelect an option:")
        for key, value in self.options.items():
            print(f"{key}: {value}")

    def get_choice(self):
        # Gets the user's menu choice
        choice = input("Enter your choice: ")
        if choice not in self.options:
            print("Invalid choice. Please try again.")
            return self.get_choice()
        return choice


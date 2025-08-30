class menu:
    def __init__(self):
        self.options = {
            "1": "Check for changes",
            "2": "Mark changes as reviewed",
            "3": "View watchlist",
            "4": "Add to watchlist",
            "5": "Remove from watchlist",
            "6": "EXIT",
        }


    def display(self):
        print("Select an option:")
        for key, value in self.options.items():
            print(f"{key}: {value}")

    def get_choice(self):
        choice = input("Enter your choice: ")
        if choice not in self.options:
            print("Invalid choice. Please try again.")
            return self.get_choice()
        if choice == "6":
            choice = self.exit()
        return choice


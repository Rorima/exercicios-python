"""
Apply the forgetting curve. You'll have to create another key-value 
pair in the json file. This key-value pair will refer to the 
forgetting curve.

Maximum interval in seconds: 157_788_000 (five years)
Minimum interval in seconds: 21_600 (6 hours)

Buttons: Good: seconds * 2
Again: Reset to 21_600

Main objective: Menu

Options:
Option to add new cards;
Display how many cards you currently have;
Option to edit a card when you're reviewing it;
Option to delete a card when you're reviewing it;
"""
import json
import time

from os import system

MIN_INTERVAL = 21_600
MAX_INTERVAL = 157_788_000


class App:
    def __init__(self):
        self.menu()

    def menu(self):
        time.sleep(0.5)
        system("cls||clear")

        print("[1] Review cards;")
        print("[2] Add cards;")
        print("[3] Exit.")

        functions = (self.review, self.add, self.finish)
        user_choice = self.treat_input(max_val=3)
        functions[user_choice]()

    def treat_input(self, max_val, min_val=0):
        
        allowed_values = [str(x) for x in range(min_val, max_val + 1)]
        
        while True:
            user_choice = input()
            if user_choice not in allowed_values:
                print("You have to choose a valid number.")
                time.sleep(1)
                continue
            else:
                return int(user_choice) - 1

    def review(self):
        print("REVIEW is under construction.")
        self.menu()

    def add(self):
        print("ADD is under construction.")
        self.menu()

    def finish(self):
        print("Program closed successfully!")

if __name__ == "__main__":
    a = App()

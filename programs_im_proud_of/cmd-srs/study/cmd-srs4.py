"""
Apply the forgetting curve. You'll have to create another key-value 
pair in the json file. This key-value pair will refer to the 
forgetting curve.

Maximum interval in seconds: 157_788_000 (five years)
Minimum interval in seconds: 21_600 (6 hours)

Buttons:
Good: seconds * 2
Again: Reset to 21_600

Main objective: Show cards

Options:
Option to add new cards;
Display how many cards you currently have;
Option to edit a card when you're reviewing it;
Option to delete a card when you're reviewing it;
When there are no cards to review, tell the user;
Display how many cards you have to review;
Option to quit review mode;

Currently working on self.review(). My objective is to make a little 
menu for the user to review their cards. I'm thinking about creating 
another file with review related functions so that the self.review() 
function won't be too long. I can also create these functions inside 
the class itself, but it would probably make things more confusing. 
I have to find a way to make the class readable and the functions 
easy to understand. If I need to create more functions in different 
files, I should do it.
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
        
        system("cls||clear")

        study_now = []

        with open("cards.json", 'r', encoding='utf-8') as f:
            cards = json.load(f)
            for card in cards["cards"]:
                if time.time() >= card["due"]:
                    study_now.append((cards["cards"].index(card), card))

        for card in study_now:
            # first view
            print(card[1]["front"])
            print()
            input("Press ENTER to show back\n>>>")
            system("cls||clear")

            # second view
            print(card[1]["front"])
            print()
            print(card[1]["back"])
            input("[1] Good\n[2] Again\n>>>")

            system("cls||clear")

        self.rewrite(cards, study_now)

        self.menu()

    def rewrite(self, cards, study_now):
        for s_card in study_now:
            cards["cards"][s_card[0]]["due"] = time.time() + 30

        with open("cards.json", 'w', encoding='utf-8') as f:
            json.dump(cards, f, indent=2)

    def add(self):
        print("ADD is under construction.")
        self.menu()

    def finish(self):
        print("Program closed successfully!")


if __name__ == "__main__":
    a = App()

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


Currently working on self.review(). If the user chose "again" in a 
card, show that card in the same review session;
"""
import json
import time

from os import system
# temp = 21_600
MIN_INTERVAL = 10
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
            user_choice = input(">>>")
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

        self.review_algo(study_now)
        self.rewrite(cards, study_now)
        self.menu()

    def review_algo(self, study_now):
        again = False

        while True:
            for card in study_now:
                if time.time() >= card[1]["due"]:
                    again = True
                    break
                else:
                    again = False

            if again:
                for card in study_now:
                    if time.time() >= card[1]["due"]:
                        
                        # first view
                        print(card[1]["front"])
                        print()
                        input("Press ENTER to show back\n")
                        system("cls||clear")

                        # second view
                        print(card[1]["front"])
                        print()
                        print(card[1]["back"])
                        print("[1] Good\n[2] Again\n")

                        user_choice = input(">>>")
                        while user_choice not in ('1', '2'):
                            print("You have to choose a valid option.")
                            user_choice = input(">>>")

                        # update card
                        self.update(card, user_choice)
                        system("cls||clear")
            else:
                break

    def update(self, card, user_choice):
        if user_choice == "1":
            card[1]["due"] = time.time() + card[1]["interval"]
            card[1]["interval"] = card[1]["interval"] * 2
        else:
            card[1]["due"] = time.time()
            card[1]["interval"] = MIN_INTERVAL

    def rewrite(self, cards, study_now):
        for s_card in study_now:
            cards["cards"][s_card[0]]["due"] = s_card[1]["due"]
            cards["cards"][s_card[0]]["interval"] = s_card[1]["interval"]

        with open("cards.json", 'w', encoding='utf-8') as f:
            json.dump(cards, f, indent=2)

    def add(self):
        print("add is under construction.")
        self.menu()

    def finish(self):
        print("Program closed successfully!")


if __name__ == "__main__":
    a = App()

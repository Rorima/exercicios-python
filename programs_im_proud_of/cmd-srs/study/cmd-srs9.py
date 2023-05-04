"""
Maximum interval in seconds: 157_788_000 (five years)
Minimum interval in seconds: 21_600 (6 hours)

Buttons:
Good: seconds * 2
Again: Reset to 21_600

Options:
Option to add new cards;
Option to edit a card when you're reviewing it;
Option to delete a card when you're reviewing it;

Currently working on: Option to quit review mode;
"""
import json
import time

from os import system
# temp = 21_600
MIN_INTERVAL = 10
MAX_INTERVAL = 157_788_000


class App:
    def __init__(self):
        self.study = True
        self.menu()

    def menu(self):
        """Present a menu to the user and call other functions based on 
        the user's choice"""
        time.sleep(0.5)
        
        self.study = True

        system("cls||clear")

        c = self.count_cards()

        print(f"Total amount of cards: {c}.")
        print("[1] Review cards;")
        print("[2] Add cards;")
        print("[3] Exit.")

        functions = (self.review1, self.add, self.finish)
        user_choice = self.treat_input(max_val=3)
        functions[user_choice]()

    def count_cards(self):
        c = 0
        with open("cards.json", 'r', encoding='utf-8') as f:
            cards = json.load(f)
        
        for card in cards["cards"]:
            c += 1

        return c

    def count_due_cards(self, deck):
        c = 0
        for card in deck:
            if time.time() >= card[1]["due"]:
                c += 1

        return c

    def treat_input(self, max_val, min_val=0):
        """Don't let the user enter a value that isn't allowed"""
        allowed_values = [str(x) for x in range(min_val, max_val + 1)]
        
        while True:
            user_choice = input(">>>")
            if user_choice not in allowed_values:
                print("You have to choose a valid number.")
                time.sleep(1)
                continue
            else:
                return int(user_choice) - 1

    def review1(self):
        """Get due cards from the deck and send them to be reviewed"""
        system("cls||clear")

        study_now = []

        with open("cards.json", 'r', encoding='utf-8') as f:
            cards = json.load(f)
            for card in cards["cards"]:
                if time.time() >= card["due"]:
                    study_now.append((cards["cards"].index(card), card))

        self.review2(study_now)
        self.rewrite(cards, study_now)
        self.menu()

    def review2(self, study_now):
        """Check if there are due cards and call review3"""

        while self.study:
            if self.dues(study_now):
                self.review3(study_now)
            else:
                break

    def dues(self, deck):
        """Calculate due cards"""
        again = False
        for card in deck:
            if time.time() >= card[1]["due"]:
                again = True
                self.study = True
                break
            else:
                again = False
                self.study = False

        return again

    def review3(self, study_now):
        """Review cards"""
        for card in study_now:
            if time.time() >= card[1]["due"]:
                c = self.count_due_cards(study_now)
                print(f"{c} cards to review.")
                print()

                # first view
                print(card[1]["front"])
                print()
                user = input("Press ENTER to show the "
                          "back of the card or send "
                          "'q' to quit review mode\n")
                
                if user.lower() == "q":
                    self.study = False
                    break

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
                continue

            break

    def update(self, card, user_choice):
        """Update the card with a new interval"""
        if user_choice == "1":
            card[1]["due"] = time.time() + card[1]["interval"]
            card[1]["interval"] = card[1]["interval"] * 2
        else:
            card[1]["due"] = time.time()
            card[1]["interval"] = MIN_INTERVAL

    def rewrite(self, cards, study_now):
        """Rewrite the deck into the json file"""
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

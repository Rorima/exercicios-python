"""
Maximum interval in seconds: 157_788_000 (five years)
Minimum interval in seconds: 21_600 (6 hours)

Buttons:
Good: seconds * 2
Again: Reset to 21_600

Options:
Option to edit a card when you're reviewing it;
Option to delete a card when you're reviewing it;

Currently working on: Efficiency

MAYBE I only need to open the file once to read the 
cards, and then add everything to an instance variable. 
This would make the code more efficient.
"""
import json
import time

from os import system
# temp = 21_600
MIN_INTERVAL = 10
MAX_INTERVAL = 157_788_000


class App:
    def __init__(self):
        self.new_cards = list()
        self.study = True
        self.deck_init()
        self.menu()

    def deck_init(self):
        with open("cards.json", 'r', encoding='utf-8') as f:
            self.cards = json.load(f)

    def menu(self):
        """Present a menu to the user and call other functions based on 
        the user's choice"""
        time.sleep(0.5)
        
        self.study = True

        self.add_new_cards()

        system("cls||clear")
        
        deck_size = len(self.cards["cards"])

        print(f"Total amount of cards: {deck_size}.")
        print("[1] Review cards;")
        print("[2] Add cards;")
        print("[3] Exit.")

        functions = (self.review1, self.add, self.finish)
        user_choice = self.treat_input(max_val=3)
        functions[user_choice]()

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

        for card in self.cards["cards"]:
            if time.time() >= card["due"]:
                study_now.append((self.cards["cards"].index(card), card))

        while self.study:
            if self.dues(study_now):
                self.review2(study_now)
            else:
                break

        self.rewrite(study_now)
        self.menu()

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

    def review2(self, study_now):
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

    def rewrite(self, study_now):
        """Rewrite the deck into the json file"""
        for s_card in study_now:
            self.cards["cards"][s_card[0]]["due"] = s_card[1]["due"]
            self.cards["cards"][s_card[0]]["interval"] = s_card[1]["interval"]

        with open("cards.json", 'w', encoding='utf-8') as f:
            json.dump(self.cards, f, indent=2)

    def add(self):
        """Get front and back data from the user"""
        while True:
            front = input("Enter the data for the front of the card or "
                         "enter '#cancel' to cancel\n")

            if front.lower() == "#cancel":
                break

            back = input("Enter the data for the back of the card\n")

            card = {
                "front": front,
                "back": back,
                "due": time.time(),
                "interval": MIN_INTERVAL
            }

            self.add_to_deck(card)

        self.menu()

    def add_to_deck(self, card):
        """Append the card to self.new_cards list"""
        self.new_cards.append(card)

    def add_new_cards(self):
        """Add the cards from self.new_cards list into self.cards and 
        dumpt everything into the json file."""
        if self.new_cards:

            for card in self.new_cards:
                self.cards["cards"].append(card)

            with open("cards.json", 'w', encoding='utf-8') as f:
                json.dump(self.cards, f, indent=2)

            self.new_cards.clear()

    def finish(self):
        print("Program closed successfully!")


if __name__ == "__main__":
    a = App()

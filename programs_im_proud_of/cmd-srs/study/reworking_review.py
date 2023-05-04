"""
Option to quit review
"""
for i in range(3):
    if True:
        print(f"Number of cards: {i}.")
        print()

        print("Front:")
        user = input("Press ENTER to show the "
                  "back of the card or ENTER "
                  "q to quit review\n")

        if user.lower() == "q":
            break

        print("Clear screen")
        print()
        
        print("Front and back")

        print("Back")

        print("[1] Good\n[2] Again\n")

        user_choice = input(">>>")
        while user_choice not in ('1', '2'):
            print("You have to choose a valid option.")
            user_choice = input(">>>")

        print("self.update(card, user_choice)")
        print("cls||clear")
        continue

    break
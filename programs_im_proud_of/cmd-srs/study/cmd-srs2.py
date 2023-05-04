"""
Read from the json file, store the items in a variable and 
close the file. Show the items to the user, edit the time and 
open the json file again, changing the time from each card 
shown to the user.

This will probably be safer because the file won't need to stay 
open until the user finish reviewing all of their cards, which 
could be hundreds of cards daily.
"""
import json
import time

study_now = []

with open("cards.json", 'r', encoding='utf-8') as f:
    cards = json.load(f)
    for card in cards["cards"]:
        if time.time() >= card["due"]:
            study_now.append((cards["cards"].index(card), card))

for card in study_now:
    print(card[1]["front"])
    print(card[1]["back"])
    print()

for s_card in study_now:
    cards["cards"][s_card[0]]["due"] = time.time() + 100

with open("cards.json", 'w', encoding='utf-8') as f:
    json.dump(cards, f, indent=2)

print(time.time()+100)
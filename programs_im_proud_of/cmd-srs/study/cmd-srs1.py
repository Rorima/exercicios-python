"""
Create a json file by hand and make your program read it.

Only read the json file in the required time.
"""
import time
import json

with open("cards.json", 'r', encoding='utf-8') as f:
    cards = json.load(f)

    for card in cards["cards"]:
        if time.time() >= card["due"]:
            print(card["front"])
            print(card["back"])
            print()

print(time.time()+100)
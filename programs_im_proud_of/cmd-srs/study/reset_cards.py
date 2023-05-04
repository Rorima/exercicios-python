import json
import time

study_now = []

with open("cards.json", 'r', encoding='utf-8') as f:
    cards = json.load(f)

for card in cards["cards"]:
    card["due"] = time.time()
    card["interval"] = 21_600

with open("cards.json", 'w', encoding='utf-8') as f:
    json.dump(cards, f, indent=2)

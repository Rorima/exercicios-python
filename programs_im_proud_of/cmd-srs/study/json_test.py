import json

data = {
    "cards": [
        {
            "front": "this is the front of card 0",
            "back": "this is the back of card 0"
        },
        {
            "front": "this is the front of card 1",
            "back": "this is the back of card 1"
        }
    ]
}

# writing data
#with open('test.json', 'w') as f:
#    json.dump(data, f, indent=2)

# accessing data
with open("test.json", 'r') as f:
    data = json.load(f)
    for card in data["cards"]:
        print(card['front'])
        print(card['back'])
        print()
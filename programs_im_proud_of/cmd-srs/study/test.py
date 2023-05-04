cards = {
    "cards": [
        {
            "front": "front1",
            "back": "back1",
            "due": 0,
            "interval": 10,
            "delete": False
        },
        {
            "front": "front2",
            "back": "back2",
            "due": 0,
            "interval": 11,
            "delete": False
        },
        {
            "front": "front3",
            "back": "back3",
            "due": 0,
            "interval": 11,
            "delete": False
        },
        {
            "front": "front4",
            "back": "back4",
            "due": 0,
            "interval": 11,
            "delete": False
        }
    ]
}


def edit(card):
    front_or_back = input("[1] Edit front;\n[2] Edit back;\n[3] Cancel.")
    if front_or_back == '1':
        card["front"] = "New front"
    elif front_or_back == '2':
        card["back"] = "New back"
    else:
        return


def select(cards):
    study_now = list()

    for card in cards["cards"]:
        if card["interval"] > 10:
            study_now.append(cards["cards"].index(card), card)

    return study_now


study_now = select(cards)

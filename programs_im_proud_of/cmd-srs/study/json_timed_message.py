"""
This is probably the main algorithm for the cards

If timed_message.json doesn't exist, create it and add 
the time of now to it, plus one hundred seconds. If it 
already exists, then check if the time of now is the 
same or greater than the time in the json file. If so, 
print the message inside the json file.
"""
import time
import json

from os.path import exists

if not exists('timed_message.json'):
    get_current_time = time.time()

    msg = {
        "message": "The time has arrived!",
        "time": get_current_time + 100
    }

    with open('timed_message.json', 'w') as f:
        json.dump(msg, f, indent=2)
else:
    with open('timed_message.json', 'r') as f:
        data = json.load(f)
        if time.time() >= data["time"]:
            print(data["message"])
        else:
            print("Not yet...")

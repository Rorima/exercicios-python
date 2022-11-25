"""
Purpose: display a random list of chords to the user.
OBS: The chords are in Roman numerals (search for functional harmony).

How I use this:
I choose a key that I'm learning and I play the chords the program
tells me to. I do this until I learn the key, which takes less than 10
minutes, but I keep on practicing the same key for a week (10 minutes a day)
until I really have it down. When I finish my study, I choose another key
and repeat the process. I learn all keys on the ukulele using this program
and this method.
"""
from random import shuffle

chords = [
    'I', 'ii', 'iii', 'IV',
    'V', 'vi', 'viiº'
]

print("Type 'exit' to exit the program. "
      "Press ENTER to display a chord.")

while True:
    answer = input("")
    
    if answer.lower() == "exit":
        break
    
    shuffle(chords)
    
    [print(chord, end=' ') for chord in chords]  # improper
    print()

print("Program exited successfully.")

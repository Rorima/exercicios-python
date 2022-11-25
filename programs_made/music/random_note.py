"""
Purpose: display a random note to the user.
The next note cannot be one of the last
two notes displayed to the user.

How I use this:
I choose a string on my guitar (or any string instrument) and I
play the note the program tells me to. I do this for about 10 minutes
a day, and I do about 60 minutes in total on each string. This helps
to memorize all of the notes on the fretboard.
"""
from random import choice
from time import sleep

current, nex, last = [None, None, None]

notes = [
    'C', 'C#', 'Db', 'D',
    'D#', 'Eb', 'E', 'F',
    'F#', 'Gb', 'G', 'G#',
    'Ab', 'A', 'A#', 'Bb', 'B'
]

nex = choice(notes)

print("Type 'exit' to exit the program. "
      "Press ENTER to display a note.")

while True:
    sleep(3)
    
    last = current
    current = nex
    nex = choice(notes)
    
    while (nex == current) or (nex == last):
        nex = choice(notes)
    
    print(current)

print("Program exited successfully.")

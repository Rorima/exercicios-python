"""
Add a way to choose the chord based on numbers

Based on this, I can either choose to continually play 
the chord while the user has the key pressed, or let
the chord play in one key press, but add another button
to mute the sound if the user doesn't want it to 
keep going.
"""
import time
import pygame

pygame.mixer.init()


def play_chord(chord, seconds=2):
    """Play the chord chosen by the user"""

    pygame.mixer.music.load(f"{chord}.mp3")
    pygame.mixer.music.play(loops=0)

    # If you want to have more freedom while playing, you can
    # comment all lines after this one.
    #time.sleep(seconds)

    # In order to make the chord sound stop, another sound has
    # to be played instead. The nothing.mp3 has no audible sound.
    #pygame.mixer.music.load("nothing.mp3")
    #pygame.mixer.music.play(loops=0)


choose_chord = [
    "nothing", "C major", 
    "D minor", "E minor", 
    "F major", "G major", 
    "A minor", "B diminished"
]

print()
print("Instructions:")
print("Press 1 to 7 to play chords.")
print("Press 0 to mute the chord.")
print("Any number less than 0 and greater \
than 7 will stop the program")
print()

while True:
    answer = int(input("Chord: "))
    if answer < 0 or answer > 7:
        break
    else:
        play_chord(choose_chord[answer])

print("Finished successfully!")

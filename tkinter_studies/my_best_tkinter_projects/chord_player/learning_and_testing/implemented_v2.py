"""
Improvements so far:
Documented (I don't know how well, though);
Less code by using a for loop for the creation of the labels.


Implement the algorithm in a simple window.

https://tkdocs.com/shipman/event-types.html
https://tkdocs.com/shipman/key-names.html

FAILED
When the key is pressed, play the chord, when it's
released, play the nothing.

DONE
Make another version where the chord is played until
the user hits the mute key, which will play the nothing.

On another versions, make the program recognize the
keypad as well, where 0 is the nothing and the 
8 is the 1 one octave higher (maybe?)

"""
import tkinter as tk
import pygame

pygame.mixer.init()


def play_chord(chord):
    """Play a chord"""
    pygame.mixer.music.load(f"{chord}.mp3")
    pygame.mixer.music.play(loops=0)


def get_key(event):
    """Receive the key pressed and call the function play_chord"""
    
    # Chords available
    choose_chord = [
        "nothing", "C major", 
        "D minor", "E minor", 
        "F major", "G major", 
        "A minor", "B diminished"
    ]

    if event.keysym.isdigit():
        chord = int(event.keysym)

        if chord >= 0 and chord < len(choose_chord):
            play_chord(choose_chord[chord])


root = tk.Tk()
root.geometry("500x300")

center_frame = tk.Frame(root, width=300, height=100, bg="green")
center_frame.pack(expand=True)

center_frame.rowconfigure(0, weight=1)
# Configuring all columns needed for the labels
for i in range(7):
    center_frame.columnconfigure(i, weight=1)

# Forcing the frame to have the proportions I stated (300x100)
center_frame.grid_propagate(0)

# Creating seven labels
for i in range(1, 8):
    # Giving alternated colors for the labels
    if i % 2 == 0:
        lbl = tk.Label(center_frame, bg="blue", fg="white", text=i)
    else:
        lbl = tk.Label(center_frame, bg="red", fg="white", text=i)
    lbl.grid(row=0, column=i-1, sticky="news")

# Getting the any key pressed
root.bind("<Key>", get_key)

root.mainloop()

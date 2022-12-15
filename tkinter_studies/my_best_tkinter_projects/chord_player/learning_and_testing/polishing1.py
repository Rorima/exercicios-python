"""
When the key is pressed, the name of the chord should
appear on the screen.

DONE: Work on the change_label function. Maybe it's good to change
the name of the chord files. This will help with expansion, if
I ever intend to add more keys to the program. If you do it,
you'll have to change the code for all of the files written so far.
Maybe it's worth it.

"""
import tkinter as tk
import pygame

pygame.mixer.init()

# I need this variable because if the user presses a key and
# keep it pressed, the sound is played multiple times and
# it sounds choppy and bad. With this variable I can check
# if the sound is already playing and not let it play again
# unless the user releases the key.
playing = False


def play_chord(chord):
    """Play the chord. Responsible for the sound only."""
    global playing
    if not playing:
        pygame.mixer.music.load(f"{chord}.mp3")
        pygame.mixer.music.play(loops=0)
        playing = True


def play_nothing(event):
    """Play nothing when the key is released and clean the chord_label"""
    global playing
    if playing:
        pygame.mixer.music.load("nothing.mp3")
        pygame.mixer.music.play(loops=0)
        playing = False
        chord_label.config(text="\n")


def get_key(event):
    """Receive the key pressed, call the function play_chord and call
    the change_label function."""

    # Available chords:
    choose_chord = [
        "nothing", "C major", 
        "D minor", "E minor", 
        "F major", "G major", 
        "A minor", "B diminished"
    ]

    if event.keysym.isdigit():
        chord = int(event.keysym)

        if chord >= 0 and chord < len(choose_chord):
            change_label(chord, choose_chord)
            play_chord(choose_chord[chord])


def change_label(number, chord_list):
    """Change the chord_label with the current chord being 
    played and its function.
    
    number: the index/number of the chord inside the list
    chord_list: a list of the available chords
    """
    chord_function = [
        '', 'I', 'ii', 'iii',
        'IV', 'V', 'vi', 'viiº'
    ]
    chord = chord_list[number] + f"\n{chord_function[number]}"
    if number != 0:
        chord_label.config(text=chord)


root = tk.Tk()
root.geometry("500x300")
root.title("Chord Player")

# This will keep everything in the middle of the screen
main_frame = tk.Frame(root)
main_frame.pack(expand=True)

# Display the chords at the top of the main frame
chord_label = tk.Label(
    main_frame, 
    font=("", 24, "bold"),
    text="\n"
)
chord_label.pack(pady=10)

# Display the numbers at the bottom so the user will know
# what to press when the program starts
number_frame = tk.Frame(main_frame)
number_frame.pack()

number_frame.rowconfigure(0, weight=1)

# Configuring all columns needed for the labels
for i in range(7):
    number_frame.columnconfigure(i, weight=1)

# Creating seven labels
for i in range(1, 8):
    lbl = tk.Label(number_frame, text=i, font=("", 18))
    lbl.grid(row=0, column=i-1, sticky="news")

# Getting any key pressed
root.bind("<Key>", get_key)
root.bind("<KeyRelease>", play_nothing)

root.mainloop()

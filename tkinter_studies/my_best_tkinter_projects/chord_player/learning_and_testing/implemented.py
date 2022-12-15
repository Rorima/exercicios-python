"""
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


def p(chord):
    pygame.mixer.music.load(f"{chord}.mp3")
    pygame.mixer.music.play(loops=0)


def get_key(event):
    choose_chord = [
        "nothing", "C major", 
        "D minor", "E minor", 
        "F major", "G major", 
        "A minor", "B diminished"
    ]

    if str(event.keysym).isdigit():
        chord = int(event.keysym)

        if chord >= 0 and chord < len(choose_chord):
            p(choose_chord[chord])


root = tk.Tk()
root.geometry("500x300")


center_frame = tk.Frame(root, width=300, height=100, bg="green")
center_frame.pack(expand=True)

center_frame.rowconfigure(0, weight=1)
for i in range(7):
    center_frame.columnconfigure(i, weight=1)

center_frame.grid_propagate(0)

lbl1 = tk.Label(center_frame, bg="blue", fg="white", text=1)
lbl1.grid(row=0, column=0, sticky="wesn")

lbl2 = tk.Label(center_frame, bg="red", fg="white", text=2)
lbl2.grid(row=0, column=1, sticky="nsew")

lbl3 = tk.Label(center_frame, bg="blue", fg="white", text=3)
lbl3.grid(row=0, column=2, sticky="nsew")

lbl4 = tk.Label(center_frame, bg="red", fg="white", text=4)
lbl4.grid(row=0, column=3, sticky="nsew")

lbl5 = tk.Label(center_frame, bg="blue", fg="white", text=5)
lbl5.grid(row=0, column=4, sticky="nsew")

lbl6 = tk.Label(center_frame, bg="red", fg="white", text=6)
lbl6.grid(row=0, column=5, sticky="nsew")

lbl7 = tk.Label(center_frame, bg="blue", fg="white", text=7)
lbl7.grid(row=0, column=6, sticky="nsew")

root.bind("<Key>", get_key)

root.mainloop()

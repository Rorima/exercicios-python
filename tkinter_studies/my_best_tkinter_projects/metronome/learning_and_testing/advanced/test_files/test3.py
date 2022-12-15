"""
Adding accent to beat one.

I've just realized that this relies on the
after function. This means that the BPM will
not be very precise. Hopefully it's imperceptible.
"""
import tkinter as tk
import pygame

pygame.mixer.init()

has_started = False
counter = 1


def start_stop_metronome():
    """Start and stop the metronome"""
    global has_started
    has_started = not has_started
    if has_started:
        controller()


def controller():
    """Call two other functions and controll the time"""
    play_sound()
    count_beat()
    id = root.after(1000, controller)
    
    if not has_started:
        root.after_cancel(id)
        print("Finished")


def count_beat():
    """Count the beat"""
    global counter
    print(counter, end="\r")
    if counter >= 4:
        counter = 1
    else:
        counter += 1


def play_sound():
    """Play the knock sound"""
    global counter
    if counter == 1:
        pygame.mixer.music.load("accent_knock.mp3")
        pygame.mixer.music.play(loops=0)
    else:
        pygame.mixer.music.load("normal_knock.mp3")
        pygame.mixer.music.play(loops=0)


root = tk.Tk()

start_stop_button = tk.Button(root, command=start_stop_metronome)
start_stop_button.pack(fill="both")

root.mainloop()
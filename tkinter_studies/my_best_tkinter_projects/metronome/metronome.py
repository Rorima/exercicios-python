"""
Create a simple metronome where the user can choose the
BPM and the time signature.
"""
import tkinter as tk
import pygame

pygame.mixer.init()

has_started = False
counter = 1
time_signature = 4


def start_stop_metronome():
    """Start and stop the metronome and reset counter"""
    global has_started, counter
    has_started = not has_started
    if has_started:
        start_stop_button.config(text="Stop")
        controller()
    else:
        counter = 1
        start_stop_button.config(text="Start")


def controller():
    """Call two other functions and control the time"""
    play_sound()
    count_beat()
    bpm = scale.get()
    # Expression to turn bpm into milliseconds
    bpm = 60 / bpm * 1000
    id = root.after(int(bpm), controller)
    
    if not has_started:
        root.after_cancel(id)


def change_time_sig(time_sig):
    """Change time signature"""
    global time_signature
    time_signature = time_sig


def count_beat():
    """Count the beat and change number_label"""
    global counter, time_signature
    number_label.config(text=counter)
    if counter >= time_signature:
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
root.geometry("500x600")
root.title("Metronome")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(
    label="1/4",
    command=lambda: change_time_sig(1)
)
file_menu.add_command(
    label="2/4",
    command=lambda: change_time_sig(2)
)
file_menu.add_command(
    label="3/4",
    command=lambda: change_time_sig(3)
)
file_menu.add_command(
    label="4/4",
    command=lambda: change_time_sig(4)
)
file_menu.add_command(
    label="5/4",
    command=lambda: change_time_sig(5)
)
file_menu.add_command(
    label="6/4",
    command=lambda: change_time_sig(6)
)
file_menu.add_command(
    label="7/4",
    command=lambda: change_time_sig(7)
)
file_menu.add_command(
    label="8/4",
    command=lambda: change_time_sig(8)
)
file_menu.add_command(
    label="9/4",
    command=lambda: change_time_sig(9)
)
file_menu.add_command(
    label="10/4",
    command=lambda: change_time_sig(10)
)
file_menu.add_command(
    label="11/4",
    command=lambda: change_time_sig(11)
)
file_menu.add_command(
    label="12/4",
    command=lambda: change_time_sig(12)
)

menubar.add_cascade(
    label="Time Signatures",
    menu=file_menu
)

number_label = tk.Label(
    root,
    font=("times new romans", 90),
    text=1
)
number_label.pack(expand=True)

scale = tk.Scale(
    root, from_=30, 
    to=240, 
    length=400, 
    orient="horizontal",
    tickinterval=210,
    sliderlength=80,
    width=30
)
scale.set(60)
scale.pack(expand=True)

start_stop_button = tk.Button(
    root,
    text="Start",
    font=("times new romans", 25),
    pady=10,
    padx=30,
    command=start_stop_metronome
)
start_stop_button.pack(expand=True)

root.mainloop()

# Glória a Deus!

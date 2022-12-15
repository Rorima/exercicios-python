"""
Only how the metronome should look.
"""
import tkinter as tk

root = tk.Tk()
root.geometry("500x600")
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(
    label="1/4"
)
file_menu.add_command(
    label="2/4"
)
file_menu.add_command(
    label="3/4"
)
file_menu.add_command(
    label="4/4"
)
file_menu.add_command(
    label="5/4"
)
file_menu.add_command(
    label="6/4"
)
file_menu.add_command(
    label="7/4"
)
file_menu.add_command(
    label="8/4"
)
file_menu.add_command(
    label="9/4"
)
file_menu.add_command(
    label="10/4"
)
file_menu.add_command(
    label="11/4"
)
file_menu.add_command(
    label="12/4"
)

menubar.add_cascade(
    label="Time Signatures",
    menu=file_menu
    
)

beat_label = tk.Label(
    root,
    font=("times new romans", 90),
    text=1
)
beat_label.pack(expand=True)

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

start_stop_b = tk.Button(
    root,
    text="Start",
    font=("times new romans", 25),
    pady=10,
    padx=30
)
start_stop_b.pack(expand=True)



root.mainloop()

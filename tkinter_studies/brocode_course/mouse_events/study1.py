import tkinter as tk


def do_something(event):
    print(f"You clicked at ({event.x}, {event.y}).")


window = tk.Tk()

window.bind("<Button-1>", do_something)  # Left mouse click
# window.bind("<Button-2>", do_something)  # Wheel mouse click
# window.bind("<Button-3>", do_something)  # Right mouse click
# window.bind("<ButtonRelease>", do_something)  # Right mouse release
# window.bind("<Enter>", do_something)  # When the mouse enters the screen
# window.bind("<Leave>", do_something)  # When the mouse leaves the screen
# window.bind("<Motion>", do_something)  # Where the mouse moves


window.mainloop()

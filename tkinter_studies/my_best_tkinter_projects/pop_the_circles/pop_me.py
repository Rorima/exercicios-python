"""
DONE: Create a function that when the circle is clicked, it
makes the circle disappear and create another circle.

DONE: Play a sound effect when the circle is popped.

DONE: Add a score.

DONE: Create a red circle that has a chance of appearing
on the screen. If the red circle appears, the user has
to click outside the circle. If the user clicks inside it,
the score restarts.

DONE: Add a highest score so far.
"""
import tkinter as tk
import ball_class

window = tk.Tk()
window.geometry("500x600")
window.config(background="#151515")
window.title("Pop me!")

score_label = tk.Label(window, text=0, font=("times new romans", 40), bg="#151515", fg="#4eea13")
score_label.pack()

canvas = tk.Canvas(window, width=500, height=500, bg="#151515", highlightcolor="red", highlightthickness=1)
canvas.pack()

highest_score_label = tk.Label(window, text=f"Highest: {0}", font=("times new romans", 20), bg="#151515", fg="#4eea13")
highest_score_label.pack()

b = ball_class.Ball(canvas, score_label, highest_score_label)

b.decide_color()

canvas.bind("<Button-1>", b.circle_click)

window.mainloop()

#GaD
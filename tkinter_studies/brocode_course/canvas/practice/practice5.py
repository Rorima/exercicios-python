"""
Create an arc that fills gradually once the user presses a button.
"""
import tkinter as tk

i = 0


def fill_arc():
    global i
    i += 1
    fill_button.config(state="disabled")

    x = canvas.after(50, fill_arc)
    canvas.create_arc(1, 1, 399, 399, fill="purple", extent=i, start=90)
    if i == 359:
        canvas.after_cancel(x)


window = tk.Tk()
window.geometry("500x500")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

canvas.create_arc(1, 1, 399, 399, fill="purple", extent=0, start=90)

fill_button = tk.Button(window, text="Fill", font=("Arial", 20), bg="#DADADA", command=fill_arc)
fill_button.pack(side="bottom", pady=20, ipadx=10, ipady=10)

window.mainloop()

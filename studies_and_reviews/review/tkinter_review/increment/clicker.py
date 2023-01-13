import tkinter as tk

clicks = 0


def click():
    global clicks
    clicks += 1
    click_label.config(text=clicks)


root = tk.Tk()
root.geometry("600x500")

click_label = tk.Label(
    root,
    text=clicks,
    font=("Constantia", 30),
    width=3,
    height=3
)
click_label.pack()

click_button = tk.Button(
    root,
    text="Click Me!",
    font=("Constantia", 30),
    width=10,
    height=3,
    command=click
)
click_button.pack()

root.mainloop()

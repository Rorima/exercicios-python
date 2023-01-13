"""
Create a hacker themed Text Widget. There should be a button to
submit the text. Print the text on the terminal.
"""
import tkinter as tk


def submit():
    print(hacker_text.get("1.0", "end"))


window = tk.Tk()
window.config(bg="black")

hacker_text = tk.Text(
    window,
    font=("Arial", 20),
    height=15,
    width=50,
    padx=15,
    pady=15,
    bg="black",
    fg="#37ec2c"
)
hacker_text.pack()

submit_button = tk.Button(
    window,
    text="Submit",
    font=("Arial", 15),
    bg="black",
    fg="#37ec2c",
    activebackground="black",
    activeforeground="#37ec2c",
    command=submit
)
submit_button.pack()

window.mainloop()

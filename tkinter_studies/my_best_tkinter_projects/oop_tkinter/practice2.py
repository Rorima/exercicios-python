"""
The same program in practice1.py, but with the code a little
bit different

So far, this is my favorite layout.
"""

import tkinter as tk


class App:
    def __init__(self, master):
        self.root = master
        self.root.geometry("400x400")
        self.root.title("Learning OOP Tkinter")

        self.center_frame = tk.Frame(master)
        self.center_frame.pack(expand=True)

        self.main_label = tk.Label(
            self.center_frame, 
            text=0,
            font=("", 30)
        )
        self.main_label.pack(pady=10)

        self.click_me_b = tk.Button(
            self.center_frame,
            text="Click me!",
            font=("", 20),
            command=self.increase
        )
        self.click_me_b.pack()

        self.counter = 0

    def increase(self):
        self.counter += 1
        self.main_label.config(text=self.counter)


root = tk.Tk()
window = App(root)
root.mainloop()
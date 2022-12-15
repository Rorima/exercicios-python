"""
Create a simple program that increases the number when
the user clicks a button.
"""
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")


class App:
    def __init__(self, master):
        self.center_frame = tk.Frame(master)
        self.center_frame.pack(expand=True)

        self.main_label = tk.Label(
            self.center_frame, 
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


window = App(root)

root.mainloop()
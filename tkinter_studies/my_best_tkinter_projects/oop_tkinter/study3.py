"""
If I'm not wrong, using this method, self becomes the root, and everytime I
want to make a change or add something to the root window, I use self.
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()


        # configure the root window
        self.title("My Awesome App")
        self.geometry("300x100")


        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()


        # button
        self.button = ttk.Button(self, text="Click Me")
        self.button["command"] = self.button_clicked
        self.button.pack()

        
        # clear button
        self.button = ttk.Button(self, text="Clear Screen")
        self.button["command"] = self.clear_screen
        self.button.pack()
    

    def button_clicked(self):
        showinfo(title="Information", message="Hello, Tkinter!")


    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

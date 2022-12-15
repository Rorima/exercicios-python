import tkinter as tk


def main():
    root = tk.Tk()
    window1 = Window(
        root, 
        "Learn OOP Tkinter", 
        "400x400", 
        "Hello!"
    )


class Window:
    n = 0

    def __init__(self, root, title, geometry, message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)


        self.display = tk.Label(self.root, text=message)
        self.display.pack()

        button1 = tk.Button(self.root, text="Increment", command=self.increment)
        button1.pack()

        self.root.mainloop()

    def increment(self):
        self.n += 1
        self.display.config(text=self.n)
        return None


main()

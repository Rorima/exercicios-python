import tkinter as tk

root = tk.Tk()
root.title("Learning to use classes")
root.geometry("400x400")

class App:
    def __init__(self, master):
        my_frame = tk.Frame(master)
        my_frame.pack()

        self.my_button = tk.Button(
            master, 
            text="Click me!",
            command=self.clicker
        )
        self.my_button.pack(pady=20)
    
    def clicker(self):
        print("You clicked!")


window = App(root)

root.mainloop()

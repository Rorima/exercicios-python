import tkinter as tk


class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Stopwatch")
        self.geometry("400x200")
        self.config(bg="#1b1b1b")

        t = "00:00"

        self.center_label = tk.Label(self, font=("", 60),text=t, fg="#77CC11", bg="#1b1b1b")
        self.center_label.pack(expand=True)



root = App()
root.mainloop()

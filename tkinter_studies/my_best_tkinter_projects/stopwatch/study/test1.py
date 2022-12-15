"""
FIX THE THIS BUGG.
Try to make it stop and start from where it stopped. Create another
program if it's needed.

"""
import tkinter as tk
import time


class App(tk.Tk):
    
    start = False
    running = False
    first = 0
    middle = ''
    last = ''
    inner_time = 0

    def __init__(self):
        super().__init__()
        
        self.title("Stopwatch")
        self.geometry("400x200")
        self.config(bg="#1b1b1b")

        self.center_label = tk.Label(
            self, 
            font=("", 60),
            text="00:00", 
            fg="#77CC11", 
            bg="#1b1b1b"
        )
        self.center_label.pack(expand=True)

        self.bind("<ButtonRelease-1>", self.start_stop)
        self.bind("<space>", self.start_stop)
        self.bind("<Double-ButtonRelease-1>", self.reset)


    def start_stop(self, event):
        if App.start:
            
            App.start = False
            App.last = time.time()
            App.inner_time = App.last - App.first

            self.center_label.config(text=f"{App.inner_time:.2f}")
            
        else:
            if not App.running:
                App.first = time.time()
            
            App.start = True
            App.running = True
            self.display_current_time()


    def display_current_time(self):
        App.middle = time.time()
        
        if App.start:
            App.inner_time = App.middle - App.first
            self.center_label.config(text=f"{App.inner_time:.2f}")
            self.after(98, self.display_current_time)


    def reset(self, event):
        App.start = False
        App.running = False
        App.first = 0
        App.middle = 0
        App.last = 0
        self.center_label.config(text=f"{App.last - App.first:.2f}")


if __name__ == "__main__":
    root = App()
    root.mainloop()

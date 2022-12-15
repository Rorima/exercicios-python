"""
Stopwatch program.

About the making of this program:
This program is more precise than the previous one I made. It was a challenge
to work with the time and figure out a way to make it precise when the user
paused and unpaused it. It's not made to be absolutely usable for all things.
It's just a pretty program, that challenged me to learn more.

Functions of this program:
The stopwatch can be started and stopped using your mouse or the spacebar key. 
If clicked twice, the stopwatch will reset.
"""
import tkinter as tk
import time


class App(tk.Tk):
    
    start = False
    running = False
    first = 0
    middle = 0
    last = 0
    inner_time = 0
    old_time = 0


    def __init__(self):
        super().__init__()
        
        self.title("Stopwatch")
        self.geometry("400x200")
        self.config(bg="#1b1b1b")

        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=3)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)

        # The main label, where the time will be displayed
        self.center_label = tk.Label(
            self, 
            font=("", 60),
            text="00:00", 
            fg="#77CC11", 
            bg="#1b1b1b"
        )

        self.fill_label1 = tk.Label(self, bg="#1b1b1b")
        self.fill_label2 = tk.Label(self, bg="#1b1b1b")
        self.fill_label3 = tk.Label(self, bg="#1b1b1b")
        
        self.fill_label4 = tk.Label(self, bg="#1b1b1b")

        self.fill_label6 = tk.Label(self, bg="#1b1b1b")

        self.fill_label7 = tk.Label(self, bg="#1b1b1b")
        self.fill_label8 = tk.Label(self, bg="#1b1b1b")
        self.fill_label9 = tk.Label(self, bg="#1b1b1b")

        self.fill_label1.grid(row=0, column=0)
        self.fill_label2.grid(row=0, column=1)
        self.fill_label3.grid(row=0, column=2)
        
        self.fill_label4.grid(row=1, column=0)
        self.center_label.grid(row=1, column=1)
        self.fill_label6.grid(row=1, column=2)

        self.fill_label7.grid(row=2, column=0)
        self.fill_label8.grid(row=2, column=1)
        self.fill_label9.grid(row=2, column=2)


        self.bind("<ButtonRelease-1>", self.start_stop)
        self.bind("<space>", self.start_stop)
        self.bind("<Double-ButtonRelease-1>", self.reset)


    def start_stop(self, event):
        """Start and stop the stopwatch"""
        if App.start:
            
            App.start = False
            App.last = time.time()
            App.inner_time = App.last - App.first
            App.old_time += App.inner_time

            self.show_current_time(App.old_time)
            
        else:
            App.first = time.time()

            App.start = True
            App.running = True
            self.calculate_current_time()


    def calculate_current_time(self):
        """Calculate the current time"""
        App.middle = time.time()
        
        if App.start:
            App.inner_time = App.middle - App.first
            self.show_current_time(App.old_time + App.inner_time)
            self.after(98, self.calculate_current_time)


    def show_current_time(self, seconds):
        """Display current time on the screen"""
        if seconds >= 3600:
            self.reset("<Double-ButtonRelease-1>")
        
        minutes = int(seconds // 60)
        seconds = seconds % 60
        seconds = round(seconds)

        if minutes < 10:
            minutes = str(minutes).zfill(2)
        if seconds < 10:
            seconds = str(seconds).zfill(2)
        
        self.center_label.config(text=f"{minutes}:{seconds}")


    def reset(self, event):
        """Reset the stopwatch"""
        App.start = False
        App.running = False
        App.first = 0
        App.middle = 0
        App.last = 0
        App.inner_time = 0
        App.old_time = 0
        self.show_current_time(0)


if __name__ == "__main__":
    root = App()
    root.mainloop()

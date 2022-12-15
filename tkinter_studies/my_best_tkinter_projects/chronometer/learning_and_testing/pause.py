"""
Trying to figure out a way to stop this and start from where
it stopped.

I think I'll have to use global variables. In order to do that,
I'll have to decrease the amount of variables I'm using.

I think I improved the algorithm.
"""
import tkinter as tk

running = False

second = 0
minute = 0
hour = 0


def pause():
    """Start and pause the cronometer"""
    global running
    if running:
        running = False
    else:
        running = True
        count_time()


def count_time():
    """Count the time"""
    global second, minute, hour
    
    if second >= 59:
        minute += 1
        second = 0
    
    if minute >= 59:
        hour += 1
        minute = 0
    
    if hour >= 59:
        hour = 0
        minute = 0
        second = 0

    second += 1

    # Adding a 0 in front of the number if the number is less than 10
    # to give some nice aesthetics
    sec_display = second if second > 9 else str(second).zfill(2)
    min_display = minute if minute > 9 else str(minute).zfill(2)
    hou_display = hour if hour > 9 else str(hour).zfill(2)
    print(f"{hou_display}:{min_display}:{sec_display}", end="\r")

    if running:
        root.after(1000, count_time)


root = tk.Tk()

b = tk.Button(
    root, 
    text="0", 
    padx=100, 
    pady=100, 
    command=pause
)
b.pack()

root.mainloop()

"""
This chronometer is not precise.
"""
import tkinter as tk

running = False

hund = 0
second = 0
minute = 0
hour = 0


def call_start(event):
    """Call the function start_n_pause after the user has pressed space"""
    start_n_pause()


def start_n_pause():
    """Start and pause the cronometer"""
    global running
    if running:
        start_stop_b.config(text="Start")
        running = False
    else:
        start_stop_b.config(text="Stop")
        running = True
        count_time()


def count_time():
    """Count the time"""
    global second, minute, hour, hund
    
    # A hundred of a second
    if hund >= 1000:
        second += 1
        hund = 0
    
    if second > 59:
        minute += 1
        second = 0
    
    if minute > 59:
        hour += 1
        minute = 0
    
    if hour > 59:
        hour = 0
        minute = 0
        second = 0

    hund += 100

    # Adding a 0 in front of the number if the number is less than 10
    # to give some nice aesthetics
    sec_display = second if second > 9 else str(second).zfill(2)
    min_display = minute if minute > 9 else str(minute).zfill(2)
    hou_display = hour if hour > 9 else str(hour).zfill(2)
    
    time = f"{hou_display}:{min_display}:{sec_display}"
    number_label.config(text=time)

    if running:
        # The right amount would be 100, but it gets unprecise pretty fast,
        # so I decided to call the function every 99 millisiconds, which takes
        # a little bit over a minute to be left behind by a normal stopwatch
        # (on my machine. Yours would be different.)
        root.after(99, count_time)


def reset():
    global second, minute, hour, hund
    
    if not running:
        second = 0
        minute = 0
        hour = 0
        hund = 0
        number_label.config(text="00:00:00")


root = tk.Tk()
root.geometry("400x200")
root.title("Chronometer")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

f = tk.Frame(root)
f.pack(expand=True)

number_label = tk.Label(
    f,
    text="00:00:00",
    font=("times new romans", 50)
)
number_label.grid(row=0, column=0, columnspan=2, sticky="ns")

start_stop_b = tk.Button(
    f,
    text="Start",
    font=("times new romans", 30),
    command=start_n_pause
)
start_stop_b.grid(row=1, column=1, sticky="nwse")

reset_b = tk.Button(
    f,
    text="Reset",
    font=("times new romans", 15, "bold"),
    command=reset
)
reset_b.grid(row=1, column=0, sticky="nwse", ipadx=1)

root.bind("<space>", call_start)

root.mainloop()

# Glória a Deus!

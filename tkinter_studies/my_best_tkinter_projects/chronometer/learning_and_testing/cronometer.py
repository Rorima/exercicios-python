"""
This chronometer is not precise.
"""
import tkinter as tk

has_started = False


def start():
    """Changes the text of the button from start to stop"""
    global has_started, pause

    if not has_started:
        start_stop_b.config(text="Stop")
        has_started = True
        crono()
    else:
        start_stop_b.config(text="Start")
        has_started = False


def crono():

    def count_time():
        """Generator for counting time"""
        seg = 0 
        dez_seg = 0 
        mi = 0 
        dez_mi = 0 
        hor = 0 
        dez_hor = 0
        while True:
            if seg >= 9:
                dez_seg += 1
                seg = -1
                
            if dez_seg >= 6:
                dez_seg = 0
                mi += 1
                
            if mi >= 10:
                dez_mi += 1
                mi = 0
                
            if dez_mi >= 6:
                hor += 1
                dez_mi = 0
                
            if hor >= 10:
                dez_hor += 1
                hor = 0
                
            if dez_hor >= 6:
                dez_hor = 0
                hor = 0
                dez_mi = 0
                mi = 0
                dez_seg = 0
                seg = 0
                    
            seg += 1
            yield f"{dez_hor}{hor}:{dez_mi}{mi}:{dez_seg}{seg}"
    
    def call_next():
        """Call next on the generator for counting time"""
        global has_started
        nonlocal gen

        text = next(gen)
        number_label.config(text=text)

        identification = root.after(1000, call_next)
        if not has_started:
            root.after_cancel(identification)

    gen = count_time()
    call_next()


root = tk.Tk()
root.geometry("400x200")
root.title("Cronômetro")
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
    command=start
)
start_stop_b.grid(row=1, column=1, sticky="nwse")

reset_b = tk.Button(
    f,
    text="Reset",
    font=("times new romans", 15, "bold")
)
reset_b.grid(row=1, column=0, sticky="nwse", ipadx=1)

root.mainloop()

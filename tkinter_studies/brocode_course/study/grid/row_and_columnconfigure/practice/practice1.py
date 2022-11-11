"""
Recreate study 1.
"""
import tkinter as tk

window = tk.Tk()
window.state("zoomed")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=4)
window.columnconfigure(2, weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=4)
window.rowconfigure(2, weight=1)

left_label = tk.Label(
    text="Left",
    bg="#A8FFD4",
    font=("Arial", 20, "bold")
).grid(row=0, column=0, rowspan=3, sticky="NSWE")

center_top = tk.Label(
    text="Center Top",
    bg="#B6A4FF",
    font=("Arial", 20, "bold")
).grid(row=0, column=1, sticky="NSWE")

center_middle = tk.Label(
    text="Center Middle",
    bg="#FFA4A5",
    font=("Arial", 20, "bold")
).grid(row=1, column=1, sticky="NSWE")

center_bottom = tk.Label(
    text="Center Bottom",
    bg="#B6A4FF",
    font=("Arial", 20, "bold")
).grid(row=2, column=1, sticky="NSWE")

right_label = tk.Label(
    text="Right",
    bg="#A8FFD4",
    font=("Arial", 20, "bold")
).grid(row=0, column=2, rowspan=3, sticky="NSWE")

window.mainloop()

import tkinter as tk

window = tk.Tk()
window.state("zoomed")
window.minsize(width=600, height=600)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=5)
window.rowconfigure(2, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)

left_label = tk.Label(
    window, 
    text="Left", 
    bg="yellow", 
    font=("Constantia", 30)
)
left_label.grid(row=0, column=0, sticky="NSEW", rowspan=3)

center_top_label = tk.Label(
    window, 
    text="Center TOP", 
    bg="lightblue",
    font=("Constantia", 30)
)
center_top_label.grid(row=0, column=1, sticky="NSEW")

center_label = tk.Label(
    window, 
    text="Center", 
    bg="pink",
    font=("Constantia", 30)
)
center_label.grid(row=1, column=1, sticky="NSEW")

center_bottom_label = tk.Label(
    window, 
    text="Center BOTTOM", 
    bg="orange",
    font=("Constantia", 30)
)
center_bottom_label.grid(row=2, column=1, sticky="NSEW")

right_label = tk.Label(
    window, 
    text="Right", 
    bg="lightgreen",
    font=("Constantia", 30)
)
right_label.grid(row=0, column=2, sticky="NSEW", rowspan=3)

window.mainloop()

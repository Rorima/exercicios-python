"""
Create a frame and place two buttons in it: Open and Save.
Place a text area under the buttons.
"""
import tkinter as tk

window = tk.Tk()
window.resizable(False, False)

button_frame = tk.Frame(window)
button_frame.grid(row=0, column=0, sticky='w')

open_button = tk.Button(button_frame, text="Open", font=("Constantia", 20))
open_button.pack(side="left")

save_button = tk.Button(button_frame, text="Save", font=("Constantia", 20))
save_button.pack(side="left")

text_area = tk.Text(
    window, 
    font=("Constantia", 20), 
    width=50, 
    height=15, 
    padx=10, 
    pady=10
)
text_area.grid(row=1, column=0)

window.mainloop()

"""
Create a TopLevel window that will display a number.
The number should increase everytime a new window is opened.
"""
import tkinter as tk

counter = 0

def click_me():
    global counter
    counter += 1
    temporary_window = tk.Toplevel()
    temporary_window.geometry("300x300")
    display_counter = tk.Label(
        temporary_window, 
        text=counter,
        font=("Constantia", 20))
    display_counter.pack()


main_window = tk.Tk()
main_window.geometry("300x300")

click_me_button = tk.Button(
    text="Click Me!",
    font=("Constantia", 15),
    command=click_me
)
click_me_button.pack()

main_window.mainloop()

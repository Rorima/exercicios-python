"""
This is possibly how the program is going to look like.
"""
import tkinter as tk
from random import randint


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def main_screen():
    clear_screen()
    
    c_frame_operations = tk.Frame(root)
    c_frame_operations.pack(expand=True)
    
    my_font = ("", 18, "bold")

    addition_b = tk.Button(
        c_frame_operations, 
        font=my_font, 
        text=" Addition",
        command=lambda: level_screen("addition"),
        image=addition_image,
        compound="left"
    )
    addition_b.grid(row=0, column=0, pady=50, padx=10, sticky="news")
    

    subtraction_b = tk.Button(
        c_frame_operations, 
        font=my_font, 
        text=" Subtraction",
        command=lambda: level_screen("subtraction"),
        image=subtraction_image,
        compound="left"
    )
    subtraction_b.grid(row=0, column=1, padx=10, pady=50, sticky="news", ipadx=12)


    multiplication_b = tk.Button(
        c_frame_operations, 
        font=my_font, 
        text=" Multiplication",
        command=lambda: level_screen("multiplication"),
        image=multiplication_image,
        compound="left"
    )
    multiplication_b.grid(row=1, column=0, padx=10, pady=50, sticky="news")
    
    
    division_b = tk.Button(
        c_frame_operations, 
        font=my_font, 
        text=" Division",
        command=lambda: level_screen("division"),
        image=division_image,
        compound="left"
    )
    division_b.grid(row=1, column=1, padx=10, pady=50, sticky="news")


def level_screen(operation):
    clear_screen()
    b_frame = tk.Frame(root)
    b_frame.pack(fill="x")
    back_button = tk.Button(b_frame, text="Back", command=lambda: main_screen())
    back_button.pack(side="left", pady=10, padx=10)

    c_frame_levels = tk.Frame(root)
    c_frame_levels.pack(expand=True)
    

    lvlb1 = tk.Button(
            c_frame_levels, 
            font=("", 18, "bold"), 
            text=f"Level 1",
            command=lambda: operation_manager(operation, 1)
    )
    
    lvlb2 = tk.Button(
            c_frame_levels, 
            font=("", 18, "bold"), 
            text=f"Level 2",
            command=lambda: operation_manager(operation, 2)
    )

    lvlb3 = tk.Button(
            c_frame_levels, 
            font=("", 18, "bold"), 
            text=f"Level 3",
            command=lambda: operation_manager(operation, 3)
    )

    lvlb4 = tk.Button(
            c_frame_levels, 
            font=("", 18, "bold"), 
            text=f"Level 4",
            command=lambda: operation_manager(operation, 4)
    )

    lvlb5 = tk.Button(
            c_frame_levels, 
            font=("", 18, "bold"), 
            text=f"Level 5",
            command=lambda: operation_manager(operation, 5)
    )
    
    level_buttons = (lvlb1, lvlb2, lvlb3, lvlb4, lvlb5)

    for b in level_buttons:
        b.pack(pady=10, ipadx=30)


def operation_manager(operation, level):
    print(f"The chosen operation was: {operation};")
    print(f"The chosen level was: {level}.")


root = tk.Tk()
root.geometry("500x600")

addition_image = tk.PhotoImage(file="addition_operator.png")
subtraction_image = tk.PhotoImage(file="subtraction_operator.png")
multiplication_image = tk.PhotoImage(file="multiplication_operator.png")
division_image = tk.PhotoImage(file="division_operator.png")
main_screen()

root.mainloop()

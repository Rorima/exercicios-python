"""
Purpose:
Show random expressions and their answers to the user.

When I was learning division (yeah...) I wanted to do some exercises,
but I didn't find a lot of them on the videos I was watching. I know
there are websites that have lot's of division exercises, but I figured
it would help me improve a little bit my programming skills if I wrote
my own random expression generator. So here it is.

"""
import tkinter as tk
from random import randint

# Each number inside the tuple represents the maximum number that an
# expression can have. The 0 is excluded. The 9 shows that in the first 
# level, the limit for the numbers used in the expression is 9. For example:
# (A random number from 1 to 9) + (A random number from 1 to 9) = n
levels = (0, 9, 20, 99, 999, 99999)


def clear_screen():
    """Remove all widgets from the screen."""
    
    for widget in root.winfo_children():
        widget.destroy()


def main_screen():
    """Create the main screen with four buttons for the four basic operations."""
    
    clear_screen()

    title = tk.Label(root, text="Four Operations", font=("", 24, "bold"))
    title.pack(pady=70)

    # Center frame to hold the operation buttons
    c_frame_operations = tk.Frame(root)
    c_frame_operations.pack()
    
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
    """Show a screen with five levels for the user to choose."""
    
    clear_screen()
    
    back_button(operation)

    # Center frame to hold all the levels
    c_frame_levels = tk.Frame(root)
    c_frame_levels.pack(expand=True)
    
    my_font = ("", 18, "bold")

    lvlb1 = tk.Button(
            c_frame_levels, 
            font=my_font, 
            text=f"Level 1",
            command=lambda: expression_screen(operation, 1)
    )
    
    lvlb2 = tk.Button(
            c_frame_levels, 
            font=my_font, 
            text=f"Level 2",
            command=lambda: expression_screen(operation, 2)
    )

    lvlb3 = tk.Button(
            c_frame_levels, 
            font=my_font, 
            text=f"Level 3",
            command=lambda: expression_screen(operation, 3)
    )

    lvlb4 = tk.Button(
            c_frame_levels, 
            font=my_font, 
            text=f"Level 4",
            command=lambda: expression_screen(operation, 4)
    )

    lvlb5 = tk.Button(
            c_frame_levels, 
            font=my_font, 
            text=f"Level 5",
            command=lambda: expression_screen(operation, 5)
    )
    
    level_buttons = (lvlb1, lvlb2, lvlb3, lvlb4, lvlb5)

    for b in level_buttons:
        b.pack(pady=10, ipadx=30)


def expression_maker(operation, level):
    """Make a random expression with the operation and level given and return
    all of the parameters."""

    num1 = randint(1, levels[level])
    num2 = randint(1, levels[level])

    if operation == "addition":
        result = num1 + num2
        operation_symbol = "+"
    elif operation == "subtraction":
        result = num1 - num2
        operation_symbol = "-"
    elif operation == "multiplication":
        result = num2 * num2
        operation_symbol = "x"
    elif operation == "division":
        result = num1 / num2
        operation_symbol = "/"

    return (operation_symbol, num1, num2, result)


def expression_screen(operation, level):
    """Create a screen that will show a random expression to the user."""

    clear_screen()
    back_button(operation, gt_lvl_screen=True)
    
    operation_symbol, num1, num2, result = expression_maker(operation, level)

    # Center frame to hold the label and button
    c_frame = tk.Frame(root)
    c_frame.pack(expand=True)

    expression_label = tk.Label(
        c_frame,
        font=("", 30),
        text=f"{num1} {operation_symbol} {num2} = ?"
    )
    expression_label.pack(expand=True, pady=100)

    show_answer_b = tk.Button(
        c_frame,
        font=("", 20),
        text="Show answer",
        command=lambda: show_answer(
            operation_symbol=operation_symbol,
            num1=num1,
            num2=num2,
            result=result,
            expression_label=expression_label,
            show_answer_b=show_answer_b,
            operation=operation,
            level=level
        )
    )
    show_answer_b.pack(side="bottom")


def show_answer(
    operation_symbol, num1, num2, 
    result, expression_label, show_answer_b, 
    operation, level):
    """Show the answer on the screen and modify the button when it is clicked."""

    if len(str(result)) > 6:
        text = f"{num1} {operation_symbol} {num2} =\n{result}"
    else:
        text = f"{num1} {operation_symbol} {num2} = {result}"
    
    expression_label.config(text=text)

    show_answer_b.config(
        text="Next", 
        command=lambda: expression_screen(operation, level)
    )
    show_answer_b.pack(side="bottom", ipadx=55)


def back_button(operation, gt_lvl_screen=False):
    """Create a back button. Go back to the main screen from the level 
    screen, and if the user is inside the expression screen, go back to 
    thel level screen."""

    b_frame = tk.Frame(root)
    b_frame.pack(fill="x")

    back_button = tk.Button(
        b_frame, 
        text="Back", 
        command=main_screen
    )

    # gt_level_screen: Go to level screen
    if gt_lvl_screen:
        back_button.config(command=lambda: level_screen(operation))

    back_button.pack(side="left", pady=10, padx=10)


root = tk.Tk()
root.geometry("500x600")
root.title("Four Operations")

addition_image = tk.PhotoImage(file="addition_operator.png")
subtraction_image = tk.PhotoImage(file="subtraction_operator.png")
multiplication_image = tk.PhotoImage(file="multiplication_operator.png")
division_image = tk.PhotoImage(file="division_operator.png")
main_screen()

root.mainloop()

"""
Create a notebook with two tabs. The first tab asks for information 
and the second tab displays the information.
"""
import tkinter as tk
from tkinter import ttk


def submit():
    display_information()
    name_entry.config(state="disabled")
    age_entry.config(state="disabled")
    prof_entry.config(state="disabled")
    submit_button.config(state="disabled")


def display_information():
    name = name_entry.get()
    age = age_entry.get()
    profession = prof_entry.get()

    info = (
        f"Name: {name};\n"
        f"Age: {age};\n"
        f"Profession: {profession}.\n"
    )

    display_name_label = tk.Label(
        frame2, 
        text=info, 
        font=("Constantia", 12),
        justify="left"
    )
    display_name_label.grid(column=0, row=0, sticky='w')


root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = tk.Frame(notebook, width=300, height=180)
frame1.pack(expand=True, fill="both")
frame2 = tk.Frame(notebook, width=300, height=180)
frame2.pack(expand=True, fill="both")

notebook.add(frame1, text="Query")
notebook.add(frame2, text="Information")

name_label = tk.Label(frame1, text="Name: ", font=("Constantia", 12))
name_label.grid(column=0, row=0, sticky="w")
name_entry = tk.Entry(frame1, font=("Constantia", 12))
name_entry.grid(column=1, row=0)

age_label = tk.Label(frame1, text="Age: ", font=("Constantia", 12))
age_label.grid(column=0, row=1, sticky="w")
age_entry = tk.Entry(frame1, font=("Constantia", 12))
age_entry.grid(column=1, row=1)

prof_label = tk.Label(frame1, text="Profession: ", font=("Constantia", 12))
prof_label.grid(column=0, row=2, sticky="w")
prof_entry = tk.Entry(frame1, font=("Constantia", 12))
prof_entry.grid(column=1, row=2)

submit_button = tk.Button(
    frame1, 
    text="Submit", 
    font=("Constantia", 12), 
    command=submit
)
submit_button.grid(column=1, row=3, sticky="e")

root.mainloop()

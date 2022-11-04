import tkinter as tk

root = tk.Tk()

title_label = tk.Label(root, text="Enter your info: ", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)

first_name_label = tk.Label(root,text="First name: ").grid(row=1, column=0)
first_name_entry = tk.Entry(root).grid(row=1, column=1)

last_name_label = tk.Label(root,text="Last name: ").grid(row=2, column=0)
last_name_entry = tk.Entry(root).grid(row=2, column=1)

email_label = tk.Label(root,text="Email: ").grid(row=3, column=0)
email_entry = tk.Entry(root).grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit").grid(row=4, column=0, columnspan=2)

root.mainloop()

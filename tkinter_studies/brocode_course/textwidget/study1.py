import tkinter as tk


def submit():
    user_text = text_area.get("1.0", "end")
    print(user_text)


root = tk.Tk()

text_area = tk.Text(
    root, 
    bg="light yellow",
    font=("Ink Free",  20),
    height=10,
    width=72,
    padx=15,
    pady=15
)
text_area.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox


def click_info():
    messagebox.showinfo(title="Infobox",
                        message="This message will be displayed to the user.")


def click_warning():
    messagebox.showwarning(title="WARNING",
                           message="DO SOMETHING!")


def click_error():
    messagebox.showerror(title="ERROR!",
                         message="Something ain't right")


def click_ask_ok_cancel():
    answer = messagebox.askokcancel(title="Title",
                           message="Ok or Cancel?")
    if answer:
        print("You clicked OK")
    else:
        print("You clicked Cancel :(")


def click_ask_retry_cancel():
    answer = messagebox.askretrycancel(title="Title",
                                       message="Retry or Cancel?")
    if answer:
        print("You clicked Retry")
    else:
        print("You clicked Cancel")


def click_ask_yes_no():
    answer = messagebox.askyesno(title="Title",
                                 message="Yes or No?")
    if answer:
        print("You clicked Yes")
    else:
        print("You clicked No")


def click_ask_question():
    answer = messagebox.askquestion(title="Ask Question",
                                    message="Do you like cake?")
    print(answer)


def click_ask_yes_no_cancel():
    answer = messagebox.askyesnocancel(title="ask Yes No Cancel",
                                       message="Do you know the way?",
                                       icon="info")
    print(answer)
    if answer:
        print("Cool")
    elif answer == False:
        print("Uncool")
    elif answer == None:
        print("Ok then.")


window = tk.Tk()

bt_info = tk.Button(window, command=click_info, text="Click for info")
bt_info.pack()

bt_warning = tk.Button(window, command=click_warning, text="Click for warning")
bt_warning.pack()

bt_error = tk.Button(window, command=click_error, text="Click for error")
bt_error.pack()

bt_ask_ok_cancel = tk.Button(window, command=click_ask_ok_cancel, text="Click for ask ok cancel")
bt_ask_ok_cancel.pack()

bt_ask_retry_cancel = tk.Button(window, command=click_ask_retry_cancel, text="Click for ask retry cancel")
bt_ask_retry_cancel.pack()

bt_ask_yes_no = tk.Button(window, command=click_ask_yes_no, text="Click for ask yes no")
bt_ask_yes_no.pack()

bt_ask_question = tk.Button(window, command=click_ask_question, text="Click for ask question")
bt_ask_question.pack()

bt_ask_yes_no_cancel = tk.Button(window, command=click_ask_yes_no_cancel, text="Click for ask yes no cancel")
bt_ask_yes_no_cancel.pack()

window.mainloop()

"""
Place a label with a text in your tkinter program.
"""
from tkinter import *

window = Tk()

window.geometry("650x700")
window.title("Sunt Enim")
window.config(background='black')

text_title = Label(text='Sunt Enim',
                   font=('Arial', 40 , 'bold'),
                   fg='white',
                   bg='black',
                   padx=10,
                   pady=10)

text_1st_paragraph = Label(text=
'''Sunt enim culpa sint consectetur deserunt
reprehenderit deserunt do duis irure consectetur aute.
Ipsum exercitation consectetur do consectetur est enim
nisi nostrud elit nostrud est. Sunt enim velit excepteur
sit esse. Quis ipsum consectetur amet nisi ipsum anim
commodo sunt officia non. Occaecat exercitation
exercitation incididunt labore tempor id dolor nostrud.
Nulla officia laborum mollit excepteur. Eu duis sint
laborum do minim.''',
                                font=('Arial', 18 ,),
                                fg='white',
                                bg='black',
                                padx=10,
                                pady=10)

text_2nd_paragraph = Label(text=
'''Laborum nulla dolore elit cupidatat dolor aute.
Ullamco enim elit laborum veniam consectetur tempor
magna proident. Mollit ut exercitation esse velit esse
laborum quis ipsum veniam ullamco incididunt tempor
commodo.''',
                                font=('Arial', 18 ,),
                                fg='white',
                                bg='black'
                           )

text_title.pack()
text_1st_paragraph.pack()
text_2nd_paragraph.pack()

window.mainloop()

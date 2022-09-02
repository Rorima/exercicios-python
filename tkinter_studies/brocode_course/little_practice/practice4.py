"""
Make a black window with green text.
"""
from tkinter import *

window = Tk()

window.geometry('700x420')
window.title('Reckah')
window.config(background='black')

hacker_code = '''
<?php

$variable = get_field('field_name');

// do something with $variable

?>
'''

nonsense_text = Label(text=hacker_code,
                      justify=LEFT,
                      font=('Roboto', 20),
                      fg='#21dc3e',
                      bg='black')

nonsense_text.grid()

window.mainloop()

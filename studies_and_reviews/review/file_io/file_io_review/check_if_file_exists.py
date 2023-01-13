"""
Use the exists() function from the os.path module to check if
the file you're looking for exists.
"""
from os.path import exists

file = "text.txt"
if exists(file):
    print(f'The "{file}" file exists.')
else:
    print('The "{file}" file doesn\'t exist.')

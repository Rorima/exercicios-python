"""
Use fieldnames.
"""
from csv import DictReader

fieldnames = ['c', 'l', 'f']

with open('countries.csv') as file:
    reader = DictReader(file, fieldnames)
    next(reader)
    for line in reader:
        print(f"Country: {line['c']}; food: {line['f']};")
        print()

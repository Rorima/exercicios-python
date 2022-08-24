"""
Write a csv file using the DictWriter class.
"""
from csv import DictWriter

# This data was randomly generated
fieldnames = ["name", "age"]
rows = [
    {"name": "Edwina Watts",
     "age": "38"},
    {"name": "Leland Rollins",
     "age": "70"},
    {"name": "Charlie Humphrey",
     "age": "66"},
    {"name": "Coley Kent",
     "age": "82"},
    {"name": "Gracia Blake",
     "age": "14"},
]

with open("people_age.csv", 'w', newline='') as f:
    writer = DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

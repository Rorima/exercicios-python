"""
Use the writerow() and writerows() functions to write to the csv file.
"""
import csv

# This data was randomly generated
header = ["name", "age"]
a_row = ["Edwina Watts", "38"]
rows = [
    ["Leland Rollins", "70"],
    ["Charlie Humphrey", "66"],
    ["Coley Kent", "82"],
    ["Gracia Blake", "14"],
    ["Libby Gamble", "21"],
    ["Christie Keller", "47"],
    ["Jerry Sherman", "97"],
    ["Jay Day", "16"],
    ["Mason Hunter", "98"]
]

with open("people_name_age.csv", 'w', newline='') as f:
    data = csv.writer(f)
    data.writerow(header)
    data.writerow(a_row)
    data.writerows(rows)

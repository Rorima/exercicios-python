"""
Read the people_and_weight.csv file and print the data on the screen.
Use the enumerate() function to go through the list.
"""
import csv

with open("people_and_weight.csv", 'r') as f:
    data = csv.reader(f)
    next(data)
    for number, person in enumerate(data, start=1):
        print(f"Person: {number};")
        print(f"Name: {person[0]};")
        print(f"Weight: {person[1]}kg;")
        print()

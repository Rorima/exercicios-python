"""
Read the people_and_weight.csv file and print the data on the screen.
"""
import csv

with open("people_and_weight.csv", 'r') as f:
    data = csv.reader(f)
    next(data)
    for line in data:
        print(line)

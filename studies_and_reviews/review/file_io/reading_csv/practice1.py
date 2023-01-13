"""
Go through a cvs file and use the enumerate function.
"""
import csv

with open("countries.csv", 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for country, food in enumerate(csv_reader, start=1):
        print(f"Country: {country} - Food: {food[2]}")

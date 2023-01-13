"""
Read the people_and_weight.csv using the DictReader class.
"""
from csv import DictReader

fieldnames = ['person', 'weight']

with open("people_and_weight.csv", 'r') as f:
    csv_reader = DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
        print(f"Person: {line['person']}")
        print(f"Weight: {line['weight']}kg.")
        print()

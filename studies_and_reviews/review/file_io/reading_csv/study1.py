import csv

with open("countries.csv", 'r') as f:
    csv_reader = csv.reader(f)
    counter = 0
    for line in csv_reader:
        counter += 1
        print(f"Line: {counter}:", line)

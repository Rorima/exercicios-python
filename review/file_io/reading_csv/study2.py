import csv

with open("countries.csv") as f:
    csv_reader = csv.DictReader(f)
    for line in csv_reader:
        print(f"Country: {line['Country']}")
        print(f"Language: {line['Language']}")
        print(f"Food: {line['Food']}")
        print()

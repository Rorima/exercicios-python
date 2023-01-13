import csv

fieldnames = ['cntry', 'lang', 'fd']

with open('countries.csv') as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
        print(f"Country: {line['cntry']};")
        print(f"Language: {line['lang']};")
        print(f"Food: {line['fd']};")
        print()

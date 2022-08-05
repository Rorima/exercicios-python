"""
Read the countries.csv using the dict reader and print the items.

This is the expected result:
Country: United States
Language: English
Food: Hamburger

Country: Brazil
Language: Portuguese
Food: Feijoada

Country: India
Language: Hindi
Food: Masala Chai Tea

Country: England
Language: English
Food: Potato
"""
from csv import DictReader

with open("countries.csv") as f:
    csv_reader = DictReader(f)
    for line in csv_reader:
        print(f"Country: {line['Country']}")
        print(f"Language: {line['Language']}")
        print(f"Food: {line['Food']}")
        print()

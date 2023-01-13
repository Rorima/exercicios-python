import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    write = csv.writer(f)
    write.writerow(header)
    write.writerow(data)

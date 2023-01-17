import csv

header = ['name', 'email']

user_name = input("What is your name?\n")
user_email = input("What is your email?\n")

with open('names.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    csv_writer.writerow(header)
    csv_writer.writerow([user_name, user_email])

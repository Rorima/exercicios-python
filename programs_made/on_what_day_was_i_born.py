import datetime

birth_date = input('Type your birth date (mm/dd/yyyy): ')
birth_date = birth_date.split('/')
birth_date = datetime.datetime(int(birth_date[2]), int(birth_date[0]), int(birth_date[1]))

if birth_date.weekday() == 0:
    print('You were born on Monday!')
elif birth_date.weekday() == 1:
    print('You were born on Tuesday!')
elif birth_date.weekday() == 2:
    print('You were born on Wednesday!')
elif birth_date.weekday() == 3:
    print('You were born on Thursday!')
elif birth_date.weekday() == 4:
    print('You were born on Friday!')
elif birth_date.weekday() == 5:
    print('You were born on Sunday!')
elif birth_date.weekday() == 6:
    print('You were born on Saturday!')

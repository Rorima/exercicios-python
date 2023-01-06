import datetime

birthdate = input('Type your birth date (mm/dd/yyyy): ')
birthdate = birthdate.split('/')
birthdate = datetime.datetime(int(birthdate[2]), int(birthdate[0]), int(birthdate[1]))

if birthdate.weekday() == 0:
    print('You were born on Monday!')
elif birthdate.weekday() == 1:
    print('You were born on Tuesday!')
elif birthdate.weekday() == 2:
    print('You were born on Wednesday!')
elif birthdate.weekday() == 3:
    print('You were born on Thursday!')
elif birthdate.weekday() == 4:
    print('You were born on Friday!')
elif birthdate.weekday() == 5:
    print('You were born on Sunday!')
elif birthdate.weekday() == 6:
    print('You were born on Saturday!')

import time

now = 1681742745.4335077

future = time.localtime(now + 60)


if time.localtime() >= future:
    print("The time has arrived!")
else:
    print("Not yet.")

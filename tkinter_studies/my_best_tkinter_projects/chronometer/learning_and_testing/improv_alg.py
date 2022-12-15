"""
I'll try to improve the cronometer algorithm 
to use less variables.
"""
import time

second = 0
minute = 0
hour = 0


def gen():
    global second, minute, hour
    while True:
        if second >= 59:
            minute += 1
            second = 0
        
        if minute >= 59:
            hour += 1
            minute = 0
        
        if hour >= 59:
            hour = 0
            minute = 0
            second = 0

        hour += 1

        sec_display = second if second > 9 else str(second).zfill(2)
        min_display = minute if minute > 9 else str(minute).zfill(2)
        hou_display = hour if hour > 9 else str(hour).zfill(2)
        yield f"{hou_display}:{min_display}:{sec_display}"


a = gen()
while True:
    print(next(a), end="\r")
    time.sleep(0.5)

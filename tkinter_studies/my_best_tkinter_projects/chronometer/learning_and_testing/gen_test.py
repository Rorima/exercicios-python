"""
Learning how to increment using generator
"""
import time

def increment(num):
    while True:
        num += 1
        yield num
    

x = increment(0)
while True:
    print(next(x))
    time.sleep(1)    

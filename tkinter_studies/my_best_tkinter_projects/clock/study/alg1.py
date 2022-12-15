"""
Create the algorithm for the clock
"""
import time

while True:
    ct = time.strftime("%H:%M:%S", time.localtime())
    print(ct, end="\r")
    time.sleep(0.2)

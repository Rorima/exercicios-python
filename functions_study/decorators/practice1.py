"""
Create a decorator that measures how long it takes for a function to run.
"""

from time import time

def how_long(func):
    
    def wrapper():
        start = time()
        func()
        finish = time()
        print(f'\nIt took {finish - start} seconds to run this function.')
        
    return wrapper


@how_long
def talker():
    for _ in range(10):
        print('blah', end=" ")


talker()

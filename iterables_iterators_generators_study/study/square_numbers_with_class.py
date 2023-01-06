"""
Create a class with dunder next and iter and square numbers.
"""

class Squaring:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        
        current = self.start
        self.start += 1
        return current * current


squared = Squaring(1, 10)

for x in squared:
    print(x)

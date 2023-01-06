"""
Exponetiate using a closure.

b == base
n == power
"""

def power(n):
    def base(b):
        print(b ** n)
    
    return base


test = power(3)
test(10)

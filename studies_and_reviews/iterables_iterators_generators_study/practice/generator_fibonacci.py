"""
Logic:

n1 = 0
n2 = 1
n3 = 0

n3 = n1 + n2
n1 = n2
n2 = n3

print(n3)
"""


def fibo():
    before = 1
    now = 0
    after = 0
    
    while True:
        after = before + now
        before = now
        now = after
        yield before


test = fibo()

counter = 0
while counter < 15:
    counter += 1
    print(next(test))

# gD

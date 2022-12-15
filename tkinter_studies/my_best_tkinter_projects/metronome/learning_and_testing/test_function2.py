"""
DISCARTED
    240bpm = 0.25s
    120bpm = 0.5s
    60bpm = 1s
    30bpm = 2s
    15bpm = 4s

    b = 60
    x = 1
    f(0.5) = 120 (60 % 0.5)
    f(1) = 60 (60 % 1)
    f(2) = 30 (60 % 2)

"""
# DISCARTED

def f(x):
    return x / 60
    """
    120 = 2
    60 = 1
    30 = 0.5
    """
x = float(input("Number: "))
print(f(x))

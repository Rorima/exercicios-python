"""
FILE VERIFIED

learning how the ration bpm/time works.
240bpm = 0.25s
120bpm = 0.5s
 ----------
|60bpm = 1s|
 ----------
30bpm = 2s
15bpm = 4s

f(0.5) == 120 (60 / 0.5)
f(1) == 60 (60 / 1)
f(2) == 30 (60 / 2)

"""
# VERIFIED

def f(x):
    """Return the seconds needed for the chosen BPM"""
    return 60 / x
    # x / 60

x = int(input("BPM: "))
print(f(x), "seconds")

# Glória a Deus!!!
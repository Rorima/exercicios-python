import time

# The objective is 30 seconds from now
objective = time.localtime(time.time() + 30)
c = 0

now = time.localtime()

while now <= objective:
    c += 1
    print(f"Not yet. {c}")
    time.sleep(1)
    now = time.localtime()

print()
print("Thirty seconds have passed!!!!")
print()
print("finished!")
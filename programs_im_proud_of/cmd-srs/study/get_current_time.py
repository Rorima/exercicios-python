import time

time_struct = time.localtime()
string_time_struct = time.asctime(time_struct)
secs_since_epoch = time.time()
test = secs_since_epoch + 10_000
future = time.localtime(test)

print(f"Time struct: {time_struct[0]}")
print(f"Time struct string: {string_time_struct}")
print(f"Seconds since epoch: {secs_since_epoch}")
print(f"10_000 seconds in the future: {future[3], future[4]}")

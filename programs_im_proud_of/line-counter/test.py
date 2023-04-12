first_count = True

for i in range(10):
    if first_count:
        if i == 3:
            continue
    else:
        print(i)

first_count = False

for i in range(10):
    if first_count:
        if i == 3:
            continue
    else:
        print(i)
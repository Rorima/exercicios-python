with open("testing1.txt", 'r') as f:
    f.seek(0)
    if f.readlines():
        print(True)
    else:
        print(False)

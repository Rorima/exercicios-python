with open("notes7.txt", 'r') as f:
    print(f.readline())
    print(f.tell())
    f.seek(11)
    print(f.readline())

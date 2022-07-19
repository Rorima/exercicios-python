link = "https://www.pythontutorial.net/python-basics/python-create-text-file/"
title = "Python create text file"
listy = [link, title]
with open("notes3.txt", 'w') as f:
    f.write("\n".join(listy))
    f.write("\n")

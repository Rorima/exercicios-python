"""
Open the readme.txt file and use the three reading methods. Print
what was inside the file.
"""
with open("readme.txt", 'r') as f:
    whole_file = f.read()
    f.seek(0)
    first_line = f.readline()
    f.seek(0)
    all_lines = f.readlines()
    
    print(f"The whole file is: \n{whole_file}\n")
    print(f"The first line is: \n{first_line}")
    print(f"All the lines are: \n{all_lines}")

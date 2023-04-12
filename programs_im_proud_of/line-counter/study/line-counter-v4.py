"""
The main objective now is to find a way to display every 
folder that the script enters and its files. I also have
to figure out a way to display this to the user, so that
the user will know what is inside what.

First, try just to display the folders that the program
goes into.
"""
from pathlib import Path


class LineCounter:

    def __init__(self):
        cwd = Path.cwd()
        self.files = list()
        self.dirs = list()
        self.iter_dirs(cwd)
        self.print_dicts()
        print()
        self.sum_lines()

    def iter_dirs(self, directory):
        """Iter over all directories"""
        
        for d in directory.iterdir():

            if d.is_dir():
                self.dirs.append(d)
                self.iter_dirs(d)
            elif d.is_file():
                self.count_lines(d)

    def count_lines(self, path):
        """Count lines from a file.
        
        Count lines from a file and add the file name with the line count 
        to the dictionary files
        """
        with open(f"{path}", 'r') as f:
            file_is_empty = not f.readlines()
            f.seek(0)

            self.files.append({f"{path.name}": len(f.readlines())})
            f.seek(0)
            
            if not file_is_empty:
                # check if there is a new line at the end of file
                new_line_eof = f.readlines()[-1][-1:] == '\n'
                if new_line_eof: self.files[-1][f"{path.name}"] += 1

    def sum_lines(self):
        """Sum the lines of the whole project"""
        total = 0
        for file in self.files:
            total += tuple(file.values())[0]
        
        print(f"Your project has a total of {total} lines of code.")

    def print_dicts(self):
        """Print the dictionaries in self.files"""
        for file in self.files:
            key, value = list(file.items())[0]
            print(f"Name: {key}\nLines: {value};")
            print()

        print("Directories checked: \n")

        for d in self.dirs:
            print(d)


if __name__ == "__main__":
    lc = LineCounter()

"""
Brainstorm:

Create a separate function that will get only the files and
count the lines. Enter the folder, use that function, and
save its results. Check if there are more folders, use that
function and save the results. Rinse and repeat.

Algorithm:

from pathlib import Path


def iter_dr(cwd):
    print(f"Directory: {cwd.name}")
    print(f"Lines: {iter_files(cwd)}")
    print()

    for d in cwd.iterdir():
        if d.is_dir():
            iter_dr(d)

def iter_files(cwd):
    total = 0

    for d in cwd.iterdir():
        if d.is_file():
            with open(f"{d}", 'r') as f:
                file_is_empty = not f.readlines()
                f.seek(0)

                if not file_is_empty:
                    # check if there is a new line at the end of file
                    new_line_eof = f.readlines()[-1][-1:] == '\n'
                    if new_line_eof: total += 1

                f.seek(0)
                total += len(f.readlines())

    return total


cwd = Path.cwd()
iter_dr(cwd)
"""
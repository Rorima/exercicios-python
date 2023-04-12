"""
line-counter-v2.py had a problem:
If there were files with the same name and the same
extension, but in different folders, it wouldn't add
one of the files to the dictionary because the name
of the file is the key, and there can't be equal
keys in a dictionary. You have to figure out
a way to fix this.

The solution might be to create a list of dictionaries.

Working on self.print_dicts: find a way to print all
of the dictionaries inside the list self.files.
"""
from pathlib import Path


class LineCounter:

    def __init__(self):
        cwd = Path.cwd()
        self.files = list()
        self.iter_dirs(cwd)
        self.print_dicts()

    def iter_dirs(self, directory):
        """Iter over all directories"""
        
        for d in directory.iterdir():

            if d.is_dir():
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

    def print_dicts(self):
        """Print the dictionaries in self.files"""
        for file in self.files:
            key, value = list(file.items())[0]
            print(f"Name: {key}\nLines: {value};")
            print()

if __name__ == "__main__":
    lc = LineCounter()

"""
This program counts lines from a project.

What to do:
1. Count all the lines from the current dir; DONE
2. Enter in all dir and count lines from them; DONE
3. Name dir and at the end show how many lines from each dir
4. Add an option to exclude certain file extensions

I'm trying to figure out a way to work with the directories. Maybe list
them all or something like that. The main purpose is to enter each
directory and read each file. Maybe this can already be done. I can
think of naming each dir in the next study file.
"""
from pathlib import Path


class LineCounter:

    def __init__(self):
        cwd = Path.cwd()
        self.files = dict()
        self.iter_dirs(cwd)
        self.print_dict()

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

            self.files[f"{path.name}"] = len(f.readlines())
            f.seek(0)
            
            if not file_is_empty:
                # check if there is a new line at the end of file
                new_line_eof = f.readlines()[-1][-1:] == '\n'
                if new_line_eof: self.files[f"{path.name}"] += 1

    def print_dict(self):
        """Print the dictionary self.files"""
        for file in self.files.items():
            print(f"Name: {file[0]}\nLines: {file[1]};")
            print()


if __name__ == "__main__":
    lc = LineCounter()

"""
This program counts lines from a project.

What to do:
1. Count all the lines from the current dir; WORKING ON THIS
2. Enter in all dir and count lines from them;
3. Name dir and at the end show how many lines from each dir
4. Add an option to exclude certain file extensions

"""
from pathlib import Path


class LineCounter:

    def __init__(self):
        self.files = dict()
        self.cwd = Path.cwd()
        self.list_files()

    def list_files(self):
        """Iter over all files from the directory and call self.count_lines"""
        for path in self.cwd.iterdir():
            if path.is_file():
                self.count_lines(path)

        self.print_dict()

    def count_lines(self, path):
        """Count lines from a file.
        
        Count lines from a file and add the file name with the line count 
        to the dictionary files
        """
        with open(f"{path.name}", 'r') as f:
            
            self.files[f"{path.name}"] = len(f.readlines())
            f.seek(0)

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

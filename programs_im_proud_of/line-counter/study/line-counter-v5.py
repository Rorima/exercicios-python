"""
Display the total amount of lines of code of each file and of 
each folder. At the end of the program show the amount of lines 
of the whole project.

It should display something like this:

Folder: folder_name, Lines: line_count
* file1: line_count;
* file2: line_count;
* file3: line_count;
* file4: line_count;

Folder: folder_name, Lines: line_count
* file1: line_count;
* file2: line_count;
* file3: line_count;
* file4: line_count;

Total lines of the project: line_count

"""
from pathlib import Path

class LineCounter:

    def __init__(self):
        cwd = Path.cwd()
        self.files = list()
        self.dirs = list()
        self.count_lines_current_file(cwd)
        self.iter_dirs(cwd)
        self.print_dirs_list()

    def count_lines_current_file(self, directory):
        files = self.iter_files(directory)
        self.dirs.append({directory.name: files})

    def iter_dirs(self, directory):

        for d in directory.iterdir():
            if d.is_dir():
                files = self.iter_files(d)
                self.dirs.append({d.name: files})
                self.iter_dirs(d)

    def iter_files(self, directory):
        
        files_list = list()

        for f in directory.iterdir():
            if f.is_file():
                dictionary = self.count_lines(f)
                files_list.append(dictionary)

        return files_list

    def count_lines(self, file):
        with open(f"{file}", 'r') as f:
            file_is_empty = not f.readlines()
            f.seek(0)

            line_count = len(f.readlines())
            f.seek(0)
            
            if not file_is_empty:
                # check if there is a new line at the end of file
                new_line_eof = f.readlines()[-1][-1:] == '\n'
                if new_line_eof: line_count += 1

        return {file.name: line_count}

    def print_dirs_list(self):
        total_lines = 0
        for item in self.dirs:
            total_lines_dir = 0
            for key, value in item.items():
                print(f"Directory: {key}")
                print(f"Files:")
                for i in value:
                    k = list(i.keys())[0]
                    v = list(i.values())[0]
                    total_lines_dir += v
                    print(f"* Name: {k}")
                    print(f"* Lines: {v}")
                    print()

                print(f"Total lines of this directory: {total_lines_dir}")
                print("*"*30)
                total_lines += total_lines_dir

            print()
            print()

        print(f"Total lines of the project: {total_lines}")


if __name__ == "__main__":
    lc = LineCounter()

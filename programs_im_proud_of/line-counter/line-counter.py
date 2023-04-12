"""
IMPORTANT NOTE: DO NOT CHANGE THE NAME THE NAME OF THIS FILE!

This program iters through directories and files and count
the total amount of lines a project has. Place the script
inside the directory you want the script to start counting
from and run it. If you want the program to read from a
particular file extension, you can add it to the tupple
ALLOWED, which contain all the file extensions that the
program will read from.

NOTE TO PROGRAMMERS:

Structure of self.dirs:

self.dirs is a list that contains dictionaries. The key of 
these dictionaries is the name of the directories present 
in that project. Their values are a list of dictionaries, and each 
dictionary inside the list contains the name of the file inside 
that particular directory as its key, and the amount of lines of that 
file as its value. This structure was chosen because it allows files 
and directories to have the same name.

Visual representation:

self.dirs: [
    {
        "directory1": [
            {"file1": lines},
            {"file2": lines}
        ]
    },
    {
        "directory2": [
            {"file1": lines},
            {"file2": lines},
            {"file3": lines},
            {"file4": lines}
        ]
    },
    {
        "directory3": [
            {"file1": lines}
        ]
    }
]
"""
from pathlib import Path

# Add here the file extensions that you want the program to read from
ALLOWED = (
    ".txt", ".py", ".md", ".c", ".cpp", 
    ".html", ".css", ".java", ".json",
    ".bat", ".cmd", ".cats", ".h", ".idc",
    ".w", ".cs", ".cake", ".cshtml", ".csx",
    ".c++", ".cc", ".cp", ".cxx", ".h++",
    ".hh", ".hpp", "hxx", ".inc", ".inl",
    ".ipp", ".tcc", ".tpp", ".csv", ".dart",
    ".js", "._js", ".bones", ".es", ".es6",
    ".frag", ".gs", ".jake", ".jsb", ".jscad",
    ".jsfl", ".jsm", ".jss", ".njs", ".pac",
    ".sjs", ".ssjs", ".sublime-build", ".sublime-commands", ".sublime-commands",
    ".sublime-completions", ".sublime-keymap", ".sublime-macro", ".sublime-menu",
    ".sublime-mousemap", ".sublime-project", ".sublime-settings", ".sublime-theme",
    ".sublime-workspace", ".sublime_metrics", ".sublime_session", ".xsjs", ".xsjslib",
    ".ipynb", ".kt", ".ktm", ".kts", ".lua", 
    ".fcgi", ".nse", ".pd_lua", ".rbxs", ".wlua",
    ".markdown", ".mkd", ".mkdn", ".mkdown", ".ron",
    ".m", ".php", ".aw", ".ctp", ".fcgi",
    ".inc", ".php3", ".php4", ".php5", ".phps",
    ".phpt", ".pl", ".al", ".cgi", ".fcgi",
    ".perl", ".ph", ".plx", ".pm", ".pod",
    ".psgi", ".t", ".ps1", ".psd1", ".psm1",
    ".bzl", ".cgi", ".fcgi", ".gyp", ".lmi",
    ".pyde", ".pyp", ".pyt", ".pyw", ".rpy",
    ".tac", ".wsgi", ".xpy", ".r", ".rd",
    ".rsx", ".rb", ".builder", ".fcgi", ".gemspec",
    ".god", ".irbrc", ".jbuilder", ".mspec", ".pluginspec",
    ".podspec", ".rabl", ".rake", ".rbuild", ".rbw", 
    ".rbx", ".ru", ".ruby", ".thor", ".watchr",
    ".rs", ".rs.in", ".sql", ".cql", ".ddl",
    ".inc", ".prc", ".tab", ".udf", ".viw",
    ".sh", ".bash", ".bats", ".cgi", ".command",
    ".fcgi", ".ksh", ".sh.in", ".tmux", ".tool",
    ".zsh", ".swift", ".tcl", ".adp", ".tm",
    ".fr", ".nb", ".ncl", ".no", ".ts",
    ".tsx", ".xml", ".ant", ".axml", ".ccxml",
    ".clixml", ".cproject", ".csl", ".csproj", ".ct",
    ".dita", ".ditamap", ".ditaval", ".dll.config", ".dotsettings",
    ".filters", ".fsproj", ".fxml", ".glade", ".gml",
    ".grxml", ".iml", ".ivy", ".jelly", ".jsproj",
    ".kml", ".launch", ".mdpolicy", ".mm", ".mod",
    ".mxml", ".nproj", ".nuspec", ".odd", ".osm",
    ".plist", ".pluginspec", ".props", ".ps1xml", ".psc1",
    ".pt", ".rdf", ".rss", ".scxml", ".srdf",
    ".storyboard", ".stTheme", ".sublime-snippet", ".targets", ".tmCommand",
    ".tml", ".tmLanguage", ".tmPreferences", ".tmSnippet", ".tmTheme",
    ".ts", ".tsx", ".ui", ".urdf", ".ux",
    ".vbproj", ".vcxproj", ".vssettings", ".vxml", ".wsdl",
    ".wsf", ".wxi", ".wxl", ".wxs", ".x3d",
    ".xacro", ".xaml", ".xib", ".xlf", ".xliff",
    ".xmi", ".xml.dist", ".xproj", ".xsd",
    ".xul", ".zcml"
)


class LineCounter:

    def __init__(self):
        cwd = Path.cwd()
        self.dirs = list()
        self.count_current_directory = True
        self.count_lines_current_file(cwd)
        self.iter_dirs(cwd)
        self.print_report()

    def count_lines_current_file(self, directory):
        """Count the lines from the files of the currect directory.

        Do not count the lines from the currect file."""
        files = self.iter_files(directory)
        self.dirs.append({directory.name: files})

    def iter_dirs(self, directory):
        """Iter through all dirs.
        
        Add the dir names into a list so that they can be displayed
        at the end of the program. Call the function self.iter_files()
        so that the program will count all the lines from this dir.
        """
        for d in directory.iterdir():
            if d.is_dir():
                files = self.iter_files(d)
                self.dirs.append({d.name: files})
                self.iter_dirs(d)

    def iter_files(self, directory):
        """Iter through all files from a dir and count their lines using 
        the self.count_lines() function.
        
        Return a list containing dictionaries that you got from 
        self.count_lines_(). There will be a new dictionary for each file. 
        The key is the name of the file, and the value is the number of 
        lines of the file.
        """
        files_list = list()

        for f in directory.iterdir():
            if f.is_file():
                if (self.count_current_directory and 
                        f.name == "line-counter.py"): 
                    continue
                
                if f.suffix in ALLOWED:
                    dictionary = self.count_lines(f)
                    files_list.append(dictionary)
                else:
                    continue

        self.count_current_directory = False
        return files_list

    def count_lines(self, file):
        """Count lines from a file.
        
        Check if the file is empty or not. Return a dictionary containing 
        the name of the file as the key and the number of lines as the 
        value.
        """
        name = file.name
        with open(f"{file}", 'r') as f:
            try:
                file_is_empty = not f.readlines()
                f.seek(0)

                # line_count receives the length of the whole file
                line_count = len(f.readlines())
                f.seek(0)
                
                if not file_is_empty:
                    # check if there is a new line at the end of file
                    new_line_eof = f.readlines()[-1][-1:] == '\n'
                    if new_line_eof: line_count += 1
            except:
                name += " ERROR"
                line_count = 0
            

        return {name: line_count}

    def print_report(self):
        """Print a final report to the user.

        Iter through self.dirs and present a user friendly representation 
        of the directories, files and amount of lines of each file, as 
        well as the amount of lines of the whole project.
        """
        total_lines = 0
        for item in self.dirs:
            total_lines_dir = 0
            for key, value in item.items():
                print(f"Directory: {key}")
                print("Files:")
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

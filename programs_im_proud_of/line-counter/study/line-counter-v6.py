"""
Add a tuple with all the file extensions that the program will
read from.

The program should read the name of the file, check if its
extension is in the tuple of files that are allowed to be read 
and if it is, read it. If it is not, jump to the next file.

Check the tuple on another file to see if everyting is written
correctly.
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
                if f.suffix in ALLOWED:
                    dictionary = self.count_lines(f)
                    files_list.append(dictionary)
                else:
                    continue

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

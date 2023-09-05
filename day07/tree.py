class File:

    def __init__(self, size, name):
        self.size = size
        self.name = name


class Directory:

    def __init__(self, name: str):
        self.name = name
        self.full_path: list[str] = []
        self.parent = None
        self.directories: list[Directory] = []
        self.files: list[File] = []

    def add_directory(self, directory: "Directory"):
        if directory.name not in [d.name for d in self.directories]:
            self.directories.append(directory)

    def add_file(self, file: File):
        if file.name not in [f.name for f in self.files]:
            self.files.append(file)


class Filesystem:
    def __init__(self):
        root_directory = Directory("/")
        root_directory.full_path = ["/"]
        self.root = root_directory
        self.current = self.root

    def get_root(self):
        return self.root

    def cd_into(self, directory_name):
        self.current = next(directory for directory in self.current.directories if directory.name == directory_name)

    def cd_out(self):
        self.current = self.current.parent

    def cd_to_root(self):
        self.current = self.root

    def add_directory(self, directory_name):
        directory = Directory(directory_name)
        directory.parent = self.current
        full_path = self.current.full_path.copy()
        full_path.append(directory_name)
        directory.full_path = full_path
        self.current.add_directory(directory)

    def add_file(self, file_size, file_name):
        file = File(file_size, file_name)
        self.current.add_file(file)

    def print(self):
        self._print(self.root, 0)

    def _print(self, node: Directory, level):
        print('\t' * level + "dir " + node.name)
        for file in node.files:
            print('\t' * (level + 1) + file.size + " " + file.name)
        for directory in node.directories:
            self._print(directory, level + 1)

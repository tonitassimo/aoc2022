class File:

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:

    def __init__(self, path: str):
        self.path = path
        self.directories: list[Directory] = []
        self.files: list[File] = []

    def add_directory(self, directory):
        self.directories = self.directories.append(directory)

    def add_files(self, files):
        self.files = self.files.append(files)

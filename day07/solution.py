from day07.tree import Filesystem

filesystem = Filesystem()


def solve():
    puzzle_input = open("day07/data.txt", "r").readlines()
    for line in puzzle_input:
        line = line[:-1]
        process_line(line)
    total_size = calculate()
    print(total_size)


def process_line(line):
    if line.startswith("$"):
        command = line[2:]
        handle_command(command)
    else:
        handle_result(line)


def handle_command(command):
    if command.startswith("cd"):
        path = command.split()[1]
        handle_cd(path)


def handle_cd(directory_name):
    if directory_name == "..":
        filesystem.cd_out()
    elif directory_name == "/":
        filesystem.cd_to_root()
    else:
        filesystem.cd_into(directory_name)


def handle_result(result):
    if result.startswith("dir"):
        directory_name = result.split()[1]
        filesystem.add_directory(directory_name)
    else:
        [file_size, file_name] = result.split()
        filesystem.add_file(file_size, file_name)


def calculate():
    filesystem.root.calculate_size()
    directories = filesystem.get_directories()
    result = [(directory.name, directory.size) for directory in directories if directory.size <= 100000]
    total_size = sum([t[1] for t in result], 0)
    return total_size

from day07.tree import Filesystem

filesystem = Filesystem()


def solve():
    puzzle_input = open("day07/data.txt", "r").readlines()
    for line in puzzle_input:
        line = line[:-1]
        process_line(line)
    filesystem.print()


def process_line(line: str):
    if line.startswith("$"):
        handle_command(line[2:])
    else:
        handle_result(line)


def handle_command(command: str):
    if command.startswith("cd"):
        path = command.split()[1]
        handle_cd(path)


def handle_cd(directory_name: str):
    if directory_name == "..":
        filesystem.cd_out()
    elif directory_name == "/":
        filesystem.cd_to_root()
    else:
        filesystem.cd_into(directory_name)


def handle_result(result: str):
    if result.startswith("dir"):
        directory_name = result.split()[1]
        filesystem.add_directory(directory_name)

def solve():
    puzzle_input = open("day07/data.txt", "r").readlines()
    for line in puzzle_input:
        process_line(line)


def process_line(line: str):
    if line.startswith("$"):
        handle_command(line[2:])
    else:
        handle_result(line)


def handle_command(command: str):
    if command.startswith("cd"):
        handle_cd(command[4:])
    elif command.startswith("ls"):
        handle_ls()


def handle_cd(directory: str):
    None

def handle_ls():
    None

def handle_result(result: str):
    print(result)

from day25.converter import snafu_to_decimal

def solve():
    puzzle = open("day25/test.txt", "r").readlines()
    for line in puzzle:
        line = line[:-1]
        print(line + " -> " + str(snafu_to_decimal(line)))

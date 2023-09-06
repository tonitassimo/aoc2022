from day08.matrix import Matrix


def solve():
    puzzle = open("day08/test.txt", "r").readlines()
    matrix = Matrix(5, 5)
    matrix.from_string(puzzle)
    matrix.print()

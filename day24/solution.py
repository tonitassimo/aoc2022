from day24.field import Field


def solve():
    puzzle = open("day24/test.txt", "r").readlines()
    field = Field(7, 7)
    field.from_string(puzzle)
    field.print()

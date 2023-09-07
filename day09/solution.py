from day09.rope import Parser


def solve():
    puzzle = open("day09/data.txt", "r").readlines()
    parser = Parser()
    parser.parse(puzzle)
    result = parser.get_result()
    print(result)

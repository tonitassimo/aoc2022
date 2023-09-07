from day08.matrix import Matrix, TreeGrid


def solve():
    puzzle = open("day08/data.txt", "r").readlines()
    matrix = Matrix(99, 99)
    matrix.from_string(puzzle)
    tree_grid = TreeGrid(matrix)
    tree_grid.walk_grid()
    count = tree_grid.get_visible_tree_count()
    print(count)

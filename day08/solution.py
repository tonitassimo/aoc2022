from day08.matrix import Matrix, TreeGrid, Position, Tree


def solve():
    puzzle = open("day08/test.txt", "r").readlines()
    matrix = Matrix(5, 5)
    matrix.from_string(puzzle)
    matrix.print()

    tree_grid = TreeGrid(matrix)
    print(matrix.get_tree_at(Position(2, 2)))
    result = tree_grid.is_tree_visible(Tree(Position(2, 2), 3))
    print(result)

    count = tree_grid.count_visible_trees()
    print(count)

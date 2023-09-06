class Position:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Matrix:

    def __init__(self, x_length, y_length):
        self._x_length = x_length
        self._y_length = y_length
        self.fields = [[Tree(Position(x, y), 0) for x in range(x_length)] for y in range(y_length)]

    def from_string(self, puzzle):
        x, y = 0, 0
        for line in puzzle:
            line = line[:-1]
            for digit in line:
                self.fields[y][x] = Tree(Position(x, y), int(digit))
                x += 1
            x = 0
            y += 1

    def print(self):
        for row in self.fields:
            row_to_print = ""
            for value in row:
                row_to_print += "  " + str(value)
            print(row_to_print)

    def get_dimensions(self):
        return self._x_length, self._y_length

    def get_tree_at(self, position: Position):
        return self.fields[position.y][position.x]


class Tree:

    def __init__(self, position, value):
        self.visible = False
        self.value = value
        self.position = position
        self._visited = False

    def visit(self):
        self._visited = True

    def __str__(self):
        return str(self.value)


class TreeGrid:

    def __init__(self, matrix: Matrix):
        self._matrix = matrix
        self._x_length, self._y_length = self._matrix.get_dimensions()

    def _visible_from_left(self, tree: Tree):
        if tree.position.x == 0:
            return True
        left_neighbour = self._matrix.get_tree_at(Position(tree.position.x - 1, tree.position.y))
        return self._visible_from_left(left_neighbour) and tree.value > left_neighbour.value

    def _visible_from_right(self, tree: Tree):
        if tree.position.x == self._x_length - 1:
            return True
        right_neighbour = self._matrix.get_tree_at(Position(tree.position.x + 1, tree.position.y))
        return self._visible_from_right(right_neighbour) and tree.value > right_neighbour.value

    def _visible_from_above(self, tree: Tree):
        if tree.position.y == 0:
            return True
        above_neighbour = self._matrix.get_tree_at(Position(tree.position.x, tree.position.y - 1))
        return self._visible_from_above(above_neighbour) and tree.value > above_neighbour.value

    def _visible_from_below(self, tree: Tree):
        if tree.position.y == self._y_length - 1:
            return True
        below_neighbour = self._matrix.get_tree_at(Position(tree.position.x, tree.position.y + 1))
        return self._visible_from_below(below_neighbour) and tree.value > below_neighbour.value

    # todo: tree.value needs to be greater than max of neighbours in a row -> keep track of the current maximum
    def is_tree_visible(self, tree: Tree) -> bool:
        result = self._visible_from_left(tree) or self._visible_from_right(tree) or self._visible_from_above(
            tree) or self._visible_from_below(tree)
        tree.visible = result
        return result

    def count_visible_trees(self):
        visible_trees = 0
        for row in self._matrix.fields:
            for tree in row:
                if self.is_tree_visible(tree):
                    visible_trees += 1
        return visible_trees

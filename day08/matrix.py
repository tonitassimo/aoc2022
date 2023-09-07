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

    def get_upper_row(self):
        return self.fields[0]

    def get_lower_row(self):
        return self.fields[self._y_length - 1]

    def get_left_column(self):
        return [self.get_tree_at(Position(0, y)) for y in range(self._y_length)]

    def get_right_column(self):
        return [self.get_tree_at(Position(self._x_length - 1, y)) for y in range(self._y_length)]


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

    def get_visible_tree_count(self):
        visible_trees = 0
        for row in self._matrix.fields:
            for tree in row:
                if tree.visible:
                    visible_trees += 1
        return visible_trees

    def walk_grid(self):
        left_edge_with_func = (self._matrix.get_left_column(), self._walk_right)
        right_edge_with_func = (self._matrix.get_right_column(), self._walk_left)
        upper_edge_with_func = (self._matrix.get_upper_row(), self._walk_down)
        lower_edge_with_func = (self._matrix.get_lower_row(), self._walk_up)

        for direction_tuple in [left_edge_with_func, right_edge_with_func, upper_edge_with_func, lower_edge_with_func]:
            for tree in direction_tuple[0]:
                direction_tuple[1](tree)

    def _walk_right(self, tree: Tree, current_max=-1):
        self._walk(tree, tree.position.x < self._x_length - 1, self._walk_right,
                   Position(tree.position.x + 1, tree.position.y), current_max)

    def _walk_left(self, tree: Tree, current_max=-1):
        self._walk(tree, tree.position.x > 0, self._walk_left, Position(tree.position.x - 1, tree.position.y),
                   current_max)

    def _walk_up(self, tree: Tree, current_max=-1):
        self._walk(tree, tree.position.y > 0, self._walk_up, Position(tree.position.x, tree.position.y - 1),
                   current_max)

    def _walk_down(self, tree: Tree, current_max=-1):
        self._walk(tree, tree.position.y < self._y_length - 1, self._walk_down,
                   Position(tree.position.x, tree.position.y + 1), current_max)

    def _walk(self, tree: Tree, condition, next_step, next_position, current_max):
        if tree.value > current_max:
            current_max = tree.value
            tree.visible = True
        if condition:
            next_tree = self._matrix.get_tree_at(next_position)
            next_step(next_tree, current_max)

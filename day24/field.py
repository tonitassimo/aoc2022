class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + self.x + " y: " + self.y


class Field:

    def __init__(self, x_length, y_length):
        self._x_length = x_length
        self._y_length = y_length
        self._fields = [[0 for _ in range(x_length)] for _ in range(y_length)]
        self._blizzards = []
        self._edges = []

    def from_string(self, puzzle):
        x, y = 0, 0
        for line in puzzle:
            line = line[:-1]
            for value in line:
                if value == "#":
                    self._edges.append(Position(x, y))
                if value == "<" or ">" or "v" or "^":
                    self._blizzards.append(Position(x, y))
                self._fields[y][x] = value
                x += 1
            x = 0
            y += 1

    def print(self):
        for row in self._fields:
            row_to_print = ""
            for value in row:
                row_to_print += "  " + str(value)
            print(row_to_print)

class Matrix:

    def __init__(self, x_length, y_length):
        self._x_length = x_length
        self._y_length = y_length
        self._fields = [[0 for _ in range(x_length)] for _ in range(y_length)]
        self._current_x = 0
        self._current_y = 0

    def set_current_field(self, x, y):
        self._current_x = x
        self._current_y = y

    def _set_field_value(self, x, y, value):
        self._fields[y][x] = value

    def _reset_position(self):
        self.set_current_field(0, 0)

    def from_string(self, puzzle):
        self._reset_position()
        for line in puzzle:
            line = line[:-1]
            for digit in line:
                self._set_field_value(self._current_x, self._current_y, digit)
                self._current_x += 1
            self._current_x = 0
            self._current_y += 1
        self._reset_position()

    def print(self):
        for row in self._fields:
            row_to_print = ""
            for value in row:
                row_to_print += "  " + str(value)
            print(row_to_print)

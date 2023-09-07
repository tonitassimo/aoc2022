import copy


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other: "Position"):
        return self.x == other.x and self.y == other.y

    def is_adjacent(self, other: "Position"):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1


class Rope:

    def __init__(self):
        self._head = Position(0, 0)
        self._head_last_position = Position(0, 0)
        self._tail = Position(0, 0)
        self._visited_by_tail = [Position(0, 0)]

    def get_visited_fields(self):
        return self._visited_by_tail

    def _increase_head_x(self):
        self._head.x += 1

    def _decrease_head_x(self):
        self._head.x -= 1

    def _increase_head_y(self):
        self._head.y += 1

    def _decrease_head_y(self):
        self._head.y -= 1

    def _move(self, steps, execute_step):
        for _ in range(steps):
            self._head_last_position = copy.copy(self._head)
            execute_step()
            if not self._head.is_adjacent(self._tail):
                self._tail = self._head_last_position
                self._add_visited_field(self._tail)

    def _add_visited_field(self, position: Position):
        if position not in self._visited_by_tail:
            self._visited_by_tail.append(self._tail)

    def move_right(self, steps):
        self._move(steps, self._increase_head_x)

    def move_left(self, steps):
        self._move(steps, self._decrease_head_x)

    def move_up(self, steps):
        self._move(steps, self._decrease_head_y)

    def move_down(self, steps):
        self._move(steps, self._increase_head_y)


class Parser:

    def __init__(self):
        self._rope = Rope()

    def get_result(self):
        return len(self._rope.get_visited_fields())

    def parse(self, puzzle):
        for line in puzzle:
            line = line[:-1]
            self._parse_line(line)

    def _parse_line(self, line):
        (direction, steps) = line.split()
        steps = int(steps)
        if direction == "R":
            self._rope.move_right(steps)
        elif direction == "L":
            self._rope.move_left(steps)
        elif direction == "U":
            self._rope.move_up(steps)
        elif direction == "D":
            self._rope.move_down(steps)

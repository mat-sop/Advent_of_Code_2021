import sys
from typing import List, Tuple


class VentLine:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_coords_between(self) -> List[Tuple[int, int]]:
        coords = []
        if self.x1 == self.x2:
            coords.append((self.x2, self.y2))
            step = -1 if self.y1 > self.y2 else 1
            coords.extend([(self.x1, i) for i in range(self.y1, self.y2, step)])
        elif self.y1 == self.y2:
            coords.append((self.x2, self.y2))
            step = -1 if self.x1 > self.x2 else 1
            coords.extend([(i, self.y1) for i in range(self.x1, self.x2, step)])
        else:
            x_step = step = -1 if self.x1 > self.x2 else 1
            y_step = -1 if self.y1 > self.y2 else 1
            coords.append((self.x1, self.y1))
            for i in range((self.x1 - self.x2) * -1 * x_step):
                coords.append(
                    (self.x1 + (x_step * (i + 1)), self.y1 + (y_step * (i + 1)))
                )
        return coords

    def __repr__(self) -> str:
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"


class OceanFloor:
    def __init__(self, vent_lines: List[VentLine], size=10) -> None:
        self.size = size
        self.vent_lines = vent_lines

    def count_dangerous_points(self, treshold=2):
        floor = [[0] * self.size for _ in range(self.size)]

        for vent_line in self.vent_lines:
            if vent_line.x1 == vent_line.x2 or vent_line.y1 == vent_line.y2:
                for (x, y) in vent_line.get_coords_between():
                    floor[x][y] += 1

        return sum([len([v for v in row if v >= treshold]) for row in floor])

    def count_all_dangerous_points(self, treshold=2):
        floor = [[0] * self.size for _ in range(self.size)]

        for vent_line in self.vent_lines:
            for (x, y) in vent_line.get_coords_between():
                floor[x][y] += 1

        return sum([len([v for v in row if v >= treshold]) for row in floor])


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    vent_lines = []
    with open(file_path, "r") as f:
        while line := f.readline():
            cord1, cord2 = line.split(" -> ")
            x1, y1 = map(int, cord1.split(","))
            x2, y2 = map(int, cord2.split(","))
            vent_lines.append(VentLine(x1, y1, x2, y2))

    floor = OceanFloor(vent_lines, 1000)

    print("### part1")
    print(floor.count_dangerous_points())

    print("### part2")
    print(floor.count_all_dangerous_points())

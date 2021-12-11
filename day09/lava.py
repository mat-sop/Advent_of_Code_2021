import sys
from pprint import pprint
from typing import List, Tuple
import math

def _get_neighbours(row: int, col: int, heightmap: List[List[int]]) -> List[int]:
    neighbours = []
    if row == 0:
        neighbours.append(heightmap[row + 1][col])
    elif row == len(heightmap) - 1:
        neighbours.append(heightmap[row - 1][col])
    else:
        neighbours.append(heightmap[row + 1][col])
        neighbours.append(heightmap[row - 1][col])

    if col == 0:
        neighbours.append(heightmap[row][col + 1])
    elif col == len(heightmap[0]) - 1:
        neighbours.append(heightmap[row][col - 1])
    else:
        neighbours.append(heightmap[row][col + 1])
        neighbours.append(heightmap[row][col - 1])

    return neighbours


def get_low_points(heightmap: List[List[int]]) -> List[int]:
    low_points = []

    for row, line in enumerate(heightmap):
        for col, value in enumerate(line):
            if value < min(_get_neighbours(row, col, heightmap)):
                low_points.append(value)

    return low_points


def count_risk_level(low_points: List[int]) -> int:
    return sum(low_points) + len(low_points)


def get_low_points_coords(heightmap: List[List[int]]) -> List[Tuple[int, int]]:
    low_points_coords = []

    for row, line in enumerate(heightmap):
        for col, value in enumerate(line):
            if value < min(_get_neighbours(row, col, heightmap)):
                low_points_coords.append((row, col))

    return low_points_coords


def _get_neighbours_coords(row: int, col: int, heightmap: List[List[int]]) -> List[Tuple[int, int]]:
    neighbours = []
    if row == 0:
        neighbours.append((row + 1,col))
    elif row == len(heightmap) - 1:
        neighbours.append((row - 1,col))
    else:
        neighbours.append((row + 1,col))
        neighbours.append((row - 1,col))

    if col == 0:
        neighbours.append((row,col + 1))
    elif col == len(heightmap[0]) - 1:
        neighbours.append((row,col - 1))
    else:
        neighbours.append((row,col + 1))
        neighbours.append((row,col - 1))

    return neighbours


def _mark_heigher_neighbours(row, col, heightmap: List[List[int]], visited: List[List[bool]]) -> List[List[bool]]:
    if heightmap[row][col] == 9:
        return visited

    visited[row][col] = True
    for n_row, n_col in _get_neighbours_coords(row, col, heightmap):
        if heightmap[n_row][n_col] > heightmap[row][col] and heightmap[n_row][n_col] != 9:
            visited = _mark_heigher_neighbours(n_row, n_col, heightmap, visited)

    return visited


def get_basins_sizes(heightmap: List[List[int]]) -> List[int]:
    basin_sizes = []

    for row, col in get_low_points_coords(heightmap):
        visited = [[False] * len(line) for line in heightmap]
        visited = _mark_heigher_neighbours(row, col, heightmap, visited)
        basin_sizes.append(sum([sum([int(v) for v in line]) for line in visited]))

    return basin_sizes


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    heightmap = []
    with open(file_path, "r") as f:
        heightmap = [list(map(int, line.strip())) for line in f.readlines()]

    print("### part1")
    print(count_risk_level(get_low_points(heightmap)))

    print("### part2")
    print(math.prod(sorted(get_basins_sizes(heightmap))[-3:]))

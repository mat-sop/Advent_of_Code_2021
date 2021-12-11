import sys
from pprint import pprint
from typing import List, Tuple


def get_adjacent_coords(
    x: int, y: int, max_x: int, max_y: int
) -> List[Tuple[int, int]]:
    coords = []
    if x == 0 and y == 0:
        return [(0, 1), (1, 0), (1, 1)]
    elif x == 0 and y == max_y:
        return [(0, max_y - 1), (1, max_y - 1), (1, max_y)]
    elif x == max_x and y == 0:
        return [(max_x - 1, 0), (max_x - 1, 1), (max_x, 1)]
    elif x == max_x and y == max_y:
        return [(max_x, max_y - 1), (max_x - 1, max_y), (max_x - 1, max_y - 1)]
    elif x == 0:
        return [(0, y - 1), (0, y + 1), (1, y - 1), (1, y), (1, y + 1)]
    elif y == 0:
        return [(x - 1, 0), (x + 1, 0), (x - 1, 1), (x, 1), (x + 1, 1)]
    elif x == max_x:
        return [
            (max_x, y - 1),
            (max_x, y + 1),
            (max_x - 1, y - 1),
            (max_x - 1, y),
            (max_x - 1, y + 1),
        ]
    elif y == max_y:
        return [
            (x - 1, max_y),
            (x + 1, max_y),
            (x - 1, max_y - 1),
            (x, max_y - 1),
            (x + 1, max_y - 1),
        ]
    else:
        return [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]


def step(octopuses: List[List[int]]) -> Tuple[List[List[int]], int]:
    flashed_coords = []
    updated_octopuses = [[i + 1 for i in line] for line in octopuses]

    for x, row in enumerate(updated_octopuses):
        for y, energy in enumerate(row):
            # print(f"x: {x}, y: {y}, energy: {energy}")
            if energy > 9:
                flashed_coords.append((x, y))


    for x, y in flashed_coords:
        for n_x, n_y in get_adjacent_coords(
            x, y, len(updated_octopuses) - 1, len(updated_octopuses[0]) - 1
        ):
            # print(f"x: {x} y: {y} n_x: {n_x} n_y: {n_y}")
            updated_octopuses[n_x][n_y] += 1
            if updated_octopuses[n_x][n_y] > 9 and (n_x, n_y) not in flashed_coords:
                flashed_coords.append((n_x, n_y))

    for x, row in enumerate(updated_octopuses):
        for y, energy in enumerate(row):
            if updated_octopuses[x][y] > 9:
                updated_octopuses[x][y] = 0

    return updated_octopuses, len(flashed_coords)


def count_flashes(octopuses: List[List[int]], steps: int) -> int:
    sum_ = 0
    for _ in range(steps):
        octopuses, flashes = step(octopuses)
        sum_ += flashes

    return sum_


def find_synchronization_step(octopuses: List[List[int]]) -> int:
    octopuses_count = sum([len(line) for line in octopuses])
    step_counter = 1
    octopuses, flashes = step(octopuses)
    while flashes != octopuses_count:
        octopuses, flashes = step(octopuses)
        step_counter += 1

    return step_counter


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    octopuses = []
    with open(file_path, "r") as f:
        while line := f.readline().strip():
            octopuses.append(list(map(int, line)))

    print("### part1")
    print(count_flashes(octopuses, 100))

    print("### part2")
    print(find_synchronization_step(octopuses))

import sys
from typing import List


def calculate_fuel_cost(crabs: List[int], destinated_position: int) -> int:
    return sum([abs(destinated_position - crab) for crab in crabs])


def get_optimal_position(crabs: List[int]) -> int:
    return sorted(crabs)[len(crabs) // 2]


def calculate_fuel_cost_v2(crabs: List[int], destinated_position: int) -> int:
    return int(sum([diff * (diff+1) / 2 for diff in [abs(destinated_position - crab) for crab in crabs]]))


def get_optimal_position_v2(crabs: List[int]) -> int:
    return round(sum(crabs)/len(crabs))


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        crabs = list(map(int, f.readline().split(",")))

    print("### part1")
    print(calculate_fuel_cost(crabs, get_optimal_position(crabs)))

    print("### part2")
    fuels = []
    for i in range(min(crabs), max(crabs)):
        fuels.append(calculate_fuel_cost_v2(crabs, i))

    print(min(fuels))
    print(fuels.index(min(fuels)))

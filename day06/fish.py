import sys
from typing import List, Optional


def simulate_fishes(
    fishes: List[int],
    days: Optional[int] = 80,
    fish_reset_counter: Optional[int] = 6,
    new_fish_counter: Optional[int] = 8,
) -> int:
    prev_fishes = fishes.copy()

    for i in range(days):
        new_fishes = []
        for fish in prev_fishes:
            if fish > 0:
                new_fishes.append(fish - 1)
            else:
                new_fishes.append(fish_reset_counter)
                new_fishes.append(new_fish_counter)
        prev_fishes = new_fishes

    return(len(prev_fishes))


def simulate_fishes_refactored(
    fishes: List[int],
    days: Optional[int] = 80
) -> int:
    counters = [0] * 10
    for fish in fishes:
        counters[fish] += 1

    for i in range(days):
        new_counters = [0] * 10
        for i in range(9):
            new_counters[i] = counters[i+1]
        new_counters[6] += counters[0]
        new_counters[8] = counters[0]

        counters = new_counters

    return(sum(counters))

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        fishes = list(map(int, f.readline().split(",")))

    print("### part1")
    print(simulate_fishes(fishes, 80))

    print("### part2")
    print(simulate_fishes_refactored(fishes, 256))

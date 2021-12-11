import sys
from typing import List, Optional


def count_increases(measurements: List[int]) -> int:
    increases_counter = 0
    for i in range(len(measurements)-1):
        if measurements[i] < measurements[i+1]:
            increases_counter += 1
    return increases_counter


def count_sliding_windows_sums(measurements: List[int], window_size: Optional[int] = 3) -> List[int]:
    result_list = []
    for i in range(len(measurements)-(window_size-1)):
        result_list.append(sum(measurements[i:i+window_size]))
    return result_list


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        measurements = list(map(int, f.readlines()))

    print("### part 1")
    increases = count_increases(measurements)
    print(increases)

    print("### part 2")
    sliding_windows_sums = count_sliding_windows_sums(measurements)
    sliding_windows_increases = count_increases(sliding_windows_sums)
    print(sliding_windows_increases)

import sys
from typing import List, Tuple


def calculate_gamma_and_epsilon_rate(report_numbers: List[str]) -> Tuple[int, int]:
    counters = [0] * len(max(report_numbers, key=len))

    for number in report_numbers:
        for (i, sign) in enumerate(number):
            if int(sign) == 0:
                counters[i] -= 1
            else:
                counters[i] += 1

    gamma_rate = ""
    epsilon_rate = ""
    for counter in counters:
        if counter > 0:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return int(gamma_rate, base=2), int(epsilon_rate, base=2)


def _get_most_common_bit(report_numbers: List[str], index: int) -> str:
    values = [number[index] for number in report_numbers]
    return "1" if values.count("1") >= values.count("0") else "0"


def _get_least_common_bit(report_numbers: List[str], index: int) -> str:
    return "1" if _get_most_common_bit(report_numbers, index) == "0" else "0"


def _filter_by_bit(report_numbers: List[str], index: int, value: str) -> List[str]:
    return [number for number in report_numbers if number[index] == value]


def find_oxygen_generator_rating(report_numbers: List[str]) -> int:
    numbers = report_numbers.copy()
    i = 0
    while len(numbers) > 1:
        numbers = _filter_by_bit(numbers, i, _get_most_common_bit(numbers, i))
        i += 1

    return int(numbers[0], base=2)


def find_CO2_scrubber_rating(report_numbers: List[str]) -> int:
    numbers = report_numbers.copy()
    i = 0
    while len(numbers) > 1:
        numbers = _filter_by_bit(numbers, i, _get_least_common_bit(numbers, i))
        i += 1

    return int(numbers[0], base=2)


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        report_numbers = f.read().splitlines()

    print("### part1")
    gamma_rate, epsilon_rate = calculate_gamma_and_epsilon_rate(report_numbers)
    print(f"gamma rate: {gamma_rate}")
    print(f"epsilon rate: {epsilon_rate}")
    print(gamma_rate * epsilon_rate)

    print("### part2")
    oxygen_generator_rating = find_oxygen_generator_rating(report_numbers)
    CO2_scrubber_rating = find_CO2_scrubber_rating(report_numbers)
    print(f"oxygen generator rating: {oxygen_generator_rating}")
    print(f"CO2 scrubber rating: {CO2_scrubber_rating}")
    print(oxygen_generator_rating * CO2_scrubber_rating)

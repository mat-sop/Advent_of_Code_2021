import sys
from typing import Dict, List
from pprint import pp, pprint


def count_unique_lengths(outputs: List[List[str]]) -> int:
    sum_ = 0
    unique_lengths = [2, 3, 4, 7]

    for line in outputs:
        for code in line:
            if len(code) in unique_lengths:
                sum_ += 1

    return sum_


def _contains(s1: str, s2: str) -> bool:
    return set(s2).issubset(set(s1))


def find_mapping(signals: List[str], output: List[str]) -> int:
    """
    0:      1:      2:      3:      4:
    aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
    ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
    gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
    aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
    dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
    gggg    gggg    ....    gggg    gggg
    correct_mapping = {
        0: "abcefg",
        1: "cf",
        2: "2cdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }
    """

    mapping = {}

    possible_values = {2: [], 3: [], 5: [], 0: [], 6: [], 9: []}
    for value in signals + output:
        if len(value) == 2:
            mapping[1] = "".join(sorted(value))
        elif len(value) == 3:
            mapping[7] = "".join(sorted(value))
        elif len(value) == 4:
            mapping[4] = "".join(sorted(value))
        elif len(value) == 7:
            mapping[8] = "".join(sorted(value))

        elif len(value) == 5:
            possible_values[2].append("".join(sorted(value)))
            possible_values[3].append("".join(sorted(value)))
            possible_values[5].append("".join(sorted(value)))
        elif len(value) == 6:
            possible_values[0].append("".join(sorted(value)))
            possible_values[6].append("".join(sorted(value)))
            possible_values[9].append("".join(sorted(value)))


    """
    aaaa
    b    c
    b    c
    dddd
    .    f
    .    f
    ....
    """
    possible_values[9] = [v for v in possible_values[9] if _contains(v, mapping[4]) and _contains(v, mapping[7])]
    mapping[9] = possible_values[9][0]
    del possible_values[9]


    """
    ---- 5/6 ----
    aaaa
    b    .
    b    .
    dddd
    .    .
    .    .
    ....
    ....
    .    .
    .    .
    ....
    e    .
    e    .
    ....
    """
    part_56 = "".join(set.union(set(mapping[4]), set(mapping[7])) - set(mapping[1]))
    part_89 = "".join(set(mapping[8]) - set(mapping[9]))

    possible_values[5] = [v for v in possible_values[5] if _contains(v, part_56) and not _contains(v, part_89)]
    possible_values[6] = [v for v in possible_values[6] if _contains(v, part_56) and _contains(v, part_89)]
    mapping[5] = possible_values[5][0]
    mapping[6] = possible_values[6][0]
    del possible_values[5]
    del possible_values[6]



    for key, value in mapping.items():
        possible_values[0] = [v for v in possible_values[0] if v != value]

    mapping[0] = possible_values[0][0]
    del possible_values[0]



    """
    aaaa
    .    .
    .    .
    ....
    e    .
    e    .
    gggg
    """
    part_04 = "".join(set(mapping[0]) - set(mapping[4]))
    possible_values[2] = [v for v in possible_values[2] if _contains(v, part_04)]
    mapping[2] = possible_values[2][0]
    del possible_values[2]


    for key, value in mapping.items():
        possible_values[3] = [v for v in possible_values[3] if v != value]

    mapping[3] = possible_values[3][0]
    del possible_values[3]

    return mapping


def decode_ouput(output: List[str], mapping: Dict[int, str]) -> int:
    reversed_mapping = {value: key for key, value in mapping.items()}
    return int("".join([str(reversed_mapping["".join(sorted(value))]) for value in output]))

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    outputs = []
    lines = []
    with open(file_path, "r") as f:
        while line := f.readline().strip():
            signals, output = line.split(" | ")
            lines.append((signals.split(" "), output.split(" ")))
            outputs.append(output.split(" "))

    print("### part1")
    print(count_unique_lengths(outputs))

    print("### part2")
    sum_ = 0
    for (signals, output) in lines:
        mapping = find_mapping(signals, output)
        sum_ += decode_ouput(output, mapping)
    print(sum_)

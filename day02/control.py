import enum
from typing import List, Optional, Tuple
import sys

def count_horizontal_position_and_depth(
    commands: List[Tuple[str, int]],
    initial_horizontal_position: Optional[int] = 0,
    initial_depth: Optional[int] = 0,
) -> Tuple[int, int]:
    horizontal_position = initial_horizontal_position
    depth = initial_depth
    for (instruction, amount) in commands:
        if instruction == "forward":
            horizontal_position += amount
        elif instruction == "down":
            depth += amount
        elif instruction == "up":
            depth -= amount
    return horizontal_position, depth


def count_horizontal_position_and_depth_v2(
    commands: List[Tuple[str, int]],
    initial_horizontal_position: Optional[int] = 0,
    initial_depth: Optional[int] = 0,
    initial_aim: Optional[int] = 0,
) -> Tuple[int, int]:
    horizontal_position = initial_horizontal_position
    depth = initial_depth
    aim = initial_aim
    for (instruction, amount) in commands:
        if instruction == "forward":
            horizontal_position += amount
            depth += aim * amount
        elif instruction == "down":
            aim += amount
        elif instruction == "up":
            aim -= amount
    return horizontal_position, depth

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        commands = f.readlines()
        parsed_commands = []
        for command in commands:
            instruction, amount = command.split()
            parsed_commands.append((instruction, int(amount)))

    print("### part 1")
    horizontal_position, depth = count_horizontal_position_and_depth(parsed_commands)
    print(f"horizontal position: {horizontal_position}")
    print(f"depth: {depth}")
    print(horizontal_position * depth)

    print("### part 2")
    horizontal_position, depth = count_horizontal_position_and_depth_v2(parsed_commands)
    print(f"horizontal position: {horizontal_position}")
    print(f"depth: {depth}")
    print(horizontal_position * depth)

import sys
from pprint import pprint
from typing import Tuple
import math

def _get_packet_version_and_type_id(packet) -> Tuple[int, int]:
    return int(packet[:3], base=2), int(packet[3:6], base=2)


def count_value_packet_length(packet: str) -> int:
    b = packet[6]
    counter = 1
    while b != "0":
        b = packet[6 + counter * 5]
        counter += 1

    return counter * 5 + 6


def decode_version_sum(packet: str) -> int:
    if len(packet) < 8:
        return 0
    version, type_id = _get_packet_version_and_type_id(packet)
    version_sum = version
    if type_id == 4:
        version_sum += decode_version_sum(packet[count_value_packet_length(packet) :])
    else:
        next_bits = 15 if packet[6] == "0" else 11
        version_sum += decode_version_sum(packet[7 + next_bits :])
    return version_sum


def count_value_packet(packet: str) -> int:
    return int("".join([c for i, c in enumerate(packet[6:]) if i % 5 != 0]), base=2)

def decode_value(packet: str) -> int:
    if len(packet) < 8:
        return []
    version, type_id = _get_packet_version_and_type_id(packet)
    values = []
    rest = ""
    if type_id == 4:
        value_packet_length = count_value_packet_length(packet)
        values.append(count_value_packet(packet[:value_packet_length]))
        rest = packet[value_packet_length:]
    else:
        next_bits = 15 if packet[6] == "0" else 11
        subpackets = int(packet[7 : 7 + next_bits], base=2)
        values.extend(decode_value(packet[7 + next_bits :]))
        rest =

    print(f"packet: {packet}, type_id: {type_id}, values: {values}")

    if type_id == 0:
        return [sum(values)]
    elif type_id == 1:
        return [math.prod(values)]
    elif type_id == 2:
        return [min(values)]
    elif type_id == 3:
        return [max(values)]
    elif type_id == 4:
        values.extend(decode_value())
        return values
    elif type_id == 5:
        return [int(values[0] > values[1])]
    elif type_id == 6:
        return [int(values[0] < values[1])]
    elif type_id == 7:
        return [int(values[0] == values[1])]


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        packet = "".join(f"{int(x, 16):04b}" for x in f.readline().strip())

    print("### part1")
    print(decode_version_sum(packet))

    print("### part2")
    print(decode_value(packet))

import sys
from typing import List, Optional

CORRUPTED_SCORING = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    }

INCOMPLETE_SCORING = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

BRACKETS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def find_first_illegal_character(line: str) -> Optional[str]:
    opening_brackets = []
    for c in line:
        if c in BRACKETS.keys():
            opening_brackets.append(c)
        else:
            if BRACKETS[opening_brackets[-1]] == c:
                opening_brackets.pop()
            else:
                return c


def find_first_illegal_characters(lines: List[str]) -> List[str]:
    illegal_characters = []
    for line in lines:
        illegal_character = find_first_illegal_character(line)
        if illegal_character:
            illegal_characters.append(illegal_character)

    return illegal_characters


def find_missing_characters(line: str) -> Optional[str]:
    opening_brackets = []
    for c in line:
        if c in BRACKETS.keys():
            opening_brackets.append(c)
        else:
            if BRACKETS[opening_brackets[-1]] == c:
                opening_brackets.pop()
            else:
                break
    return "".join([BRACKETS[c] for c in reversed(opening_brackets)])


def find_missing_characters_in_not_corrupted_lines(lines: List[str]) -> List[str]:
    not_corrupted_lines = [line for line in lines if not find_first_illegal_character(line)]
    return [find_missing_characters(line) for line in not_corrupted_lines]


def count_incomplete_scores(missing_strings: List[str]) -> List[int]:
    scores = []
    for missing_string in missing_strings:
        score = 0
        for c in missing_string:
            score *= 5
            score += INCOMPLETE_SCORING[c]
        scores.append(score)
    return scores


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    lines = []
    with open(file_path, "r") as f:
         lines = [line.strip() for line in f.readlines()]

    print("### part1")
    print(sum([CORRUPTED_SCORING.get(c, 0) for c in find_first_illegal_characters(lines)]))

    print("### part2")
    scores = count_incomplete_scores(find_missing_characters_in_not_corrupted_lines(lines))
    print(sorted(scores)[len(scores)//2])

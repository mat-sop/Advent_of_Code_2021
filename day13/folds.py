import sys
from dataclasses import dataclass
from typing import List
from pprint import pprint


@dataclass
class Dot:
    x: int
    y: int


@dataclass
class Fold:
    axis: str
    line_nr: int


def create_paper_sheet(dots: List[Dot]) -> List[List[bool]]:
    max_x = max(dots, key=lambda dot: dot.x).x
    max_y = max(dots, key=lambda dot: dot.y).y

    sheet = [[False] * (max_x + 1) for _ in range((max_y + 1))]

    for dot in dots:
        sheet[dot.y][dot.x] = True

    return sheet


def fold(sheet: List[List[bool]], fold: Fold) -> List[List[bool]]:
    if fold.axis == "y":
        return [
            [a or b for a, b in zip(line1, line2)]
            for line1, line2 in zip(
                sheet[: fold.line_nr], reversed(sheet[fold.line_nr :])
            )
        ]
    if fold.axis == "x":
        return [
            [
                a or b
                for a, b in zip(line[: fold.line_nr], reversed(line[fold.line_nr :]))
            ]
            for line in sheet
        ]


def count_dots(sheet: List[List[bool]]) -> int:
    return sum([sum(line) for line in sheet])


def display_sheet(sheet: List[List[bool]]):
    for line in sheet:
        print("".join(["#" if col else "." for col in line]))


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    dots = []
    folds = []
    with open(file_path, "r") as f:
        while line := f.readline().strip():
            x, y = map(int, line.split(","))
            dots.append(Dot(x, y))

        while line := f.readline().strip():
            axis, line_nr = line.split(" ")[-1].split("=")
            folds.append(Fold(axis, int(line_nr)))

    sheet = create_paper_sheet(dots)

    print("### part1")
    folded_sheet = fold(sheet, folds[0])
    print(count_dots(folded_sheet))

    print("### part2")
    folded_sheet = sheet
    for f in folds:
        folded_sheet = fold(folded_sheet, f)
    display_sheet(folded_sheet)

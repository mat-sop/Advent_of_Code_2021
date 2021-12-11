import sys
from typing import List


class Board:
    def __init__(self, rows: List[List[int]]) -> None:
        self.rows = rows
        self._seen_numbers = []
        for row in self.rows:
            self._seen_numbers.append([False] * len(row))
        self._last_seen = 0

    def __repr__(self) -> str:
        return str(self.rows)

    def mark_number(self, value: int) -> None:
        for (i, row) in enumerate(self.rows):
            for (j, number) in enumerate(row):
                if number == value:
                    self._seen_numbers[i][j] = True
                    self._last_seen = value
                    return

    def is_completed(self) -> bool:
        for row in self._seen_numbers:
            if all(row):
                return True

        for column in [
            [row[i] for row in self._seen_numbers]
            for i in range(len(max(self._seen_numbers, key=len)))
        ]:
            if all(column):
                return True
        return False

    def count_points(self) -> int:
        sum_ = 0
        for (i, row) in enumerate(self.rows):
            for (j, number) in enumerate(row):
                if not self._seen_numbers[i][j]:
                    sum_ += number
        return sum_ * self._last_seen


def get_score_of_first_winning_board(boards: List[Board], numbers: List[int]) -> int:
    copied_boards = boards.copy()
    for number in numbers:
        for b in copied_boards:
            b.mark_number(number)
            if b.is_completed():
                return b.count_points()


def get_score_of_last_winning_board(boards: List[Board], numbers: List[int]) -> int:
    copied_boards = boards.copy()
    for number in numbers:
        completed_boards = []
        for b in copied_boards:
            b.mark_number(number)
            if b.is_completed():
                completed_boards.append(b)

        if len(copied_boards) > 1:
            for b in completed_boards:
                copied_boards.remove(b)
        elif completed_boards:
            return completed_boards[0].count_points()

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        generated_numbers = list(map(int, f.readline().split(",")))
        boards = []

        rows_to_save = []
        while line := f.readline():
            if line == "\n":
                if rows_to_save:
                    boards.append(Board(rows_to_save))
                    rows_to_save = []
            else:
                rows_to_save.append(list(map(int, line.split())))

        if rows_to_save:
            boards.append(Board(rows_to_save))

    print("### part1")
    first_score = get_score_of_first_winning_board(boards, generated_numbers)
    print(first_score)

    print("### part2")
    last_score = get_score_of_last_winning_board(boards, generated_numbers)
    print(last_score)

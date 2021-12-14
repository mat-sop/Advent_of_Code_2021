import sys
from dataclasses import dataclass
from typing import Dict, List
from collections import defaultdict


def process_formula(formula: str, templates: Dict[str, str]) -> str:
    result = formula[0]
    for i in range(len(formula) - 1):
        pair = formula[i] + formula[i + 1]
        if insertion := templates.get(pair):
            result += insertion + pair[1]
        else:
            result += pair[1]

    return result


def count_occurences(formula: str) -> Dict[str, int]:
    occurences = defaultdict(int)
    for s in formula:
        occurences[s] += 1

    return occurences


def count_diff(occurences: Dict[str, int]) -> int:
    return (
        occurences[max(occurences, key=occurences.get)]
        - occurences[min(occurences, key=occurences.get)]
    )


def procces_formula_v2(
    formula: Dict[str, int], templates: Dict[str, str], counter: Dict[str, int]
):
    updated_formula = formula.copy()
    updated_counter = counter.copy()
    for k, v in templates.items():
        if k in formula:
            updated_formula[k[0] + v] += formula[k]
            updated_formula[v + k[1]] += formula[k]
            updated_counter[v] += formula[k]
            updated_formula[k] -= formula[k]
    return updated_formula, updated_counter


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    templates = {}
    with open(file_path, "r") as f:
        formula = f.readline().strip()
        f.readline()
        while line := f.readline().strip():
            s1, s2 = line.split(" -> ")
            templates[s1] = s2

    print("### part1")
    updated_formula = formula
    for i in range(10):
        updated_formula = process_formula(updated_formula, templates)
    occurences = count_occurences(updated_formula)
    print(count_diff(occurences))

    print("### part2")
    formula_v2 = defaultdict(int)
    for i in range(len(formula) - 1):
        formula_v2[formula[i] + formula[i + 1]] += 1

    updated_formula_v2 = formula_v2.copy()
    updated_occurences_v2 = count_occurences(formula)
    for i in range(40):
        updated_formula_v2, updated_occurences_v2 = procces_formula_v2(
            updated_formula_v2, templates, updated_occurences_v2
        )
    print(count_diff(updated_occurences_v2))

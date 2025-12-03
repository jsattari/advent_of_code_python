"""Day 4 solution."""

# ruff: noqa: E402, F841
# mypy: ignore-errors

from pathlib import Path
from typing import List

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder


def create_matrix(str_input: str) -> List[List[str]]:
    output = []

    for line in str_input.split("\n"):
        row = list(line)
        output.append(row)

    return output


def is_xmas(puzzle: List[List[str]], idx1: int, idx2: int) -> bool:
    # determine if need to stop search
    return None


def part_one(data: str) -> int:
    # turn string into a matrix
    matrix = create_matrix(data)  # type: ignore[return-value]

    # output
    total = 0  # type: ignore[return]


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")

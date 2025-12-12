"""Solution for day 6 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys
from functools import reduce
import operator

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder, list_maker


def part_one(data: str) -> int:
    """Solution for part 1."""
    # parsed data
    split_data = list_maker(data)

    # split based on spaces
    transformed = [i.split() for i in split_data]

    # zip all rows together so the value line up "vertically"
    transposed = list(zip(*transformed))

    total = 0

    for vals in transposed:
        # parse based on sum or multiplication
        if vals[-1] == "*":
            temp = reduce(operator.mul, map(int, vals[:-1]), 1)
        if vals[-1] == "+":
            temp = sum(map(int, vals[:-1]))
        total += temp

    return total


def part_two(data: str) -> int:
    """Solution for part 2."""
    # parsed data
    split_data = list_maker(data)

    # split based on spaces
    transformed = [i.split() for i in split_data]
    print(transformed)

    total = 0

    return total


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    # print(f"Part one: {part_one(data)}")

    print(f"Part two: {part_two(data)}")

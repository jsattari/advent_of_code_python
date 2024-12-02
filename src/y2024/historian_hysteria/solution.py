"""Solution for day 1 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from typing import List
from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder


def part_one(dataset: str) -> int:
    """Calculate part one solution.

    Args:
        dataset:     input data source

    Returns:
        solution
    """
    # create two lists to hold data
    list_1: List[int] = []
    list_2: List[int] = []

    # loop through data string, parse
    for line in dataset.split("\n"):
        # split nums
        num_left, num_right = line.split()

        list_1.append(int(num_left))
        list_2.append(int(num_right))

    # sort lists
    list_1.sort()
    list_2.sort()

    output = 0

    for i in range(0, len(list_1)):
        output += abs(list_1[i] - list_2[i])

    return output


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")

"""Solution for day 2 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path
from typing import List

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder


def check_safety(arr: List[int]) -> bool:
    # create array of differences between each element in a list
    asc = {arr[i + 1] - arr[i] for i in range(len(arr) - 1)}

    # check if values within diff array fit within sets
    return asc <= {1, 2, 3} or asc <= {-1, -2, -3}


def part_one(dataset: str) -> int:
    safe_reports = 0

    for line in dataset.split("\n"):
        # turn line into list
        curr = list(map(lambda x: int(x), line.split()))

        # check validity
        valid = check_safety(curr)

        # increment output
        safe_reports += valid

    return safe_reports


def part_two(dataset: str) -> int:
    safe_reports = 0

    for line in dataset.split("\n"):
        # create list form line
        curr = list(map(int, line.split()))

        # safety flags
        flags = []

        for i in range(len(curr)):
            # create new list with ele removed
            new_curr = curr[:i] + curr[i + 1 :]

            # check validity
            valid = check_safety(new_curr)

            # append bool result to list
            flags.append(valid)

        # if any ele are True, then add 1 else add 0
        safe_reports += any(flags)

    return safe_reports


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")  # incorrect at 585 (too low)

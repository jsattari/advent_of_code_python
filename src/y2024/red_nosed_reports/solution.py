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


def check_order(arr: List[int]) -> bool:
    # flags for asc or desc
    asc = desc = True

    for i in range(1, len(arr)):
        # check if asc or desc
        if arr[i] <= arr[i - 1]:
            asc = False

        if arr[i] >= arr[i - 1]:
            desc = False

    return asc or desc


def check_increments(arr: List[int], dampener=False) -> bool:
    # allowances
    dampened = 0

    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])

        if diff < 1 or diff > 3:
            if dampener:
                dampened += 1
                if dampened > 1:
                    return False
                continue
            return False

    return True


def part_one(dataset: str) -> int:
    safe_reports = 0

    for line in dataset.split("\n"):
        # turn line into list
        curr = list(map(lambda x: int(x), line.split()))

        # check row of nums for validity
        asc_or_desc = check_order(curr)
        is_valid_diff = check_increments(curr)

        # if both conditions, increment safe reports
        if asc_or_desc and is_valid_diff:
            safe_reports += 1

    return safe_reports


def part_two(dataset: str) -> int:
    safe_reports = 0

    for line in dataset.split("\n"):
        # create list form line
        curr = list(map(lambda x: int(x), line.split()))

        # check row of nums for validity
        asc_or_desc = check_order(curr)
        is_valid_diff = check_increments(curr, dampener=True)

        # if both conditions, increment safe reports
        if asc_or_desc and is_valid_diff:
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")  # incorrect at 585 (too low)

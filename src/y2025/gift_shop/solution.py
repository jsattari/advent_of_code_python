"""Solution for day 2 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder, list_maker


def check_repeat(number: int) -> bool:
    """Checks for repeating pattern in number."""
    # change to string
    num_str = str(number)

    # find midpoint
    mid = len(num_str) // 2

    return num_str[:mid] == num_str[mid:]


def check_pattern(number: int) -> bool:
    """Double string and remove first/last chars."""
    num_str = str(number)

    return num_str in (num_str + num_str)[1:-1]


def part_one(data: str) -> int:
    """Solution for part 1."""
    # parsed data
    split_data = list_maker(data, ",")

    # invalid numbers
    invalids = []

    for r in split_data:
        # split range into ints
        start, end = map(int, r.split("-"))

        # loop over range of numbers
        for i in range(start, end):
            # add to list of invalids if fails check
            if check_repeat(i):
                invalids.append(i)

    return sum(invalids)


def part_two(data: str) -> int:
    """Solution for part 2."""
    # parsed data
    split_data = list_maker(data, ",")

    # invalid numbers
    invalids = []

    for r in split_data:
        # split range into ints
        start, end = map(int, r.split("-"))

        # loop over range of numbers
        for i in range(start, end):
            # add to list of invalids if fails check
            if check_pattern(i):
                invalids.append(i)

    return sum(invalids)


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    # print(f"Part one: {part_one(data)}")

    print(f"Part two: {part_two(data)}")

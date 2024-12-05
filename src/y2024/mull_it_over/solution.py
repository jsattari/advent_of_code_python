"""Day 3 Solution."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path
from typing import List

import re
import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder


def get_nums_regexp(input_str: str) -> List[tuple]:
    # create pattern
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    return re.findall(pattern, input_str)


def part_one(dataset: str) -> int:
    # init total variable
    total = 0

    # get list of digits to multiply
    digits = get_nums_regexp(dataset)

    # loop through digits and multiply
    for tup in digits:
        total += int(tup[0]) * int(tup[1])

    return total


def part_two(dataset: str) -> int:
    """Sliding window and regexp combo"""

    # create list to hold values
    temp = []

    # set up sliding window variables
    left = 0
    right = 9

    # flag to switch based on do/don't
    check = True

    while right <= len(dataset):
        # slice string
        curr = dataset[left:right]

        # add conditions for do/don't
        if "don't()" in curr:
            check = False
            left = right
        elif "do()" in curr:
            check = True
            left = right
        else:
            # check if string contains pattern
            parsed = get_nums_regexp(curr)

            # if don't hasn't been reached, parse
            if check and len(parsed) > 0:
                temp.append(parsed[0])
                left = right

        # always increment right bookend
        right += 1

    # output
    total = 0

    # loop and multiply
    for tup in temp:
        total += int(tup[0]) * int(tup[1])

    return total


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

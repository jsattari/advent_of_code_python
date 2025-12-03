"""Solution for day 1 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder, list_maker


def part_one_solution(data: str) -> int:
    """Solution for part one."""
    # starting point
    curr = 50
    counter = 0
    split_data = list_maker(data)

    for val in split_data:
        # split values
        direction, amt = val[0], int(val[1:])

        # if direction is left, move pointer to negative
        if direction == "L":
            curr = (curr - amt) % 100

        else:
            curr = (curr + amt) % 100

        if curr == 0:
            counter += 1

    return counter


def part_two_solution(data: str) -> int:
    """Solution for part two."""
    # starting point
    curr = 50
    counter = 0
    split_data = list_maker(data)

    for val in split_data:
        direction, amt = val[0], int(val[1:])

        # increment by 1
        for _ in range(amt):
            if direction == "L":
                curr = (curr - 1) % 100
            else:
                curr = (curr + 1) % 100

            if curr == 0:
                counter += 1

    return counter


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one_solution(data)}")

    print(f"Part two: {part_two_solution(data)}")

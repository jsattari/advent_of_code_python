"""Solution for day 3 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder, list_maker


def part_one(data: str) -> int:
    """Solution for part 1."""
    # parsed data
    split_data = list_maker(data)

    jolts: list[int] = []

    for bank in split_data:
        # init variables for first two digits
        x, y = 0, 0

        for i in bank:
            num = int(i)

            if y > x:
                x = y
                y = num

            if num > y and num != x:
                y = num

        jolts.append(int(f"{x}{y}"))

    return sum(jolts)


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")

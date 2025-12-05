"""Solution for day 3 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder, list_maker


def part_one(data: str) -> list:
    """Solution for part 1."""
    # parsed data
    split_data = list_maker(data)

    jolts: list[int] = []

    for bank in split_data[:1]:
        # init variables for first two digits
        x, y = 0, 1

        # current max value
        max_val = int(bank[x])

        while y < len(bank):
            print(x, y, max_val)
            if bank[y] > bank[x]:
                x = y
                y += 1

                max_val = max(max_val, int(f"{bank[x]}{bank[y]}"))

            y += 1

        jolts.append(max_val)

    return jolts


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")

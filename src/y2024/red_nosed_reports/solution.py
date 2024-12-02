"""Solution for day 2 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder


def part_one(dataset: str) -> int:
    safe_reports = 0

    for line in dataset.split("\n"):
        # confirmation
        valid = True

        # turn line into list
        curr = list(map(lambda x: int(x), line.split()))

        # flags for asc or desc
        asc = desc = True

        for i in range(1, len(curr)):
            # check if asc or desc
            if curr[i] <= curr[i - 1]:
                asc = False

            if curr[i] >= curr[i - 1]:
                desc = False

            # check diff
            diff = abs(curr[i] - curr[i - 1])

            # must be between 1 and 3
            if diff < 1 or diff > 3:
                valid = False

        # set valid to False if not monotonic
        if not asc and not desc:
            valid = False

        # if both conditions, increment safe reports
        if valid:
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")

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

            # if second max > max, then replace
            if y > x:
                x = y
                y = num

            # replace second max with highest number available
            if num > y:
                y = num

        jolts.append(int(f"{x}{y}"))

    return sum(jolts)


def part_two(data: str) -> int:
    """Solution for part 1."""
    # parsed data
    split_data = list_maker(data)

    jolts: list[int] = []

    for bank in split_data:
        max_val = ""
        curr_idx = 0

        # loop backwards
        for i in range(12, 0, -1):
            # find current range from battery banks
            a = bank[curr_idx : len(bank) - i + 1]

            # get max from current range
            curr_max = max(a)

            # append max value of current range to overall max val str
            max_val += str(curr_max)

            # update current idx to idx of current max val
            curr_idx += a.index(curr_max) + 1

        jolts.append(int(max_val))

    return sum(jolts)


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    # print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

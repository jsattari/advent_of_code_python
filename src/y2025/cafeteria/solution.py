"""Solution for day 5 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder, list_maker


def parse_freshness_and_ids(x: list[str]) -> tuple[list[list[int]], list[int]]:
    """Accepts string split input and returns two formatted arrays of strings.

    Args:
        x:      List of parsed inputs.

    Returns:
        Two lists of strings that represent the freshness values and ids to check.
    """
    # find index of line break
    idx_of_blank: int = x.index("")

    # split freshness values
    fresh_vals: list[list[int]] = []

    # loop over str ranges and create list of integers
    for rng in x[:idx_of_blank]:
        # create range integer bookends
        nums: list[int] = list(map(int, rng.split("-")))

        # merge integers
        fresh_vals.append(nums)

    # turn id str into int
    ids: list[int] = list(map(int, x[idx_of_blank + 1 :]))

    return fresh_vals, ids


def part_one(data: str) -> int:
    """Solution for part 1."""
    # parsed data
    split_data = list_maker(data)

    # parse inputs
    freshness, ingredients = parse_freshness_and_ids(split_data)

    # counter (used set for faster lookup/no dupes)
    count: set[int] = set()

    # loop over ids
    for i in ingredients:
        # loop over freshness values
        for j in freshness:
            # add to set if in range
            if j[0] <= i <= j[1]:
                if i not in count:
                    count.add(i)

    return len(count)


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    print(f"Part one: {part_one(data)}")

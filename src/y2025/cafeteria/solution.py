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


def part_two(data: str) -> int:
    """Solution for part 2."""
    # parsed data
    split_data = list_maker(data)

    # parse inputs
    freshness, _ = parse_freshness_and_ids(split_data)

    # sort freshness ranges
    sorted_fresh = sorted(freshness)

    # establish low and high max vals
    curr_lo, curr_hi = sorted_fresh[0]

    # total fresh ids
    total = 0

    # loop over remaining id ranges
    for pair in sorted_fresh[1:]:
        # if current ranges low is less than current hi value, replace with max of the two highs
        if pair[0] <= curr_hi:
            curr_hi = max(curr_hi, pair[1])

        else:
            # increment total plus one
            total += curr_hi - curr_lo + 1

            # replace lows and hi
            curr_lo, curr_hi = pair

    return total + (curr_hi - curr_lo) + 1


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    # print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

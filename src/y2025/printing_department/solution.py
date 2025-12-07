"""Solution for day 4 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder, list_maker


def check_all_sides(arr: list[list[str]], x: int, y: int) -> bool:
    """Checks if less than 4 sides of a position have toilet paper.

    Args:
        arr:        Array of strings for consideration.
        x:          Row coordinate.
        y:          Column coordinate.

    Returns:
        True if less than 4 sides have toilet paper.
    """
    # counter
    counter = 0

    # list of surrounding positions
    positions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for a, b in positions:
        # create assumed coordinates
        dx, dy = x + a, y + b

        if 0 <= dx < len(arr) and 0 <= dy < len(arr[0]):
            if arr[dx][dy] == "@":
                counter += 1

    # True if less than for adjacent positions
    return counter < 4


def part_one(data: str) -> int:
    """Solution for part 1."""
    # parsed data
    split_data = list_maker(data)

    # transform input into nd array of chars
    parsed_split_data: list[list[str]] = [list(n) for n in split_data]

    # accessible positions
    count = 0

    for i in range(0, len(split_data)):
        for j in range(0, len(split_data[i])):
            # only count if it is a role of tp (@)
            if split_data[i][j] == "@" and check_all_sides(parsed_split_data, i, j):
                # temp[i][j] = 1
                count += 1

    return count


def part_two(data: str) -> int:
    """Solution for part 2."""
    # parsed data
    split_data = list_maker(data)

    # transform input into nd array of chars
    parsed_split_data: list[list[str]] = [list(n) for n in split_data]

    count: int = 0
    check: bool = True

    while check:
        # make a copy of the dept map
        temp: list[list[str]] = parsed_split_data.copy()

        # total for current iteration
        curr = 0

        for i in range(0, len(parsed_split_data)):
            for j in range(0, len(parsed_split_data[i])):
                # only count if it is a role of tp (@)
                if parsed_split_data[i][j] == "@" and check_all_sides(
                    parsed_split_data, i, j
                ):
                    # replace temp nd array position with dot, meaning it's removed
                    temp[i][j] = "."
                    curr += 1

        # if tp was tracked, update counts and update with new map
        if curr:
            count += curr
            parsed_split_data = temp

        else:
            # nothing was tracked, end counting as no more can be removed
            check = False

    return count


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    # print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

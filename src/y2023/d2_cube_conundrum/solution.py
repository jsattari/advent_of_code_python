# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path
from typing import List, Dict
import re

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder


def part1(dataset: str) -> int:
    CUBES = {"red": 12, "green": 13, "blue": 14}

    # pattern
    pattern = r"(\d+)\s*(red|blue|green)"
    game_pattern = r"(\d+)"

    total: List[int] = []

    for line in dataset.split("\n"):
        valid = True
        parts = line.split(";")

        for part in parts:
            matches = re.findall(pattern, part)

            while valid:
                for val, color in matches:
                    if int(val) > CUBES[color]:
                        valid = False
                break

        if valid:
            game_id = re.search(game_pattern, line)
            if game_id:
                total.append(int(game_id.group(1)))

    return sum(total)


def part2(dataset: str) -> int:
    # pattern
    pattern = r"(\d+)\s*(red|blue|green)"

    total: int = 0

    for line in dataset.split("\n"):
        parts = line.split(";")

        CUBES: Dict[str, List[int]] = {"red": [], "green": [], "blue": []}

        # parse colors, then add value to CUBES
        for part in parts:
            matches = re.findall(pattern, part)

            for val, color in matches:
                CUBES[color].append(int(val))

        # get max value of each color
        total += max(CUBES["red"]) * max(CUBES["green"]) * max(CUBES["blue"])

    return total


if __name__ == "__main__":
    # current file path
    curr_file = Path(__file__)

    # open test data file
    with file_finder(curr_file).open("r") as file:
        data = file.read()

    # print(part1(data))
    print(part2(data))

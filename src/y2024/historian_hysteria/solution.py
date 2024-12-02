"""Solution for day 1 problem."""

# ruff: noqa: E402
# mypy: disable-error-code="union-attr"

from pathlib import Path

import sys

# adding sys path for imports
curr_path = Path(__file__).parents[3]
sys.path.append(str(curr_path))

from utility.helpers import file_finder

if __name__ == "__main__":
    # open test data file
    with file_finder(Path(__file__)).open("r") as file:
        data = file.read()

    print(data)

"""Function to load inputs from current folder."""

from pathlib import Path
from typing import Union


def file_finder() -> Union[Path, None, Exception]:
    """Find input file within folder.

    Args:
        None

    Returns:
        Data contained within input file saved within folder.
    """

    # find frame of caller
    curr_dir = Path.cwd()

    # create path of input.txt
    input_file_path = curr_dir / "input.txt"

    if input_file_path.is_file():
        return input_file_path
    else:
        raise FileNotFoundError("input.txt file not found")

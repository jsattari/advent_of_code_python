"""Function to load inputs from current folder."""

from pathlib import Path
from typing import Union


def file_finder(file_path_obj: Path) -> Union[Path, None, Exception]:
    """Find input file within folder.

    Args:
        file_path_obj:  File path as object

    Returns:
        Data contained within input file saved within folder.
    """

    # get parent path of input file path
    curr_dir = file_path_obj.parents[0]

    # create path of input.txt
    input_file_path = curr_dir / "input.txt"

    if input_file_path.is_file():
        return input_file_path
    else:
        raise FileNotFoundError("input.txt file not found")


def list_maker(file_str: str) -> list[str]:
    """Accepts string from file and converts to list.

    Args:
        file_str:       String from file, may contain newline and other non-alphanum chars.

    Returns:
        List containing parsed string values.
    """
    if not file_str:
        raise ValueError("String cannot be none or empty.")

    # split on newline
    split_str = file_str.split("\n")

    return [str(i) for i in split_str]

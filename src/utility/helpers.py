#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import inspect
from pathlib import Path


def file_finder() -> str:
    """
        find input file within folder
    """

    # find frame of caller
    frame = inspect.stack()[1]

    # find get filename from frame
    filename = frame[1]

    # get absolute path
    filepath = Path(filename).resolve()

    # create path of input.txt
    input_file_path = filepath.parent / "input.txt"

    if input_file_path.is_file():
        return str(input_file_path)
    else:
        raise FileNotFoundError("input.txt file not found")

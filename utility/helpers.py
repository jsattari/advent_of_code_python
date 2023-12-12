#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pathlib import Path
from typing import Union


def file_finder(filename: str, start_path=".") -> Union[Path, None, Exception]:
    """
        find input file within folder
    """

    # starting point
    begin = Path(start_path)

    # file path
    file_path = begin / filename

    try:
        if file_path.is_file():
            return file_path

    except Exception as e:
        return e

    return None

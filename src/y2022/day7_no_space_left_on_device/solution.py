#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List, Tuple
import re

# load input data from file
folder_filename = "/2022/day7_no_space_left_on_device/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()


def find_size(cmds: List[str]) -> Tuple[int, List[int]]:
    iter_data = iter(data)
    sizes = []
    stack = [0]
    while stack:
        line = next(iter_data, "$ cd ..")
        if line == "$ cd ..":
            child = stack.pop()
            if stack:
                sizes.append(child)
                stack[-1] += child
        elif cd := re.match(r"\$ cd .+", line):  # noqa: F841
            stack.append(0)
        elif file := re.match(r"(\d+) .+", line):
            stack[-1] += int(file.group(1))

    space_needed = 30_000_000 - (70_000_000 - sizes[-1])
    sizes = sorted(sizes)

    return space_needed, sizes


if __name__ == "__main__":
    x, y = find_size(data)
    print(
        f"Part 1: {sum([y[ele] for ele in range(0, len(y) - 1) if y[ele] <= 100_000])}"  # noqa: E501
    )
    print(
        f"Part 2: {[y[ele] for ele in range(0, len(y) - 1) if y[ele] >= x][0]}"
    )  # noqa: E501

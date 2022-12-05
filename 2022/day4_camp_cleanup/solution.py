#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List, Any

# load input data from file
folder_filename = "/2022/day4_camp_cleanup/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()


# funciton to split strings into list of integers for comparison
def split_and_flatten(val: Any) -> List[int]:
    nums: List[List[Any]] = [item.split("-") for item in val.split(",")]
    flat: List[int] = [int(x) for x in nums for x in x]  # type: ignore
    return flat


if __name__ == "__main__":
    total = 0
    for row in data:
        a, b, c, d = split_and_flatten(row)
        # check if start/end points are lesser
        # than their counterparts
        if a <= c <= d <= b or c <= a <= b <= d:
            total += 1
    print(f"Part 1: {total}")

    total2 = 0
    for row in data:
        a, b, c, d = split_and_flatten(row)
        # check if the higher start point is less than
        # the lower end point to find overlaps
        if max(a, c) <= min(b, d):
            total2 += 1
    print(f"Part 2: {total2}")

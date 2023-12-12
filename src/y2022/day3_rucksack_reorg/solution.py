#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import Tuple, List

# load input data from file
folder_filename = "/2022/day3_rucksack_reorg/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()


# function to split up values
def splitter(text: str) -> Tuple[str, str]:
    mid = len(text) // 2

    return text[0:mid], text[mid:]


# function to change chars into numerical values
def convert(val: str) -> List[int]:
    return [ord(chr) - 96 if chr.islower() else ord(chr) - 38 for chr in val]


if __name__ == "__main__":
    total = 0
    for string in data:
        txt1, txt2 = splitter(string)
        nums1, nums2 = convert(txt1), convert(txt2)
        # find diff between two lists of unique numbers
        total += list(set(nums1) & set(nums2))[0]
    print(f"Part 1: {total}")

    total2 = 0
    for num in range(0, len(data) - 1, 3):
        # loop through groups of 3 strings
        right = num + 3
        chunk = data[num:right]
        nums1, nums2, nums3 = (
            convert(chunk[0]),
            convert(chunk[1]),
            convert(chunk[2]),
        )
        #  find diff between three lists of unique numbers
        total2 += list(set(nums1) & set(nums2) & set(nums3))[0]
    print(f"Part 2: {total2}")

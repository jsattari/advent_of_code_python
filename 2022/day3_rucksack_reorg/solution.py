#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import Tuple, List

# load input data from file
folder_filename = "/2022/day3_rucksack_reorg/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()


def splitter(text: str) -> Tuple[str, str]:
    mid = len(text) // 2

    return text[0:mid], text[mid:]


def convert(val: str) -> List[int]:
    return [ord(chr) - 96 if chr.islower() else ord(chr) - 38 for chr in val]


def dupe_finder(list1: List[int], list2: List[int]) -> int:
    set1, set2 = set(list1), set(list2)
    output = set1.intersection(set2)
    return list(output)[0]


if __name__ == "__main__":
    total = 0
    for string in data:
        txt1, txt2 = splitter(string)
        nums1, nums2 = convert(txt1), convert(txt2)
        total += int(dupe_finder(nums1, nums2))
    print(f"Part 1: {total}")

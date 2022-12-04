#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import Tuple, List

# load input data from file
folder_filename = "/2022/day4_camp_cleanup/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()


def contain_check(list1: List[int], list2: List[int]) -> Tuple[bool, bool]:
    output1 = all(ele in list2 for ele in list1)
    output2 = all(ele in list1 for ele in list2)
    return output1, output2


if __name__ == "__main__":
    total = 0
    for row in data[:5]:
        ele = row.split(",")

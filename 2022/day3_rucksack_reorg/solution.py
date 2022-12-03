#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import Tuple, List

# load input data from file
folder_filename = "/2022/day3_rucksack_reorg/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()


def splitter(text: str) -> Tuple[str, str]:
    mid = (len(text) - 1) // 2

    return text[0:mid], text[mid:-1]


def convert(val: str) -> List[int]:
    return [ord(chr) - 97 if chr.islower() else ord(chr) - 38 for chr in val]


if __name__ == "__main__":
    print(convert("ChEEse"))

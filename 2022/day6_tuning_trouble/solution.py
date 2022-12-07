#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib

# load input data from file
folder_filename = "/2022/day6_tuning_trouble/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read()


def find_first_marker(txt: str) -> int:
    left = 0
    right = left + 4
    word = list(txt[left:right])
    chars = set(txt[left:right])

    while len(word) != len(chars):
        left += 1
        right += 1
        word = list(txt[left:right])
        chars = set(txt[left:right])

    return right


if __name__ == "__main__":
    print(find_first_marker(data))

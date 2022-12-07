#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib

# load input data from file
folder_filename = "/2022/day6_tuning_trouble/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read()


def find_msg_marker(txt: str, char_len: int) -> int:
    # create bounds for window
    left = 0
    right = left + char_len

    """
    If length of unique chars in window
    is not equal to desired char_len, keep
    incrementing window until matching
    """
    while char_len != len(set(txt[left:right])):
        left += 1
        right += 1

    return right


if __name__ == "__main__":
    print(f"Part 1: {find_msg_marker(data, 4)}")
    print(f"Part 2: {find_msg_marker(data, 14)}")

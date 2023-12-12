#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib

# load input data from file
folder_filename = "/2022/day2_rock_paper_scissors/input.txt"
path_ = str(pathlib.Path().absolute())
data = open(path_ + folder_filename).read().splitlines()

# split data into List[List[str, str]]
lines = [line.split() for line in data]

# get numerical difference from "Rock" value for opp and self
games = [(ord(x) - ord("A"), ord(y) - ord("X")) for x, y in lines]

# find numerical difference based on part 2 scoring logic
choices = [(x, (x + y - 1) % 3) for x, y in games]


# function that returns score based on numerical inputs
def score(val1: int, val2: int) -> int:
    if (val1 - 1) % 3 == val2:
        return val2 + 1
    elif (val2 - 1) % 3 == val1:
        return val2 + 7
    return val2 + 4


if __name__ == "__main__":
    print(f"Part 1: {sum(score(x, y) for x, y in games)}")
    print(f"Part 2: {sum(score(x, y) for x, y in choices)}")

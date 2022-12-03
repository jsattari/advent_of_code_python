#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List

# load input data from file
folder_filename = "/2022/day1_calorie_counting/input.txt"
data = open(str(pathlib.Path().absolute()) + folder_filename).read()

# split into list of ints
split_data = data.split("\n\n")
calories = [[int(x) for x in text.split("\n")] for text in split_data]


def max_cals(kcals: List[List[int]]) -> int:
    """
    Part1: How many total Calories is that Elf carrying?
    """
    max_cals = 0

    for num in range(0, len(kcals) - 1):
        tot_cals = sum(calories[num])
        max_cals = max(max_cals, tot_cals)

    return max_cals


def top_three(kcals: List[List[int]]) -> int:

    """
    Part2: How many Calories are those (top3) Elves carrying in total?
    """
    summed_cals = [sum(val) for val in kcals]

    sorted_cals = sorted(summed_cals, reverse=True)

    total = sum(sorted_cals[:3])

    return total


if __name__ == "__main__":
    print(f"Part 1: {max_cals(calories)}")
    print(f"Part 2: {top_three(calories)}")

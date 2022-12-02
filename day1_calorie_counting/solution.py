#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pathlib
from typing import List

folder_filename = "/day1_calorie_counting/input.txt"
data = open(str(pathlib.Path().absolute()) + folder_filename).read()
split_data = data.split("\n\n")
calories = [[int(x) for x in text.split("\n")] for text in split_data]


def max_cals(kcals: List[List[int]]) -> int:

    max_cals = 0

    for num in range(0, len(kcals) - 1):
        tot_cals = sum(calories[num])
        max_cals = max(max_cals, tot_cals)

    return max_cals


def top_three(kcals: List[List[int]]) -> int:

    summed_cals = [sum(val) for val in kcals]

    sorted_cals = sorted(summed_cals, reverse=True)

    total = sum(sorted_cals[:3])

    return total


if __name__ == "__main__":
    print(max_cals(calories))
    print(top_three(calories))
